# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/episode_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import episode_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_episode__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/video/v1/episode_service.proto\x12\x15yandex.cloud.video.v1\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a#yandex/cloud/video/v1/episode.proto\"\'\n\x11GetEpisodeRequest\x12\x12\n\nepisode_id\x18\x01 \x01(\t\"\x93\x01\n\x13ListEpisodesRequest\x12\x13\n\tstream_id\x18\x01 \x01(\tH\x00\x12\x11\n\x07line_id\x18\x02 \x01(\tH\x00\x12\x11\n\tpage_size\x18\x64 \x01(\x03\x12\x12\n\npage_token\x18\x65 \x01(\t\x12\x10\n\x08order_by\x18\x66 \x01(\t\x12\x0e\n\x06\x66ilter\x18g \x01(\tB\x0b\n\tparent_id\"a\n\x14ListEpisodesResponse\x12\x30\n\x08\x65pisodes\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.video.v1.Episode\x12\x17\n\x0fnext_page_token\x18\x64 \x01(\t\"\xb5\x03\n\x14\x43reateEpisodeRequest\x12\x13\n\tstream_id\x18\x64 \x01(\tH\x00\x12\x11\n\x07line_id\x18\x65 \x01(\tH\x00\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x04 \x01(\t\x12.\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64vr_seconds\x18\x07 \x01(\x03\x12J\n\rpublic_access\x18\xe8\x07 \x01(\x0b\x32\x30.yandex.cloud.video.v1.EpisodePublicAccessParamsH\x01\x12S\n\x12\x61uth_system_access\x18\xea\x07 \x01(\x0b\x32\x34.yandex.cloud.video.v1.EpisodeAuthSystemAccessParamsH\x01\x42\x0b\n\tparent_idB\x0f\n\raccess_rightsJ\x06\x08\xe9\x07\x10\xea\x07\"\x1b\n\x19\x45pisodePublicAccessParams\"\x1f\n\x1d\x45pisodeAuthSystemAccessParams\"+\n\x15\x43reateEpisodeMetadata\x12\x12\n\nepisode_id\x18\x01 \x01(\t\"\xc4\x03\n\x14UpdateEpisodeRequest\x12\x12\n\nepisode_id\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x05 \x01(\t\x12.\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64vr_seconds\x18\x08 \x01(\x03\x12J\n\rpublic_access\x18\xe8\x07 \x01(\x0b\x32\x30.yandex.cloud.video.v1.EpisodePublicAccessParamsH\x00\x12S\n\x12\x61uth_system_access\x18\xea\x07 \x01(\x0b\x32\x34.yandex.cloud.video.v1.EpisodeAuthSystemAccessParamsH\x00\x42\x0f\n\raccess_rightsJ\x06\x08\xe9\x07\x10\xea\x07\"+\n\x15UpdateEpisodeMetadata\x12\x12\n\nepisode_id\x18\x01 \x01(\t\"*\n\x14\x44\x65leteEpisodeRequest\x12\x12\n\nepisode_id\x18\x01 \x01(\t\"+\n\x15\x44\x65leteEpisodeMetadata\x12\x12\n\nepisode_id\x18\x01 \x01(\t\"\xd1\x01\n\x1bPerformEpisodeActionRequest\x12\x12\n\nepisode_id\x18\x01 \x01(\t\x12?\n\x07publish\x18\xea\x07 \x01(\x0b\x32+.yandex.cloud.video.v1.PublishEpisodeActionH\x00\x12\x43\n\tunpublish\x18\xeb\x07 \x01(\x0b\x32-.yandex.cloud.video.v1.UnpublishEpisodeActionH\x00\x42\x08\n\x06\x61\x63tionJ\x06\x08\xe8\x07\x10\xe9\x07J\x06\x08\xe9\x07\x10\xea\x07\"\x16\n\x14PublishEpisodeAction\"\x18\n\x16UnpublishEpisodeAction\"2\n\x1cPerformEpisodeActionMetadata\x12\x12\n\nepisode_id\x18\x01 \x01(\t\"l\n\x1aGetEpisodePlayerURLRequest\x12\x12\n\nepisode_id\x18\x01 \x01(\t\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.yandex.cloud.video.v1.EpisodePlayerParams\"E\n\x13\x45pisodePlayerParams\x12\x0c\n\x04mute\x18\x01 \x01(\x08\x12\x10\n\x08\x61utoplay\x18\x02 \x01(\x08\x12\x0e\n\x06hidden\x18\x03 \x01(\x08\"?\n\x1bGetEpisodePlayerURLResponse\x12\x12\n\nplayer_url\x18\x01 \x01(\t\x12\x0c\n\x04html\x18\x02 \x01(\t2\xe4\x06\n\x0e\x45pisodeService\x12Q\n\x03Get\x12(.yandex.cloud.video.v1.GetEpisodeRequest\x1a\x1e.yandex.cloud.video.v1.Episode\"\x00\x12\x61\n\x04List\x12*.yandex.cloud.video.v1.ListEpisodesRequest\x1a+.yandex.cloud.video.v1.ListEpisodesResponse\"\x00\x12~\n\x06\x43reate\x12+.yandex.cloud.video.v1.CreateEpisodeRequest\x1a!.yandex.cloud.operation.Operation\"$\xb2\xd2* \n\x15\x43reateEpisodeMetadata\x12\x07\x45pisode\x12~\n\x06Update\x12+.yandex.cloud.video.v1.UpdateEpisodeRequest\x1a!.yandex.cloud.operation.Operation\"$\xb2\xd2* \n\x15UpdateEpisodeMetadata\x12\x07\x45pisode\x12\x8c\x01\n\x06\x44\x65lete\x12+.yandex.cloud.video.v1.DeleteEpisodeRequest\x1a!.yandex.cloud.operation.Operation\"2\xb2\xd2*.\n\x15\x44\x65leteEpisodeMetadata\x12\x15google.protobuf.Empty\x12\x93\x01\n\rPerformAction\x12\x32.yandex.cloud.video.v1.PerformEpisodeActionRequest\x1a!.yandex.cloud.operation.Operation\"+\xb2\xd2*\'\n\x1cPerformEpisodeActionMetadata\x12\x07\x45pisode\x12w\n\x0cGetPlayerURL\x12\x31.yandex.cloud.video.v1.GetEpisodePlayerURLRequest\x1a\x32.yandex.cloud.video.v1.GetEpisodePlayerURLResponse\"\x00\x42\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.episode_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _EPISODESERVICE.methods_by_name['Create']._options = None
  _EPISODESERVICE.methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateEpisodeMetadata\022\007Episode'
  _EPISODESERVICE.methods_by_name['Update']._options = None
  _EPISODESERVICE.methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateEpisodeMetadata\022\007Episode'
  _EPISODESERVICE.methods_by_name['Delete']._options = None
  _EPISODESERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteEpisodeMetadata\022\025google.protobuf.Empty'
  _EPISODESERVICE.methods_by_name['PerformAction']._options = None
  _EPISODESERVICE.methods_by_name['PerformAction']._serialized_options = b'\262\322*\'\n\034PerformEpisodeActionMetadata\022\007Episode'
  _globals['_GETEPISODEREQUEST']._serialized_start=248
  _globals['_GETEPISODEREQUEST']._serialized_end=287
  _globals['_LISTEPISODESREQUEST']._serialized_start=290
  _globals['_LISTEPISODESREQUEST']._serialized_end=437
  _globals['_LISTEPISODESRESPONSE']._serialized_start=439
  _globals['_LISTEPISODESRESPONSE']._serialized_end=536
  _globals['_CREATEEPISODEREQUEST']._serialized_start=539
  _globals['_CREATEEPISODEREQUEST']._serialized_end=976
  _globals['_EPISODEPUBLICACCESSPARAMS']._serialized_start=978
  _globals['_EPISODEPUBLICACCESSPARAMS']._serialized_end=1005
  _globals['_EPISODEAUTHSYSTEMACCESSPARAMS']._serialized_start=1007
  _globals['_EPISODEAUTHSYSTEMACCESSPARAMS']._serialized_end=1038
  _globals['_CREATEEPISODEMETADATA']._serialized_start=1040
  _globals['_CREATEEPISODEMETADATA']._serialized_end=1083
  _globals['_UPDATEEPISODEREQUEST']._serialized_start=1086
  _globals['_UPDATEEPISODEREQUEST']._serialized_end=1538
  _globals['_UPDATEEPISODEMETADATA']._serialized_start=1540
  _globals['_UPDATEEPISODEMETADATA']._serialized_end=1583
  _globals['_DELETEEPISODEREQUEST']._serialized_start=1585
  _globals['_DELETEEPISODEREQUEST']._serialized_end=1627
  _globals['_DELETEEPISODEMETADATA']._serialized_start=1629
  _globals['_DELETEEPISODEMETADATA']._serialized_end=1672
  _globals['_PERFORMEPISODEACTIONREQUEST']._serialized_start=1675
  _globals['_PERFORMEPISODEACTIONREQUEST']._serialized_end=1884
  _globals['_PUBLISHEPISODEACTION']._serialized_start=1886
  _globals['_PUBLISHEPISODEACTION']._serialized_end=1908
  _globals['_UNPUBLISHEPISODEACTION']._serialized_start=1910
  _globals['_UNPUBLISHEPISODEACTION']._serialized_end=1934
  _globals['_PERFORMEPISODEACTIONMETADATA']._serialized_start=1936
  _globals['_PERFORMEPISODEACTIONMETADATA']._serialized_end=1986
  _globals['_GETEPISODEPLAYERURLREQUEST']._serialized_start=1988
  _globals['_GETEPISODEPLAYERURLREQUEST']._serialized_end=2096
  _globals['_EPISODEPLAYERPARAMS']._serialized_start=2098
  _globals['_EPISODEPLAYERPARAMS']._serialized_end=2167
  _globals['_GETEPISODEPLAYERURLRESPONSE']._serialized_start=2169
  _globals['_GETEPISODEPLAYERURLRESPONSE']._serialized_end=2232
  _globals['_EPISODESERVICE']._serialized_start=2235
  _globals['_EPISODESERVICE']._serialized_end=3103
# @@protoc_insertion_point(module_scope)
