# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/compute/v1/disk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cnebius/compute/v1/disk.proto\x12\x11nebius.compute.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/annotations.proto\"\x96\x01\n\x04\x44isk\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12)\n\x04spec\x18\x02 \x01(\x0b\x32\x1b.nebius.compute.v1.DiskSpec\x12-\n\x06status\x18\x03 \x01(\x0b\x32\x1d.nebius.compute.v1.DiskStatus\"\xaf\x04\n\x08\x44iskSpec\x12\x1a\n\nsize_bytes\x18\x01 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x0esize_kibibytes\x18\x02 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x0esize_mebibytes\x18\x03 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x0esize_gibibytes\x18\x04 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x10\x62lock_size_bytes\x18\x05 \x01(\x03\x42\x04\xbaJ\x01\x02\x12>\n\x04type\x18\x06 \x01(\x0e\x32$.nebius.compute.v1.DiskSpec.DiskTypeB\n\xbaH\x03\xc8\x01\x01\xbaJ\x01\x02\x12\x46\n\x10placement_policy\x18\x07 \x01(\x0b\x32&.nebius.compute.v1.DiskPlacementPolicyB\x04\xbaJ\x01\x02\x12\x1f\n\x0fsource_image_id\x18\x08 \x01(\tB\x04\xbaJ\x01\x02H\x01\x12I\n\x13source_image_family\x18\n \x01(\x0b\x32$.nebius.compute.v1.SourceImageFamilyB\x04\xbaJ\x01\x02H\x01\"t\n\x08\x44iskType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0f\n\x0bNETWORK_SSD\x10\x01\x12\x0f\n\x0bNETWORK_HDD\x10\x02\x12\x1e\n\x1aNETWORK_SSD_NON_REPLICATED\x10\x03\x12\x15\n\x11NETWORK_SSD_IO_M3\x10\x04\x42\r\n\x04size\x12\x05\xbaH\x02\x08\x01\x42\x08\n\x06sourceJ\x04\x08\t\x10\n\"D\n\x11SourceImageFamily\x12\x1c\n\x0cimage_family\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x11\n\tparent_id\x18\x02 \x01(\t\"T\n\x13\x44iskPlacementPolicy\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\x12!\n\x19placement_group_partition\x18\x02 \x01(\x03\"\xb5\x02\n\nDiskStatus\x12\x32\n\x05state\x18\x01 \x01(\x0e\x32#.nebius.compute.v1.DiskStatus.State\x12\x19\n\x11state_description\x18\x02 \x01(\t\x12\x1d\n\x15read_write_attachment\x18\x03 \x01(\t\x12\x1d\n\x15read_only_attachments\x18\x04 \x03(\t\x12\x17\n\x0fsource_image_id\x18\x05 \x01(\t\x12\x12\n\nsize_bytes\x18\x06 \x01(\x03\x12\x13\n\x0breconciling\x18\x07 \x01(\x08\"X\n\x05State\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x42X\n\x18\x61i.nebius.pub.compute.v1B\tDiskProtoP\x01Z/github.com/nebius/gosdk/proto/nebius/compute/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.compute.v1.disk_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030ai.nebius.pub.compute.v1B\tDiskProtoP\001Z/github.com/nebius/gosdk/proto/nebius/compute/v1'
  _DISKSPEC.oneofs_by_name['size']._options = None
  _DISKSPEC.oneofs_by_name['size']._serialized_options = b'\272H\002\010\001'
  _DISKSPEC.fields_by_name['size_bytes']._options = None
  _DISKSPEC.fields_by_name['size_bytes']._serialized_options = b'\272J\001\002'
  _DISKSPEC.fields_by_name['size_kibibytes']._options = None
  _DISKSPEC.fields_by_name['size_kibibytes']._serialized_options = b'\272J\001\002'
  _DISKSPEC.fields_by_name['size_mebibytes']._options = None
  _DISKSPEC.fields_by_name['size_mebibytes']._serialized_options = b'\272J\001\002'
  _DISKSPEC.fields_by_name['size_gibibytes']._options = None
  _DISKSPEC.fields_by_name['size_gibibytes']._serialized_options = b'\272J\001\002'
  _DISKSPEC.fields_by_name['block_size_bytes']._options = None
  _DISKSPEC.fields_by_name['block_size_bytes']._serialized_options = b'\272J\001\002'
  _DISKSPEC.fields_by_name['type']._options = None
  _DISKSPEC.fields_by_name['type']._serialized_options = b'\272H\003\310\001\001\272J\001\002'
  _DISKSPEC.fields_by_name['placement_policy']._options = None
  _DISKSPEC.fields_by_name['placement_policy']._serialized_options = b'\272J\001\002'
  _DISKSPEC.fields_by_name['source_image_id']._options = None
  _DISKSPEC.fields_by_name['source_image_id']._serialized_options = b'\272J\001\002'
  _DISKSPEC.fields_by_name['source_image_family']._options = None
  _DISKSPEC.fields_by_name['source_image_family']._serialized_options = b'\272J\001\002'
  _SOURCEIMAGEFAMILY.fields_by_name['image_family']._options = None
  _SOURCEIMAGEFAMILY.fields_by_name['image_family']._serialized_options = b'\272H\003\310\001\001'
  _globals['_DISK']._serialized_start=140
  _globals['_DISK']._serialized_end=290
  _globals['_DISKSPEC']._serialized_start=293
  _globals['_DISKSPEC']._serialized_end=852
  _globals['_DISKSPEC_DISKTYPE']._serialized_start=705
  _globals['_DISKSPEC_DISKTYPE']._serialized_end=821
  _globals['_SOURCEIMAGEFAMILY']._serialized_start=854
  _globals['_SOURCEIMAGEFAMILY']._serialized_end=922
  _globals['_DISKPLACEMENTPOLICY']._serialized_start=924
  _globals['_DISKPLACEMENTPOLICY']._serialized_end=1008
  _globals['_DISKSTATUS']._serialized_start=1011
  _globals['_DISKSTATUS']._serialized_end=1320
  _globals['_DISKSTATUS_STATE']._serialized_start=1232
  _globals['_DISKSTATUS_STATE']._serialized_end=1320
# @@protoc_insertion_point(module_scope)
