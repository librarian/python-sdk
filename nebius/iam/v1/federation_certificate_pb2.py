# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/federation_certificate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*nebius/iam/v1/federation_certificate.proto\x12\rnebius.iam.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/annotations.proto\"\xdd\x01\n\x15\x46\x65\x64\x65rationCertificate\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadataB\x06\xbaH\x03\xc8\x01\x01\x12>\n\x04spec\x18\x02 \x01(\x0b\x32(.nebius.iam.v1.FederationCertificateSpecB\x06\xbaH\x03\xc8\x01\x01\x12@\n\x06status\x18\x03 \x01(\x0b\x32*.nebius.iam.v1.FederationCertificateStatusB\x04\xbaJ\x01\x05:\x04\xbaJ\x01\x02\"D\n\x19\x46\x65\x64\x65rationCertificateSpec\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\tB\x04\xbaJ\x01\x02\"\x9b\x02\n\x1b\x46\x65\x64\x65rationCertificateStatus\x12?\n\x05state\x18\x01 \x01(\x0e\x32\x30.nebius.iam.v1.FederationCertificateStatus.State\x12\x11\n\talgorithm\x18\x03 \x01(\t\x12\x10\n\x08key_size\x18\x04 \x01(\x03\x12.\n\nnot_before\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tnot_after\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"7\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0b\n\x07\x45XPIRED\x10\x02\x42\x61\n\x14\x61i.nebius.pub.iam.v1B\x1a\x46\x65\x64\x65rationCertificateProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.federation_certificate_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\032FederationCertificateProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _FEDERATIONCERTIFICATE.fields_by_name['metadata']._options = None
  _FEDERATIONCERTIFICATE.fields_by_name['metadata']._serialized_options = b'\272H\003\310\001\001'
  _FEDERATIONCERTIFICATE.fields_by_name['spec']._options = None
  _FEDERATIONCERTIFICATE.fields_by_name['spec']._serialized_options = b'\272H\003\310\001\001'
  _FEDERATIONCERTIFICATE.fields_by_name['status']._options = None
  _FEDERATIONCERTIFICATE.fields_by_name['status']._serialized_options = b'\272J\001\005'
  _FEDERATIONCERTIFICATE._options = None
  _FEDERATIONCERTIFICATE._serialized_options = b'\272J\001\002'
  _FEDERATIONCERTIFICATESPEC.fields_by_name['data']._options = None
  _FEDERATIONCERTIFICATESPEC.fields_by_name['data']._serialized_options = b'\272J\001\002'
  _globals['_FEDERATIONCERTIFICATE']._serialized_start=183
  _globals['_FEDERATIONCERTIFICATE']._serialized_end=404
  _globals['_FEDERATIONCERTIFICATESPEC']._serialized_start=406
  _globals['_FEDERATIONCERTIFICATESPEC']._serialized_end=474
  _globals['_FEDERATIONCERTIFICATESTATUS']._serialized_start=477
  _globals['_FEDERATIONCERTIFICATESTATUS']._serialized_end=760
  _globals['_FEDERATIONCERTIFICATESTATUS_STATE']._serialized_start=705
  _globals['_FEDERATIONCERTIFICATESTATUS_STATE']._serialized_end=760
# @@protoc_insertion_point(module_scope)