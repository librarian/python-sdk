# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/logging/v1/log_entry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.logging.v1 import log_resource_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/logging/v1/log_entry.proto\x12\x17yandex.cloud.logging.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a*yandex/cloud/logging/v1/log_resource.proto\x1a\x1dyandex/cloud/validation.proto\"\xf9\x02\n\x08LogEntry\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12;\n\x08resource\x18\x02 \x01(\x0b\x32).yandex.cloud.logging.v1.LogEntryResource\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bingested_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08saved_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x05level\x18\x06 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\x12\x0f\n\x07message\x18\x07 \x01(\t\x12-\n\x0cjson_payload\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1d\n\x0bstream_name\x18\t \x01(\tB\x08\x8a\xc8\x31\x04<=63\"\xf8\x01\n\x10IncomingLogEntry\x12\x33\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\x12\x36\n\x05level\x18\x02 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\x12\x1c\n\x07message\x18\x03 \x01(\tB\x0b\xba\xc8\x31\x07<=65536\x12:\n\x0cjson_payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x0b\xba\xc8\x31\x07<=65536\x12\x1d\n\x0bstream_name\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=63\"\xab\x01\n\x10LogEntryDefaults\x12\x36\n\x05level\x18\x02 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\x12:\n\x0cjson_payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x0b\xba\xc8\x31\x07<=65536\x12\x1d\n\x0bstream_name\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=63J\x04\x08\x03\x10\x04\"\x99\x01\n\x0b\x44\x65stination\x12;\n\x0clog_group_id\x18\x01 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12\x38\n\tfolder_id\x18\x02 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x42\x13\n\x0b\x64\x65stination\x12\x04\xc0\xc1\x31\x01\"\xa2\x01\n\x08LogLevel\x12\x36\n\x05level\x18\x01 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\"^\n\x05Level\x12\x15\n\x11LEVEL_UNSPECIFIED\x10\x00\x12\t\n\x05TRACE\x10\x01\x12\t\n\x05\x44\x45\x42UG\x10\x02\x12\x08\n\x04INFO\x10\x03\x12\x08\n\x04WARN\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x12\t\n\x05\x46\x41TAL\x10\x06\x42\x62\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.logging.v1.log_entry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging'
  _LOGENTRY.fields_by_name['stream_name']._options = None
  _LOGENTRY.fields_by_name['stream_name']._serialized_options = b'\212\3101\004<=63'
  _INCOMINGLOGENTRY.fields_by_name['timestamp']._options = None
  _INCOMINGLOGENTRY.fields_by_name['timestamp']._serialized_options = b'\350\3071\001'
  _INCOMINGLOGENTRY.fields_by_name['message']._options = None
  _INCOMINGLOGENTRY.fields_by_name['message']._serialized_options = b'\272\3101\007<=65536'
  _INCOMINGLOGENTRY.fields_by_name['json_payload']._options = None
  _INCOMINGLOGENTRY.fields_by_name['json_payload']._serialized_options = b'\272\3101\007<=65536'
  _INCOMINGLOGENTRY.fields_by_name['stream_name']._options = None
  _INCOMINGLOGENTRY.fields_by_name['stream_name']._serialized_options = b'\212\3101\004<=63'
  _LOGENTRYDEFAULTS.fields_by_name['json_payload']._options = None
  _LOGENTRYDEFAULTS.fields_by_name['json_payload']._serialized_options = b'\272\3101\007<=65536'
  _LOGENTRYDEFAULTS.fields_by_name['stream_name']._options = None
  _LOGENTRYDEFAULTS.fields_by_name['stream_name']._serialized_options = b'\212\3101\004<=63'
  _DESTINATION.oneofs_by_name['destination']._options = None
  _DESTINATION.oneofs_by_name['destination']._serialized_options = b'\300\3011\001'
  _DESTINATION.fields_by_name['log_group_id']._options = None
  _DESTINATION.fields_by_name['log_group_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _DESTINATION.fields_by_name['folder_id']._options = None
  _DESTINATION.fields_by_name['folder_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _globals['_LOGENTRY']._serialized_start=207
  _globals['_LOGENTRY']._serialized_end=584
  _globals['_INCOMINGLOGENTRY']._serialized_start=587
  _globals['_INCOMINGLOGENTRY']._serialized_end=835
  _globals['_LOGENTRYDEFAULTS']._serialized_start=838
  _globals['_LOGENTRYDEFAULTS']._serialized_end=1009
  _globals['_DESTINATION']._serialized_start=1012
  _globals['_DESTINATION']._serialized_end=1165
  _globals['_LOGLEVEL']._serialized_start=1168
  _globals['_LOGLEVEL']._serialized_end=1330
  _globals['_LOGLEVEL_LEVEL']._serialized_start=1236
  _globals['_LOGLEVEL_LEVEL']._serialized_end=1330
# @@protoc_insertion_point(module_scope)
