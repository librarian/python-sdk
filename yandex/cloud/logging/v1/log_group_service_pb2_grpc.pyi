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
import yandex.cloud.logging.v1.log_group_pb2
import yandex.cloud.logging.v1.log_group_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class LogGroupServiceStub:
    """A set of methods for managing log groups."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupRequest,
        yandex.cloud.logging.v1.log_group_pb2.LogGroup,
    ]
    """Returns the specified log group.

    To get the list of all available log groups, make a [List] request.
    """

    Stats: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsResponse,
    ]
    """Returns stats for the specified log group."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsResponse,
    ]
    """Retrieves the list of log groups in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.CreateLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a log group in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.UpdateLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified log group."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.DeleteLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified log group."""

    ListResources: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesResponse,
    ]
    """Retrieves the resources (type and IDs) in the specified log group."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsResponse,
    ]
    """Lists operations for the specified log group."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified log group."""

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the specified log group."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified log group."""

class LogGroupServiceAsyncStub:
    """A set of methods for managing log groups."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupRequest,
        yandex.cloud.logging.v1.log_group_pb2.LogGroup,
    ]
    """Returns the specified log group.

    To get the list of all available log groups, make a [List] request.
    """

    Stats: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsResponse,
    ]
    """Returns stats for the specified log group."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsResponse,
    ]
    """Retrieves the list of log groups in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.CreateLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a log group in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.UpdateLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified log group."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.DeleteLogGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified log group."""

    ListResources: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesResponse,
    ]
    """Retrieves the resources (type and IDs) in the specified log group."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsRequest,
        yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsResponse,
    ]
    """Lists operations for the specified log group."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified log group."""

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the specified log group."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified log group."""

class LogGroupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing log groups."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.logging.v1.log_group_pb2.LogGroup, collections.abc.Awaitable[yandex.cloud.logging.v1.log_group_pb2.LogGroup]]:
        """Returns the specified log group.

        To get the list of all available log groups, make a [List] request.
        """

    @abc.abstractmethod
    def Stats(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsResponse, collections.abc.Awaitable[yandex.cloud.logging.v1.log_group_service_pb2.GetLogGroupStatsResponse]]:
        """Returns stats for the specified log group."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsResponse, collections.abc.Awaitable[yandex.cloud.logging.v1.log_group_service_pb2.ListLogGroupsResponse]]:
        """Retrieves the list of log groups in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.CreateLogGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a log group in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.UpdateLogGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified log group."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.DeleteLogGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified log group."""

    @abc.abstractmethod
    def ListResources(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesResponse, collections.abc.Awaitable[yandex.cloud.logging.v1.log_group_service_pb2.ListResourcesResponse]]:
        """Retrieves the resources (type and IDs) in the specified log group."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsResponse, collections.abc.Awaitable[yandex.cloud.logging.v1.log_group_service_pb2.ListOperationsResponse]]:
        """Lists operations for the specified log group."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """Lists existing access bindings for the specified log group."""

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the specified log group."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the specified log group."""

def add_LogGroupServiceServicer_to_server(servicer: LogGroupServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...