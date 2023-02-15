"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Platform:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PlatformEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Platform.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNDEFINED_PLATFORM: _Platform.ValueType  # 0
    DRY: _Platform.ValueType  # 1
    TANK: _Platform.ValueType  # 2
    CONTAINER: _Platform.ValueType  # 3
    RORO: _Platform.ValueType  # 4
    AUXILLIARY: _Platform.ValueType  # 5

class Platform(_Platform, metaclass=_PlatformEnumTypeWrapper):
    """Platform Enum"""

UNDEFINED_PLATFORM: Platform.ValueType  # 0
DRY: Platform.ValueType  # 1
TANK: Platform.ValueType  # 2
CONTAINER: Platform.ValueType  # 3
RORO: Platform.ValueType  # 4
AUXILLIARY: Platform.ValueType  # 5
global___Platform = Platform

class _LadenStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LadenStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LadenStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNDEFINED_LADEN_STATUS: _LadenStatus.ValueType  # 0
    LADEN: _LadenStatus.ValueType  # 1
    BALLAST: _LadenStatus.ValueType  # 2

class LadenStatus(_LadenStatus, metaclass=_LadenStatusEnumTypeWrapper): ...

UNDEFINED_LADEN_STATUS: LadenStatus.ValueType  # 0
LADEN: LadenStatus.ValueType  # 1
BALLAST: LadenStatus.ValueType  # 2
global___LadenStatus = LadenStatus

class _PortCallStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PortCallStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PortCallStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNDEFINED_PORT_CALL_STATUS: _PortCallStatus.ValueType  # 0
    IN_PORT: _PortCallStatus.ValueType  # 1
    IN_ANCHORAGE: _PortCallStatus.ValueType  # 2
    IN_BERTH: _PortCallStatus.ValueType  # 3
    IN_SHIPYARD: _PortCallStatus.ValueType  # 4
    AT_SEA: _PortCallStatus.ValueType  # 5

class PortCallStatus(_PortCallStatus, metaclass=_PortCallStatusEnumTypeWrapper): ...

UNDEFINED_PORT_CALL_STATUS: PortCallStatus.ValueType  # 0
IN_PORT: PortCallStatus.ValueType  # 1
IN_ANCHORAGE: PortCallStatus.ValueType  # 2
IN_BERTH: PortCallStatus.ValueType  # 3
IN_SHIPYARD: PortCallStatus.ValueType  # 4
AT_SEA: PortCallStatus.ValueType  # 5
global___PortCallStatus = PortCallStatus

class _VesselStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VesselStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VesselStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNDEFINED_VESSEL_STATUS: _VesselStatus.ValueType  # 0
    BALLASTING: _VesselStatus.ValueType  # 1
    IN_TRANSIT: _VesselStatus.ValueType  # 2
    YARD: _VesselStatus.ValueType  # 3
    LOADING: _VesselStatus.ValueType  # 4
    DISCHARGING: _VesselStatus.ValueType  # 5
    WAITING_TO_LOAD: _VesselStatus.ValueType  # 6
    WAITING_TO_DISCHARGE: _VesselStatus.ValueType  # 7
    BUNKERING: _VesselStatus.ValueType  # 8

class VesselStatus(_VesselStatus, metaclass=_VesselStatusEnumTypeWrapper): ...

UNDEFINED_VESSEL_STATUS: VesselStatus.ValueType  # 0
BALLASTING: VesselStatus.ValueType  # 1
IN_TRANSIT: VesselStatus.ValueType  # 2
YARD: VesselStatus.ValueType  # 3
LOADING: VesselStatus.ValueType  # 4
DISCHARGING: VesselStatus.ValueType  # 5
WAITING_TO_LOAD: VesselStatus.ValueType  # 6
WAITING_TO_DISCHARGE: VesselStatus.ValueType  # 7
BUNKERING: VesselStatus.ValueType  # 8
global___VesselStatus = VesselStatus

@typing_extensions.final
class VesselState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_STATE_FIELD_NUMBER: builtins.int
    CARGO_STATE_FIELD_NUMBER: builtins.int
    PARSED_DESTINATIONS_FIELD_NUMBER: builtins.int
    PREDICTED_DESTINATIONS_FIELD_NUMBER: builtins.int
    @property
    def base_state(self) -> global___BaseState:
        """Base state containing ground truth data for the vessel on a specific date"""
    @property
    def cargo_state(self) -> global___CargoState:
        """Predicted and enriched fields relating to cargo state"""
    @property
    def parsed_destinations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParsedDestination]: ...
    @property
    def predicted_destinations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PredictedDestination]: ...
    def __init__(
        self,
        *,
        base_state: global___BaseState | None = ...,
        cargo_state: global___CargoState | None = ...,
        parsed_destinations: collections.abc.Iterable[global___ParsedDestination] | None = ...,
        predicted_destinations: collections.abc.Iterable[global___PredictedDestination] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_state", b"base_state", "cargo_state", b"cargo_state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_state", b"base_state", "cargo_state", b"cargo_state", "parsed_destinations", b"parsed_destinations", "predicted_destinations", b"predicted_destinations"]) -> None: ...

global___VesselState = VesselState

@typing_extensions.final
class BaseState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLATFORM_FIELD_NUMBER: builtins.int
    IMO_FIELD_NUMBER: builtins.int
    MMSI_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    NAVIGATIONAL_STATUS_CODE_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    PORT_ID_FIELD_NUMBER: builtins.int
    ANCHORAGE_ID_FIELD_NUMBER: builtins.int
    BERTH_ID_FIELD_NUMBER: builtins.int
    SHIPYARD_ID_FIELD_NUMBER: builtins.int
    RELATED_PORT_ID_FIELD_NUMBER: builtins.int
    ECA_ZONE_ID_FIELD_NUMBER: builtins.int
    PIRACY_ZONE_ID_FIELD_NUMBER: builtins.int
    VIP_ZONE_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    DESTINATION_UPDATED_FIELD_NUMBER: builtins.int
    ETA_FIELD_NUMBER: builtins.int
    ETA_UPDATED_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    LATITUDE_FIELD_NUMBER: builtins.int
    COURSE_FIELD_NUMBER: builtins.int
    HEADING_FIELD_NUMBER: builtins.int
    SPEED_FIELD_NUMBER: builtins.int
    DRAUGHT_FIELD_NUMBER: builtins.int
    LADEN_STATUS_DRAUGHT_FIELD_NUMBER: builtins.int
    HOURS_CARRIED_FORWARD_FIELD_NUMBER: builtins.int
    platform: global___Platform.ValueType
    imo: builtins.int
    mmsi: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    navigational_status_code: builtins.int
    zone_id: builtins.int
    port_id: builtins.int
    anchorage_id: builtins.int
    berth_id: builtins.int
    shipyard_id: builtins.int
    related_port_id: builtins.int
    eca_zone_id: builtins.int
    piracy_zone_id: builtins.int
    vip_zone_id: builtins.int
    destination: builtins.str
    @property
    def destination_updated(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def eta(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def eta_updated(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    longitude: builtins.float
    latitude: builtins.float
    course: builtins.float
    heading: builtins.float
    speed: builtins.float
    draught: builtins.float
    laden_status_draught: global___LadenStatus.ValueType
    hours_carried_forward: builtins.int
    def __init__(
        self,
        *,
        platform: global___Platform.ValueType = ...,
        imo: builtins.int = ...,
        mmsi: builtins.int = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        navigational_status_code: builtins.int = ...,
        zone_id: builtins.int = ...,
        port_id: builtins.int = ...,
        anchorage_id: builtins.int = ...,
        berth_id: builtins.int = ...,
        shipyard_id: builtins.int = ...,
        related_port_id: builtins.int = ...,
        eca_zone_id: builtins.int = ...,
        piracy_zone_id: builtins.int = ...,
        vip_zone_id: builtins.int = ...,
        destination: builtins.str = ...,
        destination_updated: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        eta: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        eta_updated: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        longitude: builtins.float = ...,
        latitude: builtins.float = ...,
        course: builtins.float = ...,
        heading: builtins.float = ...,
        speed: builtins.float = ...,
        draught: builtins.float = ...,
        laden_status_draught: global___LadenStatus.ValueType = ...,
        hours_carried_forward: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["destination_updated", b"destination_updated", "eta", b"eta", "eta_updated", b"eta_updated", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["anchorage_id", b"anchorage_id", "berth_id", b"berth_id", "course", b"course", "destination", b"destination", "destination_updated", b"destination_updated", "draught", b"draught", "eca_zone_id", b"eca_zone_id", "eta", b"eta", "eta_updated", b"eta_updated", "heading", b"heading", "hours_carried_forward", b"hours_carried_forward", "imo", b"imo", "laden_status_draught", b"laden_status_draught", "latitude", b"latitude", "longitude", b"longitude", "mmsi", b"mmsi", "navigational_status_code", b"navigational_status_code", "piracy_zone_id", b"piracy_zone_id", "platform", b"platform", "port_id", b"port_id", "related_port_id", b"related_port_id", "shipyard_id", b"shipyard_id", "speed", b"speed", "timestamp", b"timestamp", "vip_zone_id", b"vip_zone_id", "zone_id", b"zone_id"]) -> None: ...

global___BaseState = BaseState

@typing_extensions.final
class CargoState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMODITY_ID_FIELD_NUMBER: builtins.int
    LADEN_STATUS_MODEL_FIELD_NUMBER: builtins.int
    TRADE_FLOW_ID_FIELD_NUMBER: builtins.int
    VESSEL_STATUS_FIELD_NUMBER: builtins.int
    LAST_VISITED_PORT_ID_FIELD_NUMBER: builtins.int
    LAST_OPS_BERTH_ID_FIELD_NUMBER: builtins.int
    LAST_OPS_PORT_ID_FIELD_NUMBER: builtins.int
    LAST_OPS_PORT_CALL_ID_FIELD_NUMBER: builtins.int
    LAST_OPS_PORT_REGION_ID_FIELD_NUMBER: builtins.int
    LAST_OPS_DEPARTURE_FIELD_NUMBER: builtins.int
    NEXT_VISITED_PORT_ID_FIELD_NUMBER: builtins.int
    NEXT_VISTED_ARRIVAL_FIELD_NUMBER: builtins.int
    NEXT_OPS_PORT_ID_FIELD_NUMBER: builtins.int
    NEXT_OPS_PORT_CALL_ID_FIELD_NUMBER: builtins.int
    NEXT_OPS_PORT_REGION_ID_FIELD_NUMBER: builtins.int
    NEXT_OPS_ARRIVAL_FIELD_NUMBER: builtins.int
    VOLUME_ON_BOARD_FIELD_NUMBER: builtins.int
    VOLUME_UNIT_FIELD_NUMBER: builtins.int
    commodity_id: builtins.int
    laden_status_model: global___LadenStatus.ValueType
    trade_flow_id: builtins.str
    vessel_status: global___VesselStatus.ValueType
    last_visited_port_id: builtins.int
    last_ops_berth_id: builtins.int
    last_ops_port_id: builtins.int
    last_ops_port_call_id: builtins.str
    last_ops_port_region_id: builtins.str
    @property
    def last_ops_departure(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    next_visited_port_id: builtins.int
    @property
    def next_visted_arrival(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    next_ops_port_id: builtins.int
    next_ops_port_call_id: builtins.str
    next_ops_port_region_id: builtins.str
    @property
    def next_ops_arrival(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    volume_on_board: builtins.float
    volume_unit: builtins.str
    def __init__(
        self,
        *,
        commodity_id: builtins.int = ...,
        laden_status_model: global___LadenStatus.ValueType = ...,
        trade_flow_id: builtins.str = ...,
        vessel_status: global___VesselStatus.ValueType = ...,
        last_visited_port_id: builtins.int = ...,
        last_ops_berth_id: builtins.int = ...,
        last_ops_port_id: builtins.int = ...,
        last_ops_port_call_id: builtins.str = ...,
        last_ops_port_region_id: builtins.str = ...,
        last_ops_departure: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        next_visited_port_id: builtins.int = ...,
        next_visted_arrival: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        next_ops_port_id: builtins.int = ...,
        next_ops_port_call_id: builtins.str = ...,
        next_ops_port_region_id: builtins.str = ...,
        next_ops_arrival: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        volume_on_board: builtins.float = ...,
        volume_unit: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["last_ops_departure", b"last_ops_departure", "next_ops_arrival", b"next_ops_arrival", "next_visted_arrival", b"next_visted_arrival"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["commodity_id", b"commodity_id", "laden_status_model", b"laden_status_model", "last_ops_berth_id", b"last_ops_berth_id", "last_ops_departure", b"last_ops_departure", "last_ops_port_call_id", b"last_ops_port_call_id", "last_ops_port_id", b"last_ops_port_id", "last_ops_port_region_id", b"last_ops_port_region_id", "last_visited_port_id", b"last_visited_port_id", "next_ops_arrival", b"next_ops_arrival", "next_ops_port_call_id", b"next_ops_port_call_id", "next_ops_port_id", b"next_ops_port_id", "next_ops_port_region_id", b"next_ops_port_region_id", "next_visited_port_id", b"next_visited_port_id", "next_visted_arrival", b"next_visted_arrival", "trade_flow_id", b"trade_flow_id", "vessel_status", b"vessel_status", "volume_on_board", b"volume_on_board", "volume_unit", b"volume_unit"]) -> None: ...

global___CargoState = CargoState

@typing_extensions.final
class PredictedDestinations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREDICTED_DESTINATIONS_FIELD_NUMBER: builtins.int
    @property
    def predicted_destinations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PredictedDestination]: ...
    def __init__(
        self,
        *,
        predicted_destinations: collections.abc.Iterable[global___PredictedDestination] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["predicted_destinations", b"predicted_destinations"]) -> None: ...

global___PredictedDestinations = PredictedDestinations

@typing_extensions.final
class PredictedDestination(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCORE_FIELD_NUMBER: builtins.int
    PORT_ID_FIELD_NUMBER: builtins.int
    COUNTRY_CODE_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    EXPLANATION_FIELD_NUMBER: builtins.int
    ETA_FIELD_NUMBER: builtins.int
    score: builtins.float
    port_id: builtins.int
    country_code: builtins.str
    region_id: builtins.str
    explanation: builtins.str
    @property
    def eta(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        score: builtins.float = ...,
        port_id: builtins.int = ...,
        country_code: builtins.str = ...,
        region_id: builtins.str = ...,
        explanation: builtins.str = ...,
        eta: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["eta", b"eta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["country_code", b"country_code", "eta", b"eta", "explanation", b"explanation", "port_id", b"port_id", "region_id", b"region_id", "score", b"score"]) -> None: ...

global___PredictedDestination = PredictedDestination

@typing_extensions.final
class ParsedDestinations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARSED_DESTINATIONS_FIELD_NUMBER: builtins.int
    @property
    def parsed_destinations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParsedDestination]: ...
    def __init__(
        self,
        *,
        parsed_destinations: collections.abc.Iterable[global___ParsedDestination] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parsed_destinations", b"parsed_destinations"]) -> None: ...

global___ParsedDestinations = ParsedDestinations

@typing_extensions.final
class ParsedDestination(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _DestinationMatchType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _DestinationMatchTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ParsedDestination._DestinationMatchType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNDEFINED_MATCH_STATUS: ParsedDestination._DestinationMatchType.ValueType  # 0
        EXACT_MATCH: ParsedDestination._DestinationMatchType.ValueType  # 1
        PORT_NAME_NGRAM_MATCH: ParsedDestination._DestinationMatchType.ValueType  # 2
        COUNTRY_MATCH: ParsedDestination._DestinationMatchType.ValueType  # 3

    class DestinationMatchType(_DestinationMatchType, metaclass=_DestinationMatchTypeEnumTypeWrapper): ...
    UNDEFINED_MATCH_STATUS: ParsedDestination.DestinationMatchType.ValueType  # 0
    EXACT_MATCH: ParsedDestination.DestinationMatchType.ValueType  # 1
    PORT_NAME_NGRAM_MATCH: ParsedDestination.DestinationMatchType.ValueType  # 2
    COUNTRY_MATCH: ParsedDestination.DestinationMatchType.ValueType  # 3

    SCORE_FIELD_NUMBER: builtins.int
    PORT_ID_FIELD_NUMBER: builtins.int
    COUNTRY_CODE_FIELD_NUMBER: builtins.int
    MATCH_TYPE_FIELD_NUMBER: builtins.int
    score: builtins.float
    port_id: builtins.int
    country_code: builtins.str
    match_type: global___ParsedDestination.DestinationMatchType.ValueType
    def __init__(
        self,
        *,
        score: builtins.float = ...,
        port_id: builtins.int = ...,
        country_code: builtins.str = ...,
        match_type: global___ParsedDestination.DestinationMatchType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["country_code", b"country_code", "match_type", b"match_type", "port_id", b"port_id", "score", b"score"]) -> None: ...

global___ParsedDestination = ParsedDestination
