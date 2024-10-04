# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/compute/v1/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dnebius/compute/v1/image.proto\x12\x11nebius.compute.v1\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/annotations.proto\"\x99\x01\n\x05Image\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12*\n\x04spec\x18\x02 \x01(\x0b\x32\x1c.nebius.compute.v1.ImageSpec\x12.\n\x06status\x18\x03 \x01(\x0b\x32\x1e.nebius.compute.v1.ImageStatus\"n\n\tImageSpec\x12\x1e\n\x0b\x64\x65scription\x18\x01 \x01(\tB\x04\xbaJ\x01\x02H\x00\x88\x01\x01\x12\x1a\n\x0cimage_family\x18\x02 \x01(\tB\x04\xbaJ\x01\x02\x12\x15\n\x07version\x18\x03 \x01(\tB\x04\xbaJ\x01\x02\x42\x0e\n\x0c_description\"\x85\x02\n\x0bImageStatus\x12\x33\n\x05state\x18\x01 \x01(\x0e\x32$.nebius.compute.v1.ImageStatus.State\x12\x19\n\x11state_description\x18\x02 \x01(\t\x12\x1a\n\x12storage_size_bytes\x18\x03 \x01(\x03\x12\x1b\n\x13min_disk_size_bytes\x18\x04 \x01(\x03\x12\x13\n\x0breconciling\x18\x05 \x01(\x08\"X\n\x05State\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x42Y\n\x18\x61i.nebius.pub.compute.v1B\nImageProtoP\x01Z/github.com/nebius/gosdk/proto/nebius/compute/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.compute.v1.image_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030ai.nebius.pub.compute.v1B\nImageProtoP\001Z/github.com/nebius/gosdk/proto/nebius/compute/v1'
  _IMAGESPEC.fields_by_name['description']._options = None
  _IMAGESPEC.fields_by_name['description']._serialized_options = b'\272J\001\002'
  _IMAGESPEC.fields_by_name['image_family']._options = None
  _IMAGESPEC.fields_by_name['image_family']._serialized_options = b'\272J\001\002'
  _IMAGESPEC.fields_by_name['version']._options = None
  _IMAGESPEC.fields_by_name['version']._serialized_options = b'\272J\001\002'
  _globals['_IMAGE']._serialized_start=112
  _globals['_IMAGE']._serialized_end=265
  _globals['_IMAGESPEC']._serialized_start=267
  _globals['_IMAGESPEC']._serialized_end=377
  _globals['_IMAGESTATUS']._serialized_start=380
  _globals['_IMAGESTATUS']._serialized_end=641
  _globals['_IMAGESTATUS_STATE']._serialized_start=553
  _globals['_IMAGESTATUS_STATE']._serialized_end=641
# @@protoc_insertion_point(module_scope)
