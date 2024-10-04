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
import nebius.compute.v1.filesystem_pb2
import nebius.compute.v1.filesystem_service_pb2
import nebius.compute.v1.operation_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class FilesystemServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.GetFilesystemRequest,
        nebius.compute.v1.filesystem_pb2.Filesystem,
    ]

    GetByName: grpc.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.compute.v1.filesystem_pb2.Filesystem,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.ListFilesystemsRequest,
        nebius.compute.v1.filesystem_service_pb2.ListFilesystemsResponse,
    ]

    Create: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.CreateFilesystemRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.UpdateFilesystemRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.DeleteFilesystemRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    ListOperationsByParent: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class FilesystemServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.GetFilesystemRequest,
        nebius.compute.v1.filesystem_pb2.Filesystem,
    ]

    GetByName: grpc.aio.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.compute.v1.filesystem_pb2.Filesystem,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.ListFilesystemsRequest,
        nebius.compute.v1.filesystem_service_pb2.ListFilesystemsResponse,
    ]

    Create: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.CreateFilesystemRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.UpdateFilesystemRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.filesystem_service_pb2.DeleteFilesystemRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    ListOperationsByParent: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class FilesystemServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.compute.v1.filesystem_service_pb2.GetFilesystemRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.filesystem_pb2.Filesystem, collections.abc.Awaitable[nebius.compute.v1.filesystem_pb2.Filesystem]]: ...

    @abc.abstractmethod
    def GetByName(
        self,
        request: nebius.common.v1.metadata_pb2.GetByNameRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.filesystem_pb2.Filesystem, collections.abc.Awaitable[nebius.compute.v1.filesystem_pb2.Filesystem]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.compute.v1.filesystem_service_pb2.ListFilesystemsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.filesystem_service_pb2.ListFilesystemsResponse, collections.abc.Awaitable[nebius.compute.v1.filesystem_service_pb2.ListFilesystemsResponse]]: ...

    @abc.abstractmethod
    def Create(
        self,
        request: nebius.compute.v1.filesystem_service_pb2.CreateFilesystemRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: nebius.compute.v1.filesystem_service_pb2.UpdateFilesystemRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: nebius.compute.v1.filesystem_service_pb2.DeleteFilesystemRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def ListOperationsByParent(
        self,
        request: nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_service_pb2.ListOperationsResponse, collections.abc.Awaitable[nebius.common.v1.operation_service_pb2.ListOperationsResponse]]: ...

def add_FilesystemServiceServicer_to_server(servicer: FilesystemServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
