# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/stt/v2/stt_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/ai/stt/v2/stt_service.proto\x12\x16yandex.cloud.ai.stt.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\"\x93\x01\n\x1dLongRunningRecognitionRequest\x12\x39\n\x06\x63onfig\x18\x01 \x01(\x0b\x32).yandex.cloud.ai.stt.v2.RecognitionConfig\x12\x37\n\x05\x61udio\x18\x02 \x01(\x0b\x32(.yandex.cloud.ai.stt.v2.RecognitionAudio\"a\n\x1eLongRunningRecognitionResponse\x12?\n\x06\x63hunks\x18\x01 \x03(\x0b\x32/.yandex.cloud.ai.stt.v2.SpeechRecognitionResult\"\x88\x01\n\x1bStreamingRecognitionRequest\x12;\n\x06\x63onfig\x18\x01 \x01(\x0b\x32).yandex.cloud.ai.stt.v2.RecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streaming_request\"}\n\x1cStreamingRecognitionResponse\x12>\n\x06\x63hunks\x18\x01 \x03(\x0b\x32..yandex.cloud.ai.stt.v2.SpeechRecognitionChunkJ\x04\x08\x02\x10\x03R\x17\x65nd_of_single_utterance\"D\n\x10RecognitionAudio\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x42\x0e\n\x0c\x61udio_source\"f\n\x11RecognitionConfig\x12>\n\rspecification\x18\x01 \x01(\x0b\x32\'.yandex.cloud.ai.stt.v2.RecognitionSpec\x12\x11\n\tfolder_id\x18\x02 \x01(\t\"\x99\x03\n\x0fRecognitionSpec\x12M\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32\x35.yandex.cloud.ai.stt.v2.RecognitionSpec.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x03\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x18\n\x10profanity_filter\x18\x04 \x01(\x08\x12\r\n\x05model\x18\x05 \x01(\t\x12\x17\n\x0fpartial_results\x18\x07 \x01(\x08\x12\x18\n\x10single_utterance\x18\x08 \x01(\x08\x12\x1b\n\x13\x61udio_channel_count\x18\t \x01(\x03\x12\x13\n\x0braw_results\x18\n \x01(\x08\x12\x17\n\x0fliterature_text\x18\x0b \x01(\x08\"X\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x10\n\x0cLINEAR16_PCM\x10\x01\x12\x0c\n\x08OGG_OPUS\x10\x02\x12\x07\n\x03MP3\x10\x03J\x04\x08\x06\x10\x07\"\x8d\x01\n\x16SpeechRecognitionChunk\x12J\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.ai.stt.v2.SpeechRecognitionAlternative\x12\r\n\x05\x66inal\x18\x02 \x01(\x08\x12\x18\n\x10\x65nd_of_utterance\x18\x03 \x01(\x08\"z\n\x17SpeechRecognitionResult\x12J\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.ai.stt.v2.SpeechRecognitionAlternative\x12\x13\n\x0b\x63hannel_tag\x18\x02 \x01(\x03\"q\n\x1cSpeechRecognitionAlternative\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12/\n\x05words\x18\x03 \x03(\x0b\x32 .yandex.cloud.ai.stt.v2.WordInfo\"\x88\x01\n\x08WordInfo\x12-\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x32\xdb\x02\n\nSttService\x12\xc4\x01\n\x14LongRunningRecognize\x12\x35.yandex.cloud.ai.stt.v2.LongRunningRecognitionRequest\x1a!.yandex.cloud.operation.Operation\"R\xb2\xd2* \x12\x1eLongRunningRecognitionResponse\x82\xd3\xe4\x93\x02(\"#/speech/stt/v2/longRunningRecognize:\x01*\x12\x85\x01\n\x12StreamingRecognize\x12\x33.yandex.cloud.ai.stt.v2.StreamingRecognitionRequest\x1a\x34.yandex.cloud.ai.stt.v2.StreamingRecognitionResponse\"\x00(\x01\x30\x01\x42\\\n\x1ayandex.cloud.api.ai.stt.v2Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/stt/v2;sttb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.stt.v2.stt_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032yandex.cloud.api.ai.stt.v2Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/stt/v2;stt'
  _STTSERVICE.methods_by_name['LongRunningRecognize']._options = None
  _STTSERVICE.methods_by_name['LongRunningRecognize']._serialized_options = b'\262\322* \022\036LongRunningRecognitionResponse\202\323\344\223\002(\"#/speech/stt/v2/longRunningRecognize:\001*'
  _globals['_LONGRUNNINGRECOGNITIONREQUEST']._serialized_start=205
  _globals['_LONGRUNNINGRECOGNITIONREQUEST']._serialized_end=352
  _globals['_LONGRUNNINGRECOGNITIONRESPONSE']._serialized_start=354
  _globals['_LONGRUNNINGRECOGNITIONRESPONSE']._serialized_end=451
  _globals['_STREAMINGRECOGNITIONREQUEST']._serialized_start=454
  _globals['_STREAMINGRECOGNITIONREQUEST']._serialized_end=590
  _globals['_STREAMINGRECOGNITIONRESPONSE']._serialized_start=592
  _globals['_STREAMINGRECOGNITIONRESPONSE']._serialized_end=717
  _globals['_RECOGNITIONAUDIO']._serialized_start=719
  _globals['_RECOGNITIONAUDIO']._serialized_end=787
  _globals['_RECOGNITIONCONFIG']._serialized_start=789
  _globals['_RECOGNITIONCONFIG']._serialized_end=891
  _globals['_RECOGNITIONSPEC']._serialized_start=894
  _globals['_RECOGNITIONSPEC']._serialized_end=1303
  _globals['_RECOGNITIONSPEC_AUDIOENCODING']._serialized_start=1209
  _globals['_RECOGNITIONSPEC_AUDIOENCODING']._serialized_end=1297
  _globals['_SPEECHRECOGNITIONCHUNK']._serialized_start=1306
  _globals['_SPEECHRECOGNITIONCHUNK']._serialized_end=1447
  _globals['_SPEECHRECOGNITIONRESULT']._serialized_start=1449
  _globals['_SPEECHRECOGNITIONRESULT']._serialized_end=1571
  _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_start=1573
  _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_end=1686
  _globals['_WORDINFO']._serialized_start=1689
  _globals['_WORDINFO']._serialized_end=1825
  _globals['_STTSERVICE']._serialized_start=1828
  _globals['_STTSERVICE']._serialized_end=2175
# @@protoc_insertion_point(module_scope)
