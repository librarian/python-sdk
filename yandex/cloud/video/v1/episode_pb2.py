# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/episode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#yandex/cloud/video/v1/episode.proto\x12\x15yandex.cloud.video.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb3\x05\n\x07\x45pisode\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12\x0f\n\x07line_id\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x06 \x01(\t\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64vr_seconds\x18\t \x01(\x03\x12J\n\x11visibility_status\x18\n \x01(\x0e\x32/.yandex.cloud.video.v1.Episode.VisibilityStatus\x12J\n\rpublic_access\x18\xe8\x07 \x01(\x0b\x32\x30.yandex.cloud.video.v1.EpisodePublicAccessRightsH\x00\x12S\n\x12\x61uth_system_access\x18\xea\x07 \x01(\x0b\x32\x34.yandex.cloud.video.v1.EpisodeAuthSystemAccessRightsH\x00\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"U\n\x10VisibilityStatus\x12!\n\x1dVISIBILITY_STATUS_UNSPECIFIED\x10\x00\x12\r\n\tPUBLISHED\x10\x01\x12\x0f\n\x0bUNPUBLISHED\x10\x02\x42\x0f\n\raccess_rightsJ\x05\x08\x66\x10\xe8\x07J\x04\x08\x0b\x10\x64J\x06\x08\xe9\x07\x10\xea\x07\"\x1b\n\x19\x45pisodePublicAccessRights\"\x1f\n\x1d\x45pisodeAuthSystemAccessRightsB\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.episode_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _globals['_EPISODE']._serialized_start=96
  _globals['_EPISODE']._serialized_end=787
  _globals['_EPISODE_VISIBILITYSTATUS']._serialized_start=664
  _globals['_EPISODE_VISIBILITYSTATUS']._serialized_end=749
  _globals['_EPISODEPUBLICACCESSRIGHTS']._serialized_start=789
  _globals['_EPISODEPUBLICACCESSRIGHTS']._serialized_end=816
  _globals['_EPISODEAUTHSYSTEMACCESSRIGHTS']._serialized_start=818
  _globals['_EPISODEAUTHSYSTEMACCESSRIGHTS']._serialized_end=849
# @@protoc_insertion_point(module_scope)
