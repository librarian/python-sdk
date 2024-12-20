"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AgentType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AgentTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AgentType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    AGENT_UNDEFINED: _AgentType.ValueType  # 0
    O11Y_AGENT: _AgentType.ValueType  # 1

class AgentType(_AgentType, metaclass=_AgentTypeEnumTypeWrapper): ...

AGENT_UNDEFINED: AgentType.ValueType  # 0
O11Y_AGENT: AgentType.ValueType  # 1
global___AgentType = AgentType

class _AgentState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AgentStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AgentState.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STATE_UNDEFINED: _AgentState.ValueType  # 0
    STATE_HEALTHY: _AgentState.ValueType  # 1
    STATE_ERROR: _AgentState.ValueType  # 2

class AgentState(_AgentState, metaclass=_AgentStateEnumTypeWrapper): ...

STATE_UNDEFINED: AgentState.ValueType  # 0
STATE_HEALTHY: AgentState.ValueType  # 1
STATE_ERROR: AgentState.ValueType  # 2
global___AgentState = AgentState

class _Action:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Action.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACTION_UNDEFINED: _Action.ValueType  # 0
    NOP: _Action.ValueType  # 1
    UPDATE: _Action.ValueType  # 2
    RESTART: _Action.ValueType  # 3

class Action(_Action, metaclass=_ActionEnumTypeWrapper): ...

ACTION_UNDEFINED: Action.ValueType  # 0
NOP: Action.ValueType  # 1
UPDATE: Action.ValueType  # 2
RESTART: Action.ValueType  # 3
global___Action = Action

@typing.final
class GetVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    AGENT_VERSION_FIELD_NUMBER: builtins.int
    UPDATER_VERSION_FIELD_NUMBER: builtins.int
    PARENT_ID_FIELD_NUMBER: builtins.int
    INSTANCE_ID_FIELD_NUMBER: builtins.int
    OS_INFO_FIELD_NUMBER: builtins.int
    AGENT_STATE_FIELD_NUMBER: builtins.int
    AGENT_UPTIME_FIELD_NUMBER: builtins.int
    SYSTEM_UPTIME_FIELD_NUMBER: builtins.int
    UPDATER_UPTIME_FIELD_NUMBER: builtins.int
    AGENT_STATE_MESSAGES_FIELD_NUMBER: builtins.int
    type: global___AgentType.ValueType
    agent_version: builtins.str
    updater_version: builtins.str
    parent_id: builtins.str
    instance_id: builtins.str
    agent_state: global___AgentState.ValueType
    @property
    def os_info(self) -> global___OSInfo: ...
    @property
    def agent_uptime(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def system_uptime(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def updater_uptime(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def agent_state_messages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        type: global___AgentType.ValueType = ...,
        agent_version: builtins.str = ...,
        updater_version: builtins.str = ...,
        parent_id: builtins.str = ...,
        instance_id: builtins.str = ...,
        os_info: global___OSInfo | None = ...,
        agent_state: global___AgentState.ValueType = ...,
        agent_uptime: google.protobuf.duration_pb2.Duration | None = ...,
        system_uptime: google.protobuf.duration_pb2.Duration | None = ...,
        updater_uptime: google.protobuf.duration_pb2.Duration | None = ...,
        agent_state_messages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["agent_uptime", b"agent_uptime", "os_info", b"os_info", "system_uptime", b"system_uptime", "updater_uptime", b"updater_uptime"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["agent_state", b"agent_state", "agent_state_messages", b"agent_state_messages", "agent_uptime", b"agent_uptime", "agent_version", b"agent_version", "instance_id", b"instance_id", "os_info", b"os_info", "parent_id", b"parent_id", "system_uptime", b"system_uptime", "type", b"type", "updater_uptime", b"updater_uptime", "updater_version", b"updater_version"]) -> None: ...

global___GetVersionRequest = GetVersionRequest

@typing.final
class OSInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    UNAME_FIELD_NUMBER: builtins.int
    ARCHITECTURE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Example: "Ubuntu 22.04.4 LTS" """
    uname: builtins.str
    """Example: "Linux computeimage-abcdef 6.5.0-44-generic #44~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Jun 18 14:36:16 UTC 2 x86_64 x86_64 x86_64 GNU/Linux" """
    architecture: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        uname: builtins.str = ...,
        architecture: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["architecture", b"architecture", "name", b"name", "uname", b"uname"]) -> None: ...

global___OSInfo = OSInfo

@typing.final
class GetVersionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTION_FIELD_NUMBER: builtins.int
    NOP_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    RESTART_FIELD_NUMBER: builtins.int
    action: global___Action.ValueType
    @property
    def nop(self) -> global___NopActionParams: ...
    @property
    def update(self) -> global___UpdateActionParams: ...
    @property
    def restart(self) -> global___RestartActionParams: ...
    def __init__(
        self,
        *,
        action: global___Action.ValueType = ...,
        nop: global___NopActionParams | None = ...,
        update: global___UpdateActionParams | None = ...,
        restart: global___RestartActionParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["nop", b"nop", "response", b"response", "restart", b"restart", "update", b"update"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["action", b"action", "nop", b"nop", "response", b"response", "restart", b"restart", "update", b"update"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["response", b"response"]) -> typing.Literal["nop", "update", "restart"] | None: ...

global___GetVersionResponse = GetVersionResponse

@typing.final
class NopActionParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NopActionParams = NopActionParams

@typing.final
class UpdateActionParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    REPO_URL_FIELD_NUMBER: builtins.int
    version: builtins.str
    repo_url: builtins.str
    def __init__(
        self,
        *,
        version: builtins.str = ...,
        repo_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["repo_url", b"repo_url", "version", b"version"]) -> None: ...

global___UpdateActionParams = UpdateActionParams

@typing.final
class RestartActionParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RestartActionParams = RestartActionParams
