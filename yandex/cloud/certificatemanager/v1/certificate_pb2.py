# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/certificatemanager/v1/certificate.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/certificatemanager/v1/certificate.proto',
  package='yandex.cloud.certificatemanager.v1',
  syntax='proto3',
  serialized_options=b'\n&yandex.cloud.api.certificatemanager.v1ZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/certificatemanager/v1;certificatemanager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4yandex/cloud/certificatemanager/v1/certificate.proto\x12\"yandex.cloud.certificatemanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfa\x06\n\x0b\x43\x65rtificate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12K\n\x06labels\x18\x06 \x03(\x0b\x32;.yandex.cloud.certificatemanager.v1.Certificate.LabelsEntry\x12\x41\n\x04type\x18\x07 \x01(\x0e\x32\x33.yandex.cloud.certificatemanager.v1.CertificateType\x12\x0f\n\x07\x64omains\x18\x08 \x03(\t\x12\x46\n\x06status\x18\t \x01(\x0e\x32\x36.yandex.cloud.certificatemanager.v1.Certificate.Status\x12\x0e\n\x06issuer\x18\n \x01(\t\x12\x0f\n\x07subject\x18\x0b \x01(\t\x12\x0e\n\x06serial\x18\x0c \x01(\t\x12.\n\nupdated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tissued_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tnot_after\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nnot_before\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\nchallenges\x18\x11 \x03(\x0b\x32-.yandex.cloud.certificatemanager.v1.Challenge\x12\x1b\n\x13\x64\x65letion_protection\x18\x12 \x01(\x08\x12\x18\n\x10incomplete_chain\x18\x13 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"x\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0e\n\nVALIDATING\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\n\n\x06ISSUED\x10\x03\x12\x0b\n\x07REVOKED\x10\x04\x12\x0c\n\x08RENEWING\x10\x05\x12\x12\n\x0eRENEWAL_FAILED\x10\x06\"\x8c\x05\n\tChallenge\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.yandex.cloud.certificatemanager.v1.ChallengeType\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x44\n\x06status\x18\x05 \x01(\x0e\x32\x34.yandex.cloud.certificatemanager.v1.Challenge.Status\x12\x0f\n\x07message\x18\x06 \x01(\t\x12\r\n\x05\x65rror\x18\x07 \x01(\t\x12P\n\rdns_challenge\x18\x08 \x01(\x0b\x32\x37.yandex.cloud.certificatemanager.v1.Challenge.DnsRecordH\x00\x12P\n\x0ehttp_challenge\x18\t \x01(\x0b\x32\x36.yandex.cloud.certificatemanager.v1.Challenge.HttpFileH\x00\x1a\x36\n\tDnsRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x1a(\n\x08HttpFile\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"U\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\t\n\x05VALID\x10\x03\x12\x0b\n\x07INVALID\x10\x04\x42\x0b\n\tchallenge\"]\n\x07Version\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0e\x63\x65rtificate_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*N\n\x0f\x43\x65rtificateType\x12 \n\x1c\x43\x45RTIFICATE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08IMPORTED\x10\x01\x12\x0b\n\x07MANAGED\x10\x02*B\n\rChallengeType\x12\x1e\n\x1a\x43HALLENGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03\x44NS\x10\x01\x12\x08\n\x04HTTP\x10\x02\x42\x83\x01\n&yandex.cloud.api.certificatemanager.v1ZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/certificatemanager/v1;certificatemanagerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_CERTIFICATETYPE = _descriptor.EnumDescriptor(
  name='CertificateType',
  full_name='yandex.cloud.certificatemanager.v1.CertificateType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CERTIFICATE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IMPORTED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MANAGED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1768,
  serialized_end=1846,
)
_sym_db.RegisterEnumDescriptor(_CERTIFICATETYPE)

CertificateType = enum_type_wrapper.EnumTypeWrapper(_CERTIFICATETYPE)
_CHALLENGETYPE = _descriptor.EnumDescriptor(
  name='ChallengeType',
  full_name='yandex.cloud.certificatemanager.v1.ChallengeType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DNS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1848,
  serialized_end=1914,
)
_sym_db.RegisterEnumDescriptor(_CHALLENGETYPE)

ChallengeType = enum_type_wrapper.EnumTypeWrapper(_CHALLENGETYPE)
CERTIFICATE_TYPE_UNSPECIFIED = 0
IMPORTED = 1
MANAGED = 2
CHALLENGE_TYPE_UNSPECIFIED = 0
DNS = 1
HTTP = 2


_CERTIFICATE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.certificatemanager.v1.Certificate.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALIDATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ISSUED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REVOKED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RENEWING', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RENEWAL_FAILED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=896,
  serialized_end=1016,
)
_sym_db.RegisterEnumDescriptor(_CERTIFICATE_STATUS)

_CHALLENGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.certificatemanager.v1.Challenge.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALID', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1573,
  serialized_end=1658,
)
_sym_db.RegisterEnumDescriptor(_CHALLENGE_STATUS)


_CERTIFICATE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.certificatemanager.v1.Certificate.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.certificatemanager.v1.Certificate.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.certificatemanager.v1.Certificate.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=849,
  serialized_end=894,
)

_CERTIFICATE = _descriptor.Descriptor(
  name='Certificate',
  full_name='yandex.cloud.certificatemanager.v1.Certificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.certificatemanager.v1.Certificate.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.certificatemanager.v1.Certificate.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.certificatemanager.v1.Certificate.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.certificatemanager.v1.Certificate.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.certificatemanager.v1.Certificate.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.certificatemanager.v1.Certificate.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.certificatemanager.v1.Certificate.type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domains', full_name='yandex.cloud.certificatemanager.v1.Certificate.domains', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.certificatemanager.v1.Certificate.status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issuer', full_name='yandex.cloud.certificatemanager.v1.Certificate.issuer', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='yandex.cloud.certificatemanager.v1.Certificate.subject', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial', full_name='yandex.cloud.certificatemanager.v1.Certificate.serial', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='yandex.cloud.certificatemanager.v1.Certificate.updated_at', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issued_at', full_name='yandex.cloud.certificatemanager.v1.Certificate.issued_at', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='not_after', full_name='yandex.cloud.certificatemanager.v1.Certificate.not_after', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='not_before', full_name='yandex.cloud.certificatemanager.v1.Certificate.not_before', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='challenges', full_name='yandex.cloud.certificatemanager.v1.Certificate.challenges', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deletion_protection', full_name='yandex.cloud.certificatemanager.v1.Certificate.deletion_protection', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='incomplete_chain', full_name='yandex.cloud.certificatemanager.v1.Certificate.incomplete_chain', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CERTIFICATE_LABELSENTRY, ],
  enum_types=[
    _CERTIFICATE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=1016,
)


_CHALLENGE_DNSRECORD = _descriptor.Descriptor(
  name='DnsRecord',
  full_name='yandex.cloud.certificatemanager.v1.Challenge.DnsRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.certificatemanager.v1.Challenge.DnsRecord.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.certificatemanager.v1.Challenge.DnsRecord.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.certificatemanager.v1.Challenge.DnsRecord.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1475,
  serialized_end=1529,
)

_CHALLENGE_HTTPFILE = _descriptor.Descriptor(
  name='HttpFile',
  full_name='yandex.cloud.certificatemanager.v1.Challenge.HttpFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='yandex.cloud.certificatemanager.v1.Challenge.HttpFile.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='yandex.cloud.certificatemanager.v1.Challenge.HttpFile.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1531,
  serialized_end=1571,
)

_CHALLENGE = _descriptor.Descriptor(
  name='Challenge',
  full_name='yandex.cloud.certificatemanager.v1.Challenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='yandex.cloud.certificatemanager.v1.Challenge.domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.certificatemanager.v1.Challenge.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.certificatemanager.v1.Challenge.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='yandex.cloud.certificatemanager.v1.Challenge.updated_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.certificatemanager.v1.Challenge.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='yandex.cloud.certificatemanager.v1.Challenge.message', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='yandex.cloud.certificatemanager.v1.Challenge.error', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dns_challenge', full_name='yandex.cloud.certificatemanager.v1.Challenge.dns_challenge', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='http_challenge', full_name='yandex.cloud.certificatemanager.v1.Challenge.http_challenge', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CHALLENGE_DNSRECORD, _CHALLENGE_HTTPFILE, ],
  enum_types=[
    _CHALLENGE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='challenge', full_name='yandex.cloud.certificatemanager.v1.Challenge.challenge',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1019,
  serialized_end=1671,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='yandex.cloud.certificatemanager.v1.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.certificatemanager.v1.Version.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='certificate_id', full_name='yandex.cloud.certificatemanager.v1.Version.certificate_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.certificatemanager.v1.Version.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1673,
  serialized_end=1766,
)

_CERTIFICATE_LABELSENTRY.containing_type = _CERTIFICATE
_CERTIFICATE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CERTIFICATE.fields_by_name['labels'].message_type = _CERTIFICATE_LABELSENTRY
_CERTIFICATE.fields_by_name['type'].enum_type = _CERTIFICATETYPE
_CERTIFICATE.fields_by_name['status'].enum_type = _CERTIFICATE_STATUS
_CERTIFICATE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CERTIFICATE.fields_by_name['issued_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CERTIFICATE.fields_by_name['not_after'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CERTIFICATE.fields_by_name['not_before'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CERTIFICATE.fields_by_name['challenges'].message_type = _CHALLENGE
_CERTIFICATE_STATUS.containing_type = _CERTIFICATE
_CHALLENGE_DNSRECORD.containing_type = _CHALLENGE
_CHALLENGE_HTTPFILE.containing_type = _CHALLENGE
_CHALLENGE.fields_by_name['type'].enum_type = _CHALLENGETYPE
_CHALLENGE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHALLENGE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHALLENGE.fields_by_name['status'].enum_type = _CHALLENGE_STATUS
_CHALLENGE.fields_by_name['dns_challenge'].message_type = _CHALLENGE_DNSRECORD
_CHALLENGE.fields_by_name['http_challenge'].message_type = _CHALLENGE_HTTPFILE
_CHALLENGE_STATUS.containing_type = _CHALLENGE
_CHALLENGE.oneofs_by_name['challenge'].fields.append(
  _CHALLENGE.fields_by_name['dns_challenge'])
_CHALLENGE.fields_by_name['dns_challenge'].containing_oneof = _CHALLENGE.oneofs_by_name['challenge']
_CHALLENGE.oneofs_by_name['challenge'].fields.append(
  _CHALLENGE.fields_by_name['http_challenge'])
_CHALLENGE.fields_by_name['http_challenge'].containing_oneof = _CHALLENGE.oneofs_by_name['challenge']
_VERSION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Certificate'] = _CERTIFICATE
DESCRIPTOR.message_types_by_name['Challenge'] = _CHALLENGE
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.enum_types_by_name['CertificateType'] = _CERTIFICATETYPE
DESCRIPTOR.enum_types_by_name['ChallengeType'] = _CHALLENGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CERTIFICATE_LABELSENTRY,
    '__module__' : 'yandex.cloud.certificatemanager.v1.certificate_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.certificatemanager.v1.Certificate.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CERTIFICATE,
  '__module__' : 'yandex.cloud.certificatemanager.v1.certificate_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.certificatemanager.v1.Certificate)
  })
_sym_db.RegisterMessage(Certificate)
_sym_db.RegisterMessage(Certificate.LabelsEntry)

Challenge = _reflection.GeneratedProtocolMessageType('Challenge', (_message.Message,), {

  'DnsRecord' : _reflection.GeneratedProtocolMessageType('DnsRecord', (_message.Message,), {
    'DESCRIPTOR' : _CHALLENGE_DNSRECORD,
    '__module__' : 'yandex.cloud.certificatemanager.v1.certificate_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.certificatemanager.v1.Challenge.DnsRecord)
    })
  ,

  'HttpFile' : _reflection.GeneratedProtocolMessageType('HttpFile', (_message.Message,), {
    'DESCRIPTOR' : _CHALLENGE_HTTPFILE,
    '__module__' : 'yandex.cloud.certificatemanager.v1.certificate_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.certificatemanager.v1.Challenge.HttpFile)
    })
  ,
  'DESCRIPTOR' : _CHALLENGE,
  '__module__' : 'yandex.cloud.certificatemanager.v1.certificate_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.certificatemanager.v1.Challenge)
  })
_sym_db.RegisterMessage(Challenge)
_sym_db.RegisterMessage(Challenge.DnsRecord)
_sym_db.RegisterMessage(Challenge.HttpFile)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'yandex.cloud.certificatemanager.v1.certificate_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.certificatemanager.v1.Version)
  })
_sym_db.RegisterMessage(Version)


DESCRIPTOR._options = None
_CERTIFICATE_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
