"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import nebius.storage.v1.base_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CurrentBucketCounters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIMPLE_OBJECTS_QUANTITY_FIELD_NUMBER: builtins.int
    SIMPLE_OBJECTS_SIZE_FIELD_NUMBER: builtins.int
    MULTIPART_OBJECTS_QUANTITY_FIELD_NUMBER: builtins.int
    MULTIPART_OBJECTS_SIZE_FIELD_NUMBER: builtins.int
    MULTIPART_UPLOADS_QUANTITY_FIELD_NUMBER: builtins.int
    INFLIGHT_PARTS_QUANTITY_FIELD_NUMBER: builtins.int
    INFLIGHT_PARTS_SIZE_FIELD_NUMBER: builtins.int
    simple_objects_quantity: builtins.int
    simple_objects_size: builtins.int
    multipart_objects_quantity: builtins.int
    multipart_objects_size: builtins.int
    multipart_uploads_quantity: builtins.int
    inflight_parts_quantity: builtins.int
    inflight_parts_size: builtins.int
    def __init__(
        self,
        *,
        simple_objects_quantity: builtins.int = ...,
        simple_objects_size: builtins.int = ...,
        multipart_objects_quantity: builtins.int = ...,
        multipart_objects_size: builtins.int = ...,
        multipart_uploads_quantity: builtins.int = ...,
        inflight_parts_quantity: builtins.int = ...,
        inflight_parts_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["inflight_parts_quantity", b"inflight_parts_quantity", "inflight_parts_size", b"inflight_parts_size", "multipart_objects_quantity", b"multipart_objects_quantity", "multipart_objects_size", b"multipart_objects_size", "multipart_uploads_quantity", b"multipart_uploads_quantity", "simple_objects_quantity", b"simple_objects_quantity", "simple_objects_size", b"simple_objects_size"]) -> None: ...

global___CurrentBucketCounters = CurrentBucketCounters

@typing.final
class NonCurrentBucketCounters(google.protobuf.message.Message):
    """Counters for non-current object versions (for versioning buckets)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIMPLE_OBJECTS_QUANTITY_FIELD_NUMBER: builtins.int
    SIMPLE_OBJECTS_SIZE_FIELD_NUMBER: builtins.int
    MULTIPART_OBJECTS_QUANTITY_FIELD_NUMBER: builtins.int
    MULTIPART_OBJECTS_SIZE_FIELD_NUMBER: builtins.int
    simple_objects_quantity: builtins.int
    simple_objects_size: builtins.int
    multipart_objects_quantity: builtins.int
    multipart_objects_size: builtins.int
    def __init__(
        self,
        *,
        simple_objects_quantity: builtins.int = ...,
        simple_objects_size: builtins.int = ...,
        multipart_objects_quantity: builtins.int = ...,
        multipart_objects_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multipart_objects_quantity", b"multipart_objects_quantity", "multipart_objects_size", b"multipart_objects_size", "simple_objects_quantity", b"simple_objects_quantity", "simple_objects_size", b"simple_objects_size"]) -> None: ...

global___NonCurrentBucketCounters = NonCurrentBucketCounters

@typing.final
class BucketCounters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STORAGE_CLASS_FIELD_NUMBER: builtins.int
    COUNTERS_FIELD_NUMBER: builtins.int
    NON_CURRENT_COUNTERS_FIELD_NUMBER: builtins.int
    storage_class: nebius.storage.v1.base_pb2.StorageClass.ValueType
    @property
    def counters(self) -> global___CurrentBucketCounters: ...
    @property
    def non_current_counters(self) -> global___NonCurrentBucketCounters: ...
    def __init__(
        self,
        *,
        storage_class: nebius.storage.v1.base_pb2.StorageClass.ValueType = ...,
        counters: global___CurrentBucketCounters | None = ...,
        non_current_counters: global___NonCurrentBucketCounters | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["counters", b"counters", "non_current_counters", b"non_current_counters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["counters", b"counters", "non_current_counters", b"non_current_counters", "storage_class", b"storage_class"]) -> None: ...

global___BucketCounters = BucketCounters