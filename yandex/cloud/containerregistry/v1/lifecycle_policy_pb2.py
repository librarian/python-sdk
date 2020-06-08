# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/lifecycle_policy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/containerregistry/v1/lifecycle_policy.proto',
  package='yandex.cloud.containerregistry.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry',
  serialized_pb=b'\n8yandex/cloud/containerregistry/v1/lifecycle_policy.proto\x12!yandex.cloud.containerregistry.v1\x1a\x1dyandex/cloud/validation.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x02\n\x0fLifecyclePolicy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rrepository_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12I\n\x06status\x18\x05 \x01(\x0e\x32\x39.yandex.cloud.containerregistry.v1.LifecyclePolicy.Status\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x05rules\x18\x07 \x03(\x0b\x32\x30.yandex.cloud.containerregistry.v1.LifecycleRule\":\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xbc\x01\n\rLifecycleRule\x12\x1e\n\x0b\x64\x65scription\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12;\n\rexpire_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05>=24h\x12\x1d\n\ntag_regexp\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x10\n\x08untagged\x18\x04 \x01(\x08\x12\x1d\n\x0cretained_top\x18\x05 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0B\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_LIFECYCLEPOLICY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=469,
  serialized_end=527,
)
_sym_db.RegisterEnumDescriptor(_LIFECYCLEPOLICY_STATUS)


_LIFECYCLEPOLICY = _descriptor.Descriptor(
  name='LifecyclePolicy',
  full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repository_id', full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.repository_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='yandex.cloud.containerregistry.v1.LifecyclePolicy.rules', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LIFECYCLEPOLICY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=527,
)


_LIFECYCLERULE = _descriptor.Descriptor(
  name='LifecycleRule',
  full_name='yandex.cloud.containerregistry.v1.LifecycleRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.containerregistry.v1.LifecycleRule.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire_period', full_name='yandex.cloud.containerregistry.v1.LifecycleRule.expire_period', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\005>=24h', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_regexp', full_name='yandex.cloud.containerregistry.v1.LifecycleRule.tag_regexp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='untagged', full_name='yandex.cloud.containerregistry.v1.LifecycleRule.untagged', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retained_top', full_name='yandex.cloud.containerregistry.v1.LifecycleRule.retained_top', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR),
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
  serialized_start=530,
  serialized_end=718,
)

_LIFECYCLEPOLICY.fields_by_name['status'].enum_type = _LIFECYCLEPOLICY_STATUS
_LIFECYCLEPOLICY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LIFECYCLEPOLICY.fields_by_name['rules'].message_type = _LIFECYCLERULE
_LIFECYCLEPOLICY_STATUS.containing_type = _LIFECYCLEPOLICY
_LIFECYCLERULE.fields_by_name['expire_period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['LifecyclePolicy'] = _LIFECYCLEPOLICY
DESCRIPTOR.message_types_by_name['LifecycleRule'] = _LIFECYCLERULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LifecyclePolicy = _reflection.GeneratedProtocolMessageType('LifecyclePolicy', (_message.Message,), {
  'DESCRIPTOR' : _LIFECYCLEPOLICY,
  '__module__' : 'yandex.cloud.containerregistry.v1.lifecycle_policy_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.LifecyclePolicy)
  })
_sym_db.RegisterMessage(LifecyclePolicy)

LifecycleRule = _reflection.GeneratedProtocolMessageType('LifecycleRule', (_message.Message,), {
  'DESCRIPTOR' : _LIFECYCLERULE,
  '__module__' : 'yandex.cloud.containerregistry.v1.lifecycle_policy_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.LifecycleRule)
  })
_sym_db.RegisterMessage(LifecycleRule)


DESCRIPTOR._options = None
_LIFECYCLERULE.fields_by_name['description']._options = None
_LIFECYCLERULE.fields_by_name['expire_period']._options = None
_LIFECYCLERULE.fields_by_name['tag_regexp']._options = None
_LIFECYCLERULE.fields_by_name['retained_top']._options = None
# @@protoc_insertion_point(module_scope)
