"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.assistants.v1.users.user_pb2
import yandex.cloud.ai.assistants.v1.users.user_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class UserServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.CreateUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_pb2.User,
    ]

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.GetUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_pb2.User,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.UpdateUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_pb2.User,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.DeleteUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.DeleteUserResponse,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.ListUsersRequest,
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.ListUsersResponse,
    ]

class UserServiceAsyncStub:
    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.CreateUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_pb2.User,
    ]

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.GetUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_pb2.User,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.UpdateUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_pb2.User,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.DeleteUserRequest,
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.DeleteUserResponse,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.ListUsersRequest,
        yandex.cloud.ai.assistants.v1.users.user_service_pb2.ListUsersResponse,
    ]

class UserServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.ai.assistants.v1.users.user_service_pb2.CreateUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.users.user_pb2.User, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.users.user_pb2.User]]: ...

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.ai.assistants.v1.users.user_service_pb2.GetUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.users.user_pb2.User, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.users.user_pb2.User]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.ai.assistants.v1.users.user_service_pb2.UpdateUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.users.user_pb2.User, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.users.user_pb2.User]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.ai.assistants.v1.users.user_service_pb2.DeleteUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.users.user_service_pb2.DeleteUserResponse, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.users.user_service_pb2.DeleteUserResponse]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.ai.assistants.v1.users.user_service_pb2.ListUsersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.users.user_service_pb2.ListUsersResponse, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.users.user_service_pb2.ListUsersResponse]]: ...

def add_UserServiceServicer_to_server(servicer: UserServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
