# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/agent/v1/test_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.loadtesting.agent.v1 import test_pb2 as yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_test__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/loadtesting/agent/v1/test_service.proto',
  package='yandex.cloud.loadtesting.agent.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agent',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4yandex/cloud/loadtesting/agent/v1/test_service.proto\x12!yandex.cloud.loadtesting.agent.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1dyandex/cloud/validation.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a,yandex/cloud/loadtesting/agent/v1/test.proto\"/\n\x0eGetTestRequest\x12\x1d\n\x07test_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xe3\x06\n\x11\x43reateTestRequest\x12\x1b\n\tfolder_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x91\x01\n\x06labels\x18\x04 \x03(\x0b\x32@.yandex.cloud.loadtesting.agent.v1.CreateTestRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x12\x44\n\tgenerator\x18\x05 \x01(\x0e\x32\x31.yandex.cloud.loadtesting.agent.v1.Test.Generator\x12#\n\x11\x61gent_instance_id\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12$\n\x0etarget_address\x18\x07 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x13\n\x0btarget_port\x18\x08 \x01(\x03\x12 \n\x0etarget_version\x18\t \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x11\n\tinstances\x18\n \x01(\x03\x12\x42\n\rload_schedule\x18\x0b \x01(\x0b\x32+.yandex.cloud.loadtesting.agent.v1.Schedule\x12\x14\n\x06\x63onfig\x18\x0c \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x07\x61mmo_id\x18\r \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tammo_urls\x18\x0e \x03(\tB\n\x8a\xc8\x31\x06<=1024\x12\x14\n\x0c\x61mmo_headers\x18\x0f \x03(\t\x12>\n\tammo_type\x18\x10 \x01(\x0e\x32+.yandex.cloud.loadtesting.agent.v1.AmmoType\x12\x0b\n\x03ssl\x18\x11 \x01(\x08\x12\x17\n\x0fimbalance_point\x18\x12 \x01(\x03\x12\x14\n\x0cimbalance_ts\x18\x13 \x01(\x03\x12\x1c\n\x14logging_log_group_id\x18\x14 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x12\x43reateTestMetadata\x12\x0f\n\x07test_id\x18\x01 \x01(\t\"\xf5\x03\n\x11UpdateTestRequest\x12\x1d\n\x07test_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x91\x01\n\x06labels\x18\x05 \x03(\x0b\x32@.yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x12\x10\n\x08\x66\x61vorite\x18\x06 \x01(\x08\x12 \n\x0etarget_version\x18\x07 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x17\n\x0fimbalance_point\x18\x08 \x01(\x03\x12\x14\n\x0cimbalance_ts\x18\t \x01(\x03\x12\x19\n\x11imbalance_comment\x18\n \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x12UpdateTestMetadata\x12\x0f\n\x07test_id\x18\x01 \x01(\t2\xfe\x03\n\x0bTestService\x12\x90\x01\n\x03Get\x12\x31.yandex.cloud.loadtesting.agent.v1.GetTestRequest\x1a\'.yandex.cloud.loadtesting.agent.v1.Test\"-\x82\xd3\xe4\x93\x02\'\x12%/loadtesting/agent/v1/tests/{test_id}\x12\xa7\x01\n\x06\x43reate\x12\x34.yandex.cloud.loadtesting.agent.v1.CreateTestRequest\x1a!.yandex.cloud.operation.Operation\"D\x82\xd3\xe4\x93\x02 \"\x1b/loadtesting/agent/v1/tests:\x01*\xb2\xd2*\x1a\n\x12\x43reateTestMetadata\x12\x04Test\x12\xb1\x01\n\x06Update\x12\x34.yandex.cloud.loadtesting.agent.v1.UpdateTestRequest\x1a!.yandex.cloud.operation.Operation\"N\x82\xd3\xe4\x93\x02*2%/loadtesting/agent/v1/tests/{test_id}:\x01*\xb2\xd2*\x1a\n\x12UpdateTestMetadata\x12\x04TestBt\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agentb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_test__pb2.DESCRIPTOR,])




_GETTESTREQUEST = _descriptor.Descriptor(
  name='GetTestRequest',
  full_name='yandex.cloud.loadtesting.agent.v1.GetTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_id', full_name='yandex.cloud.loadtesting.agent.v1.GetTestRequest.test_id', index=0,
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
  serialized_start=306,
  serialized_end=353,
)


_CREATETESTREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1178,
  serialized_end=1223,
)

_CREATETESTREQUEST = _descriptor.Descriptor(
  name='CreateTestRequest',
  full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generator', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.generator', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent_instance_id', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.agent_instance_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_address', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.target_address', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_port', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.target_port', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_version', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.target_version', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instances', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.instances', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_schedule', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.load_schedule', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.config', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ammo_id', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.ammo_id', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ammo_urls', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.ammo_urls', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=1024', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ammo_headers', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.ammo_headers', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ammo_type', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.ammo_type', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssl', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.ssl', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imbalance_point', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.imbalance_point', index=17,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imbalance_ts', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.imbalance_ts', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logging_log_group_id', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestRequest.logging_log_group_id', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CREATETESTREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=1223,
)


_CREATETESTMETADATA = _descriptor.Descriptor(
  name='CreateTestMetadata',
  full_name='yandex.cloud.loadtesting.agent.v1.CreateTestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_id', full_name='yandex.cloud.loadtesting.agent.v1.CreateTestMetadata.test_id', index=0,
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
  serialized_start=1225,
  serialized_end=1262,
)


_UPDATETESTREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1178,
  serialized_end=1223,
)

_UPDATETESTREQUEST = _descriptor.Descriptor(
  name='UpdateTestRequest',
  full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_id', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.test_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='favorite', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.favorite', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_version', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.target_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imbalance_point', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.imbalance_point', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imbalance_ts', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.imbalance_ts', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imbalance_comment', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.imbalance_comment', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_UPDATETESTREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1265,
  serialized_end=1766,
)


_UPDATETESTMETADATA = _descriptor.Descriptor(
  name='UpdateTestMetadata',
  full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_id', full_name='yandex.cloud.loadtesting.agent.v1.UpdateTestMetadata.test_id', index=0,
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
  serialized_start=1768,
  serialized_end=1805,
)

_CREATETESTREQUEST_LABELSENTRY.containing_type = _CREATETESTREQUEST
_CREATETESTREQUEST.fields_by_name['labels'].message_type = _CREATETESTREQUEST_LABELSENTRY
_CREATETESTREQUEST.fields_by_name['generator'].enum_type = yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_test__pb2._TEST_GENERATOR
_CREATETESTREQUEST.fields_by_name['load_schedule'].message_type = yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_test__pb2._SCHEDULE
_CREATETESTREQUEST.fields_by_name['ammo_type'].enum_type = yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_test__pb2._AMMOTYPE
_UPDATETESTREQUEST_LABELSENTRY.containing_type = _UPDATETESTREQUEST
_UPDATETESTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATETESTREQUEST.fields_by_name['labels'].message_type = _UPDATETESTREQUEST_LABELSENTRY
DESCRIPTOR.message_types_by_name['GetTestRequest'] = _GETTESTREQUEST
DESCRIPTOR.message_types_by_name['CreateTestRequest'] = _CREATETESTREQUEST
DESCRIPTOR.message_types_by_name['CreateTestMetadata'] = _CREATETESTMETADATA
DESCRIPTOR.message_types_by_name['UpdateTestRequest'] = _UPDATETESTREQUEST
DESCRIPTOR.message_types_by_name['UpdateTestMetadata'] = _UPDATETESTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTestRequest = _reflection.GeneratedProtocolMessageType('GetTestRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTESTREQUEST,
  '__module__' : 'yandex.cloud.loadtesting.agent.v1.test_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.GetTestRequest)
  })
_sym_db.RegisterMessage(GetTestRequest)

CreateTestRequest = _reflection.GeneratedProtocolMessageType('CreateTestRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATETESTREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.loadtesting.agent.v1.test_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.CreateTestRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATETESTREQUEST,
  '__module__' : 'yandex.cloud.loadtesting.agent.v1.test_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.CreateTestRequest)
  })
_sym_db.RegisterMessage(CreateTestRequest)
_sym_db.RegisterMessage(CreateTestRequest.LabelsEntry)

CreateTestMetadata = _reflection.GeneratedProtocolMessageType('CreateTestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATETESTMETADATA,
  '__module__' : 'yandex.cloud.loadtesting.agent.v1.test_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.CreateTestMetadata)
  })
_sym_db.RegisterMessage(CreateTestMetadata)

UpdateTestRequest = _reflection.GeneratedProtocolMessageType('UpdateTestRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATETESTREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.loadtesting.agent.v1.test_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATETESTREQUEST,
  '__module__' : 'yandex.cloud.loadtesting.agent.v1.test_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.UpdateTestRequest)
  })
_sym_db.RegisterMessage(UpdateTestRequest)
_sym_db.RegisterMessage(UpdateTestRequest.LabelsEntry)

UpdateTestMetadata = _reflection.GeneratedProtocolMessageType('UpdateTestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETESTMETADATA,
  '__module__' : 'yandex.cloud.loadtesting.agent.v1.test_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.UpdateTestMetadata)
  })
_sym_db.RegisterMessage(UpdateTestMetadata)


DESCRIPTOR._options = None
_GETTESTREQUEST.fields_by_name['test_id']._options = None
_CREATETESTREQUEST_LABELSENTRY._options = None
_CREATETESTREQUEST.fields_by_name['folder_id']._options = None
_CREATETESTREQUEST.fields_by_name['name']._options = None
_CREATETESTREQUEST.fields_by_name['description']._options = None
_CREATETESTREQUEST.fields_by_name['labels']._options = None
_CREATETESTREQUEST.fields_by_name['agent_instance_id']._options = None
_CREATETESTREQUEST.fields_by_name['target_address']._options = None
_CREATETESTREQUEST.fields_by_name['target_version']._options = None
_CREATETESTREQUEST.fields_by_name['config']._options = None
_CREATETESTREQUEST.fields_by_name['ammo_id']._options = None
_CREATETESTREQUEST.fields_by_name['ammo_urls']._options = None
_UPDATETESTREQUEST_LABELSENTRY._options = None
_UPDATETESTREQUEST.fields_by_name['test_id']._options = None
_UPDATETESTREQUEST.fields_by_name['name']._options = None
_UPDATETESTREQUEST.fields_by_name['description']._options = None
_UPDATETESTREQUEST.fields_by_name['labels']._options = None
_UPDATETESTREQUEST.fields_by_name['target_version']._options = None

_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='yandex.cloud.loadtesting.agent.v1.TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1808,
  serialized_end=2318,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.loadtesting.agent.v1.TestService.Get',
    index=0,
    containing_service=None,
    input_type=_GETTESTREQUEST,
    output_type=yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_test__pb2._TEST,
    serialized_options=b'\202\323\344\223\002\'\022%/loadtesting/agent/v1/tests/{test_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.loadtesting.agent.v1.TestService.Create',
    index=1,
    containing_service=None,
    input_type=_CREATETESTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002 \"\033/loadtesting/agent/v1/tests:\001*\262\322*\032\n\022CreateTestMetadata\022\004Test',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.loadtesting.agent.v1.TestService.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATETESTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002*2%/loadtesting/agent/v1/tests/{test_id}:\001*\262\322*\032\n\022UpdateTestMetadata\022\004Test',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)