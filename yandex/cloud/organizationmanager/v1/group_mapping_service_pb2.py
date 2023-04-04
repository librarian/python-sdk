# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/group_mapping_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.organizationmanager.v1 import group_mapping_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_group__mapping__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/organizationmanager/v1/group_mapping_service.proto',
  package='yandex.cloud.organizationmanager.v1',
  syntax='proto3',
  serialized_options=b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?yandex/cloud/organizationmanager/v1/group_mapping_service.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x37yandex/cloud/organizationmanager/v1/group_mapping.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a google/protobuf/field_mask.proto\"=\n\x16GetGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"c\n\x17GetGroupMappingResponse\x12H\n\rgroup_mapping\x18\x01 \x01(\x0b\x32\x31.yandex.cloud.organizationmanager.v1.GroupMapping\"Q\n\x19\x43reateGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"3\n\x1a\x43reateGroupMappingMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\"\x8b\x01\n\x19UpdateGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x38\n\x0eupdated_fields\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe8\xc7\x31\x01\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"3\n\x1aUpdateGroupMappingMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\"@\n\x19\x44\x65leteGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"3\n\x1a\x44\x65leteGroupMappingMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\"\xb0\x01\n\x1eUpdateGroupMappingItemsRequest\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12i\n\x19group_mapping_item_deltas\x18\x04 \x03(\x0b\x32:.yandex.cloud.organizationmanager.v1.GroupMappingItemDeltaB\n\x82\xc8\x31\x06\x31-1000\"\xe6\x01\n\x15GroupMappingItemDelta\x12\x43\n\x04item\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.organizationmanager.v1.GroupMappingItem\x12Q\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x41.yandex.cloud.organizationmanager.v1.GroupMappingItemDelta.Action\"5\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\"8\n\x1fUpdateGroupMappingItemsMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\"\x80\x01\n\x1fUpdateGroupMappingItemsResponse\x12]\n\x19group_mapping_item_deltas\x18\x04 \x03(\x0b\x32:.yandex.cloud.organizationmanager.v1.GroupMappingItemDelta\"\x9e\x01\n\x1cListGroupMappingItemsRequest\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"\x8c\x01\n\x1dListGroupMappingItemsResponse\x12R\n\x13group_mapping_items\x18\x01 \x03(\x0b\x32\x35.yandex.cloud.organizationmanager.v1.GroupMappingItem\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd0\x07\n\x13GroupMappingService\x12\x80\x01\n\x03Get\x12;.yandex.cloud.organizationmanager.v1.GetGroupMappingRequest\x1a<.yandex.cloud.organizationmanager.v1.GetGroupMappingResponse\x12\x9b\x01\n\x06\x43reate\x12>.yandex.cloud.organizationmanager.v1.CreateGroupMappingRequest\x1a!.yandex.cloud.operation.Operation\".\xb2\xd2**\n\x1a\x43reateGroupMappingMetadata\x12\x0cGroupMapping\x12\x9b\x01\n\x06Update\x12>.yandex.cloud.organizationmanager.v1.UpdateGroupMappingRequest\x1a!.yandex.cloud.operation.Operation\".\xb2\xd2**\n\x1aUpdateGroupMappingMetadata\x12\x0cGroupMapping\x12\xa4\x01\n\x06\x44\x65lete\x12>.yandex.cloud.organizationmanager.v1.DeleteGroupMappingRequest\x1a!.yandex.cloud.operation.Operation\"7\xb2\xd2*3\n\x1a\x44\x65leteGroupMappingMetadata\x12\x15google.protobuf.Empty\x12\x92\x01\n\tListItems\x12\x41.yandex.cloud.organizationmanager.v1.ListGroupMappingItemsRequest\x1a\x42.yandex.cloud.organizationmanager.v1.ListGroupMappingItemsResponse\x12\xbd\x01\n\x0bUpdateItems\x12\x43.yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsRequest\x1a!.yandex.cloud.operation.Operation\"F\xb2\xd2*B\n\x1fUpdateGroupMappingItemsMetadata\x12\x1fUpdateGroupMappingItemsResponseB\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_group__mapping__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])



_GROUPMAPPINGITEMDELTA_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='yandex.cloud.organizationmanager.v1.GroupMappingItemDelta.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1271,
  serialized_end=1324,
)
_sym_db.RegisterEnumDescriptor(_GROUPMAPPINGITEMDELTA_ACTION)


_GETGROUPMAPPINGREQUEST = _descriptor.Descriptor(
  name='GetGroupMappingRequest',
  full_name='yandex.cloud.organizationmanager.v1.GetGroupMappingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.GetGroupMappingRequest.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=361,
)


_GETGROUPMAPPINGRESPONSE = _descriptor.Descriptor(
  name='GetGroupMappingResponse',
  full_name='yandex.cloud.organizationmanager.v1.GetGroupMappingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_mapping', full_name='yandex.cloud.organizationmanager.v1.GetGroupMappingResponse.group_mapping', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=363,
  serialized_end=462,
)


_CREATEGROUPMAPPINGREQUEST = _descriptor.Descriptor(
  name='CreateGroupMappingRequest',
  full_name='yandex.cloud.organizationmanager.v1.CreateGroupMappingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.CreateGroupMappingRequest.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.organizationmanager.v1.CreateGroupMappingRequest.enabled', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=545,
)


_CREATEGROUPMAPPINGMETADATA = _descriptor.Descriptor(
  name='CreateGroupMappingMetadata',
  full_name='yandex.cloud.organizationmanager.v1.CreateGroupMappingMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.CreateGroupMappingMetadata.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=598,
)


_UPDATEGROUPMAPPINGREQUEST = _descriptor.Descriptor(
  name='UpdateGroupMappingRequest',
  full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingRequest.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_fields', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingRequest.updated_fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingRequest.enabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=601,
  serialized_end=740,
)


_UPDATEGROUPMAPPINGMETADATA = _descriptor.Descriptor(
  name='UpdateGroupMappingMetadata',
  full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingMetadata.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=742,
  serialized_end=793,
)


_DELETEGROUPMAPPINGREQUEST = _descriptor.Descriptor(
  name='DeleteGroupMappingRequest',
  full_name='yandex.cloud.organizationmanager.v1.DeleteGroupMappingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.DeleteGroupMappingRequest.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=795,
  serialized_end=859,
)


_DELETEGROUPMAPPINGMETADATA = _descriptor.Descriptor(
  name='DeleteGroupMappingMetadata',
  full_name='yandex.cloud.organizationmanager.v1.DeleteGroupMappingMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.DeleteGroupMappingMetadata.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=861,
  serialized_end=912,
)


_UPDATEGROUPMAPPINGITEMSREQUEST = _descriptor.Descriptor(
  name='UpdateGroupMappingItemsRequest',
  full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsRequest.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_mapping_item_deltas', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsRequest.group_mapping_item_deltas', index=1,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\0061-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=915,
  serialized_end=1091,
)


_GROUPMAPPINGITEMDELTA = _descriptor.Descriptor(
  name='GroupMappingItemDelta',
  full_name='yandex.cloud.organizationmanager.v1.GroupMappingItemDelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='yandex.cloud.organizationmanager.v1.GroupMappingItemDelta.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='yandex.cloud.organizationmanager.v1.GroupMappingItemDelta.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GROUPMAPPINGITEMDELTA_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1094,
  serialized_end=1324,
)


_UPDATEGROUPMAPPINGITEMSMETADATA = _descriptor.Descriptor(
  name='UpdateGroupMappingItemsMetadata',
  full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsMetadata.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1326,
  serialized_end=1382,
)


_UPDATEGROUPMAPPINGITEMSRESPONSE = _descriptor.Descriptor(
  name='UpdateGroupMappingItemsResponse',
  full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_mapping_item_deltas', full_name='yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsResponse.group_mapping_item_deltas', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1385,
  serialized_end=1513,
)


_LISTGROUPMAPPINGITEMSREQUEST = _descriptor.Descriptor(
  name='ListGroupMappingItemsRequest',
  full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsRequest.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=2000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1516,
  serialized_end=1674,
)


_LISTGROUPMAPPINGITEMSRESPONSE = _descriptor.Descriptor(
  name='ListGroupMappingItemsResponse',
  full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_mapping_items', full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsResponse.group_mapping_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.organizationmanager.v1.ListGroupMappingItemsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1677,
  serialized_end=1817,
)

_GETGROUPMAPPINGRESPONSE.fields_by_name['group_mapping'].message_type = yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_group__mapping__pb2._GROUPMAPPING
_UPDATEGROUPMAPPINGREQUEST.fields_by_name['updated_fields'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATEGROUPMAPPINGITEMSREQUEST.fields_by_name['group_mapping_item_deltas'].message_type = _GROUPMAPPINGITEMDELTA
_GROUPMAPPINGITEMDELTA.fields_by_name['item'].message_type = yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_group__mapping__pb2._GROUPMAPPINGITEM
_GROUPMAPPINGITEMDELTA.fields_by_name['action'].enum_type = _GROUPMAPPINGITEMDELTA_ACTION
_GROUPMAPPINGITEMDELTA_ACTION.containing_type = _GROUPMAPPINGITEMDELTA
_UPDATEGROUPMAPPINGITEMSRESPONSE.fields_by_name['group_mapping_item_deltas'].message_type = _GROUPMAPPINGITEMDELTA
_LISTGROUPMAPPINGITEMSRESPONSE.fields_by_name['group_mapping_items'].message_type = yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_group__mapping__pb2._GROUPMAPPINGITEM
DESCRIPTOR.message_types_by_name['GetGroupMappingRequest'] = _GETGROUPMAPPINGREQUEST
DESCRIPTOR.message_types_by_name['GetGroupMappingResponse'] = _GETGROUPMAPPINGRESPONSE
DESCRIPTOR.message_types_by_name['CreateGroupMappingRequest'] = _CREATEGROUPMAPPINGREQUEST
DESCRIPTOR.message_types_by_name['CreateGroupMappingMetadata'] = _CREATEGROUPMAPPINGMETADATA
DESCRIPTOR.message_types_by_name['UpdateGroupMappingRequest'] = _UPDATEGROUPMAPPINGREQUEST
DESCRIPTOR.message_types_by_name['UpdateGroupMappingMetadata'] = _UPDATEGROUPMAPPINGMETADATA
DESCRIPTOR.message_types_by_name['DeleteGroupMappingRequest'] = _DELETEGROUPMAPPINGREQUEST
DESCRIPTOR.message_types_by_name['DeleteGroupMappingMetadata'] = _DELETEGROUPMAPPINGMETADATA
DESCRIPTOR.message_types_by_name['UpdateGroupMappingItemsRequest'] = _UPDATEGROUPMAPPINGITEMSREQUEST
DESCRIPTOR.message_types_by_name['GroupMappingItemDelta'] = _GROUPMAPPINGITEMDELTA
DESCRIPTOR.message_types_by_name['UpdateGroupMappingItemsMetadata'] = _UPDATEGROUPMAPPINGITEMSMETADATA
DESCRIPTOR.message_types_by_name['UpdateGroupMappingItemsResponse'] = _UPDATEGROUPMAPPINGITEMSRESPONSE
DESCRIPTOR.message_types_by_name['ListGroupMappingItemsRequest'] = _LISTGROUPMAPPINGITEMSREQUEST
DESCRIPTOR.message_types_by_name['ListGroupMappingItemsResponse'] = _LISTGROUPMAPPINGITEMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGroupMappingRequest = _reflection.GeneratedProtocolMessageType('GetGroupMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGROUPMAPPINGREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.GetGroupMappingRequest)
  })
_sym_db.RegisterMessage(GetGroupMappingRequest)

GetGroupMappingResponse = _reflection.GeneratedProtocolMessageType('GetGroupMappingResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGROUPMAPPINGRESPONSE,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.GetGroupMappingResponse)
  })
_sym_db.RegisterMessage(GetGroupMappingResponse)

CreateGroupMappingRequest = _reflection.GeneratedProtocolMessageType('CreateGroupMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGROUPMAPPINGREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.CreateGroupMappingRequest)
  })
_sym_db.RegisterMessage(CreateGroupMappingRequest)

CreateGroupMappingMetadata = _reflection.GeneratedProtocolMessageType('CreateGroupMappingMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGROUPMAPPINGMETADATA,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.CreateGroupMappingMetadata)
  })
_sym_db.RegisterMessage(CreateGroupMappingMetadata)

UpdateGroupMappingRequest = _reflection.GeneratedProtocolMessageType('UpdateGroupMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGROUPMAPPINGREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UpdateGroupMappingRequest)
  })
_sym_db.RegisterMessage(UpdateGroupMappingRequest)

UpdateGroupMappingMetadata = _reflection.GeneratedProtocolMessageType('UpdateGroupMappingMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGROUPMAPPINGMETADATA,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UpdateGroupMappingMetadata)
  })
_sym_db.RegisterMessage(UpdateGroupMappingMetadata)

DeleteGroupMappingRequest = _reflection.GeneratedProtocolMessageType('DeleteGroupMappingRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGROUPMAPPINGREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.DeleteGroupMappingRequest)
  })
_sym_db.RegisterMessage(DeleteGroupMappingRequest)

DeleteGroupMappingMetadata = _reflection.GeneratedProtocolMessageType('DeleteGroupMappingMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGROUPMAPPINGMETADATA,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.DeleteGroupMappingMetadata)
  })
_sym_db.RegisterMessage(DeleteGroupMappingMetadata)

UpdateGroupMappingItemsRequest = _reflection.GeneratedProtocolMessageType('UpdateGroupMappingItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGROUPMAPPINGITEMSREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsRequest)
  })
_sym_db.RegisterMessage(UpdateGroupMappingItemsRequest)

GroupMappingItemDelta = _reflection.GeneratedProtocolMessageType('GroupMappingItemDelta', (_message.Message,), {
  'DESCRIPTOR' : _GROUPMAPPINGITEMDELTA,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.GroupMappingItemDelta)
  })
_sym_db.RegisterMessage(GroupMappingItemDelta)

UpdateGroupMappingItemsMetadata = _reflection.GeneratedProtocolMessageType('UpdateGroupMappingItemsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGROUPMAPPINGITEMSMETADATA,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsMetadata)
  })
_sym_db.RegisterMessage(UpdateGroupMappingItemsMetadata)

UpdateGroupMappingItemsResponse = _reflection.GeneratedProtocolMessageType('UpdateGroupMappingItemsResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGROUPMAPPINGITEMSRESPONSE,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UpdateGroupMappingItemsResponse)
  })
_sym_db.RegisterMessage(UpdateGroupMappingItemsResponse)

ListGroupMappingItemsRequest = _reflection.GeneratedProtocolMessageType('ListGroupMappingItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTGROUPMAPPINGITEMSREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListGroupMappingItemsRequest)
  })
_sym_db.RegisterMessage(ListGroupMappingItemsRequest)

ListGroupMappingItemsResponse = _reflection.GeneratedProtocolMessageType('ListGroupMappingItemsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTGROUPMAPPINGITEMSRESPONSE,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListGroupMappingItemsResponse)
  })
_sym_db.RegisterMessage(ListGroupMappingItemsResponse)


DESCRIPTOR._options = None
_GETGROUPMAPPINGREQUEST.fields_by_name['federation_id']._options = None
_CREATEGROUPMAPPINGREQUEST.fields_by_name['federation_id']._options = None
_UPDATEGROUPMAPPINGREQUEST.fields_by_name['federation_id']._options = None
_UPDATEGROUPMAPPINGREQUEST.fields_by_name['updated_fields']._options = None
_DELETEGROUPMAPPINGREQUEST.fields_by_name['federation_id']._options = None
_UPDATEGROUPMAPPINGITEMSREQUEST.fields_by_name['federation_id']._options = None
_UPDATEGROUPMAPPINGITEMSREQUEST.fields_by_name['group_mapping_item_deltas']._options = None
_LISTGROUPMAPPINGITEMSREQUEST.fields_by_name['federation_id']._options = None
_LISTGROUPMAPPINGITEMSREQUEST.fields_by_name['page_size']._options = None
_LISTGROUPMAPPINGITEMSREQUEST.fields_by_name['page_token']._options = None
_LISTGROUPMAPPINGITEMSREQUEST.fields_by_name['filter']._options = None

_GROUPMAPPINGSERVICE = _descriptor.ServiceDescriptor(
  name='GroupMappingService',
  full_name='yandex.cloud.organizationmanager.v1.GroupMappingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1820,
  serialized_end=2796,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.organizationmanager.v1.GroupMappingService.Get',
    index=0,
    containing_service=None,
    input_type=_GETGROUPMAPPINGREQUEST,
    output_type=_GETGROUPMAPPINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.organizationmanager.v1.GroupMappingService.Create',
    index=1,
    containing_service=None,
    input_type=_CREATEGROUPMAPPINGREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\262\322**\n\032CreateGroupMappingMetadata\022\014GroupMapping',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.organizationmanager.v1.GroupMappingService.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEGROUPMAPPINGREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\262\322**\n\032UpdateGroupMappingMetadata\022\014GroupMapping',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.organizationmanager.v1.GroupMappingService.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEGROUPMAPPINGREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\262\322*3\n\032DeleteGroupMappingMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListItems',
    full_name='yandex.cloud.organizationmanager.v1.GroupMappingService.ListItems',
    index=4,
    containing_service=None,
    input_type=_LISTGROUPMAPPINGITEMSREQUEST,
    output_type=_LISTGROUPMAPPINGITEMSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateItems',
    full_name='yandex.cloud.organizationmanager.v1.GroupMappingService.UpdateItems',
    index=5,
    containing_service=None,
    input_type=_UPDATEGROUPMAPPINGITEMSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\262\322*B\n\037UpdateGroupMappingItemsMetadata\022\037UpdateGroupMappingItemsResponse',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GROUPMAPPINGSERVICE)

DESCRIPTOR.services_by_name['GroupMappingService'] = _GROUPMAPPINGSERVICE

# @@protoc_insertion_point(module_scope)