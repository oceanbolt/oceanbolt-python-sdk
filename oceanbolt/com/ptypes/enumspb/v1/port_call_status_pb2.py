# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ptypes/enumspb/v1/port_call_status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ptypes/enumspb/v1/port_call_status.proto\x12\x1foceanbolt.com.ptypes.enumspb.v1*w\n\rPolygonStatus\x12\x1c\n\x18UNDEFINED_POLYGON_STATUS\x10\x00\x12\x0b\n\x07IN_PORT\x10\x01\x12\x10\n\x0cIN_ANCHORAGE\x10\x02\x12\x0c\n\x08IN_BERTH\x10\x03\x12\x0f\n\x0bIN_SHIPYARD\x10\x04\x12\n\n\x06\x41T_SEA\x10\x05\x42GZEgitlab.com/veson/oceanbolt/gen-proto-go/gen/ptypes/enumspb/v1;enumspbb\x06proto3')

_POLYGONSTATUS = DESCRIPTOR.enum_types_by_name['PolygonStatus']
PolygonStatus = enum_type_wrapper.EnumTypeWrapper(_POLYGONSTATUS)
UNDEFINED_POLYGON_STATUS = 0
IN_PORT = 1
IN_ANCHORAGE = 2
IN_BERTH = 3
IN_SHIPYARD = 4
AT_SEA = 5


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZEgitlab.com/veson/oceanbolt/gen-proto-go/gen/ptypes/enumspb/v1;enumspb'
  _POLYGONSTATUS._serialized_start=77
  _POLYGONSTATUS._serialized_end=196
# @@protoc_insertion_point(module_scope)
