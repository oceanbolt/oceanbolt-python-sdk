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
    package='oceanbolt.com.tradeflows.v3',
    manifest={
        'TradeFlowDataRequest',
        'GetVoyagesResponse',
        'GetLocationVolumeResponse',
        'LocationVolume',
        'GetTradeFlowAggregationResponse',
        'AggregationGroup',
        'AggregationRow',
        'GetTradeFlowTimeseriesResponse',
        'TimeseriesGroup',
        'TimeseriesRow',
        'GeoPoint',
        'Voyage',
        'GetTradeFlowHistogramResponse',
        'HistogramGroup',
    },
)


class TradeFlowDataRequest(proto.Message):
    r"""TradeFlow Data Requests and Responses

    Attributes:
        frequency (str):

        commodity (Sequence[str]):

        commodityGroup (Sequence[str]):

        flow_direction (str):

        imo (Sequence[int]):

        load_port_id (Sequence[int]):

        load_port_unlocode (Sequence[str]):

        discharge_port_id (Sequence[int]):

        discharge_port_unlocode (Sequence[str]):

        load_berth_id (Sequence[int]):

        discharge_berth_id (Sequence[int]):

        segment (Sequence[str]):

        sub_segment (Sequence[str]):

        start_date (str):

        end_date (str):

        load_country_code (Sequence[str]):

        discharge_country_code (Sequence[str]):

        load_region (Sequence[str]):

        discharge_region (Sequence[str]):

        status (Sequence[str]):

        exclude_intra_country (bool):

        exclude_unknown_destinations (bool):

        exclude_missing_load_berth (bool):

        exclude_missing_discharge_berth (bool):

        next_token (str):

        max_results (int):

        format_ (str):

        group_by (str):

        pivot_by (str):

        tall_format (bool):

        metric (str):

        parceling (Sequence[str]):

        limit_groups (bool):

        last_n_days (int):

        sort (str):

    """

    frequency = proto.Field(proto.STRING, number=1)

    commodity = proto.RepeatedField(proto.STRING, number=2)

    commodityGroup = proto.RepeatedField(proto.STRING, number=30)

    flow_direction = proto.Field(proto.STRING, number=3)

    imo = proto.RepeatedField(proto.INT32, number=4)

    load_port_id = proto.RepeatedField(proto.INT32, number=19)

    load_port_unlocode = proto.RepeatedField(proto.STRING, number=28)

    discharge_port_id = proto.RepeatedField(proto.INT32, number=20)

    discharge_port_unlocode = proto.RepeatedField(proto.STRING, number=29)

    load_berth_id = proto.RepeatedField(proto.INT32, number=5)

    discharge_berth_id = proto.RepeatedField(proto.INT32, number=18)

    segment = proto.RepeatedField(proto.STRING, number=6)

    sub_segment = proto.RepeatedField(proto.STRING, number=27)

    start_date = proto.Field(proto.STRING, number=7)

    end_date = proto.Field(proto.STRING, number=8)

    load_country_code = proto.RepeatedField(proto.STRING, number=9)

    discharge_country_code = proto.RepeatedField(proto.STRING, number=10)

    load_region = proto.RepeatedField(proto.STRING, number=11)

    discharge_region = proto.RepeatedField(proto.STRING, number=12)

    status = proto.RepeatedField(proto.STRING, number=32)

    exclude_intra_country = proto.Field(proto.BOOL, number=13)

    exclude_unknown_destinations = proto.Field(proto.BOOL, number=14)

    exclude_missing_load_berth = proto.Field(proto.BOOL, number=24)

    exclude_missing_discharge_berth = proto.Field(proto.BOOL, number=25)

    next_token = proto.Field(proto.STRING, number=15)

    max_results = proto.Field(proto.INT32, number=16)

    format_ = proto.Field(proto.STRING, number=17)

    group_by = proto.Field(proto.STRING, number=21)

    pivot_by = proto.Field(proto.STRING, number=34)

    tall_format = proto.Field(proto.BOOL, number=35)

    metric = proto.Field(proto.STRING, number=22)

    parceling = proto.RepeatedField(proto.STRING, number=26)

    limit_groups = proto.Field(proto.BOOL, number=31)

    last_n_days = proto.Field(proto.INT32, number=33)

    sort = proto.Field(proto.STRING, number=36)


class GetVoyagesResponse(proto.Message):
    r"""

    Attributes:
        data (Sequence[oceanbolt.com.tradeflows_v3.types.Voyage]):

        next_token (str):

        prev_token (str):

        csv (str):

        xlsx (str):

    """

    data = proto.RepeatedField(proto.MESSAGE, number=7,
        message='Voyage',
    )

    next_token = proto.Field(proto.STRING, number=1)

    prev_token = proto.Field(proto.STRING, number=2)

    csv = proto.Field(proto.STRING, number=8)

    xlsx = proto.Field(proto.STRING, number=9)


class GetLocationVolumeResponse(proto.Message):
    r"""

    Attributes:
        data (Sequence[oceanbolt.com.tradeflows_v3.types.LocationVolume]):

    """

    data = proto.RepeatedField(proto.MESSAGE, number=1,
        message='LocationVolume',
    )


class LocationVolume(proto.Message):
    r"""

    Attributes:
        location_name (str):

        location_id (str):

        value (google.protobuf.wrappers_pb2.DoubleValue):

        coords (oceanbolt.com.tradeflows_v3.types.GeoPoint):

    """

    location_name = proto.Field(proto.STRING, number=1)

    location_id = proto.Field(proto.STRING, number=2)

    value = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.DoubleValue,
    )

    coords = proto.Field(proto.MESSAGE, number=4,
        message='GeoPoint',
    )


class GetTradeFlowAggregationResponse(proto.Message):
    r"""

    Attributes:
        data (Sequence[oceanbolt.com.tradeflows_v3.types.AggregationGroup]):

        file_url (str):

    """

    data = proto.RepeatedField(proto.MESSAGE, number=1,
        message='AggregationGroup',
    )

    file_url = proto.Field(proto.STRING, number=2)


class AggregationGroup(proto.Message):
    r"""

    Attributes:
        group (str):

        rows (Sequence[oceanbolt.com.tradeflows_v3.types.AggregationRow]):

    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
        message='AggregationRow',
    )


class AggregationRow(proto.Message):
    r"""

    Attributes:
        category (str):

        value (google.protobuf.wrappers_pb2.DoubleValue):

    """

    category = proto.Field(proto.STRING, number=1)

    value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )


class GetTradeFlowTimeseriesResponse(proto.Message):
    r"""

    Attributes:
        timeseries (Sequence[oceanbolt.com.tradeflows_v3.types.TimeseriesGroup]):

        csv (str):

        xlsx (str):

    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='TimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=4)

    xlsx = proto.Field(proto.STRING, number=5)


class TimeseriesGroup(proto.Message):
    r"""

    Attributes:
        group (str):

        group_value (google.protobuf.wrappers_pb2.DoubleValue):

        rows (Sequence[oceanbolt.com.tradeflows_v3.types.TimeseriesRow]):

    """

    group = proto.Field(proto.STRING, number=1)

    group_value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )

    rows = proto.RepeatedField(proto.MESSAGE, number=3,
        message='TimeseriesRow',
    )


class TimeseriesRow(proto.Message):
    r"""

    Attributes:
        date (str):

        value (google.protobuf.wrappers_pb2.DoubleValue):

    """

    date = proto.Field(proto.STRING, number=1)

    value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )


class GeoPoint(proto.Message):
    r"""

    Attributes:
        lat (float):

        lon (float):

    """

    lat = proto.Field(proto.DOUBLE, number=1)

    lon = proto.Field(proto.DOUBLE, number=2)


class Voyage(proto.Message):
    r"""

    Attributes:
        voyage_id (str):

        flow_id (str):

        imo (int):

        vessel_name (str):

        segment (str):

        sub_segment (str):

        dwt (float):

        commodity (str):

        commodity_value (str):

        commodity_group (str):

        volume (float):

        load_port_id (int):

        load_port_name (str):

        load_port_unlocode (str):

        load_berth_id (int):

        load_berth_name (str):

        load_country_code (str):

        load_country (str):

        load_region (str):

        load_port_arrived_at (str):

        load_port_berthed_at (str):

        load_port_departed_at (str):

        load_port_days_total (float):

        load_port_days_berthed (float):

        load_port_days_waiting (float):

        discharge_port_id (int):

        discharge_port_name (str):

        discharge_port_unlocode (str):

        discharge_berth_name (str):

        discharge_country_code (str):

        discharge_country (str):

        discharge_region (str):

        discharge_port_arrived_at (str):

        discharge_port_berthed_at (str):

        discharge_port_departed_at (str):

        discharge_port_days_total (float):

        discharge_port_days_berthed (float):

        discharge_port_days_waiting (float):

        days_steaming (float):

        days_total_duration (float):

        distance_calculated (float):

        distance_actual (float):

        eta (str):

        destination (str):

        status (str):

        parceling (bool):

    """

    voyage_id = proto.Field(proto.STRING, number=52)

    flow_id = proto.Field(proto.STRING, number=51)

    imo = proto.Field(proto.INT32, number=1)

    vessel_name = proto.Field(proto.STRING, number=2)

    segment = proto.Field(proto.STRING, number=3)

    sub_segment = proto.Field(proto.STRING, number=49)

    dwt = proto.Field(proto.DOUBLE, number=37)

    commodity = proto.Field(proto.STRING, number=4)

    commodity_value = proto.Field(proto.STRING, number=5)

    commodity_group = proto.Field(proto.STRING, number=6)

    volume = proto.Field(proto.DOUBLE, number=7)

    load_port_id = proto.Field(proto.INT32, number=8)

    load_port_name = proto.Field(proto.STRING, number=9)

    load_port_unlocode = proto.Field(proto.STRING, number=35)

    load_berth_id = proto.Field(proto.INT32, number=10)

    load_berth_name = proto.Field(proto.STRING, number=11)

    load_country_code = proto.Field(proto.STRING, number=12)

    load_country = proto.Field(proto.STRING, number=13)

    load_region = proto.Field(proto.STRING, number=14)

    load_port_arrived_at = proto.Field(proto.STRING, number=15)

    load_port_berthed_at = proto.Field(proto.STRING, number=17)

    load_port_departed_at = proto.Field(proto.STRING, number=18)

    load_port_days_total = proto.Field(proto.DOUBLE, number=46)

    load_port_days_berthed = proto.Field(proto.DOUBLE, number=47)

    load_port_days_waiting = proto.Field(proto.DOUBLE, number=48)

    discharge_port_id = proto.Field(proto.INT32, number=21)

    discharge_port_name = proto.Field(proto.STRING, number=22)

    discharge_port_unlocode = proto.Field(proto.STRING, number=36)

    discharge_berth_name = proto.Field(proto.STRING, number=23)

    discharge_country_code = proto.Field(proto.STRING, number=24)

    discharge_country = proto.Field(proto.STRING, number=25)

    discharge_region = proto.Field(proto.STRING, number=26)

    discharge_port_arrived_at = proto.Field(proto.STRING, number=27)

    discharge_port_berthed_at = proto.Field(proto.STRING, number=29)

    discharge_port_departed_at = proto.Field(proto.STRING, number=30)

    discharge_port_days_total = proto.Field(proto.DOUBLE, number=40)

    discharge_port_days_berthed = proto.Field(proto.DOUBLE, number=41)

    discharge_port_days_waiting = proto.Field(proto.DOUBLE, number=42)

    days_steaming = proto.Field(proto.DOUBLE, number=43)

    days_total_duration = proto.Field(proto.DOUBLE, number=50)

    distance_calculated = proto.Field(proto.DOUBLE, number=44)

    distance_actual = proto.Field(proto.DOUBLE, number=45)

    eta = proto.Field(proto.STRING, number=33)

    destination = proto.Field(proto.STRING, number=34)

    status = proto.Field(proto.STRING, number=38)

    parceling = proto.Field(proto.BOOL, number=39)


class GetTradeFlowHistogramResponse(proto.Message):
    r"""

    Attributes:
        grouping_variable (str):

        number_of_groups (int):

        groups (Sequence[oceanbolt.com.tradeflows_v3.types.HistogramGroup]):

    """

    grouping_variable = proto.Field(proto.STRING, number=1)

    number_of_groups = proto.Field(proto.INT32, number=3)

    groups = proto.RepeatedField(proto.MESSAGE, number=2,
        message='HistogramGroup',
    )


class HistogramGroup(proto.Message):
    r"""

    Attributes:
        group (str):

        number_of_values (int):

        values (Sequence[float]):

    """

    group = proto.Field(proto.STRING, number=1)

    number_of_values = proto.Field(proto.INT32, number=3)

    values = proto.RepeatedField(proto.DOUBLE, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))
