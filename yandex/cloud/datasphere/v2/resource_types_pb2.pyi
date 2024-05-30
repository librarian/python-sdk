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

class _ResourceType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ResourceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ResourceType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESOURCE_TYPE_UNSPECIFIED: _ResourceType.ValueType  # 0
    RESOURCE_TYPE_UNPINNED_CHECKPOINT: _ResourceType.ValueType  # 1
    RESOURCE_TYPE_SECRET: _ResourceType.ValueType  # 2
    RESOURCE_TYPE_DOCKER_IMAGE: _ResourceType.ValueType  # 3
    RESOURCE_TYPE_DATASET: _ResourceType.ValueType  # 4
    RESOURCE_TYPE_S3: _ResourceType.ValueType  # 5
    RESOURCE_TYPE_NODE: _ResourceType.ValueType  # 6
    RESOURCE_TYPE_PINNED_CHECKPOINT: _ResourceType.ValueType  # 7
    RESOURCE_TYPE_ALIAS: _ResourceType.ValueType  # 8

class ResourceType(_ResourceType, metaclass=_ResourceTypeEnumTypeWrapper): ...

RESOURCE_TYPE_UNSPECIFIED: ResourceType.ValueType  # 0
RESOURCE_TYPE_UNPINNED_CHECKPOINT: ResourceType.ValueType  # 1
RESOURCE_TYPE_SECRET: ResourceType.ValueType  # 2
RESOURCE_TYPE_DOCKER_IMAGE: ResourceType.ValueType  # 3
RESOURCE_TYPE_DATASET: ResourceType.ValueType  # 4
RESOURCE_TYPE_S3: ResourceType.ValueType  # 5
RESOURCE_TYPE_NODE: ResourceType.ValueType  # 6
RESOURCE_TYPE_PINNED_CHECKPOINT: ResourceType.ValueType  # 7
RESOURCE_TYPE_ALIAS: ResourceType.ValueType  # 8
global___ResourceType = ResourceType