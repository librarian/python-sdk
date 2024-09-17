"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.iam.v1.workload.oidc.federation_pb2
import yandex.cloud.iam.v1.workload.oidc.federation_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class FederationServiceStub:
    """A set of methods for managing OIDC workload identity federations."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.GetFederationRequest,
        yandex.cloud.iam.v1.workload.oidc.federation_pb2.Federation,
    ]
    """Returns the specified OIDC workload identity federation.

    To get the list of available OIDC workload identity federation, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.ListFederationsRequest,
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.ListFederationsResponse,
    ]
    """Retrieves the list of OIDC workload identity federations in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.CreateFederationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an OIDC workload identity federation in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.UpdateFederationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified OIDC workload identity federation."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.DeleteFederationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified OIDC workload identity federation."""

class FederationServiceAsyncStub:
    """A set of methods for managing OIDC workload identity federations."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.GetFederationRequest,
        yandex.cloud.iam.v1.workload.oidc.federation_pb2.Federation,
    ]
    """Returns the specified OIDC workload identity federation.

    To get the list of available OIDC workload identity federation, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.ListFederationsRequest,
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.ListFederationsResponse,
    ]
    """Retrieves the list of OIDC workload identity federations in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.CreateFederationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an OIDC workload identity federation in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.UpdateFederationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified OIDC workload identity federation."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.DeleteFederationRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified OIDC workload identity federation."""

class FederationServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing OIDC workload identity federations."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.GetFederationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iam.v1.workload.oidc.federation_pb2.Federation, collections.abc.Awaitable[yandex.cloud.iam.v1.workload.oidc.federation_pb2.Federation]]:
        """Returns the specified OIDC workload identity federation.

        To get the list of available OIDC workload identity federation, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.ListFederationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.ListFederationsResponse, collections.abc.Awaitable[yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.ListFederationsResponse]]:
        """Retrieves the list of OIDC workload identity federations in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.CreateFederationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates an OIDC workload identity federation in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.UpdateFederationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified OIDC workload identity federation."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.iam.v1.workload.oidc.federation_service_pb2.DeleteFederationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified OIDC workload identity federation."""

def add_FederationServiceServicer_to_server(servicer: FederationServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...