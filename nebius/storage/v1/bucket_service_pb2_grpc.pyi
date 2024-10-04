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
import nebius.storage.v1.bucket_pb2
import nebius.storage.v1.bucket_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class BucketServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.GetBucketRequest,
        nebius.storage.v1.bucket_pb2.Bucket,
    ]

    GetByName: grpc.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.storage.v1.bucket_pb2.Bucket,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.ListBucketsRequest,
        nebius.storage.v1.bucket_service_pb2.ListBucketsResponse,
    ]

    Create: grpc.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.CreateBucketRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.UpdateBucketRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.DeleteBucketRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

class BucketServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.GetBucketRequest,
        nebius.storage.v1.bucket_pb2.Bucket,
    ]

    GetByName: grpc.aio.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.storage.v1.bucket_pb2.Bucket,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.ListBucketsRequest,
        nebius.storage.v1.bucket_service_pb2.ListBucketsResponse,
    ]

    Create: grpc.aio.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.CreateBucketRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.UpdateBucketRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        nebius.storage.v1.bucket_service_pb2.DeleteBucketRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

class BucketServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.storage.v1.bucket_service_pb2.GetBucketRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.storage.v1.bucket_pb2.Bucket, collections.abc.Awaitable[nebius.storage.v1.bucket_pb2.Bucket]]: ...

    @abc.abstractmethod
    def GetByName(
        self,
        request: nebius.common.v1.metadata_pb2.GetByNameRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.storage.v1.bucket_pb2.Bucket, collections.abc.Awaitable[nebius.storage.v1.bucket_pb2.Bucket]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.storage.v1.bucket_service_pb2.ListBucketsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.storage.v1.bucket_service_pb2.ListBucketsResponse, collections.abc.Awaitable[nebius.storage.v1.bucket_service_pb2.ListBucketsResponse]]: ...

    @abc.abstractmethod
    def Create(
        self,
        request: nebius.storage.v1.bucket_service_pb2.CreateBucketRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: nebius.storage.v1.bucket_service_pb2.UpdateBucketRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: nebius.storage.v1.bucket_service_pb2.DeleteBucketRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

def add_BucketServiceServicer_to_server(servicer: BucketServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
