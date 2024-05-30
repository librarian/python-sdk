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
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.video.v1.stream_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_id", b"stream_id"]) -> None: ...

global___GetStreamRequest = GetStreamRequest

@typing.final
class ListStreamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    page_size: builtins.int
    """The maximum number of the results per page to return. Default value: 100."""
    page_token: builtins.str
    """Page token for getting the next page of the result."""
    order_by: builtins.str
    """By which column the listing should be ordered and in which direction,
    format is "createdAt desc". "id asc" if omitted.
    Possible fields: ["id", "title", "startTime", "finishTime", "createdAt", "updatedAt"]
    Both snake_case and camelCase are supported for fields.
    """
    filter: builtins.str
    """Filter expression that filters resources listed in the response.
    Expressions are composed of terms connected by logic operators.
    Value in quotes: `'` or `"`
    Example: "key1='value' AND key2='value'"
    Supported operators: ["AND"].
    Supported fields: ["title", "lineId", "status"]
    Both snake_case and camelCase are supported for fields.
    """
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        order_by: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "filter", b"filter", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListStreamsRequest = ListStreamsRequest

@typing.final
class ListStreamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page."""
    @property
    def streams(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.stream_pb2.Stream]:
        """List of streams for channel."""

    def __init__(
        self,
        *,
        streams: collections.abc.Iterable[yandex.cloud.video.v1.stream_pb2.Stream] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "streams", b"streams"]) -> None: ...

global___ListStreamsResponse = ListStreamsResponse

@typing.final
class CreateStreamRequest(google.protobuf.message.Message):
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

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    LINE_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ON_DEMAND_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    line_id: builtins.str
    """ID of the line."""
    title: builtins.str
    """Stream title."""
    description: builtins.str
    """Stream description."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    @property
    def on_demand(self) -> global___OnDemandParams:
        """On demand stream. It starts immediately when a signal appears."""

    @property
    def schedule(self) -> global___ScheduleParams:
        """Schedule stream. Determines when to start receiving the signal or finish time."""

    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        line_id: builtins.str = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        on_demand: global___OnDemandParams | None = ...,
        schedule: global___ScheduleParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["on_demand", b"on_demand", "schedule", b"schedule", "stream_type", b"stream_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "description", b"description", "labels", b"labels", "line_id", b"line_id", "on_demand", b"on_demand", "schedule", b"schedule", "stream_type", b"stream_type", "thumbnail_id", b"thumbnail_id", "title", b"title"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["stream_type", b"stream_type"]) -> typing.Literal["on_demand", "schedule"] | None: ...

global___CreateStreamRequest = CreateStreamRequest

@typing.final
class OnDemandParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___OnDemandParams = OnDemandParams

@typing.final
class ScheduleParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_TIME_FIELD_NUMBER: builtins.int
    FINISH_TIME_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def finish_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finish_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["finish_time", b"finish_time", "start_time", b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["finish_time", b"finish_time", "start_time", b"start_time"]) -> None: ...

global___ScheduleParams = ScheduleParams

@typing.final
class CreateStreamMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_id", b"stream_id"]) -> None: ...

global___CreateStreamMetadata = CreateStreamMetadata

@typing.final
class UpdateStreamRequest(google.protobuf.message.Message):
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

    STREAM_ID_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    LINE_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ON_DEMAND_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    line_id: builtins.str
    """ID of the line."""
    title: builtins.str
    """Stream title."""
    description: builtins.str
    """Stream description."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the stream are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    @property
    def on_demand(self) -> global___OnDemandParams:
        """On demand stream. It starts immediately when a signal appears."""

    @property
    def schedule(self) -> global___ScheduleParams:
        """Schedule stream. Determines when to start receiving the signal or finish time."""

    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        line_id: builtins.str = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        on_demand: global___OnDemandParams | None = ...,
        schedule: global___ScheduleParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["field_mask", b"field_mask", "on_demand", b"on_demand", "schedule", b"schedule", "stream_type", b"stream_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "field_mask", b"field_mask", "labels", b"labels", "line_id", b"line_id", "on_demand", b"on_demand", "schedule", b"schedule", "stream_id", b"stream_id", "stream_type", b"stream_type", "thumbnail_id", b"thumbnail_id", "title", b"title"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["stream_type", b"stream_type"]) -> typing.Literal["on_demand", "schedule"] | None: ...

global___UpdateStreamRequest = UpdateStreamRequest

@typing.final
class UpdateStreamMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_id", b"stream_id"]) -> None: ...

global___UpdateStreamMetadata = UpdateStreamMetadata

@typing.final
class DeleteStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_id", b"stream_id"]) -> None: ...

global___DeleteStreamRequest = DeleteStreamRequest

@typing.final
class DeleteStreamMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_id", b"stream_id"]) -> None: ...

global___DeleteStreamMetadata = DeleteStreamMetadata

@typing.final
class PerformStreamActionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    PUBLISH_FIELD_NUMBER: builtins.int
    STOP_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    @property
    def publish(self) -> global___PublishAction: ...
    @property
    def stop(self) -> global___StopAction: ...
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
        publish: global___PublishAction | None = ...,
        stop: global___StopAction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["action", b"action", "publish", b"publish", "stop", b"stop"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["action", b"action", "publish", b"publish", "stop", b"stop", "stream_id", b"stream_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["action", b"action"]) -> typing.Literal["publish", "stop"] | None: ...

global___PerformStreamActionRequest = PerformStreamActionRequest

@typing.final
class PublishAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___PublishAction = PublishAction

@typing.final
class StopAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___StopAction = StopAction

@typing.final
class PerformStreamActionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_id", b"stream_id"]) -> None: ...

global___PerformStreamActionMetadata = PerformStreamActionMetadata