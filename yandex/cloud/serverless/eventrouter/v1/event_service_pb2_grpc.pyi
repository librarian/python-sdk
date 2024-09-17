"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing
import yandex.cloud.serverless.eventrouter.v1.event_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class EventServiceStub:
    """Service for put events to bus for serverless eventrouter."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Put: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.event_service_pb2.PutEventRequest,
        google.protobuf.empty_pb2.Empty,
    ]
    """Puts event to bus."""

class EventServiceAsyncStub:
    """Service for put events to bus for serverless eventrouter."""

    Put: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.event_service_pb2.PutEventRequest,
        google.protobuf.empty_pb2.Empty,
    ]
    """Puts event to bus."""

class EventServiceServicer(metaclass=abc.ABCMeta):
    """Service for put events to bus for serverless eventrouter."""

    @abc.abstractmethod
    def Put(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.event_service_pb2.PutEventRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]:
        """Puts event to bus."""

def add_EventServiceServicer_to_server(servicer: EventServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
