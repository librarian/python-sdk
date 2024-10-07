import inspect
from typing import TYPE_CHECKING, Any, Dict, Optional, Type, Union

import grpc

from nebiusai import _channels, _helpers, _operation_waiter
from nebiusai._backoff import backoff_exponential_with_jitter
from nebiusai._retry_interceptor import RetryInterceptor

if TYPE_CHECKING:
    import logging

    from nebius.common.v1.operation_pb2 import Operation
    from nebiusai._operation_waiter import OperationWaiter
    from nebiusai.operations import (
        MetaType,
        OperationError,
        OperationResult,
        RequestType,
        ResponseType,
    )


class SDK:
    def __init__(
        self,
        interceptor: Union[
            grpc.UnaryUnaryClientInterceptor,
            grpc.UnaryStreamClientInterceptor,
            grpc.StreamUnaryClientInterceptor,
            grpc.StreamStreamClientInterceptor,
            None,
        ] = None,
        user_agent: Optional[str] = None,
        endpoints: Optional[Dict[str, str]] = None,
        token: Optional[str] = None,
        iam_token: Optional[str] = None,
        endpoint: Optional[str] = None,
        service_account_key: Optional[Dict[str, str]] = None,
        root_certificates: Optional[bytes] = None,
        private_key: Optional[bytes] = None,
        certificate_chain: Optional[bytes] = None,
        **kwargs: str,
    ):
        """
        API entry-point object.

        :param interceptor: GRPC interceptor to be used instead of default RetryInterceptor
        :param user_agent: String to prepend User-Agent metadata header for all GRPC requests made via SDK object
        :param endpoints: Dict with services endpoints overrides. Example: {'vpc': 'new.vpc.endpoint:443'}

        """
        self._channels = _channels.Channels(
            user_agent,
            endpoints,
            token,
            iam_token,
            endpoint,
            service_account_key,
            root_certificates,
            private_key,
            certificate_chain,
            **kwargs,
        )
        if interceptor is None:
            interceptor = RetryInterceptor(
                max_retry_count=5,
                per_call_timeout=30,
                back_off_func=backoff_exponential_with_jitter(1, 30),
            )
        self._default_interceptor = interceptor
        self.helpers = _helpers.Helpers(self)

    def client(
        self,
        stub_ctor: Type,
        interceptor: Union[
            grpc.UnaryUnaryClientInterceptor,
            grpc.UnaryStreamClientInterceptor,
            grpc.StreamUnaryClientInterceptor,
            grpc.StreamStreamClientInterceptor,
            None,
        ] = None,
        endpoint: Optional[str] = None,
        insecure: bool = False,
    ) -> Any:
        service = _service_for_ctor(stub_ctor)
        channel = self._channels.channel(service, endpoint, insecure)
        if interceptor is not None:
            channel = grpc.intercept_channel(channel, interceptor)
        elif self._default_interceptor is not None:
            channel = grpc.intercept_channel(channel, self._default_interceptor)
        return stub_ctor(channel)

    def waiter(self, operation_id: str, timeout: Optional[float] = None) -> "OperationWaiter":
        return _operation_waiter.operation_waiter(self, operation_id, timeout)

    def wait_operation_and_get_result(
        self,
        operation: "Operation",
        response_type: Optional[Type["ResponseType"]] = None,
        meta_type: Optional[Type["MetaType"]] = None,
        timeout: Optional[float] = None,
        logger: Optional["logging.Logger"] = None,
    ) -> Union["OperationResult[ResponseType, MetaType]", "OperationError"]:
        return _operation_waiter.get_operation_result(self, operation, response_type, meta_type, timeout, logger)

    def create_operation_and_get_result(
        self,
        request: Type["RequestType"],
        service: Any,
        method_name: str,
        response_type: Optional[Type["ResponseType"]] = None,
        meta_type: Optional[Type["MetaType"]] = None,
        timeout: Optional[float] = None,
        logger: Optional["logging.Logger"] = None,
    ) -> Union["OperationResult", "OperationError"]:
        operation = getattr(self.client(service), method_name)(request)
        return self.wait_operation_and_get_result(
            operation,
            response_type=response_type,
            meta_type=meta_type,
            timeout=timeout,
            logger=logger,
        )


def _service_for_ctor(stub_ctor: Any) -> str:
    m = inspect.getmodule(stub_ctor)
    if m is not None:
        name = m.__name__
        if not name.startswith("nebius"):
            raise RuntimeError(f"Not a nebius service {stub_ctor}")

        for k, v in _supported_modules:
            if name.startswith(k):
                return v

    raise RuntimeError(f"Unknown service {stub_ctor}")


_supported_modules = [
    ("nebius.common", "common"),
    ("nebius.compute", "compute"),
    ("nebius.registry", "container-registry"),
    ("nebius.iam", "iam"),
    ("nebius.mk8s", "managed-kubernetes"),
    ("nebius.storage", "storage-api"),
    ("nebius.vpc", "vpc"),
]
