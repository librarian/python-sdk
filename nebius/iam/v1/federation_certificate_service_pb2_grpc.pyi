"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nebius.common.v1.operation_pb2
import nebius.iam.v1.federation_certificate_pb2
import nebius.iam.v1.federation_certificate_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class FederationCertificateServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.CreateFederationCertificateRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Get: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.GetFederationCertificateRequest,
        nebius.iam.v1.federation_certificate_pb2.FederationCertificate,
    ]

    ListByFederation: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.ListFederationCertificateByFederationRequest,
        nebius.iam.v1.federation_certificate_service_pb2.ListFederationCertificateResponse,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.UpdateFederationCertificateRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.DeleteFederationCertificateRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

class FederationCertificateServiceAsyncStub:
    Create: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.CreateFederationCertificateRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.GetFederationCertificateRequest,
        nebius.iam.v1.federation_certificate_pb2.FederationCertificate,
    ]

    ListByFederation: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.ListFederationCertificateByFederationRequest,
        nebius.iam.v1.federation_certificate_service_pb2.ListFederationCertificateResponse,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.UpdateFederationCertificateRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.federation_certificate_service_pb2.DeleteFederationCertificateRequest,
        nebius.common.v1.operation_pb2.Operation,
    ]

class FederationCertificateServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Create(
        self,
        request: nebius.iam.v1.federation_certificate_service_pb2.CreateFederationCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Get(
        self,
        request: nebius.iam.v1.federation_certificate_service_pb2.GetFederationCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.iam.v1.federation_certificate_pb2.FederationCertificate, collections.abc.Awaitable[nebius.iam.v1.federation_certificate_pb2.FederationCertificate]]: ...

    @abc.abstractmethod
    def ListByFederation(
        self,
        request: nebius.iam.v1.federation_certificate_service_pb2.ListFederationCertificateByFederationRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.iam.v1.federation_certificate_service_pb2.ListFederationCertificateResponse, collections.abc.Awaitable[nebius.iam.v1.federation_certificate_service_pb2.ListFederationCertificateResponse]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: nebius.iam.v1.federation_certificate_service_pb2.UpdateFederationCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: nebius.iam.v1.federation_certificate_service_pb2.DeleteFederationCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_pb2.Operation, collections.abc.Awaitable[nebius.common.v1.operation_pb2.Operation]]: ...

def add_FederationCertificateServiceServicer_to_server(servicer: FederationCertificateServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
