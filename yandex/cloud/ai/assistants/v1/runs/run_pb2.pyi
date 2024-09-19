"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
import yandex.cloud.ai.assistants.v1.common_pb2
import yandex.cloud.ai.assistants.v1.threads.message_pb2
import yandex.cloud.ai.common.common_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Run(google.protobuf.message.Message):
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

    ID_FIELD_NUMBER: builtins.int
    ASSISTANT_ID_FIELD_NUMBER: builtins.int
    THREAD_ID_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    USAGE_FIELD_NUMBER: builtins.int
    CUSTOM_PROMPT_TRUNCATION_OPTIONS_FIELD_NUMBER: builtins.int
    CUSTOM_COMPLETION_OPTIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    assistant_id: builtins.str
    thread_id: builtins.str
    created_by: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def state(self) -> global___RunState: ...
    @property
    def usage(self) -> global___ContentUsage: ...
    @property
    def custom_prompt_truncation_options(self) -> yandex.cloud.ai.assistants.v1.common_pb2.PromptTruncationOptions: ...
    @property
    def custom_completion_options(self) -> yandex.cloud.ai.assistants.v1.common_pb2.CompletionOptions: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        assistant_id: builtins.str = ...,
        thread_id: builtins.str = ...,
        created_by: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        state: global___RunState | None = ...,
        usage: global___ContentUsage | None = ...,
        custom_prompt_truncation_options: yandex.cloud.ai.assistants.v1.common_pb2.PromptTruncationOptions | None = ...,
        custom_completion_options: yandex.cloud.ai.assistants.v1.common_pb2.CompletionOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "custom_completion_options", b"custom_completion_options", "custom_prompt_truncation_options", b"custom_prompt_truncation_options", "state", b"state", "usage", b"usage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assistant_id", b"assistant_id", "created_at", b"created_at", "created_by", b"created_by", "custom_completion_options", b"custom_completion_options", "custom_prompt_truncation_options", b"custom_prompt_truncation_options", "id", b"id", "labels", b"labels", "state", b"state", "thread_id", b"thread_id", "usage", b"usage"]) -> None: ...

global___Run = Run

@typing.final
class RunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RunStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RunStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RunState._RunStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RUN_STATUS_UNSPECIFIED: RunState._RunStatus.ValueType  # 0
        PENDING: RunState._RunStatus.ValueType  # 1
        IN_PROGRESS: RunState._RunStatus.ValueType  # 2
        FAILED: RunState._RunStatus.ValueType  # 3
        COMPLETED: RunState._RunStatus.ValueType  # 4

    class RunStatus(_RunStatus, metaclass=_RunStatusEnumTypeWrapper): ...
    RUN_STATUS_UNSPECIFIED: RunState.RunStatus.ValueType  # 0
    PENDING: RunState.RunStatus.ValueType  # 1
    IN_PROGRESS: RunState.RunStatus.ValueType  # 2
    FAILED: RunState.RunStatus.ValueType  # 3
    COMPLETED: RunState.RunStatus.ValueType  # 4

    STATUS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    COMPLETED_MESSAGE_FIELD_NUMBER: builtins.int
    status: global___RunState.RunStatus.ValueType
    @property
    def error(self) -> yandex.cloud.ai.common.common_pb2.Error: ...
    @property
    def completed_message(self) -> yandex.cloud.ai.assistants.v1.threads.message_pb2.Message: ...
    def __init__(
        self,
        *,
        status: global___RunState.RunStatus.ValueType = ...,
        error: yandex.cloud.ai.common.common_pb2.Error | None = ...,
        completed_message: yandex.cloud.ai.assistants.v1.threads.message_pb2.Message | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["StateData", b"StateData", "completed_message", b"completed_message", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["StateData", b"StateData", "completed_message", b"completed_message", "error", b"error", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["StateData", b"StateData"]) -> typing.Literal["error", "completed_message"] | None: ...

global___RunState = RunState

@typing.final
class ContentUsage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROMPT_TOKENS_FIELD_NUMBER: builtins.int
    COMPLETION_TOKENS_FIELD_NUMBER: builtins.int
    TOTAL_TOKENS_FIELD_NUMBER: builtins.int
    prompt_tokens: builtins.int
    completion_tokens: builtins.int
    total_tokens: builtins.int
    def __init__(
        self,
        *,
        prompt_tokens: builtins.int = ...,
        completion_tokens: builtins.int = ...,
        total_tokens: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["completion_tokens", b"completion_tokens", "prompt_tokens", b"prompt_tokens", "total_tokens", b"total_tokens"]) -> None: ...

global___ContentUsage = ContentUsage
