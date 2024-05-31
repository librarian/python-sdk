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
import yandex.cloud.operation.operation_pb2
import yandex.cloud.organizationmanager.v1.organization_pb2
import yandex.cloud.organizationmanager.v1.organization_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class OrganizationServiceStub:
    """A set of methods for managing Organization resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.GetOrganizationRequest,
        yandex.cloud.organizationmanager.v1.organization_pb2.Organization,
    ]
    """Returns the specified Organization resource.

    To get the list of available Organization resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationsRequest,
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationsResponse,
    ]
    """Retrieves the list of Organization resources."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.UpdateOrganizationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified organization."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationOperationsRequest,
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationOperationsResponse,
    ]
    """Lists operations for the specified organization."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the specified organization.
    """

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the specified organization."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified organization."""

class OrganizationServiceAsyncStub:
    """A set of methods for managing Organization resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.GetOrganizationRequest,
        yandex.cloud.organizationmanager.v1.organization_pb2.Organization,
    ]
    """Returns the specified Organization resource.

    To get the list of available Organization resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationsRequest,
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationsResponse,
    ]
    """Retrieves the list of Organization resources."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.UpdateOrganizationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified organization."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationOperationsRequest,
        yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationOperationsResponse,
    ]
    """Lists operations for the specified organization."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the specified organization.
    """

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the specified organization."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified organization."""

class OrganizationServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Organization resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.organizationmanager.v1.organization_service_pb2.GetOrganizationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.organization_pb2.Organization, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.organization_pb2.Organization]]:
        """Returns the specified Organization resource.

        To get the list of available Organization resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationsResponse, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationsResponse]]:
        """Retrieves the list of Organization resources."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.organizationmanager.v1.organization_service_pb2.UpdateOrganizationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified organization."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationOperationsResponse, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.organization_service_pb2.ListOrganizationOperationsResponse]]:
        """Lists operations for the specified organization."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """access

        Lists access bindings for the specified organization.
        """

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the specified organization."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the specified organization."""

def add_OrganizationServiceServicer_to_server(servicer: OrganizationServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
