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
import typing
import yandex.cloud.video.v1.stream_line_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetStreamLineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___GetStreamLineRequest = GetStreamLineRequest

@typing.final
class ListStreamLinesRequest(google.protobuf.message.Message):
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
    Possible fields: ["id", "title", "createdAt", "updatedAt"]
    Both snake_case and camelCase are supported for fields.
    """
    filter: builtins.str
    """Filter expression that filters resources listed in the response.
    Expressions are composed of terms connected by logic operators.
    Value in quotes: `'` or `"`
    Example: "key1='value' AND key2='value'"
    Supported operators: ["AND"].
    Supported fields: ["title"]
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

global___ListStreamLinesRequest = ListStreamLinesRequest

@typing.final
class ListStreamLinesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page."""
    @property
    def stream_lines(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.stream_line_pb2.StreamLine]:
        """List of lines for channel."""

    def __init__(
        self,
        *,
        stream_lines: collections.abc.Iterable[yandex.cloud.video.v1.stream_line_pb2.StreamLine] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "stream_lines", b"stream_lines"]) -> None: ...

global___ListStreamLinesResponse = ListStreamLinesResponse

@typing.final
class CreateStreamLineRequest(google.protobuf.message.Message):
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
    TITLE_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    RTMP_PUSH_FIELD_NUMBER: builtins.int
    SRT_PUSH_FIELD_NUMBER: builtins.int
    RTMP_PULL_FIELD_NUMBER: builtins.int
    SRT_PULL_FIELD_NUMBER: builtins.int
    TCP_PULL_FIELD_NUMBER: builtins.int
    RTSP_PULL_FIELD_NUMBER: builtins.int
    MANUAL_LINE_FIELD_NUMBER: builtins.int
    AUTO_LINE_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    title: builtins.str
    """Line title."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    @property
    def rtmp_push(self) -> global___RTMPPushParams:
        """RTMP push input type."""

    @property
    def srt_push(self) -> global___SRTPushParams:
        """SRT push input type."""

    @property
    def rtmp_pull(self) -> global___RTMPPullParams:
        """RTMP pull input type."""

    @property
    def srt_pull(self) -> global___SRTPullParams:
        """SRT pull input type."""

    @property
    def tcp_pull(self) -> global___TCPPullParams:
        """TCP pull input type."""

    @property
    def rtsp_pull(self) -> global___RTSPPullParams:
        """RTSP pull input type."""

    @property
    def manual_line(self) -> global___ManualLineParams:
        """Manual control of stream."""

    @property
    def auto_line(self) -> global___AutoLineParams:
        """Automatic control of stream."""

    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        title: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        rtmp_push: global___RTMPPushParams | None = ...,
        srt_push: global___SRTPushParams | None = ...,
        rtmp_pull: global___RTMPPullParams | None = ...,
        srt_pull: global___SRTPullParams | None = ...,
        tcp_pull: global___TCPPullParams | None = ...,
        rtsp_pull: global___RTSPPullParams | None = ...,
        manual_line: global___ManualLineParams | None = ...,
        auto_line: global___AutoLineParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["auto_line", b"auto_line", "input_params", b"input_params", "line_type_params", b"line_type_params", "manual_line", b"manual_line", "rtmp_pull", b"rtmp_pull", "rtmp_push", b"rtmp_push", "rtsp_pull", b"rtsp_pull", "srt_pull", b"srt_pull", "srt_push", b"srt_push", "tcp_pull", b"tcp_pull"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auto_line", b"auto_line", "channel_id", b"channel_id", "input_params", b"input_params", "labels", b"labels", "line_type_params", b"line_type_params", "manual_line", b"manual_line", "rtmp_pull", b"rtmp_pull", "rtmp_push", b"rtmp_push", "rtsp_pull", b"rtsp_pull", "srt_pull", b"srt_pull", "srt_push", b"srt_push", "tcp_pull", b"tcp_pull", "thumbnail_id", b"thumbnail_id", "title", b"title"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["input_params", b"input_params"]) -> typing.Literal["rtmp_push", "srt_push", "rtmp_pull", "srt_pull", "tcp_pull", "rtsp_pull"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["line_type_params", b"line_type_params"]) -> typing.Literal["manual_line", "auto_line"] | None: ...

global___CreateStreamLineRequest = CreateStreamLineRequest

@typing.final
class CreateStreamLineMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___CreateStreamLineMetadata = CreateStreamLineMetadata

@typing.final
class UpdateStreamLineRequest(google.protobuf.message.Message):
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

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    RTMP_PUSH_FIELD_NUMBER: builtins.int
    SRT_PUSH_FIELD_NUMBER: builtins.int
    RTMP_PULL_FIELD_NUMBER: builtins.int
    SRT_PULL_FIELD_NUMBER: builtins.int
    TCP_PULL_FIELD_NUMBER: builtins.int
    RTSP_PULL_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    title: builtins.str
    """Line title."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the line are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    @property
    def rtmp_push(self) -> global___RTMPPushParams:
        """RTMP push input type."""

    @property
    def srt_push(self) -> global___SRTPushParams:
        """SRT push input type."""

    @property
    def rtmp_pull(self) -> global___RTMPPullParams:
        """RTMP pull input type."""

    @property
    def srt_pull(self) -> global___SRTPullParams:
        """SRT pull input type."""

    @property
    def tcp_pull(self) -> global___TCPPullParams:
        """TCP pull input type."""

    @property
    def rtsp_pull(self) -> global___RTSPPullParams:
        """RTSP pull input type."""

    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        title: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        rtmp_push: global___RTMPPushParams | None = ...,
        srt_push: global___SRTPushParams | None = ...,
        rtmp_pull: global___RTMPPullParams | None = ...,
        srt_pull: global___SRTPullParams | None = ...,
        tcp_pull: global___TCPPullParams | None = ...,
        rtsp_pull: global___RTSPPullParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["field_mask", b"field_mask", "input_params", b"input_params", "rtmp_pull", b"rtmp_pull", "rtmp_push", b"rtmp_push", "rtsp_pull", b"rtsp_pull", "srt_pull", b"srt_pull", "srt_push", b"srt_push", "tcp_pull", b"tcp_pull"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["field_mask", b"field_mask", "input_params", b"input_params", "labels", b"labels", "rtmp_pull", b"rtmp_pull", "rtmp_push", b"rtmp_push", "rtsp_pull", b"rtsp_pull", "srt_pull", b"srt_pull", "srt_push", b"srt_push", "stream_line_id", b"stream_line_id", "tcp_pull", b"tcp_pull", "thumbnail_id", b"thumbnail_id", "title", b"title"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["input_params", b"input_params"]) -> typing.Literal["rtmp_push", "srt_push", "rtmp_pull", "srt_pull", "tcp_pull", "rtsp_pull"] | None: ...

global___UpdateStreamLineRequest = UpdateStreamLineRequest

@typing.final
class UpdateStreamLineMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___UpdateStreamLineMetadata = UpdateStreamLineMetadata

@typing.final
class DeleteStreamLineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___DeleteStreamLineRequest = DeleteStreamLineRequest

@typing.final
class DeleteStreamLineMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___DeleteStreamLineMetadata = DeleteStreamLineMetadata

@typing.final
class PerformLineActionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    ACTIVATE_FIELD_NUMBER: builtins.int
    DEACTIVATE_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    @property
    def activate(self) -> global___ActivateAction: ...
    @property
    def deactivate(self) -> global___DeactivateAction: ...
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
        activate: global___ActivateAction | None = ...,
        deactivate: global___DeactivateAction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["action", b"action", "activate", b"activate", "deactivate", b"deactivate"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["action", b"action", "activate", b"activate", "deactivate", b"deactivate", "stream_line_id", b"stream_line_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["action", b"action"]) -> typing.Literal["activate", "deactivate"] | None: ...

global___PerformLineActionRequest = PerformLineActionRequest

@typing.final
class PerformLineActionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___PerformLineActionMetadata = PerformLineActionMetadata

@typing.final
class RTMPPushParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RTMPPushParams = RTMPPushParams

@typing.final
class SRTPushParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___SRTPushParams = SRTPushParams

@typing.final
class RTMPPullParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """URL of a RTMP streaming server."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___RTMPPullParams = RTMPPullParams

@typing.final
class SRTPullParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """URL of a SRT streaming server."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___SRTPullParams = SRTPullParams

@typing.final
class TCPPullParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """URL of a TCP streaming server."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___TCPPullParams = TCPPullParams

@typing.final
class RTSPPullParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """URL of a RTSP streaming server."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___RTSPPullParams = RTSPPullParams

@typing.final
class ManualLineParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ManualLineParams = ManualLineParams

@typing.final
class AutoLineParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AutoLineParams = AutoLineParams

@typing.final
class ActivateAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ActivateAction = ActivateAction

@typing.final
class DeactivateAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeactivateAction = DeactivateAction

@typing.final
class GetStreamKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___GetStreamKeyRequest = GetStreamKeyRequest

@typing.final
class UpdateStreamKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___UpdateStreamKeyRequest = UpdateStreamKeyRequest

@typing.final
class UpdateStreamKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_LINE_ID_FIELD_NUMBER: builtins.int
    stream_line_id: builtins.str
    """ID of the line."""
    def __init__(
        self,
        *,
        stream_line_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["stream_line_id", b"stream_line_id"]) -> None: ...

global___UpdateStreamKeyMetadata = UpdateStreamKeyMetadata