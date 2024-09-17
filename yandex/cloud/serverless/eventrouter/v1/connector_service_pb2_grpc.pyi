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
import yandex.cloud.serverless.eventrouter.v1.connector_pb2
import yandex.cloud.serverless.eventrouter.v1.connector_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ConnectorServiceStub:
    """A set of methods for managing connectors for serverless eventrouter."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.GetConnectorRequest,
        yandex.cloud.serverless.eventrouter.v1.connector_pb2.Connector,
    ]
    """Returns the specified bus.
    To get the list of all available connectors, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorsRequest,
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorsResponse,
    ]
    """Retrieves the list of connectors in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.CreateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a connector in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.UpdateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified connector."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.DeleteConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified connector."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.StartConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified connector."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.StopConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified connector."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified bus."""

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the connector."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified connector."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorOperationsRequest,
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorOperationsResponse,
    ]
    """Lists operations for the specified connector."""

class ConnectorServiceAsyncStub:
    """A set of methods for managing connectors for serverless eventrouter."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.GetConnectorRequest,
        yandex.cloud.serverless.eventrouter.v1.connector_pb2.Connector,
    ]
    """Returns the specified bus.
    To get the list of all available connectors, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorsRequest,
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorsResponse,
    ]
    """Retrieves the list of connectors in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.CreateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a connector in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.UpdateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified connector."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.DeleteConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified connector."""

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.StartConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified connector."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.StopConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified connector."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified bus."""

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the connector."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified connector."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorOperationsRequest,
        yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorOperationsResponse,
    ]
    """Lists operations for the specified connector."""

class ConnectorServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing connectors for serverless eventrouter."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.GetConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.eventrouter.v1.connector_pb2.Connector, collections.abc.Awaitable[yandex.cloud.serverless.eventrouter.v1.connector_pb2.Connector]]:
        """Returns the specified bus.
        To get the list of all available connectors, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorsResponse, collections.abc.Awaitable[yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorsResponse]]:
        """Retrieves the list of connectors in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.CreateConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a connector in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.UpdateConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified connector."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.DeleteConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified connector."""

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.StartConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Starts the specified connector."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.StopConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stops the specified connector."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """Lists existing access bindings for the specified bus."""

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the connector."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the specified connector."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorOperationsResponse, collections.abc.Awaitable[yandex.cloud.serverless.eventrouter.v1.connector_service_pb2.ListConnectorOperationsResponse]]:
        """Lists operations for the specified connector."""

def add_ConnectorServiceServicer_to_server(servicer: ConnectorServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
