"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Health:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Health.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    HEALTH_UNKNOWN: _Health.ValueType  # 0
    """Cluster is in unknown state (we have no data)."""
    ALIVE: _Health.ValueType  # 1
    """Cluster is alive and well."""
    DEAD: _Health.ValueType  # 2
    """Cluster is inoperable (it cannot perform any of its essential functions)."""
    DEGRADED: _Health.ValueType  # 3
    """Cluster is partially alive (it can perform some of its essential functions)."""

class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...

HEALTH_UNKNOWN: Health.ValueType  # 0
"""Cluster is in unknown state (we have no data)."""
ALIVE: Health.ValueType  # 1
"""Cluster is alive and well."""
DEAD: Health.ValueType  # 2
"""Cluster is inoperable (it cannot perform any of its essential functions)."""
DEGRADED: Health.ValueType  # 3
"""Cluster is partially alive (it can perform some of its essential functions)."""
global___Health = Health

@typing.final
class Resources(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: builtins.str
    """ID of the preset for computational resources available to an instance (CPU, memory etc.)."""
    def __init__(
        self,
        *,
        resource_preset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_preset_id", b"resource_preset_id"]) -> None: ...

global___Resources = Resources