"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.datasphere.v2.s3_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class S3ServiceStub:
    """A set of methods for managing S3 configurations."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Activate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.s3_service_pb2.ActivateS3Request,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Activates shared s3 for project"""

    Deactivate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.s3_service_pb2.DeactivateS3Request,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deactivates shared s3 for project"""

class S3ServiceAsyncStub:
    """A set of methods for managing S3 configurations."""

    Activate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.s3_service_pb2.ActivateS3Request,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Activates shared s3 for project"""

    Deactivate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.s3_service_pb2.DeactivateS3Request,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deactivates shared s3 for project"""

class S3ServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing S3 configurations."""

    @abc.abstractmethod
    def Activate(
        self,
        request: yandex.cloud.datasphere.v2.s3_service_pb2.ActivateS3Request,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Activates shared s3 for project"""

    @abc.abstractmethod
    def Deactivate(
        self,
        request: yandex.cloud.datasphere.v2.s3_service_pb2.DeactivateS3Request,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deactivates shared s3 for project"""

def add_S3ServiceServicer_to_server(servicer: S3ServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
