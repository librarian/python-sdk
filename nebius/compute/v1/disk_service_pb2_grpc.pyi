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
import nebius.common.v1.operation_service_pb2
import nebius.compute.v1.disk_pb2
import nebius.compute.v1.disk_service_pb2
import nebius.compute.v1.operation_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DiskServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.GetDiskRequest,
        nebius.compute.v1.disk_pb2.Disk,
    ]

    GetByName: grpc.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.compute.v1.disk_pb2.Disk,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.ListDisksRequest,
        nebius.compute.v1.disk_service_pb2.ListDisksResponse,
    ]

    Create: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.CreateDiskRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.UpdateDiskRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.DeleteDiskRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    ListOperationsByParent: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class DiskServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.GetDiskRequest,
        nebius.compute.v1.disk_pb2.Disk,
    ]

    GetByName: grpc.aio.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.compute.v1.disk_pb2.Disk,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.ListDisksRequest,
        nebius.compute.v1.disk_service_pb2.ListDisksResponse,
    ]

    Create: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.CreateDiskRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.UpdateDiskRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.disk_service_pb2.DeleteDiskRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    ListOperationsByParent: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class DiskServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.compute.v1.disk_service_pb2.GetDiskRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.disk_pb2.Disk, collections.abc.Awaitable[nebius.compute.v1.disk_pb2.Disk]]: ...

    @abc.abstractmethod
    def GetByName(
        self,
        request: nebius.common.v1.metadata_pb2.GetByNameRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.disk_pb2.Disk, collections.abc.Awaitable[nebius.compute.v1.disk_pb2.Disk]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.compute.v1.disk_service_pb2.ListDisksRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.disk_service_pb2.ListDisksResponse, collections.abc.Awaitable[nebius.compute.v1.disk_service_pb2.ListDisksResponse]]: ...

    @abc.abstractmethod
    def Create(
        self,
        request: nebius.compute.v1.disk_service_pb2.CreateDiskRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: nebius.compute.v1.disk_service_pb2.UpdateDiskRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: nebius.compute.v1.disk_service_pb2.DeleteDiskRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def ListOperationsByParent(
        self,
        request: nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_service_pb2.ListOperationsResponse, collections.abc.Awaitable[nebius.common.v1.operation_service_pb2.ListOperationsResponse]]: ...

def add_DiskServiceServicer_to_server(servicer: DiskServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
