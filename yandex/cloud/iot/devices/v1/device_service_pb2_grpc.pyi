"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.iot.devices.v1.device_pb2
import yandex.cloud.iot.devices.v1.device_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DeviceServiceStub:
    """A set of methods for managing devices."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.GetDeviceRequest,
        yandex.cloud.iot.devices.v1.device_pb2.Device,
    ]
    """Returns the specified device.

    To get the list of available devices, make a [List] request.
    """

    GetByName: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.GetByNameDeviceRequest,
        yandex.cloud.iot.devices.v1.device_pb2.Device,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicesRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicesResponse,
    ]
    """Retrieves the list of devices in the specified registry."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.CreateDeviceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a device in the specified registry."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.UpdateDeviceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified device."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDeviceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified device."""

    ListCertificates: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceCertificatesRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceCertificatesResponse,
    ]
    """Retrieves the list of device certificates for the specified device."""

    AddCertificate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.AddDeviceCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds a certificate."""

    DeleteCertificate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDeviceCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified device certificate."""

    ListPasswords: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicePasswordsRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicePasswordsResponse,
    ]
    """Retrieves the list of passwords for the specified device."""

    AddPassword: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.AddDevicePasswordRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds password for the specified device."""

    DeletePassword: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDevicePasswordRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified password."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceOperationsRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceOperationsResponse,
    ]
    """Lists operations for the specified device."""

class DeviceServiceAsyncStub:
    """A set of methods for managing devices."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.GetDeviceRequest,
        yandex.cloud.iot.devices.v1.device_pb2.Device,
    ]
    """Returns the specified device.

    To get the list of available devices, make a [List] request.
    """

    GetByName: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.GetByNameDeviceRequest,
        yandex.cloud.iot.devices.v1.device_pb2.Device,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicesRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicesResponse,
    ]
    """Retrieves the list of devices in the specified registry."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.CreateDeviceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a device in the specified registry."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.UpdateDeviceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified device."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDeviceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified device."""

    ListCertificates: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceCertificatesRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceCertificatesResponse,
    ]
    """Retrieves the list of device certificates for the specified device."""

    AddCertificate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.AddDeviceCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds a certificate."""

    DeleteCertificate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDeviceCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified device certificate."""

    ListPasswords: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicePasswordsRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicePasswordsResponse,
    ]
    """Retrieves the list of passwords for the specified device."""

    AddPassword: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.AddDevicePasswordRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds password for the specified device."""

    DeletePassword: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDevicePasswordRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified password."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceOperationsRequest,
        yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceOperationsResponse,
    ]
    """Lists operations for the specified device."""

class DeviceServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing devices."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.GetDeviceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iot.devices.v1.device_pb2.Device, collections.abc.Awaitable[yandex.cloud.iot.devices.v1.device_pb2.Device]]:
        """Returns the specified device.

        To get the list of available devices, make a [List] request.
        """

    @abc.abstractmethod
    def GetByName(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.GetByNameDeviceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iot.devices.v1.device_pb2.Device, collections.abc.Awaitable[yandex.cloud.iot.devices.v1.device_pb2.Device]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicesResponse, collections.abc.Awaitable[yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicesResponse]]:
        """Retrieves the list of devices in the specified registry."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.CreateDeviceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a device in the specified registry."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.UpdateDeviceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified device."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDeviceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified device."""

    @abc.abstractmethod
    def ListCertificates(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceCertificatesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceCertificatesResponse, collections.abc.Awaitable[yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceCertificatesResponse]]:
        """Retrieves the list of device certificates for the specified device."""

    @abc.abstractmethod
    def AddCertificate(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.AddDeviceCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Adds a certificate."""

    @abc.abstractmethod
    def DeleteCertificate(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDeviceCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified device certificate."""

    @abc.abstractmethod
    def ListPasswords(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicePasswordsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicePasswordsResponse, collections.abc.Awaitable[yandex.cloud.iot.devices.v1.device_service_pb2.ListDevicePasswordsResponse]]:
        """Retrieves the list of passwords for the specified device."""

    @abc.abstractmethod
    def AddPassword(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.AddDevicePasswordRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Adds password for the specified device."""

    @abc.abstractmethod
    def DeletePassword(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.DeleteDevicePasswordRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified password."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceOperationsResponse, collections.abc.Awaitable[yandex.cloud.iot.devices.v1.device_service_pb2.ListDeviceOperationsResponse]]:
        """Lists operations for the specified device."""

def add_DeviceServiceServicer_to_server(servicer: DeviceServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
