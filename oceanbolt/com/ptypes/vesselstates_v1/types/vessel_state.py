# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.ptypes.vesselstates.v1',
    manifest={
        'Platform',
        'LadenStatus',
        'PortCallStatus',
        'VesselStatus',
        'VesselState',
        'BaseState',
        'CargoState',
        'PredictedDestinations',
        'PredictedDestination',
        'ParsedDestinations',
        'ParsedDestination',
    },
)


class Platform(proto.Enum):
    r""""""
    UNDEFINED_PLATFORM = 0
    DRY = 1
    TANK = 2
    CONTAINER = 3
    RORO = 4
    AUXILLIARY = 5


class LadenStatus(proto.Enum):
    r""""""
    UNDEFINED_LADEN_STATUS = 0
    LADEN = 1
    BALLAST = 2


class PortCallStatus(proto.Enum):
    r""""""
    UNDEFINED_PORT_CALL_STATUS = 0
    IN_PORT = 1
    IN_ANCHORAGE = 2
    IN_BERTH = 3
    IN_SHIPYARD = 4
    AT_SEA = 5


class VesselStatus(proto.Enum):
    r""""""
    UNDEFINED_VESSEL_STATUS = 0
    BALLASTING = 1
    IN_TRANSIT = 2
    YARD = 3
    LOADING = 4
    DISCHARGING = 5
    WAITING_TO_LOAD = 6
    WAITING_TO_DISCHARGE = 7
    BUNKERING = 8


class VesselState(proto.Message):
    r"""

    Attributes:
        base_state (oceanbolt.com.ptypes.vesselstates_v1.types.BaseState):
            Base state containing ground truth data for
            the vessel on a specific date
        cargo_state (oceanbolt.com.ptypes.vesselstates_v1.types.CargoState):
            Predicted and enriched fields relating to
            cargo state
        parsed_destinations (Sequence[oceanbolt.com.ptypes.vesselstates_v1.types.ParsedDestination]):

        predicted_destinations (Sequence[oceanbolt.com.ptypes.vesselstates_v1.types.PredictedDestination]):

    """

    base_state = proto.Field(
        proto.MESSAGE,
        number=1,
        message='BaseState',
    )
    cargo_state = proto.Field(
        proto.MESSAGE,
        number=2,
        message='CargoState',
    )
    parsed_destinations = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='ParsedDestination',
    )
    predicted_destinations = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='PredictedDestination',
    )


class BaseState(proto.Message):
    r"""

    Attributes:
        platform (oceanbolt.com.ptypes.vesselstates_v1.types.Platform):

        imo (int):

        mmsi (int):

        timestamp (google.protobuf.timestamp_pb2.Timestamp):

        navigational_status_code (int):

        zone_id (int):

        port_id (int):

        anchorage_id (int):

        berth_id (int):

        shipyard_id (int):

        related_port_id (int):

        eca_zone_id (int):

        piracy_zone_id (int):

        vip_zone_id (int):

        destination (str):

        destination_updated (google.protobuf.timestamp_pb2.Timestamp):

        eta (google.protobuf.timestamp_pb2.Timestamp):

        eta_updated (google.protobuf.timestamp_pb2.Timestamp):

        longitude (float):

        latitude (float):

        course (float):

        heading (float):

        speed (float):

        draught (float):

        laden_status_draught (oceanbolt.com.ptypes.vesselstates_v1.types.LadenStatus):

        hours_carried_forward (int):

    """

    platform = proto.Field(
        proto.ENUM,
        number=1,
        enum='Platform',
    )
    imo = proto.Field(
        proto.UINT32,
        number=2,
    )
    mmsi = proto.Field(
        proto.UINT32,
        number=3,
    )
    timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    navigational_status_code = proto.Field(
        proto.UINT32,
        number=5,
    )
    zone_id = proto.Field(
        proto.UINT32,
        number=6,
    )
    port_id = proto.Field(
        proto.UINT32,
        number=7,
    )
    anchorage_id = proto.Field(
        proto.UINT32,
        number=8,
    )
    berth_id = proto.Field(
        proto.UINT32,
        number=9,
    )
    shipyard_id = proto.Field(
        proto.UINT32,
        number=10,
    )
    related_port_id = proto.Field(
        proto.UINT32,
        number=11,
    )
    eca_zone_id = proto.Field(
        proto.UINT32,
        number=12,
    )
    piracy_zone_id = proto.Field(
        proto.UINT32,
        number=13,
    )
    vip_zone_id = proto.Field(
        proto.UINT32,
        number=26,
    )
    destination = proto.Field(
        proto.STRING,
        number=14,
    )
    destination_updated = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    eta = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    eta_updated = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    longitude = proto.Field(
        proto.DOUBLE,
        number=18,
    )
    latitude = proto.Field(
        proto.DOUBLE,
        number=19,
    )
    course = proto.Field(
        proto.DOUBLE,
        number=20,
    )
    heading = proto.Field(
        proto.DOUBLE,
        number=21,
    )
    speed = proto.Field(
        proto.DOUBLE,
        number=22,
    )
    draught = proto.Field(
        proto.DOUBLE,
        number=23,
    )
    laden_status_draught = proto.Field(
        proto.ENUM,
        number=24,
        enum='LadenStatus',
    )
    hours_carried_forward = proto.Field(
        proto.UINT32,
        number=25,
    )


class CargoState(proto.Message):
    r"""

    Attributes:
        commodity_id (int):

        laden_status_model (oceanbolt.com.ptypes.vesselstates_v1.types.LadenStatus):

        trade_flow_id (str):

        vessel_status (oceanbolt.com.ptypes.vesselstates_v1.types.VesselStatus):

        last_visited_port_id (int):

        last_ops_port_id (int):

        last_ops_port_call_id (str):

    """

    commodity_id = proto.Field(
        proto.UINT32,
        number=1,
    )
    laden_status_model = proto.Field(
        proto.ENUM,
        number=2,
        enum='LadenStatus',
    )
    trade_flow_id = proto.Field(
        proto.STRING,
        number=3,
    )
    vessel_status = proto.Field(
        proto.ENUM,
        number=5,
        enum='VesselStatus',
    )
    last_visited_port_id = proto.Field(
        proto.UINT32,
        number=6,
    )
    last_ops_port_id = proto.Field(
        proto.UINT32,
        number=7,
    )
    last_ops_port_call_id = proto.Field(
        proto.STRING,
        number=8,
    )


class PredictedDestinations(proto.Message):
    r"""

    Attributes:
        predicted_destinations (Sequence[oceanbolt.com.ptypes.vesselstates_v1.types.PredictedDestination]):

    """

    predicted_destinations = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='PredictedDestination',
    )


class PredictedDestination(proto.Message):
    r"""

    Attributes:
        score (float):

        port_id (int):

        country_code (str):

        region_id (str):

    """

    score = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    port_id = proto.Field(
        proto.UINT32,
        number=2,
    )
    country_code = proto.Field(
        proto.STRING,
        number=3,
    )
    region_id = proto.Field(
        proto.STRING,
        number=4,
    )


class ParsedDestinations(proto.Message):
    r"""

    Attributes:
        parsed_destinations (Sequence[oceanbolt.com.ptypes.vesselstates_v1.types.ParsedDestination]):

    """

    parsed_destinations = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='ParsedDestination',
    )


class ParsedDestination(proto.Message):
    r"""

    Attributes:
        score (float):

        port_id (int):

        country_code (str):

        match_type (oceanbolt.com.ptypes.vesselstates_v1.types.ParsedDestination.DestinationMatchType):

    """
    class DestinationMatchType(proto.Enum):
        r""""""
        UNDEFINED_MATCH_STATUS = 0
        EXACT_MATCH = 1
        PORT_NAME_NGRAM_MATCH = 2
        COUNTRY_MATCH = 3

    score = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    port_id = proto.Field(
        proto.UINT32,
        number=2,
    )
    country_code = proto.Field(
        proto.STRING,
        number=3,
    )
    match_type = proto.Field(
        proto.ENUM,
        number=4,
        enum=DestinationMatchType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
