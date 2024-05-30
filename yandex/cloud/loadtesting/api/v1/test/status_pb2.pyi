"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Status:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Status.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STATUS_UNSPECIFIED: _Status.ValueType  # 0
    """Status is unspecified."""
    CREATED: _Status.ValueType  # 1
    """Test has been created, but not started by any agent."""
    INITIATED: _Status.ValueType  # 2
    """Execution stage: initialization."""
    PREPARING: _Status.ValueType  # 3
    """Execution stage: data preparation and warm-up."""
    RUNNING: _Status.ValueType  # 4
    """Execution stage: load generation."""
    FINISHING: _Status.ValueType  # 5
    """Execution stage: termination."""
    DONE: _Status.ValueType  # 6
    """Test is done."""
    POST_PROCESSING: _Status.ValueType  # 7
    """Execution stage: results post-processing."""
    FAILED: _Status.ValueType  # 8
    """Test has failed due to some error."""
    STOPPING: _Status.ValueType  # 9
    """Test is being stopped."""
    STOPPED: _Status.ValueType  # 10
    """Test has been stopped."""
    AUTOSTOPPED: _Status.ValueType  # 11
    """Test has been stopped automatically by satisfying autostop condition."""
    WAITING: _Status.ValueType  # 12
    """Execution stage: waiting for a trigger to start."""
    DELETING: _Status.ValueType  # 13
    """Test is being deleted."""
    LOST: _Status.ValueType  # 14
    """Test status has not been reported in a while during execution stage.

    Means that either an agent is too busy to send it, got offline, or failed without
    reporting a final status.
    """

class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...

STATUS_UNSPECIFIED: Status.ValueType  # 0
"""Status is unspecified."""
CREATED: Status.ValueType  # 1
"""Test has been created, but not started by any agent."""
INITIATED: Status.ValueType  # 2
"""Execution stage: initialization."""
PREPARING: Status.ValueType  # 3
"""Execution stage: data preparation and warm-up."""
RUNNING: Status.ValueType  # 4
"""Execution stage: load generation."""
FINISHING: Status.ValueType  # 5
"""Execution stage: termination."""
DONE: Status.ValueType  # 6
"""Test is done."""
POST_PROCESSING: Status.ValueType  # 7
"""Execution stage: results post-processing."""
FAILED: Status.ValueType  # 8
"""Test has failed due to some error."""
STOPPING: Status.ValueType  # 9
"""Test is being stopped."""
STOPPED: Status.ValueType  # 10
"""Test has been stopped."""
AUTOSTOPPED: Status.ValueType  # 11
"""Test has been stopped automatically by satisfying autostop condition."""
WAITING: Status.ValueType  # 12
"""Execution stage: waiting for a trigger to start."""
DELETING: Status.ValueType  # 13
"""Test is being deleted."""
LOST: Status.ValueType  # 14
"""Test status has not been reported in a while during execution stage.

Means that either an agent is too busy to send it, got offline, or failed without
reporting a final status.
"""
global___Status = Status