# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/speechsense/v1/talk_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.speechsense.v1 import audio_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_audio__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/speechsense/v1/talk_service.proto\x12\x1byandex.cloud.speechsense.v1\x1a\'yandex/cloud/speechsense/v1/audio.proto\"\xa0\x01\n\x11StreamTalkRequest\x12=\n\x08metadata\x18\x01 \x01(\x0b\x32).yandex.cloud.speechsense.v1.TalkMetadataH\x00\x12\x43\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.speechsense.v1.AudioStreamingRequestH\x00\x42\x07\n\x05\x45vent\"\x8a\x01\n\x11UploadTalkRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32).yandex.cloud.speechsense.v1.TalkMetadata\x12\x38\n\x05\x61udio\x18\x02 \x01(\x0b\x32).yandex.cloud.speechsense.v1.AudioRequest\"\x9b\x01\n\x0cTalkMetadata\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x45\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x35.yandex.cloud.speechsense.v1.TalkMetadata.FieldsEntry\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x12UploadTalkResponse\x12\x0f\n\x07talk_id\x18\x01 \x01(\t2\xed\x01\n\x0bTalkService\x12s\n\x0eUploadAsStream\x12..yandex.cloud.speechsense.v1.StreamTalkRequest\x1a/.yandex.cloud.speechsense.v1.UploadTalkResponse(\x01\x12i\n\x06Upload\x12..yandex.cloud.speechsense.v1.UploadTalkRequest\x1a/.yandex.cloud.speechsense.v1.UploadTalkResponseBy\n\x1fyandex.cloud.api.speechsense.v1B\tTalkProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsenseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.speechsense.v1.talk_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037yandex.cloud.api.speechsense.v1B\tTalkProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsense'
  _TALKMETADATA_FIELDSENTRY._options = None
  _TALKMETADATA_FIELDSENTRY._serialized_options = b'8\001'
  _globals['_STREAMTALKREQUEST']._serialized_start=121
  _globals['_STREAMTALKREQUEST']._serialized_end=281
  _globals['_UPLOADTALKREQUEST']._serialized_start=284
  _globals['_UPLOADTALKREQUEST']._serialized_end=422
  _globals['_TALKMETADATA']._serialized_start=425
  _globals['_TALKMETADATA']._serialized_end=580
  _globals['_TALKMETADATA_FIELDSENTRY']._serialized_start=535
  _globals['_TALKMETADATA_FIELDSENTRY']._serialized_end=580
  _globals['_UPLOADTALKRESPONSE']._serialized_start=582
  _globals['_UPLOADTALKRESPONSE']._serialized_end=619
  _globals['_TALKSERVICE']._serialized_start=622
  _globals['_TALKSERVICE']._serialized_end=859
# @@protoc_insertion_point(module_scope)
