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
import google.protobuf.wrappers_pb2
import google.rpc.code_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _HttpCodeInterval:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _HttpCodeIntervalEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_HttpCodeInterval.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    HTTP_CODE_INTERVAL_UNSPECIFIED: _HttpCodeInterval.ValueType  # 0
    HTTP_1XX: _HttpCodeInterval.ValueType  # 1
    HTTP_2XX: _HttpCodeInterval.ValueType  # 2
    HTTP_3XX: _HttpCodeInterval.ValueType  # 3
    HTTP_4XX: _HttpCodeInterval.ValueType  # 4
    HTTP_5XX: _HttpCodeInterval.ValueType  # 5
    HTTP_ALL: _HttpCodeInterval.ValueType  # 6

class HttpCodeInterval(_HttpCodeInterval, metaclass=_HttpCodeIntervalEnumTypeWrapper): ...

HTTP_CODE_INTERVAL_UNSPECIFIED: HttpCodeInterval.ValueType  # 0
HTTP_1XX: HttpCodeInterval.ValueType  # 1
HTTP_2XX: HttpCodeInterval.ValueType  # 2
HTTP_3XX: HttpCodeInterval.ValueType  # 3
HTTP_4XX: HttpCodeInterval.ValueType  # 4
HTTP_5XX: HttpCodeInterval.ValueType  # 5
HTTP_ALL: HttpCodeInterval.ValueType  # 6
global___HttpCodeInterval = HttpCodeInterval

@typing.final
class LogDiscardRule(google.protobuf.message.Message):
    """LogDiscardRule discards a fraction of logs with certain codes.
    If neither codes or intervals are provided, rule applies to all logs.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_CODES_FIELD_NUMBER: builtins.int
    HTTP_CODE_INTERVALS_FIELD_NUMBER: builtins.int
    GRPC_CODES_FIELD_NUMBER: builtins.int
    DISCARD_PERCENT_FIELD_NUMBER: builtins.int
    @property
    def http_codes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """HTTP codes that should be discarded."""

    @property
    def http_code_intervals(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___HttpCodeInterval.ValueType]:
        """Groups of HTTP codes like 4xx that should be discarded."""

    @property
    def grpc_codes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[google.rpc.code_pb2.Code.ValueType]:
        """GRPC codes that should be discarded"""

    @property
    def discard_percent(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Percent of logs to be discarded: 0 - keep all, 100 or unset - discard all"""

    def __init__(
        self,
        *,
        http_codes: collections.abc.Iterable[builtins.int] | None = ...,
        http_code_intervals: collections.abc.Iterable[global___HttpCodeInterval.ValueType] | None = ...,
        grpc_codes: collections.abc.Iterable[google.rpc.code_pb2.Code.ValueType] | None = ...,
        discard_percent: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["discard_percent", b"discard_percent"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["discard_percent", b"discard_percent", "grpc_codes", b"grpc_codes", "http_code_intervals", b"http_code_intervals", "http_codes", b"http_codes"]) -> None: ...

global___LogDiscardRule = LogDiscardRule

@typing.final
class LogOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    DISCARD_RULES_FIELD_NUMBER: builtins.int
    DISABLE_FIELD_NUMBER: builtins.int
    log_group_id: builtins.str
    """Cloud Logging log group ID to store access logs.
    If not set then logs will be stored in default log group for the folder
    where load balancer located.
    """
    disable: builtins.bool
    """Do not send logs to Cloud Logging log group."""
    @property
    def discard_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LogDiscardRule]:
        """ordered list of rules, first matching rule applies"""

    def __init__(
        self,
        *,
        log_group_id: builtins.str = ...,
        discard_rules: collections.abc.Iterable[global___LogDiscardRule] | None = ...,
        disable: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["disable", b"disable", "discard_rules", b"discard_rules", "log_group_id", b"log_group_id"]) -> None: ...

global___LogOptions = LogOptions