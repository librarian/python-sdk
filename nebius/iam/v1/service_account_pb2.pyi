"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import nebius.common.v1.metadata_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ServiceAccount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> global___ServiceAccountSpec: ...
    @property
    def status(self) -> global___ServiceAccountStatus: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___ServiceAccountSpec | None = ...,
        status: global___ServiceAccountStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___ServiceAccount = ServiceAccount

@typing.final
class ServiceAccountSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    description: builtins.str
    def __init__(
        self,
        *,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description"]) -> None: ...

global___ServiceAccountSpec = ServiceAccountSpec

@typing.final
class ServiceAccountStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVE_FIELD_NUMBER: builtins.int
    active: builtins.bool
    def __init__(
        self,
        *,
        active: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["active", b"active"]) -> None: ...

global___ServiceAccountStatus = ServiceAccountStatus
