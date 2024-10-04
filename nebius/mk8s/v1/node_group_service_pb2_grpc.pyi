"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nebius.common.v1.metadata_pb2
import nebius.common.v1.operation_pb2
import nebius.mk8s.v1.node_group_pb2
import nebius.mk8s.v1.node_group_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class NodeGroupServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.GetNodeGroupRequest,
        nebius.mk8s.v1.node_group_pb2.NodeGroup,
    ]

    GetByName: grpc.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.mk8s.v1.node_group_pb2.NodeGroup,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.ListNodeGroupsRequest,
        nebius.mk8s.v1.node_group_service_pb2.ListNodeGroupsResponse,
    ]

    Create: grpc.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.CreateNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.UpdateNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.DeleteNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Upgrade: grpc.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.UpgradeNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

class NodeGroupServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.GetNodeGroupRequest,
        nebius.mk8s.v1.node_group_pb2.NodeGroup,
    ]

    GetByName: grpc.aio.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.mk8s.v1.node_group_pb2.NodeGroup,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.ListNodeGroupsRequest,
        nebius.mk8s.v1.node_group_service_pb2.ListNodeGroupsResponse,
    ]

    Create: grpc.aio.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.CreateNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.UpdateNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.DeleteNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Upgrade: grpc.aio.UnaryUnaryMultiCallable[
        nebius.mk8s.v1.node_group_service_pb2.UpgradeNodeGroupRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

class NodeGroupServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.mk8s.v1.node_group_service_pb2.GetNodeGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.mk8s.v1.node_group_pb2.NodeGroup, collections.abc.Awaitable[nebius.mk8s.v1.node_group_pb2.NodeGroup]]: ...

    @abc.abstractmethod
    def GetByName(
        self,
        request: nebius.common.v1.metadata_pb2.GetByNameRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.mk8s.v1.node_group_pb2.NodeGroup, collections.abc.Awaitable[nebius.mk8s.v1.node_group_pb2.NodeGroup]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.mk8s.v1.node_group_service_pb2.ListNodeGroupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.mk8s.v1.node_group_service_pb2.ListNodeGroupsResponse, collections.abc.Awaitable[nebius.mk8s.v1.node_group_service_pb2.ListNodeGroupsResponse]]: ...

    @abc.abstractmethod
    def Create(
        self,
        request: nebius.mk8s.v1.node_group_service_pb2.CreateNodeGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: nebius.mk8s.v1.node_group_service_pb2.UpdateNodeGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: nebius.mk8s.v1.node_group_service_pb2.DeleteNodeGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Upgrade(
        self,
        request: nebius.mk8s.v1.node_group_service_pb2.UpgradeNodeGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

def add_NodeGroupServiceServicer_to_server(servicer: NodeGroupServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...