"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.iam.v1.refresh_token_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class RefreshTokenServiceStub:
    """A set of methods for managing Refresh Tokens."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.refresh_token_service_pb2.ListRefreshTokensRequest,
        yandex.cloud.iam.v1.refresh_token_service_pb2.ListRefreshTokensResponse,
    ]
    """List subjects Refresh Tokens."""

    Revoke: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.refresh_token_service_pb2.RevokeRefreshTokenRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revoke Refresh Tokens. Several Refresh Tokens can be revoked by one request."""

class RefreshTokenServiceAsyncStub:
    """A set of methods for managing Refresh Tokens."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.refresh_token_service_pb2.ListRefreshTokensRequest,
        yandex.cloud.iam.v1.refresh_token_service_pb2.ListRefreshTokensResponse,
    ]
    """List subjects Refresh Tokens."""

    Revoke: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.refresh_token_service_pb2.RevokeRefreshTokenRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revoke Refresh Tokens. Several Refresh Tokens can be revoked by one request."""

class RefreshTokenServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Refresh Tokens."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.iam.v1.refresh_token_service_pb2.ListRefreshTokensRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iam.v1.refresh_token_service_pb2.ListRefreshTokensResponse, collections.abc.Awaitable[yandex.cloud.iam.v1.refresh_token_service_pb2.ListRefreshTokensResponse]]:
        """List subjects Refresh Tokens."""

    @abc.abstractmethod
    def Revoke(
        self,
        request: yandex.cloud.iam.v1.refresh_token_service_pb2.RevokeRefreshTokenRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Revoke Refresh Tokens. Several Refresh Tokens can be revoked by one request."""

def add_RefreshTokenServiceServicer_to_server(servicer: RefreshTokenServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
