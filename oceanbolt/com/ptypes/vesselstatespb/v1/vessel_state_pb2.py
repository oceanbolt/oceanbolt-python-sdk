# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ptypes/vesselstatespb/v1/vessel_state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+ptypes/vesselstatespb/v1/vessel_state.proto\x12&oceanbolt.com.ptypes.vesselstatespb.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x95\x03\n\x0bVesselState\x12P\n\nbase_state\x18\x01 \x01(\x0b\x32\x31.oceanbolt.com.ptypes.vesselstatespb.v1.BaseStateR\tbaseState\x12S\n\x0b\x63\x61rgo_state\x18\x02 \x01(\x0b\x32\x32.oceanbolt.com.ptypes.vesselstatespb.v1.CargoStateR\ncargoState\x12j\n\x13parsed_destinations\x18\x03 \x03(\x0b\x32\x39.oceanbolt.com.ptypes.vesselstatespb.v1.ParsedDestinationR\x12parsedDestinations\x12s\n\x16predicted_destinations\x18\x04 \x03(\x0b\x32<.oceanbolt.com.ptypes.vesselstatespb.v1.PredictedDestinationR\x15predictedDestinations\"\xa3\x08\n\tBaseState\x12L\n\x08platform\x18\x01 \x01(\x0e\x32\x30.oceanbolt.com.ptypes.vesselstatespb.v1.PlatformR\x08platform\x12\x10\n\x03imo\x18\x02 \x01(\rR\x03imo\x12\x12\n\x04mmsi\x18\x03 \x01(\rR\x04mmsi\x12\x38\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12\x38\n\x18navigational_status_code\x18\x05 \x01(\rR\x16navigationalStatusCode\x12\x17\n\x07zone_id\x18\x06 \x01(\rR\x06zoneId\x12\x17\n\x07port_id\x18\x07 \x01(\rR\x06portId\x12!\n\x0c\x61nchorage_id\x18\x08 \x01(\rR\x0b\x61nchorageId\x12\x19\n\x08\x62\x65rth_id\x18\t \x01(\rR\x07\x62\x65rthId\x12\x1f\n\x0bshipyard_id\x18\n \x01(\rR\nshipyardId\x12&\n\x0frelated_port_id\x18\x0b \x01(\rR\rrelatedPortId\x12\x1e\n\x0b\x65\x63\x61_zone_id\x18\x0c \x01(\rR\tecaZoneId\x12$\n\x0epiracy_zone_id\x18\r \x01(\rR\x0cpiracyZoneId\x12\x1e\n\x0bvip_zone_id\x18\x1a \x01(\rR\tvipZoneId\x12 \n\x0b\x64\x65stination\x18\x0e \x01(\tR\x0b\x64\x65stination\x12K\n\x13\x64\x65stination_updated\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x12\x64\x65stinationUpdated\x12,\n\x03\x65ta\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65ta\x12;\n\x0b\x65ta_updated\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\netaUpdated\x12\x1c\n\tlongitude\x18\x12 \x01(\x01R\tlongitude\x12\x1a\n\x08latitude\x18\x13 \x01(\x01R\x08latitude\x12\x16\n\x06\x63ourse\x18\x14 \x01(\x01R\x06\x63ourse\x12\x18\n\x07heading\x18\x15 \x01(\x01R\x07heading\x12\x14\n\x05speed\x18\x16 \x01(\x01R\x05speed\x12\x18\n\x07\x64raught\x18\x17 \x01(\x01R\x07\x64raught\x12\x65\n\x14laden_status_draught\x18\x18 \x01(\x0e\x32\x33.oceanbolt.com.ptypes.vesselstatespb.v1.LadenStatusR\x12ladenStatusDraught\x12\x32\n\x15hours_carried_forward\x18\x19 \x01(\rR\x13hoursCarriedForward\"\x9c\x04\n\nCargoState\x12!\n\x0c\x63ommodity_id\x18\x01 \x01(\rR\x0b\x63ommodityId\x12\x61\n\x12laden_status_model\x18\x02 \x01(\x0e\x32\x33.oceanbolt.com.ptypes.vesselstatespb.v1.LadenStatusR\x10ladenStatusModel\x12\"\n\rtrade_flow_id\x18\x03 \x01(\tR\x0btradeFlowId\x12Y\n\rvessel_status\x18\x05 \x01(\x0e\x32\x34.oceanbolt.com.ptypes.vesselstatespb.v1.VesselStatusR\x0cvesselStatus\x12/\n\x14last_visited_port_id\x18\x06 \x01(\rR\x11lastVisitedPortId\x12\'\n\x10last_ops_port_id\x18\x07 \x01(\rR\rlastOpsPortId\x12\x30\n\x15last_ops_port_call_id\x18\x08 \x01(\tR\x11lastOpsPortCallId\x12\x34\n\x17last_ops_port_region_id\x18\t \x01(\tR\x13lastOpsPortRegionId\x12&\n\x0fvolume_on_board\x18\n \x01(\x01R\rvolumeOnBoard\x12\x1f\n\x0bvolume_unit\x18\x0b \x01(\tR\nvolumeUnit\"\x8c\x01\n\x15PredictedDestinations\x12s\n\x16predicted_destinations\x18\x01 \x03(\x0b\x32<.oceanbolt.com.ptypes.vesselstatespb.v1.PredictedDestinationR\x15predictedDestinations\"\xa7\x01\n\x14PredictedDestination\x12\x14\n\x05score\x18\x01 \x01(\x01R\x05score\x12\x17\n\x07port_id\x18\x02 \x01(\rR\x06portId\x12!\n\x0c\x63ountry_code\x18\x03 \x01(\tR\x0b\x63ountryCode\x12\x1b\n\tregion_id\x18\x04 \x01(\tR\x08regionId\x12 \n\x0b\x65xplanation\x18\x05 \x01(\tR\x0b\x65xplanation\"\x80\x01\n\x12ParsedDestinations\x12j\n\x13parsed_destinations\x18\x01 \x03(\x0b\x32\x39.oceanbolt.com.ptypes.vesselstatespb.v1.ParsedDestinationR\x12parsedDestinations\"\xc7\x02\n\x11ParsedDestination\x12\x14\n\x05score\x18\x01 \x01(\x01R\x05score\x12\x17\n\x07port_id\x18\x02 \x01(\rR\x06portId\x12!\n\x0c\x63ountry_code\x18\x03 \x01(\tR\x0b\x63ountryCode\x12m\n\nmatch_type\x18\x04 \x01(\x0e\x32N.oceanbolt.com.ptypes.vesselstatespb.v1.ParsedDestination.DestinationMatchTypeR\tmatchType\"q\n\x14\x44\x65stinationMatchType\x12\x1a\n\x16UNDEFINED_MATCH_STATUS\x10\x00\x12\x0f\n\x0b\x45XACT_MATCH\x10\x01\x12\x19\n\x15PORT_NAME_NGRAM_MATCH\x10\x02\x12\x11\n\rCOUNTRY_MATCH\x10\x03*^\n\x08Platform\x12\x16\n\x12UNDEFINED_PLATFORM\x10\x00\x12\x07\n\x03\x44RY\x10\x01\x12\x08\n\x04TANK\x10\x02\x12\r\n\tCONTAINER\x10\x03\x12\x08\n\x04RORO\x10\x04\x12\x0e\n\nAUXILLIARY\x10\x05*A\n\x0bLadenStatus\x12\x1a\n\x16UNDEFINED_LADEN_STATUS\x10\x00\x12\t\n\x05LADEN\x10\x01\x12\x0b\n\x07\x42\x41LLAST\x10\x02*z\n\x0ePortCallStatus\x12\x1e\n\x1aUNDEFINED_PORT_CALL_STATUS\x10\x00\x12\x0b\n\x07IN_PORT\x10\x01\x12\x10\n\x0cIN_ANCHORAGE\x10\x02\x12\x0c\n\x08IN_BERTH\x10\x03\x12\x0f\n\x0bIN_SHIPYARD\x10\x04\x12\n\n\x06\x41T_SEA\x10\x05*\xb1\x01\n\x0cVesselStatus\x12\x1b\n\x17UNDEFINED_VESSEL_STATUS\x10\x00\x12\x0e\n\nBALLASTING\x10\x01\x12\x0e\n\nIN_TRANSIT\x10\x02\x12\x08\n\x04YARD\x10\x03\x12\x0b\n\x07LOADING\x10\x04\x12\x0f\n\x0b\x44ISCHARGING\x10\x05\x12\x13\n\x0fWAITING_TO_LOAD\x10\x06\x12\x18\n\x14WAITING_TO_DISCHARGE\x10\x07\x12\r\n\tBUNKERING\x10\x08\x42UZSgitlab.com/veson/oceanbolt/gen-proto-go/gen/ptypes/vesselstatespb/v1;vesselstatespbb\x06proto3')

_PLATFORM = DESCRIPTOR.enum_types_by_name['Platform']
Platform = enum_type_wrapper.EnumTypeWrapper(_PLATFORM)
_LADENSTATUS = DESCRIPTOR.enum_types_by_name['LadenStatus']
LadenStatus = enum_type_wrapper.EnumTypeWrapper(_LADENSTATUS)
_PORTCALLSTATUS = DESCRIPTOR.enum_types_by_name['PortCallStatus']
PortCallStatus = enum_type_wrapper.EnumTypeWrapper(_PORTCALLSTATUS)
_VESSELSTATUS = DESCRIPTOR.enum_types_by_name['VesselStatus']
VesselStatus = enum_type_wrapper.EnumTypeWrapper(_VESSELSTATUS)
UNDEFINED_PLATFORM = 0
DRY = 1
TANK = 2
CONTAINER = 3
RORO = 4
AUXILLIARY = 5
UNDEFINED_LADEN_STATUS = 0
LADEN = 1
BALLAST = 2
UNDEFINED_PORT_CALL_STATUS = 0
IN_PORT = 1
IN_ANCHORAGE = 2
IN_BERTH = 3
IN_SHIPYARD = 4
AT_SEA = 5
UNDEFINED_VESSEL_STATUS = 0
BALLASTING = 1
IN_TRANSIT = 2
YARD = 3
LOADING = 4
DISCHARGING = 5
WAITING_TO_LOAD = 6
WAITING_TO_DISCHARGE = 7
BUNKERING = 8


_VESSELSTATE = DESCRIPTOR.message_types_by_name['VesselState']
_BASESTATE = DESCRIPTOR.message_types_by_name['BaseState']
_CARGOSTATE = DESCRIPTOR.message_types_by_name['CargoState']
_PREDICTEDDESTINATIONS = DESCRIPTOR.message_types_by_name['PredictedDestinations']
_PREDICTEDDESTINATION = DESCRIPTOR.message_types_by_name['PredictedDestination']
_PARSEDDESTINATIONS = DESCRIPTOR.message_types_by_name['ParsedDestinations']
_PARSEDDESTINATION = DESCRIPTOR.message_types_by_name['ParsedDestination']
_PARSEDDESTINATION_DESTINATIONMATCHTYPE = _PARSEDDESTINATION.enum_types_by_name['DestinationMatchType']
VesselState = _reflection.GeneratedProtocolMessageType('VesselState', (_message.Message,), {
  'DESCRIPTOR' : _VESSELSTATE,
  '__module__' : 'ptypes.vesselstatespb.v1.vessel_state_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.vesselstatespb.v1.VesselState)
  })
_sym_db.RegisterMessage(VesselState)

BaseState = _reflection.GeneratedProtocolMessageType('BaseState', (_message.Message,), {
  'DESCRIPTOR' : _BASESTATE,
  '__module__' : 'ptypes.vesselstatespb.v1.vessel_state_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.vesselstatespb.v1.BaseState)
  })
_sym_db.RegisterMessage(BaseState)

CargoState = _reflection.GeneratedProtocolMessageType('CargoState', (_message.Message,), {
  'DESCRIPTOR' : _CARGOSTATE,
  '__module__' : 'ptypes.vesselstatespb.v1.vessel_state_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.vesselstatespb.v1.CargoState)
  })
_sym_db.RegisterMessage(CargoState)

PredictedDestinations = _reflection.GeneratedProtocolMessageType('PredictedDestinations', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTEDDESTINATIONS,
  '__module__' : 'ptypes.vesselstatespb.v1.vessel_state_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.vesselstatespb.v1.PredictedDestinations)
  })
_sym_db.RegisterMessage(PredictedDestinations)

PredictedDestination = _reflection.GeneratedProtocolMessageType('PredictedDestination', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTEDDESTINATION,
  '__module__' : 'ptypes.vesselstatespb.v1.vessel_state_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.vesselstatespb.v1.PredictedDestination)
  })
_sym_db.RegisterMessage(PredictedDestination)

ParsedDestinations = _reflection.GeneratedProtocolMessageType('ParsedDestinations', (_message.Message,), {
  'DESCRIPTOR' : _PARSEDDESTINATIONS,
  '__module__' : 'ptypes.vesselstatespb.v1.vessel_state_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.vesselstatespb.v1.ParsedDestinations)
  })
_sym_db.RegisterMessage(ParsedDestinations)

ParsedDestination = _reflection.GeneratedProtocolMessageType('ParsedDestination', (_message.Message,), {
  'DESCRIPTOR' : _PARSEDDESTINATION,
  '__module__' : 'ptypes.vesselstatespb.v1.vessel_state_pb2'
  # @@protoc_insertion_point(class_scope:oceanbolt.com.ptypes.vesselstatespb.v1.ParsedDestination)
  })
_sym_db.RegisterMessage(ParsedDestination)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZSgitlab.com/veson/oceanbolt/gen-proto-go/gen/ptypes/vesselstatespb/v1;vesselstatespb'
  _PLATFORM._serialized_start=2907
  _PLATFORM._serialized_end=3001
  _LADENSTATUS._serialized_start=3003
  _LADENSTATUS._serialized_end=3068
  _PORTCALLSTATUS._serialized_start=3070
  _PORTCALLSTATUS._serialized_end=3192
  _VESSELSTATUS._serialized_start=3195
  _VESSELSTATUS._serialized_end=3372
  _VESSELSTATE._serialized_start=121
  _VESSELSTATE._serialized_end=526
  _BASESTATE._serialized_start=529
  _BASESTATE._serialized_end=1588
  _CARGOSTATE._serialized_start=1591
  _CARGOSTATE._serialized_end=2131
  _PREDICTEDDESTINATIONS._serialized_start=2134
  _PREDICTEDDESTINATIONS._serialized_end=2274
  _PREDICTEDDESTINATION._serialized_start=2277
  _PREDICTEDDESTINATION._serialized_end=2444
  _PARSEDDESTINATIONS._serialized_start=2447
  _PARSEDDESTINATIONS._serialized_end=2575
  _PARSEDDESTINATION._serialized_start=2578
  _PARSEDDESTINATION._serialized_end=2905
  _PARSEDDESTINATION_DESTINATIONMATCHTYPE._serialized_start=2792
  _PARSEDDESTINATION_DESTINATIONMATCHTYPE._serialized_end=2905
# @@protoc_insertion_point(module_scope)
