"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.video.v1.stream_line_pb2
import yandex.cloud.video.v1.stream_line_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class StreamLineServiceStub:
    """Stream line management service."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.GetStreamLineRequest,
        yandex.cloud.video.v1.stream_line_pb2.StreamLine,
    ]
    """Returns the specific stream line."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.ListStreamLinesRequest,
        yandex.cloud.video.v1.stream_line_service_pb2.ListStreamLinesResponse,
    ]
    """List lines for channel."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.CreateStreamLineRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create stream line."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.UpdateStreamLineRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update stream line."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.DeleteStreamLineRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete stream line."""

    PerformAction: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.PerformLineActionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Perform an action on the line."""

    GetStreamKey: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.GetStreamKeyRequest,
        yandex.cloud.video.v1.stream_line_pb2.PushStreamKey,
    ]
    """Returns unique stream key."""

    UpdateStreamKey: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.UpdateStreamKeyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Change stream key."""

class StreamLineServiceAsyncStub:
    """Stream line management service."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.GetStreamLineRequest,
        yandex.cloud.video.v1.stream_line_pb2.StreamLine,
    ]
    """Returns the specific stream line."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.ListStreamLinesRequest,
        yandex.cloud.video.v1.stream_line_service_pb2.ListStreamLinesResponse,
    ]
    """List lines for channel."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.CreateStreamLineRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create stream line."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.UpdateStreamLineRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update stream line."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.DeleteStreamLineRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete stream line."""

    PerformAction: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.PerformLineActionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Perform an action on the line."""

    GetStreamKey: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.GetStreamKeyRequest,
        yandex.cloud.video.v1.stream_line_pb2.PushStreamKey,
    ]
    """Returns unique stream key."""

    UpdateStreamKey: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.stream_line_service_pb2.UpdateStreamKeyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Change stream key."""

class StreamLineServiceServicer(metaclass=abc.ABCMeta):
    """Stream line management service."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.GetStreamLineRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.stream_line_pb2.StreamLine, collections.abc.Awaitable[yandex.cloud.video.v1.stream_line_pb2.StreamLine]]:
        """Returns the specific stream line."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.ListStreamLinesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.stream_line_service_pb2.ListStreamLinesResponse, collections.abc.Awaitable[yandex.cloud.video.v1.stream_line_service_pb2.ListStreamLinesResponse]]:
        """List lines for channel."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.CreateStreamLineRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Create stream line."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.UpdateStreamLineRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Update stream line."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.DeleteStreamLineRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Delete stream line."""

    @abc.abstractmethod
    def PerformAction(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.PerformLineActionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Perform an action on the line."""

    @abc.abstractmethod
    def GetStreamKey(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.GetStreamKeyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.stream_line_pb2.PushStreamKey, collections.abc.Awaitable[yandex.cloud.video.v1.stream_line_pb2.PushStreamKey]]:
        """Returns unique stream key."""

    @abc.abstractmethod
    def UpdateStreamKey(
        self,
        request: yandex.cloud.video.v1.stream_line_service_pb2.UpdateStreamKeyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Change stream key."""

def add_StreamLineServiceServicer_to_server(servicer: StreamLineServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...