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


__protobuf__ = proto.module(
    package='oceanbolt.com.vesselstates.v3',
    manifest={
        'GetVesselStatesRequest',
        'GetVesselStatesForDateRequest',
        'VesselStatesResponse',
        'VesselState',
    },
)


class GetVesselStatesRequest(proto.Message):
    r"""Request message for VesselStateService.GetVesselStates

    Attributes:
        imo (Sequence[int]):
            included vessel imos
        start_date (str):

        end_date (str):

        format_ (str):
            response format (default is json, supported:
            csv, xlsx)
    """

    imo = proto.RepeatedField(proto.INT32, number=1)

    start_date = proto.Field(proto.STRING, number=2)

    end_date = proto.Field(proto.STRING, number=3)

    format_ = proto.Field(proto.STRING, number=4)


class GetVesselStatesForDateRequest(proto.Message):
    r"""Request message for
    VesselStateService.GetAllVesselStatesForDate

    Attributes:
        date (str):

        format_ (str):
            response format (default is json, supported:
            csv, xlsx)
    """

    date = proto.Field(proto.STRING, number=1)

    format_ = proto.Field(proto.STRING, number=2)


class VesselStatesResponse(proto.Message):
    r"""Request message for VesselStateService.GetVesselStates and
    VesselStateService.GetAllVesselStatesForDate.

    Attributes:
        vessel_states (Sequence[oceanbolt.com.vesselstates_v3.types.VesselState]):
            A collection of VesselState objects that is
            returned by the API.
        csv (str):

        xlsx (str):

    """

    vessel_states = proto.RepeatedField(proto.MESSAGE, number=1,
        message='VesselState',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class VesselState(proto.Message):
    r"""VesselState object

    Attributes:
        vessel_name (str):
            Name of the vessel.
        imo (int):
            IMO number of the vessel.
        mmsi (int):
            MMSI number of the vessel.
        timestamp (str):
            UTC timestamp for the VesselState.
        dwt (float):
            DWT of the vessel.
        segment (str):
            Segment of the vessel.
        sub_segment (str):
            Sub segment of the vessel.
        vessel_type (str):
            The vessel type.
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

        vessel_status (str):

        laden_status_model (str):
            The laden status of the vessel as determined
            from the the Oceanbolt Algorithms, taking into
            account prior berth visits, prior draught
            changes etc.
        laden_status_draught (str):
            The laden status according to the current
            draught as reported by the Master.
        destination (str):

        destination_port_name (str):

        destination_region (str):

        destination_country_code (str):

        destination_score (float):

        eta (str):

        navigational_status (str):

        navigational_status_code (int):

        port_call_status (str):

        commodity_group (str):

        commodity_name (str):

        direction (str):

        speed_status (str):

        hours_carried_forward (int):
            A indicator describing if the given
            VesselState was recorded directly from AIS, or
            if it was backfilled and carried forward from
            the last received observation. The value is zero
            for observations that are derived directly from
            a received AIS position, for observations that
            are carried forward the value will indicate the
            number of hours the current observations has
            been carried forward.
    """

    vessel_name = proto.Field(proto.STRING, number=1)

    imo = proto.Field(proto.UINT32, number=2)

    mmsi = proto.Field(proto.UINT32, number=3)

    timestamp = proto.Field(proto.STRING, number=38)

    dwt = proto.Field(proto.DOUBLE, number=6)

    segment = proto.Field(proto.STRING, number=7)

    sub_segment = proto.Field(proto.STRING, number=8)

    vessel_type = proto.Field(proto.STRING, number=40)

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

    vessel_status = proto.Field(proto.STRING, number=10)

    laden_status_model = proto.Field(proto.STRING, number=11)

    laden_status_draught = proto.Field(proto.STRING, number=12)

    destination = proto.Field(proto.STRING, number=13)

    destination_port_name = proto.Field(proto.STRING, number=14)

    destination_region = proto.Field(proto.STRING, number=15)

    destination_country_code = proto.Field(proto.STRING, number=16)

    destination_score = proto.Field(proto.DOUBLE, number=41)

    eta = proto.Field(proto.STRING, number=17)

    navigational_status = proto.Field(proto.STRING, number=18)

    navigational_status_code = proto.Field(proto.UINT32, number=45)

    port_call_status = proto.Field(proto.STRING, number=22)

    commodity_group = proto.Field(proto.STRING, number=23)

    commodity_name = proto.Field(proto.STRING, number=24)

    direction = proto.Field(proto.STRING, number=25)

    speed_status = proto.Field(proto.STRING, number=26)

    hours_carried_forward = proto.Field(proto.UINT32, number=43)


__all__ = tuple(sorted(__protobuf__.manifest))
