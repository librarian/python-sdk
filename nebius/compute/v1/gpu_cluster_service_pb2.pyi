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
import nebius.compute.v1.gpu_cluster_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetGpuClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___GetGpuClusterRequest = GetGpuClusterRequest

@typing.final
class ListGpuClustersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    parent_id: builtins.str
    page_size: builtins.int
    page_token: builtins.str
    filter: builtins.str
    def __init__(
        self,
        *,
        parent_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "parent_id", b"parent_id"]) -> None: ...

global___ListGpuClustersRequest = ListGpuClustersRequest

@typing.final
class CreateGpuClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> nebius.compute.v1.gpu_cluster_pb2.GpuClusterSpec: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: nebius.compute.v1.gpu_cluster_pb2.GpuClusterSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> None: ...

global___CreateGpuClusterRequest = CreateGpuClusterRequest

@typing.final
class UpdateGpuClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> nebius.compute.v1.gpu_cluster_pb2.GpuClusterSpec: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: nebius.compute.v1.gpu_cluster_pb2.GpuClusterSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec"]) -> None: ...

global___UpdateGpuClusterRequest = UpdateGpuClusterRequest

@typing.final
class DeleteGpuClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___DeleteGpuClusterRequest = DeleteGpuClusterRequest

@typing.final
class ListGpuClustersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nebius.compute.v1.gpu_cluster_pb2.GpuCluster]: ...
    def __init__(
        self,
        *,
        items: collections.abc.Iterable[nebius.compute.v1.gpu_cluster_pb2.GpuCluster] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["items", b"items", "next_page_token", b"next_page_token"]) -> None: ...

global___ListGpuClustersResponse = ListGpuClustersResponse
