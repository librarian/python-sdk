"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.logging.v1.log_ingestion_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class LogIngestionServiceStub:
    """A set of methods for writing to log groups."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Write: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteRequest,
        yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteResponse,
    ]
    """Write log entries to specified destination."""

class LogIngestionServiceAsyncStub:
    """A set of methods for writing to log groups."""

    Write: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteRequest,
        yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteResponse,
    ]
    """Write log entries to specified destination."""

class LogIngestionServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for writing to log groups."""

    @abc.abstractmethod
    def Write(
        self,
        request: yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteResponse, collections.abc.Awaitable[yandex.cloud.logging.v1.log_ingestion_service_pb2.WriteResponse]]:
        """Write log entries to specified destination."""

def add_LogIngestionServiceServicer_to_server(servicer: LogIngestionServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...