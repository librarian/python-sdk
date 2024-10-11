import logging
import time
from datetime import datetime
from typing import TYPE_CHECKING, Optional, Type, Union

import grpc
from google.rpc.code_pb2 import Code

from nebius.common.v1.operation_service_pb2 import GetOperationRequest
from nebius.common.v1.operation_service_pb2_grpc import OperationServiceStub
from nebiusai._backoff import backoff_exponential_jittered_min_interval
from nebiusai._retry_interceptor import RetryInterceptor
from nebiusai.operations import MetaType, OperationError, OperationResult, ResponseType

if TYPE_CHECKING:
    from nebius.common.v1.operation_pb2 import Operation
    from nebiusai._sdk import SDK


def operation_waiter(sdk: "SDK", service_ctor: Type, operation_id: str, timeout: Optional[float]) -> "OperationWaiter":
    retriable_codes = (
        grpc.StatusCode.UNAVAILABLE,
        grpc.StatusCode.RESOURCE_EXHAUSTED,
        grpc.StatusCode.INTERNAL,
    )
    # withstand server downtime for ~3.4 minutes with an exponential backoff
    retry_interceptor = RetryInterceptor(
        max_retry_count=13,
        per_call_timeout=30,
        back_off_func=backoff_exponential_jittered_min_interval(),
        retriable_codes=retriable_codes,
    )
    operation_service = sdk.client(
        service_ctor,
        OperationServiceStub,
        interceptor=retry_interceptor,
    )
    return OperationWaiter(operation_id, operation_service, timeout)


def wait_for_operation(sdk: "SDK", service_ctor: Type, operation_id: str, timeout: Optional[float]) -> Optional["Operation"]:
    waiter = operation_waiter(sdk, service_ctor, operation_id, timeout)
    for _ in waiter:
        time.sleep(1)
    return waiter.operation


def get_operation_result(
    sdk: "SDK",
    service_ctor: Type,
    operation: "Operation",
    response_type: Optional[Type["ResponseType"]] = None,
    meta_type: Optional[Type["MetaType"]] = None,
    timeout: Optional[float] = None,
    logger: Optional[logging.Logger] = None,
) -> Union["OperationResult[ResponseType, MetaType]", "OperationError"]:
    if not logger:
        logger = logging.getLogger()
        logger.addHandler(logging.NullHandler())
    created_at = datetime.fromtimestamp(operation.created_at.seconds)
    message = (
        "Running operation. ID: {id}. "
        "Created at: {created_at}. "
        "Resource id: {resource_id}. "
    )
    message = message.format(
        id=operation.id,
        created_at=created_at,
        resource_id=operation.resource_id,
    )
    logger.info(message)
    result = wait_for_operation(sdk, service_ctor, operation.id, timeout=timeout)
    if result is None:
        return OperationError(message="Unexpected operation result", operation_result=OperationResult(operation))
    if result.status.code != Code.OK:
        logger.info("result %s", result)
        error_message = (
            "Error operation. ID: {id}. Error code: {code}. Details: {details}."
        )
        error_message = error_message.format(
            id=result.id,
            code=result.status.code,
            details=result.status.details,
        )
        logger.error(error_message)
        raise OperationError(message=error_message, operation_result=OperationResult(operation))

    log_message = f"Done operation. ID: {operation.id}."

    logger.info(log_message)
    return result.resource_id


class OperationWaiter:
    def __init__(self, operation_id: str, operation_service: "OperationServiceStub", timeout: Optional[float] = None):
        self.__operation: Optional["Operation"] = None
        self.__operation_id = operation_id
        self.__operation_service = operation_service
        self.__deadline = time.time() + timeout if timeout else None

    @property
    def operation(self) -> Optional["Operation"]:
        return self.__operation

    @property
    def done(self) -> bool:
        self.__operation: Operation = self.__operation_service.Get(GetOperationRequest(id=self.__operation_id))
        check_operation = self.__operation is not None
        check_status = self.__operation.status is not None
        check_finished_at = self.__operation.finished_at.seconds != 0
        logging.debug("Operation condition: %s and %s and %s = %s",
            check_operation, check_status, check_finished_at, check_operation and check_status and check_finished_at
        )

        return check_operation and check_status and check_finished_at

    def __iter__(self) -> "OperationWaiter":
        return self

    def __next__(self) -> None:
        if self.done or self.__deadline is not None and time.time() >= self.__deadline:
            raise StopIteration()

    next = __next__  # for Python 2
