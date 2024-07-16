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
import yandex.cloud.video.v1.episode_pb2
import yandex.cloud.video.v1.episode_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class EpisodeServiceStub:
    """Episode management service."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodeRequest,
        yandex.cloud.video.v1.episode_pb2.Episode,
    ]
    """Returns the specific channel."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.ListEpisodesRequest,
        yandex.cloud.video.v1.episode_service_pb2.ListEpisodesResponse,
    ]
    """List episodes for stream or line."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.CreateEpisodeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create episode."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.UpdateEpisodeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update episode."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.DeleteEpisodeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete episode."""

    PerformAction: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.PerformEpisodeActionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Perform an action on the episode."""

    GetPlayerURL: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodePlayerURLRequest,
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodePlayerURLResponse,
    ]
    """Returns url to the player."""

    GetManifests: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodeManifestsRequest,
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodeManifestsResponse,
    ]
    """Returns manifest urls."""

class EpisodeServiceAsyncStub:
    """Episode management service."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodeRequest,
        yandex.cloud.video.v1.episode_pb2.Episode,
    ]
    """Returns the specific channel."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.ListEpisodesRequest,
        yandex.cloud.video.v1.episode_service_pb2.ListEpisodesResponse,
    ]
    """List episodes for stream or line."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.CreateEpisodeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create episode."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.UpdateEpisodeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update episode."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.DeleteEpisodeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete episode."""

    PerformAction: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.PerformEpisodeActionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Perform an action on the episode."""

    GetPlayerURL: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodePlayerURLRequest,
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodePlayerURLResponse,
    ]
    """Returns url to the player."""

    GetManifests: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodeManifestsRequest,
        yandex.cloud.video.v1.episode_service_pb2.GetEpisodeManifestsResponse,
    ]
    """Returns manifest urls."""

class EpisodeServiceServicer(metaclass=abc.ABCMeta):
    """Episode management service."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.GetEpisodeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.episode_pb2.Episode, collections.abc.Awaitable[yandex.cloud.video.v1.episode_pb2.Episode]]:
        """Returns the specific channel."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.ListEpisodesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.episode_service_pb2.ListEpisodesResponse, collections.abc.Awaitable[yandex.cloud.video.v1.episode_service_pb2.ListEpisodesResponse]]:
        """List episodes for stream or line."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.CreateEpisodeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Create episode."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.UpdateEpisodeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Update episode."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.DeleteEpisodeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Delete episode."""

    @abc.abstractmethod
    def PerformAction(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.PerformEpisodeActionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Perform an action on the episode."""

    @abc.abstractmethod
    def GetPlayerURL(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.GetEpisodePlayerURLRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.episode_service_pb2.GetEpisodePlayerURLResponse, collections.abc.Awaitable[yandex.cloud.video.v1.episode_service_pb2.GetEpisodePlayerURLResponse]]:
        """Returns url to the player."""

    @abc.abstractmethod
    def GetManifests(
        self,
        request: yandex.cloud.video.v1.episode_service_pb2.GetEpisodeManifestsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.episode_service_pb2.GetEpisodeManifestsResponse, collections.abc.Awaitable[yandex.cloud.video.v1.episode_service_pb2.GetEpisodeManifestsResponse]]:
        """Returns manifest urls."""

def add_EpisodeServiceServicer_to_server(servicer: EpisodeServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
