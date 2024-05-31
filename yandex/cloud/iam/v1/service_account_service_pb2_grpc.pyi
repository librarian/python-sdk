"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.access.access_pb2
import yandex.cloud.iam.v1.service_account_pb2
import yandex.cloud.iam.v1.service_account_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ServiceAccountServiceStub:
    """A set of methods for managing ServiceAccount resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.GetServiceAccountRequest,
        yandex.cloud.iam.v1.service_account_pb2.ServiceAccount,
    ]
    """Returns the specified ServiceAccount resource.

    To get the list of available ServiceAccount resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsRequest,
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsResponse,
    ]
    """Retrieves the list of ServiceAccount resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.CreateServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a service account in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.UpdateServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified service account."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.DeleteServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified service account."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the specified service account.
    """

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the service account."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified service account."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsRequest,
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsResponse,
    ]
    """Lists operations for the specified service account."""

class ServiceAccountServiceAsyncStub:
    """A set of methods for managing ServiceAccount resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.GetServiceAccountRequest,
        yandex.cloud.iam.v1.service_account_pb2.ServiceAccount,
    ]
    """Returns the specified ServiceAccount resource.

    To get the list of available ServiceAccount resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsRequest,
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsResponse,
    ]
    """Retrieves the list of ServiceAccount resources in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.CreateServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a service account in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.UpdateServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified service account."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.DeleteServiceAccountRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified service account."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the specified service account.
    """

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the service account."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified service account."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsRequest,
        yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsResponse,
    ]
    """Lists operations for the specified service account."""

class ServiceAccountServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing ServiceAccount resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.GetServiceAccountRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iam.v1.service_account_pb2.ServiceAccount, collections.abc.Awaitable[yandex.cloud.iam.v1.service_account_pb2.ServiceAccount]]:
        """Returns the specified ServiceAccount resource.

        To get the list of available ServiceAccount resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsResponse, collections.abc.Awaitable[yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountsResponse]]:
        """Retrieves the list of ServiceAccount resources in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.CreateServiceAccountRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a service account in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.UpdateServiceAccountRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified service account."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.DeleteServiceAccountRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified service account."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """access

        Lists access bindings for the specified service account.
        """

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the service account."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the specified service account."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsResponse, collections.abc.Awaitable[yandex.cloud.iam.v1.service_account_service_pb2.ListServiceAccountOperationsResponse]]:
        """Lists operations for the specified service account."""

def add_ServiceAccountServiceServicer_to_server(servicer: ServiceAccountServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
