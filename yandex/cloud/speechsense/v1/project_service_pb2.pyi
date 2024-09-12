"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.speechsense.v1.project_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FILTERS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """project name"""
    connection_id: builtins.str
    """id of connection the project should belong too"""
    description: builtins.str
    """project description"""
    @property
    def filters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.speechsense.v1.project_pb2.FieldFilter]:
        """project filters"""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        connection_id: builtins.str = ...,
        description: builtins.str = ...,
        filters: collections.abc.Iterable[yandex.cloud.speechsense.v1.project_pb2.FieldFilter] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connection_id", b"connection_id", "description", b"description", "filters", b"filters", "name", b"name"]) -> None: ...

global___CreateProjectRequest = CreateProjectRequest

@typing.final
class CreateProjectMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___CreateProjectMetadata = CreateProjectMetadata
