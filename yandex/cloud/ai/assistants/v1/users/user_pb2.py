# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/assistants/v1/users/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.common import common_pb2 as yandex_dot_cloud_dot_ai_dot_common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/ai/assistants/v1/users/user.proto\x12#yandex.cloud.ai.assistants.v1.users\x1a#yandex/cloud/ai/common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcb\x03\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x12\n\ncreated_by\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nupdated_by\x18\x08 \x01(\t\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x11\x65xpiration_config\x18\n \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12.\n\nexpires_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x45\n\x06labels\x18\x0c \x03(\x0b\x32\x35.yandex.cloud.ai.assistants.v1.users.User.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42x\n\'yandex.cloud.api.ai.assistants.v1.usersZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/users;usersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.assistants.v1.users.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'yandex.cloud.api.ai.assistants.v1.usersZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/users;users'
  _USER_LABELSENTRY._options = None
  _USER_LABELSENTRY._serialized_options = b'8\001'
  _globals['_USER']._serialized_start=158
  _globals['_USER']._serialized_end=617
  _globals['_USER_LABELSENTRY']._serialized_start=572
  _globals['_USER_LABELSENTRY']._serialized_end=617
# @@protoc_insertion_point(module_scope)
