"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import nebius.common.v1.metadata_pb2
import nebius.iam.v1.service_account_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> nebius.iam.v1.service_account_pb2.ServiceAccountSpec: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: nebius.iam.v1.service_account_pb2.ServiceAccountSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> None: ...

global___CreateServiceAccountRequest = CreateServiceAccountRequest

@typing.final
class GetServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___GetServiceAccountRequest = GetServiceAccountRequest

@typing.final
class GetServiceAccountByNameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    parent_id: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        parent_id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "parent_id", b"parent_id"]) -> None: ...

global___GetServiceAccountByNameRequest = GetServiceAccountByNameRequest

@typing.final
class ListServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    parent_id: builtins.str
    """Represents the container ID."""
    page_size: builtins.int
    """Specifies the maximum number of items to return in the response.
    Default value: 10
    """
    page_token: builtins.str
    """Token for pagination, allowing the retrieval of the next set of results."""
    filter: builtins.str
    """A filter to narrow down the results based on specific criteria."""
    def __init__(
        self,
        *,
        parent_id: builtins.str = ...,
        page_size: builtins.int | None = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_page_size", b"_page_size", "page_size", b"page_size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_page_size", b"_page_size", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "parent_id", b"parent_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_page_size", b"_page_size"]) -> typing.Literal["page_size"] | None: ...

global___ListServiceAccountRequest = ListServiceAccountRequest

@typing.final
class UpdateServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> nebius.iam.v1.service_account_pb2.ServiceAccountSpec: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: nebius.iam.v1.service_account_pb2.ServiceAccountSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> None: ...

global___UpdateServiceAccountRequest = UpdateServiceAccountRequest

@typing.final
class DeleteServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___DeleteServiceAccountRequest = DeleteServiceAccountRequest

@typing.final
class ListServiceAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for pagination, indicating the next set of results can be retrieved using this token."""
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nebius.iam.v1.service_account_pb2.ServiceAccount]:
        """List of service accounts returned in the response. The field should be named as `items` for consistency."""

    def __init__(
        self,
        *,
        items: collections.abc.Iterable[nebius.iam.v1.service_account_pb2.ServiceAccount] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["items", b"items", "next_page_token", b"next_page_token"]) -> None: ...

global___ListServiceAccountResponse = ListServiceAccountResponse
