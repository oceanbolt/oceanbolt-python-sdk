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


from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.vessels.v3',
    manifest={
        'ListVesselsRequest',
        'ListVesselsResponse',
        'ListStoppageEventsRequest',
        'ListStoppageEventsResponse',
        'Vessel',
        'StoppageEvent',
    },
)


class ListVesselsRequest(proto.Message):
    r"""Vessels

    Attributes:
        dwt (Sequence[float]):
            min,max on the dwt columns
        eta (Sequence[str]):
            before,after on the eta columns
        segment (Sequence[str]):
            included segments
        sub_segment (Sequence[str]):
            included sub segments
        load_region (Sequence[str]):
            included load regions
        load_country (Sequence[str]):
            included load countries
        load_port (Sequence[str]):
            included load ports
        destination_region (Sequence[str]):
            included discharge regions
        destination_country (Sequence[str]):
            included discharge countries
        destination_port (Sequence[str]):
            included discharge ports
        destination_unlocode (Sequence[str]):
            included discharge ports
        cargo_status (Sequence[str]):
            included cargo states
        laden_status (Sequence[str]):
            included laden states
        laden_status_draught (Sequence[str]):
            included laden states
        speed (Sequence[float]):
            min,max on the speed column
        draught (Sequence[float]):
            min,max on the draught column
        exclude_unknown_destination (bool):
            include rows where destination_country is blank
        group (str):
            group by filter parameter
        range_ (str):
            range value for timeseries request (ex:
            month/monthly, week/weekly)
        flow_date (str):
            flow date (of load/discharge) for timeseries
            request
        commodity (Sequence[str]):
            included commodity values
        commodity_group (Sequence[str]):
            included commodity values
        zone_id (Sequence[int]):
            included zone ids
        port_id (Sequence[int]):
            included port ids
        anchorage_id (Sequence[int]):
            included anchorage ids
        berth_id (Sequence[int]):
            included berth ids
        shipyard_id (Sequence[int]):
            included shipyard ids
        direction (Sequence[str]):
            included diretions
        imo (Sequence[int]):
            included diretions
        port_status (Sequence[str]):

        exclude_mpv (bool):

        limit (int):

        hours_since_last (int):
            parameter for aisquality request
        format_ (str):
            response format (default is json, supported
            csv)
    """

    dwt = proto.RepeatedField(proto.DOUBLE, number=1)

    eta = proto.RepeatedField(proto.STRING, number=2)

    segment = proto.RepeatedField(proto.STRING, number=3)

    sub_segment = proto.RepeatedField(proto.STRING, number=4)

    load_region = proto.RepeatedField(proto.STRING, number=5)

    load_country = proto.RepeatedField(proto.STRING, number=6)

    load_port = proto.RepeatedField(proto.STRING, number=7)

    destination_region = proto.RepeatedField(proto.STRING, number=8)

    destination_country = proto.RepeatedField(proto.STRING, number=9)

    destination_port = proto.RepeatedField(proto.STRING, number=10)

    destination_unlocode = proto.RepeatedField(proto.STRING, number=35)

    cargo_status = proto.RepeatedField(proto.STRING, number=11)

    laden_status = proto.RepeatedField(proto.STRING, number=12)

    laden_status_draught = proto.RepeatedField(proto.STRING, number=29)

    speed = proto.RepeatedField(proto.DOUBLE, number=13)

    draught = proto.RepeatedField(proto.DOUBLE, number=14)

    exclude_unknown_destination = proto.Field(proto.BOOL, number=15)

    group = proto.Field(proto.STRING, number=16)

    range_ = proto.Field(proto.STRING, number=17)

    flow_date = proto.Field(proto.STRING, number=18)

    commodity = proto.RepeatedField(proto.STRING, number=19)

    commodity_group = proto.RepeatedField(proto.STRING, number=30)

    zone_id = proto.RepeatedField(proto.UINT32, number=21)

    port_id = proto.RepeatedField(proto.UINT32, number=22)

    anchorage_id = proto.RepeatedField(proto.UINT32, number=23)

    berth_id = proto.RepeatedField(proto.UINT32, number=24)

    shipyard_id = proto.RepeatedField(proto.UINT32, number=25)

    direction = proto.RepeatedField(proto.STRING, number=26)

    imo = proto.RepeatedField(proto.UINT32, number=28)

    port_status = proto.RepeatedField(proto.STRING, number=31)

    exclude_mpv = proto.Field(proto.BOOL, number=32)

    limit = proto.Field(proto.UINT32, number=33)

    hours_since_last = proto.Field(proto.UINT32, number=34)

    format_ = proto.Field(proto.STRING, number=27)


class ListVesselsResponse(proto.Message):
    r"""

    Attributes:
        vessels (Sequence[oceanbolt.com.vessels_v3.types.Vessel]):

        csv (str):

        xlsx (str):

    """

    vessels = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Vessel',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class ListStoppageEventsRequest(proto.Message):
    r"""VesselStoppageEvents

    Attributes:
        imo (Sequence[int]):
            included vessel imos
        startDate (str):

        endDate (str):

        format_ (str):
            response format (default is json, supported:
            csv, xlsx)
    """

    imo = proto.RepeatedField(proto.INT32, number=1)

    startDate = proto.Field(proto.STRING, number=2)

    endDate = proto.Field(proto.STRING, number=3)

    format_ = proto.Field(proto.STRING, number=4)


class ListStoppageEventsResponse(proto.Message):
    r"""

    Attributes:
        stoppage_events (Sequence[oceanbolt.com.vessels_v3.types.StoppageEvent]):

        csv (str):

        xlsx (str):

    """

    stoppage_events = proto.RepeatedField(proto.MESSAGE, number=1,
        message='StoppageEvent',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class Vessel(proto.Message):
    r"""Entities

    Attributes:
        vessel_name (str):

        imo (int):

        mmsi (int):

        last_position_received (str):

        last_static_received (str):

        dwt (float):

        segment (str):

        sub_segment (str):

        zone_id (int):

        zone_name (str):

        port_id (int):

        port_name (str):

        anchorage_id (int):

        anchorage_name (str):

        berth_id (int):

        berth_name (str):

        shipyard_id (int):

        shipyard_name (str):

        related_port_id (int):

        related_port_name (str):

        cargo_status (str):

        laden_status (str):

        laden_status_draught (str):

        destination (str):

        destination_port_name (str):

        destination_region (str):

        destination_country_code (str):

        eta (str):

        navigational_status (int):

        last_port_name (str):

        last_country_code (str):

        last_region (str):

        port_call_status (str):

        commodity_group (str):

        commodity_name (str):

        direction (str):

        speed (float):

    """

    vessel_name = proto.Field(proto.STRING, number=1)

    imo = proto.Field(proto.UINT32, number=2)

    mmsi = proto.Field(proto.UINT32, number=3)

    last_position_received = proto.Field(proto.STRING, number=4)

    last_static_received = proto.Field(proto.STRING, number=5)

    dwt = proto.Field(proto.DOUBLE, number=6)

    segment = proto.Field(proto.STRING, number=7)

    sub_segment = proto.Field(proto.STRING, number=8)

    zone_id = proto.Field(proto.UINT32, number=9)

    zone_name = proto.Field(proto.STRING, number=27)

    port_id = proto.Field(proto.UINT32, number=28)

    port_name = proto.Field(proto.STRING, number=29)

    anchorage_id = proto.Field(proto.UINT32, number=30)

    anchorage_name = proto.Field(proto.STRING, number=31)

    berth_id = proto.Field(proto.UINT32, number=32)

    berth_name = proto.Field(proto.STRING, number=33)

    shipyard_id = proto.Field(proto.UINT32, number=34)

    shipyard_name = proto.Field(proto.STRING, number=35)

    related_port_id = proto.Field(proto.UINT32, number=36)

    related_port_name = proto.Field(proto.STRING, number=37)

    cargo_status = proto.Field(proto.STRING, number=10)

    laden_status = proto.Field(proto.STRING, number=11)

    laden_status_draught = proto.Field(proto.STRING, number=12)

    destination = proto.Field(proto.STRING, number=13)

    destination_port_name = proto.Field(proto.STRING, number=14)

    destination_region = proto.Field(proto.STRING, number=15)

    destination_country_code = proto.Field(proto.STRING, number=16)

    eta = proto.Field(proto.STRING, number=17)

    navigational_status = proto.Field(proto.UINT32, number=18)

    last_port_name = proto.Field(proto.STRING, number=19)

    last_country_code = proto.Field(proto.STRING, number=20)

    last_region = proto.Field(proto.STRING, number=21)

    port_call_status = proto.Field(proto.STRING, number=22)

    commodity_group = proto.Field(proto.STRING, number=23)

    commodity_name = proto.Field(proto.STRING, number=24)

    direction = proto.Field(proto.STRING, number=25)

    speed = proto.Field(proto.DOUBLE, number=26)


class StoppageEvent(proto.Message):
    r"""

    Attributes:
        imo (int):

        started_at (str):

        ended_at (str):

        port_id (int):

        port_name (str):

        zone_id (int):

        zone_name (str):

        min_speed_observed (google.protobuf.wrappers_pb2.DoubleValue):

        duration_hours (google.protobuf.wrappers_pb2.DoubleValue):

        lat (float):

        lon (float):

        classification (str):

    """

    imo = proto.Field(proto.INT32, number=1)

    started_at = proto.Field(proto.STRING, number=2)

    ended_at = proto.Field(proto.STRING, number=3)

    port_id = proto.Field(proto.INT32, number=4)

    port_name = proto.Field(proto.STRING, number=5)

    zone_id = proto.Field(proto.INT32, number=6)

    zone_name = proto.Field(proto.STRING, number=7)

    min_speed_observed = proto.Field(proto.MESSAGE, number=8,
        message=wrappers.DoubleValue,
    )

    duration_hours = proto.Field(proto.MESSAGE, number=9,
        message=wrappers.DoubleValue,
    )

    lat = proto.Field(proto.DOUBLE, number=10)

    lon = proto.Field(proto.DOUBLE, number=11)

    classification = proto.Field(proto.STRING, number=12)


__all__ = tuple(sorted(__protobuf__.manifest))
