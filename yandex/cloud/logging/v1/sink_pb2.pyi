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
class Sink(google.protobuf.message.Message):
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

    @typing.final
    class Yds(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        STREAM_NAME_FIELD_NUMBER: builtins.int
        stream_name: builtins.str
        """Fully qualified name of data stream"""
        def __init__(
            self,
            *,
            stream_name: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["stream_name", b"stream_name"]) -> None: ...

    @typing.final
    class S3(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BUCKET_FIELD_NUMBER: builtins.int
        PREFIX_FIELD_NUMBER: builtins.int
        bucket: builtins.str
        """Object storage bucket"""
        prefix: builtins.str
        """Prefix to use for saved log object names"""
        def __init__(
            self,
            *,
            bucket: builtins.str = ...,
            prefix: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["bucket", b"bucket", "prefix", b"prefix"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CLOUD_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    YDS_FIELD_NUMBER: builtins.int
    S3_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Sink ID."""
    folder_id: builtins.str
    """Sink folder ID."""
    cloud_id: builtins.str
    """Sink cloud ID."""
    name: builtins.str
    """Sink name."""
    description: builtins.str
    """Sink description."""
    service_account_id: builtins.str
    """Logs will be written to the sink on behalf of this service account"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Sink creation time."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Sink labels."""

    @property
    def yds(self) -> global___Sink.Yds:
        """Yandex data stream"""

    @property
    def s3(self) -> global___Sink.S3:
        """Object storage"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        cloud_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        service_account_id: builtins.str = ...,
        yds: global___Sink.Yds | None = ...,
        s3: global___Sink.S3 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "s3", b"s3", "sink", b"sink", "yds", b"yds"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "s3", b"s3", "service_account_id", b"service_account_id", "sink", b"sink", "yds", b"yds"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["sink", b"sink"]) -> typing.Literal["yds", "s3"] | None: ...

global___Sink = Sink