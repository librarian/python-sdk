# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/datatransfer/v1/endpoint/common.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x1bgoogle/protobuf/empty.proto\"-\n\x07\x41ltName\x12\x11\n\tfrom_name\x18\x01 \x01(\t\x12\x0f\n\x07to_name\x18\x02 \x01(\t\" \n\x06Secret\x12\r\n\x03raw\x18\x01 \x01(\tH\x00\x42\x07\n\x05value\"\x87\x01\n\tColSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.yandex.cloud.datatransfer.v1.endpoint.ColumnType\x12\x0b\n\x03key\x18\x03 \x01(\x08\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x0c\n\x04path\x18\x05 \x01(\t\"\x86\x01\n\x07TLSMode\x12*\n\x08\x64isabled\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x43\n\x07\x65nabled\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.datatransfer.v1.endpoint.TLSConfigH\x00\x42\n\n\x08tls_mode\"#\n\tTLSConfig\x12\x16\n\x0e\x63\x61_certificate\x18\x01 \x01(\t\".\n\x0b\x43olumnValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x42\x07\n\x05value\"\xc0\x01\n\x19\x44\x61taTransformationOptions\x12\x16\n\x0e\x63loud_function\x18\x01 \x01(\t\x12\x19\n\x11number_of_retries\x18\x02 \x01(\x03\x12\x13\n\x0b\x62uffer_size\x18\x03 \x01(\t\x12\x1d\n\x15\x62uffer_flush_interval\x18\x04 \x01(\t\x12\x1a\n\x12invocation_timeout\x18\x05 \x01(\t\x12\x1a\n\x12service_account_id\x18\x08 \x01(\tJ\x04\x08\x06\x10\x08\"S\n\tFieldList\x12@\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x30.yandex.cloud.datatransfer.v1.endpoint.ColSchemaJ\x04\x08\x01\x10\x02\"q\n\nDataSchema\x12\x15\n\x0bjson_fields\x18\x01 \x01(\tH\x00\x12\x42\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.datatransfer.v1.endpoint.FieldListH\x00\x42\x08\n\x06schema\"\x08\n\x06NoAuth*h\n\x13ObjectTransferStage\x12%\n!OBJECT_TRANSFER_STAGE_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x42\x45\x46ORE_DATA\x10\x01\x12\x0e\n\nAFTER_DATA\x10\x02\x12\t\n\x05NEVER\x10\x03*U\n\rCleanupPolicy\x12\x1e\n\x1a\x43LEANUP_POLICY_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\x08\n\x04\x44ROP\x10\x02\x12\x0c\n\x08TRUNCATE\x10\x03*\xc9\x01\n\nColumnType\x12\x1b\n\x17\x43OLUMN_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05INT32\x10\x01\x12\t\n\x05INT16\x10\x02\x12\x08\n\x04INT8\x10\x03\x12\n\n\x06UINT64\x10\x04\x12\n\n\x06UINT32\x10\x05\x12\n\n\x06UINT16\x10\x06\x12\t\n\x05UINT8\x10\x07\x12\n\n\x06\x44OUBLE\x10\x08\x12\x0b\n\x07\x42OOLEAN\x10\t\x12\n\n\x06STRING\x10\n\x12\x08\n\x04UTF8\x10\x0b\x12\x07\n\x03\x41NY\x10\x0c\x12\x0c\n\x08\x44\x41TETIME\x10\r\x12\t\n\x05INT64\x10\x0e\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.endpoint.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _globals['_OBJECTTRANSFERSTAGE']._serialized_start=968
  _globals['_OBJECTTRANSFERSTAGE']._serialized_end=1072
  _globals['_CLEANUPPOLICY']._serialized_start=1074
  _globals['_CLEANUPPOLICY']._serialized_end=1159
  _globals['_COLUMNTYPE']._serialized_start=1162
  _globals['_COLUMNTYPE']._serialized_end=1363
  _globals['_ALTNAME']._serialized_start=122
  _globals['_ALTNAME']._serialized_end=167
  _globals['_SECRET']._serialized_start=169
  _globals['_SECRET']._serialized_end=201
  _globals['_COLSCHEMA']._serialized_start=204
  _globals['_COLSCHEMA']._serialized_end=339
  _globals['_TLSMODE']._serialized_start=342
  _globals['_TLSMODE']._serialized_end=476
  _globals['_TLSCONFIG']._serialized_start=478
  _globals['_TLSCONFIG']._serialized_end=513
  _globals['_COLUMNVALUE']._serialized_start=515
  _globals['_COLUMNVALUE']._serialized_end=561
  _globals['_DATATRANSFORMATIONOPTIONS']._serialized_start=564
  _globals['_DATATRANSFORMATIONOPTIONS']._serialized_end=756
  _globals['_FIELDLIST']._serialized_start=758
  _globals['_FIELDLIST']._serialized_end=841
  _globals['_DATASCHEMA']._serialized_start=843
  _globals['_DATASCHEMA']._serialized_end=956
  _globals['_NOAUTH']._serialized_start=958
  _globals['_NOAUTH']._serialized_end=966
# @@protoc_insertion_point(module_scope)
