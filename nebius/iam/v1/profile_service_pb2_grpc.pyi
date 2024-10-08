"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nebius.iam.v1.profile_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ProfileServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.profile_service_pb2.GetProfileRequest,
        nebius.iam.v1.profile_service_pb2.GetProfileResponse,
    ]

class ProfileServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.profile_service_pb2.GetProfileRequest,
        nebius.iam.v1.profile_service_pb2.GetProfileResponse,
    ]

class ProfileServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.iam.v1.profile_service_pb2.GetProfileRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.iam.v1.profile_service_pb2.GetProfileResponse, collections.abc.Awaitable[nebius.iam.v1.profile_service_pb2.GetProfileResponse]]: ...

def add_ProfileServiceServicer_to_server(servicer: ProfileServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
