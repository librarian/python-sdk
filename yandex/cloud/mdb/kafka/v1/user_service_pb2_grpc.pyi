"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.kafka.v1.user_pb2
import yandex.cloud.mdb.kafka.v1.user_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class UserServiceStub:
    """A set of methods for managing Kafka users."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.GetUserRequest,
        yandex.cloud.mdb.kafka.v1.user_pb2.User,
    ]
    """Returns the specified Kafka user.

    To get the list of available Kafka users, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.ListUsersRequest,
        yandex.cloud.mdb.kafka.v1.user_service_pb2.ListUsersResponse,
    ]
    """Retrieves the list of Kafka users in the specified cluster."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.CreateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a Kafka user in the specified cluster."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.UpdateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified Kafka user."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.DeleteUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified Kafka user."""

    GrantPermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.GrantUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Grants permission to the specified Kafka user."""

    RevokePermission: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.RevokeUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revokes permission from the specified Kafka user."""

class UserServiceAsyncStub:
    """A set of methods for managing Kafka users."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.GetUserRequest,
        yandex.cloud.mdb.kafka.v1.user_pb2.User,
    ]
    """Returns the specified Kafka user.

    To get the list of available Kafka users, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.ListUsersRequest,
        yandex.cloud.mdb.kafka.v1.user_service_pb2.ListUsersResponse,
    ]
    """Retrieves the list of Kafka users in the specified cluster."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.CreateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a Kafka user in the specified cluster."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.UpdateUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified Kafka user."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.DeleteUserRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified Kafka user."""

    GrantPermission: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.GrantUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Grants permission to the specified Kafka user."""

    RevokePermission: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.user_service_pb2.RevokeUserPermissionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revokes permission from the specified Kafka user."""

class UserServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Kafka users."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.kafka.v1.user_service_pb2.GetUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.kafka.v1.user_pb2.User, collections.abc.Awaitable[yandex.cloud.mdb.kafka.v1.user_pb2.User]]:
        """Returns the specified Kafka user.

        To get the list of available Kafka users, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.kafka.v1.user_service_pb2.ListUsersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.kafka.v1.user_service_pb2.ListUsersResponse, collections.abc.Awaitable[yandex.cloud.mdb.kafka.v1.user_service_pb2.ListUsersResponse]]:
        """Retrieves the list of Kafka users in the specified cluster."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.kafka.v1.user_service_pb2.CreateUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a Kafka user in the specified cluster."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.kafka.v1.user_service_pb2.UpdateUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified Kafka user."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.kafka.v1.user_service_pb2.DeleteUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified Kafka user."""

    @abc.abstractmethod
    def GrantPermission(
        self,
        request: yandex.cloud.mdb.kafka.v1.user_service_pb2.GrantUserPermissionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Grants permission to the specified Kafka user."""

    @abc.abstractmethod
    def RevokePermission(
        self,
        request: yandex.cloud.mdb.kafka.v1.user_service_pb2.RevokeUserPermissionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Revokes permission from the specified Kafka user."""

def add_UserServiceServicer_to_server(servicer: UserServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
