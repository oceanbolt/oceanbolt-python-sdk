# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ptypes/aispb/v1/ais.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19ptypes/aispb/v1/ais.proto\x12\x1doceanbolt.com.ptypes.aispb.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x91\x04\n\x13\x41isPositionExtended\x12\x10\n\x03lon\x18\x02 \x01(\x01R\x03lon\x12\x10\n\x03lat\x18\x01 \x01(\x01R\x03lat\x12\x38\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12\x32\n\x05speed\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x05speed\x12L\n\x13navigational_status\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x12navigationalStatus\x12 \n\x0b\x64\x65stination\x18\x06 \x01(\tR\x0b\x64\x65stination\x12,\n\x03\x65ta\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65ta\x12\x36\n\x07\x64raught\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x07\x64raught\x12\x34\n\x06\x63ourse\x18\t \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x06\x63ourse\x12\x36\n\x07heading\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x07heading\x12\x10\n\x03imo\x18\n \x01(\x05R\x03imo\x12\x12\n\x04mmsi\x18\x0b \x01(\x05R\x04mmsi\"\x89\x04\n\x0b\x41isPosition\x12\x10\n\x03lon\x18\x02 \x01(\x01R\x03lon\x12\x10\n\x03lat\x18\x01 \x01(\x01R\x03lat\x12\x38\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12\x32\n\x05speed\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x05speed\x12L\n\x13navigational_status\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x12navigationalStatus\x12 \n\x0b\x64\x65stination\x18\x06 \x01(\tR\x0b\x64\x65stination\x12,\n\x03\x65ta\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65ta\x12\x36\n\x07\x64raught\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x07\x64raught\x12\x34\n\x06\x63ourse\x18\t \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x06\x63ourse\x12\x36\n\x07heading\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x07heading\x12\x10\n\x03imo\x18\n \x01(\x05R\x03imo\x12\x12\n\x04mmsi\x18\x0b \x01(\x05R\x04mmsiBLZJgitlab.com/veson/oceanbolt/gen-proto-go/gen/services/ptypes/aispb/v1;aispbb\x06proto3')



_AISPOSITIONEXTENDED = DESCRIPTOR.message_types_by_name['AisPositionExtended']
_AISPOSITION = DESCRIPTOR.message_types_by_name['AisPosition']
AisPositionExtended = _reflection.GeneratedProtocolMessageType('AisPositionExtended', (_message.Message,), {
  'DESCRIPTOR' : _AISPOSITIONEXTENDED,
  '__module__' : 'ptypes.aispb.v1.ais_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.aispb.v1.AisPositionExtended)
  })
_sym_db.RegisterMessage(AisPositionExtended)

AisPosition = _reflection.GeneratedProtocolMessageType('AisPosition', (_message.Message,), {
  'DESCRIPTOR' : _AISPOSITION,
  '__module__' : 'ptypes.aispb.v1.ais_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.aispb.v1.AisPosition)
  })
_sym_db.RegisterMessage(AisPosition)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgitlab.com/veson/oceanbolt/gen-proto-go/gen/services/ptypes/aispb/v1;aispb'
  _AISPOSITIONEXTENDED._serialized_start=126
  _AISPOSITIONEXTENDED._serialized_end=655
  _AISPOSITION._serialized_start=658
  _AISPOSITION._serialized_end=1179
# @@protoc_insertion_point(module_scope)
