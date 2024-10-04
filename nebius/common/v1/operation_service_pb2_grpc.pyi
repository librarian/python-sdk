"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nebius.common.v1.operation_pb2
import nebius.common.v1.operation_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class OperationServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.common.v1.operation_service_pb2.GetOperationRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.common.v1.operation_service_pb2.ListOperationsRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class OperationServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.common.v1.operation_service_pb2.GetOperationRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.common.v1.operation_service_pb2.ListOperationsRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class OperationServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.common.v1.operation_service_pb2.GetOperationRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.common.v1.operation_service_pb2.ListOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_service_pb2.ListOperationsResponse, collections.abc.Awaitable[nebius.common.v1.operation_service_pb2.ListOperationsResponse]]: ...

def add_OperationServiceServicer_to_server(servicer: OperationServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
