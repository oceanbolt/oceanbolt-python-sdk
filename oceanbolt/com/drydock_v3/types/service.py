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
    package='oceanbolt.com.drydock.v3',
    manifest={
        'EmptyParams',
        'EmptyResponse',
        'GetTonnageDryDockRequest',
        'GetTonnageDryDockResponse',
        'DryDockValue',
        'DryDockSummaryRequest',
        'DryDockSummaryResponse',
        'DryDockSummaryValue',
        'GetDryDockStaysRequest',
        'GetDryDockStaysResponse',
        'ShipyardStay',
    },
)


class EmptyParams(proto.Message):
    r""""""


class EmptyResponse(proto.Message):
    r""""""


class GetTonnageDryDockRequest(proto.Message):
    r""" Dry Dock Requests and Responses
    GetTonnageDryDock

    Attributes:
        segment (Sequence[str]):

        metric (str):

        absolute (bool):

        format_ (str):

        sort (str):

    """

    segment = proto.RepeatedField(proto.STRING, number=1)

    metric = proto.Field(proto.STRING, number=2)

    absolute = proto.Field(proto.BOOL, number=3)

    format_ = proto.Field(proto.STRING, number=4)

    sort = proto.Field(proto.STRING, number=5)


class GetTonnageDryDockResponse(proto.Message):
    r"""

    Attributes:
        drydock_values (Sequence[oceanbolt.com.drydock_v3.types.DryDockValue]):

        csv (str):

        xlsx (str):

    """

    drydock_values = proto.RepeatedField(proto.MESSAGE, number=1,
        message='DryDockValue',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class DryDockValue(proto.Message):
    r"""

    Attributes:
        date (str):

        value (google.protobuf.wrappers_pb2.DoubleValue):

        year (google.protobuf.wrappers_pb2.Int32Value):

        unified_date (str):

    """

    date = proto.Field(proto.STRING, number=1)

    value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )

    year = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.Int32Value,
    )

    unified_date = proto.Field(proto.STRING, number=4)


class DryDockSummaryRequest(proto.Message):
    r"""DryDockSummary

    Attributes:
        segment (Sequence[str]):

    """

    segment = proto.RepeatedField(proto.STRING, number=1)


class DryDockSummaryResponse(proto.Message):
    r"""

    Attributes:
        drydock_summary_values (Sequence[oceanbolt.com.drydock_v3.types.DryDockSummaryValue]):

    """

    drydock_summary_values = proto.RepeatedField(proto.MESSAGE, number=1,
        message='DryDockSummaryValue',
    )


class DryDockSummaryValue(proto.Message):
    r"""

    Attributes:
        month (str):

        segment (str):

        average_days_in_dock (google.protobuf.wrappers_pb2.Int32Value):

        completed_dock_stays (google.protobuf.wrappers_pb2.Int32Value):

    """

    month = proto.Field(proto.STRING, number=1)

    segment = proto.Field(proto.STRING, number=2)

    average_days_in_dock = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.Int32Value,
    )

    completed_dock_stays = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.Int32Value,
    )


class GetDryDockStaysRequest(proto.Message):
    r"""DryDockstays

    Attributes:
        imo (Sequence[int]):
            List of unique vessel identifiers (IMO numbers). This allows
            filtering to show data only for a subset of vessels.
            Example: [1234567,7654321].
        port_id (Sequence[int]):

        shipyard_id (Sequence[int]):

        unlocode (Sequence[str]):
            UNLOCODE of the port.
        segment (Sequence[str]):

        sub_segment (Sequence[str]):

        start_date (str):
            The UTC start date of the date filter
        end_date (str):
            The UTC end date of the date filter
        latest_only (bool):
            Flat to indiciate whether only the latest
            port call should be included on an IMO basis. If
            this is enabled, only the latest port call for
            each imo passing the filter will be returned.
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
        sort (str):
            Specifies whether results should be sorted in ascending or
            descing order. Allowed values: ["asc","desc"].
        group_by (str):
            Determines the grouping of the timeseries data. This
            parameter only applies to the **/drydock/timeseries**
            endpoint.
    """

    imo = proto.RepeatedField(proto.INT32, number=1)

    port_id = proto.RepeatedField(proto.INT32, number=2)

    shipyard_id = proto.RepeatedField(proto.INT32, number=3)

    unlocode = proto.RepeatedField(proto.STRING, number=6)

    segment = proto.RepeatedField(proto.STRING, number=10)

    sub_segment = proto.RepeatedField(proto.STRING, number=11)

    start_date = proto.Field(proto.STRING, number=8)

    end_date = proto.Field(proto.STRING, number=9)

    latest_only = proto.Field(proto.BOOL, number=5)

    format_ = proto.Field(proto.STRING, number=4)

    sort = proto.Field(proto.STRING, number=7)

    group_by = proto.Field(proto.STRING, number=12)


class GetDryDockStaysResponse(proto.Message):
    r"""

    Attributes:
        data (Sequence[oceanbolt.com.drydock_v3.types.ShipyardStay]):

        csv (str):

        xlsx (str):

        previous_token (str):

        next_token (str):

        max_results (int):

    """

    data = proto.RepeatedField(proto.MESSAGE, number=1,
        message='ShipyardStay',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)

    previous_token = proto.Field(proto.STRING, number=4)

    next_token = proto.Field(proto.STRING, number=5)

    max_results = proto.Field(proto.INT32, number=6)


class ShipyardStay(proto.Message):
    r"""

    Attributes:
        shipyard_stay_id (str):

        imo (int):

        mmsi (int):

        vessel_name (str):

        segment (str):

        subsegment (str):

        dwt (float):

        port_id (int):

        port_name (str):

        port_unlocode (str):

        country_code (str):

        region (str):

        shipyard_name (str):

        shipyard_id (int):

        arrived_at (str):

        departed_at (str):

        duration_days (google.protobuf.wrappers_pb2.DoubleValue):

    """

    shipyard_stay_id = proto.Field(proto.STRING, number=1)

    imo = proto.Field(proto.INT32, number=2)

    mmsi = proto.Field(proto.INT32, number=3)

    vessel_name = proto.Field(proto.STRING, number=4)

    segment = proto.Field(proto.STRING, number=5)

    subsegment = proto.Field(proto.STRING, number=6)

    dwt = proto.Field(proto.DOUBLE, number=7)

    port_id = proto.Field(proto.INT32, number=8)

    port_name = proto.Field(proto.STRING, number=9)

    port_unlocode = proto.Field(proto.STRING, number=10)

    country_code = proto.Field(proto.STRING, number=11)

    region = proto.Field(proto.STRING, number=12)

    shipyard_name = proto.Field(proto.STRING, number=13)

    shipyard_id = proto.Field(proto.INT32, number=14)

    arrived_at = proto.Field(proto.STRING, number=15)

    departed_at = proto.Field(proto.STRING, number=16)

    duration_days = proto.Field(proto.MESSAGE, number=18,
        message=wrappers.DoubleValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
