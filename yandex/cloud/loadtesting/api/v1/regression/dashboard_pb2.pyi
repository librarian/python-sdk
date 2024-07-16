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
import yandex.cloud.loadtesting.api.v1.regression.widget_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Dashboard(google.protobuf.message.Message):
    """Regression dashboard."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Content(google.protobuf.message.Message):
        """Content of regression dashboard."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        WIDGETS_FIELD_NUMBER: builtins.int
        @property
        def widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadtesting.api.v1.regression.widget_pb2.Widget]:
            """Widgets."""

        def __init__(
            self,
            *,
            widgets: collections.abc.Iterable[yandex.cloud.loadtesting.api.v1.regression.widget_pb2.Widget] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["widgets", b"widgets"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    UPDATED_BY_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the dashboard."""
    name: builtins.str
    """Name of the dashboard."""
    description: builtins.str
    """Description of the dashboard."""
    created_by: builtins.str
    """UA or SA that created the dashboard."""
    updated_by: builtins.str
    """UA or SA that updated the dashboard last time."""
    etag: builtins.str
    """Etag of the dashboard."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Last update timestamp."""

    @property
    def content(self) -> global___Dashboard.Content:
        """Dashboard content."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        updated_by: builtins.str = ...,
        etag: builtins.str = ...,
        content: global___Dashboard.Content | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["content", b"content", "created_at", b"created_at", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "created_at", b"created_at", "created_by", b"created_by", "description", b"description", "etag", b"etag", "id", b"id", "name", b"name", "updated_at", b"updated_at", "updated_by", b"updated_by"]) -> None: ...

global___Dashboard = Dashboard
