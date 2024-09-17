"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetPrivateEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    private_endpoint_id: builtins.str
    """ID of the PrivateEndpoint resource to return.

    To get PrivateEndpoint resource ID make a [PrivateEndpointService.List]
    request.
    """
    def __init__(
        self,
        *,
        private_endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["private_endpoint_id", b"private_endpoint_id"]) -> None: ...

global___GetPrivateEndpointRequest = GetPrivateEndpointRequest

@typing.final
class InternalIpv4AddressSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the subnet that address belongs to."""
    address: builtins.str
    """Value of address."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "subnet_id", b"subnet_id"]) -> None: ...

global___InternalIpv4AddressSpec = InternalIpv4AddressSpec

@typing.final
class AddressSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    INTERNAL_IPV4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of IP address to associate with private endpoint."""
    @property
    def internal_ipv4_address_spec(self) -> global___InternalIpv4AddressSpec:
        """Internal ipv4 address specification."""

    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
        internal_ipv4_address_spec: global___InternalIpv4AddressSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["address", b"address", "address_id", b"address_id", "internal_ipv4_address_spec", b"internal_ipv4_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "address_id", b"address_id", "internal_ipv4_address_spec", b"internal_ipv4_address_spec"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["address", b"address"]) -> typing.Literal["address_id", "internal_ipv4_address_spec"] | None: ...

global___AddressSpec = AddressSpec

@typing.final
class CreatePrivateEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    DNS_OPTIONS_FIELD_NUMBER: builtins.int
    OBJECT_STORAGE_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a private endpoint in.

    To get a folder ID make a
    [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the private endpoint.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the private endpoint."""
    network_id: builtins.str
    """ID of the network to create a private endpoint in."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Private endpoint labels as `key:value` pairs."""

    @property
    def address_spec(self) -> global___AddressSpec:
        """Private endpoint address specification."""

    @property
    def dns_options(self) -> yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint.DnsOptions:
        """Private endpoint dns options."""

    @property
    def object_storage(self) -> yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint.ObjectStorage:
        """Yandex Cloud Object Storage."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        network_id: builtins.str = ...,
        address_spec: global___AddressSpec | None = ...,
        dns_options: yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint.DnsOptions | None = ...,
        object_storage: yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint.ObjectStorage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["address_spec", b"address_spec", "dns_options", b"dns_options", "object_storage", b"object_storage", "service", b"service"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address_spec", b"address_spec", "description", b"description", "dns_options", b"dns_options", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "network_id", b"network_id", "object_storage", b"object_storage", "service", b"service"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["service", b"service"]) -> typing.Literal["object_storage"] | None: ...

global___CreatePrivateEndpointRequest = CreatePrivateEndpointRequest

@typing.final
class CreatePrivateEndpointMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    private_endpoint_id: builtins.str
    """ID of the private endpoint that is being created."""
    def __init__(
        self,
        *,
        private_endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["private_endpoint_id", b"private_endpoint_id"]) -> None: ...

global___CreatePrivateEndpointMetadata = CreatePrivateEndpointMetadata

@typing.final
class UpdatePrivateEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    DNS_OPTIONS_FIELD_NUMBER: builtins.int
    private_endpoint_id: builtins.str
    """ID of the private endpoint to update.

    To get the private endpoint ID make a [PrivateEndpointService.List]
    request.
    """
    name: builtins.str
    """New name for the private endpoint.
    The name must be unique within the folder.
    """
    description: builtins.str
    """New description of the private endpoint."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the PrivateEndpoint should be
        updated.
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Private endpoint labels as `key:value` pairs.

        Existing set of labels is completely replaced by the provided set, so if
        you just want to add or remove a label:
        1. Get the current set of labels with a [PrivateEndpointService.Get]
        request.
        2. Add or remove a label in this set.
        3. Send the new set in this field.
        """

    @property
    def address_spec(self) -> global___AddressSpec:
        """Private endpoint address specification."""

    @property
    def dns_options(self) -> yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint.DnsOptions:
        """Private endpoint dns options."""

    def __init__(
        self,
        *,
        private_endpoint_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        address_spec: global___AddressSpec | None = ...,
        dns_options: yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint.DnsOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["address_spec", b"address_spec", "dns_options", b"dns_options", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address_spec", b"address_spec", "description", b"description", "dns_options", b"dns_options", "labels", b"labels", "name", b"name", "private_endpoint_id", b"private_endpoint_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdatePrivateEndpointRequest = UpdatePrivateEndpointRequest

@typing.final
class UpdatePrivateEndpointMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    private_endpoint_id: builtins.str
    """ID of the private endpoint that is being updated."""
    def __init__(
        self,
        *,
        private_endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["private_endpoint_id", b"private_endpoint_id"]) -> None: ...

global___UpdatePrivateEndpointMetadata = UpdatePrivateEndpointMetadata

@typing.final
class DeletePrivateEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    private_endpoint_id: builtins.str
    """ID of the private endpoint to delete.

    To get a private endpoint ID make a [PrivateEndpointService.List] request.
    """
    def __init__(
        self,
        *,
        private_endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["private_endpoint_id", b"private_endpoint_id"]) -> None: ...

global___DeletePrivateEndpointRequest = DeletePrivateEndpointRequest

@typing.final
class DeletePrivateEndpointMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    private_endpoint_id: builtins.str
    """ID of the private endpoint that is being deleted."""
    def __init__(
        self,
        *,
        private_endpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["private_endpoint_id", b"private_endpoint_id"]) -> None: ...

global___DeletePrivateEndpointMetadata = DeletePrivateEndpointMetadata

@typing.final
class ListPrivateEndpointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list private endpoints in.

    To get the folder ID use a
    [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of
    available results is larger than `page_size`, the service returns a
    [ListPrivateEndpointsResponse.next_page_token] that can be used to get the
    next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListPrivateEndpointsResponse.next_page_token] returned by a previous list
    request.
    """
    filter: builtins.str
    """A filter expression that filters PrivateEndpoint listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on
    [PrivateEndpoint.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match
    the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`. Example of a filter:
    `name=my-private-endpoint`.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["container", b"container", "folder_id", b"folder_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["container", b"container", "filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["container", b"container"]) -> typing.Literal["folder_id"] | None: ...

global___ListPrivateEndpointsRequest = ListPrivateEndpointsRequest

@typing.final
class ListPrivateEndpointsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_ENDPOINTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is
    greater than the specified [ListPrivateEndpointsRequest.page_size], use
    `next_page_token` as the value for the
    [ListPrivateEndpointsRequest.page_token] parameter in the next list
    request.

    Each subsequent page will have its own `next_page_token` to continue paging
    through the results.
    """
    @property
    def private_endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint]:
        """List of private endpoints."""

    def __init__(
        self,
        *,
        private_endpoints: collections.abc.Iterable[yandex.cloud.vpc.v1.privatelink.private_endpoint_pb2.PrivateEndpoint] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "private_endpoints", b"private_endpoints"]) -> None: ...

global___ListPrivateEndpointsResponse = ListPrivateEndpointsResponse

@typing.final
class ListPrivateEndpointOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    private_endpoint_id: builtins.str
    """ID of the private endpoint to list operations for.

    To get a private endpoint ID make a [PrivateEndpointService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of
    available results is larger than [page_size], the service returns a
    [ListPrivateEndpointOperationsResponse.next_page_token] that can be used to
    get the next page of results in subsequent list requests. Default value:
    100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListPrivateEndpointOperationsResponse.next_page_token] returned by a
    previous list request.
    """
    def __init__(
        self,
        *,
        private_endpoint_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "private_endpoint_id", b"private_endpoint_id"]) -> None: ...

global___ListPrivateEndpointOperationsRequest = ListPrivateEndpointOperationsRequest

@typing.final
class ListPrivateEndpointOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is
    greater than the specified
    [ListPrivateEndpointOperationsRequest.page_size], use `next_page_token` as
    the value for the [ListPrivateEndpointOperationsRequest.page_token]
    parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging
    through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified private endpoint."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListPrivateEndpointOperationsResponse = ListPrivateEndpointOperationsResponse