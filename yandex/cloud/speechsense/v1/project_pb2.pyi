"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Project(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_BY_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    FILTERS_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    connection_id: builtins.str
    description: builtins.str
    created_by: builtins.str
    modified_by: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def filters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FieldFilter]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        connection_id: builtins.str = ...,
        description: builtins.str = ...,
        created_by: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_by: builtins.str = ...,
        modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        filters: collections.abc.Iterable[global___FieldFilter] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "modified_at", b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["connection_id", b"connection_id", "created_at", b"created_at", "created_by", b"created_by", "description", b"description", "filters", b"filters", "id", b"id", "modified_at", b"modified_at", "modified_by", b"modified_by", "name", b"name"]) -> None: ...

global___Project = Project

@typing.final
class FieldFilter(google.protobuf.message.Message):
    """simple filters to match talks based on their connection metadata"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    FIELD_VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    """connection metadata field key"""
    field_value: builtins.str
    """connection metadata field value"""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        field_value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["field_value", b"field_value", "key", b"key"]) -> None: ...

global___FieldFilter = FieldFilter
