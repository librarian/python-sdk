# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/stream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"yandex/cloud/video/v1/stream.proto\x12\x15yandex.cloud.video.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x93\x06\n\x06Stream\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x0f\n\x07line_id\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x06 \x01(\t\x12:\n\x06status\x18\x08 \x01(\x0e\x32*.yandex.cloud.video.v1.Stream.StreamStatus\x12.\n\nstart_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cpublish_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\ton_demand\x18\xe8\x07 \x01(\x0b\x32\x1f.yandex.cloud.video.v1.OnDemandH\x00\x12\x34\n\x08schedule\x18\xe9\x07 \x01(\x0b\x32\x1f.yandex.cloud.video.v1.ScheduleH\x00\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x06labels\x18\xc8\x01 \x03(\x0b\x32).yandex.cloud.video.v1.Stream.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"m\n\x0cStreamStatus\x12\x1d\n\x19STREAM_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07OFFLINE\x10\x01\x12\r\n\tPREPARING\x10\x02\x12\t\n\x05READY\x10\x03\x12\t\n\x05ONAIR\x10\x04\x12\x0c\n\x08\x46INISHED\x10\x05\x42\r\n\x0bstream_typeJ\x05\x08\x66\x10\xc8\x01J\x06\x08\xc9\x01\x10\xe8\x07J\x04\x08\x0c\x10\x64J\x04\x08\x07\x10\x08\"\n\n\x08OnDemand\"k\n\x08Schedule\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.stream_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _STREAM_LABELSENTRY._options = None
  _STREAM_LABELSENTRY._serialized_options = b'8\001'
  _globals['_STREAM']._serialized_start=95
  _globals['_STREAM']._serialized_end=882
  _globals['_STREAM_LABELSENTRY']._serialized_start=684
  _globals['_STREAM_LABELSENTRY']._serialized_end=729
  _globals['_STREAM_STREAMSTATUS']._serialized_start=731
  _globals['_STREAM_STREAMSTATUS']._serialized_end=840
  _globals['_ONDEMAND']._serialized_start=884
  _globals['_ONDEMAND']._serialized_end=894
  _globals['_SCHEDULE']._serialized_start=896
  _globals['_SCHEDULE']._serialized_end=1003
# @@protoc_insertion_point(module_scope)
