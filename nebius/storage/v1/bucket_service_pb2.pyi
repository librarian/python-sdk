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
import nebius.storage.v1.bucket_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___GetBucketRequest = GetBucketRequest

@typing.final
class CreateBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> nebius.storage.v1.bucket_pb2.BucketSpec: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: nebius.storage.v1.bucket_pb2.BucketSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> None: ...

global___CreateBucketRequest = CreateBucketRequest

@typing.final
class UpdateBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> nebius.storage.v1.bucket_pb2.BucketSpec: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: nebius.storage.v1.bucket_pb2.BucketSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> None: ...

global___UpdateBucketRequest = UpdateBucketRequest

@typing.final
class DeleteBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___DeleteBucketRequest = DeleteBucketRequest

@typing.final
class ListBucketsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    parent_id: builtins.str
    """Represents the container ID."""
    page_size: builtins.int
    """Specifies the maximum number of items to return in the response."""
    page_token: builtins.str
    """Token for pagination, allowing the retrieval of the next set of results."""
    filter: builtins.str
    """A filter to narrow down the results based on specific criteria."""
    def __init__(
        self,
        *,
        parent_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "parent_id", b"parent_id"]) -> None: ...

global___ListBucketsRequest = ListBucketsRequest

@typing.final
class ListBucketsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for pagination, indicating the next set of results can be retrieved using this token."""
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nebius.storage.v1.bucket_pb2.Bucket]:
        """List of buckets returned in the response. The field should be named as `items` for consistency."""

    def __init__(
        self,
        *,
        items: collections.abc.Iterable[nebius.storage.v1.bucket_pb2.Bucket] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["items", b"items", "next_page_token", b"next_page_token"]) -> None: ...

global___ListBucketsResponse = ListBucketsResponse
