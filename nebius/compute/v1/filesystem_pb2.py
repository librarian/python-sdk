# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/compute/v1/filesystem.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"nebius/compute/v1/filesystem.proto\x12\x11nebius.compute.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/annotations.proto\"\xa8\x01\n\nFilesystem\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12/\n\x04spec\x18\x02 \x01(\x0b\x32!.nebius.compute.v1.FilesystemSpec\x12\x33\n\x06status\x18\x03 \x01(\x0b\x32#.nebius.compute.v1.FilesystemStatus\"\xcc\x02\n\x0e\x46ilesystemSpec\x12\x1a\n\nsize_bytes\x18\x01 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x0esize_kibibytes\x18\x02 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x0esize_mebibytes\x18\x03 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x0esize_gibibytes\x18\x04 \x01(\x03\x42\x04\xbaJ\x01\x02H\x00\x12\x1e\n\x10\x62lock_size_bytes\x18\x05 \x01(\x03\x42\x04\xbaJ\x01\x02\x12J\n\x04type\x18\x06 \x01(\x0e\x32\x30.nebius.compute.v1.FilesystemSpec.FilesystemTypeB\n\xbaH\x03\xc8\x01\x01\xbaJ\x01\x02\"C\n\x0e\x46ilesystemType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0f\n\x0bNETWORK_SSD\x10\x01\x12\x0f\n\x0bNETWORK_HDD\x10\x02\x42\r\n\x04size\x12\x05\xbaH\x02\x08\x01\"\xa9\x02\n\x10\x46ilesystemStatus\x12\x38\n\x05state\x18\x01 \x01(\x0e\x32).nebius.compute.v1.FilesystemStatus.State\x12\x19\n\x11state_description\x18\x02 \x01(\t\x12\x1e\n\x16read_write_attachments\x18\x03 \x03(\t\x12\x1d\n\x15read_only_attachments\x18\x04 \x03(\t\x12\x12\n\nsize_bytes\x18\x05 \x01(\x03\x12\x13\n\x0breconciling\x18\x06 \x01(\x08\"X\n\x05State\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x42^\n\x18\x61i.nebius.pub.compute.v1B\x0f\x46ilesystemProtoP\x01Z/github.com/nebius/gosdk/proto/nebius/compute/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.compute.v1.filesystem_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030ai.nebius.pub.compute.v1B\017FilesystemProtoP\001Z/github.com/nebius/gosdk/proto/nebius/compute/v1'
  _FILESYSTEMSPEC.oneofs_by_name['size']._options = None
  _FILESYSTEMSPEC.oneofs_by_name['size']._serialized_options = b'\272H\002\010\001'
  _FILESYSTEMSPEC.fields_by_name['size_bytes']._options = None
  _FILESYSTEMSPEC.fields_by_name['size_bytes']._serialized_options = b'\272J\001\002'
  _FILESYSTEMSPEC.fields_by_name['size_kibibytes']._options = None
  _FILESYSTEMSPEC.fields_by_name['size_kibibytes']._serialized_options = b'\272J\001\002'
  _FILESYSTEMSPEC.fields_by_name['size_mebibytes']._options = None
  _FILESYSTEMSPEC.fields_by_name['size_mebibytes']._serialized_options = b'\272J\001\002'
  _FILESYSTEMSPEC.fields_by_name['size_gibibytes']._options = None
  _FILESYSTEMSPEC.fields_by_name['size_gibibytes']._serialized_options = b'\272J\001\002'
  _FILESYSTEMSPEC.fields_by_name['block_size_bytes']._options = None
  _FILESYSTEMSPEC.fields_by_name['block_size_bytes']._serialized_options = b'\272J\001\002'
  _FILESYSTEMSPEC.fields_by_name['type']._options = None
  _FILESYSTEMSPEC.fields_by_name['type']._serialized_options = b'\272H\003\310\001\001\272J\001\002'
  _globals['_FILESYSTEM']._serialized_start=146
  _globals['_FILESYSTEM']._serialized_end=314
  _globals['_FILESYSTEMSPEC']._serialized_start=317
  _globals['_FILESYSTEMSPEC']._serialized_end=649
  _globals['_FILESYSTEMSPEC_FILESYSTEMTYPE']._serialized_start=567
  _globals['_FILESYSTEMSPEC_FILESYSTEMTYPE']._serialized_end=634
  _globals['_FILESYSTEMSTATUS']._serialized_start=652
  _globals['_FILESYSTEMSTATUS']._serialized_end=949
  _globals['_FILESYSTEMSTATUS_STATE']._serialized_start=861
  _globals['_FILESYSTEMSTATUS_STATE']._serialized_end=949
# @@protoc_insertion_point(module_scope)
