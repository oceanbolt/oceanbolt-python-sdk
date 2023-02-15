# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import wrappers_pb2  # type: ignore
from oceanbolt.com.ptypes.filters import vessel_filter_pb2  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.tradeflows.v3',
    manifest={
        'GetTradeLaneMetricsResponse',
        'TradeLaneMetric',
        'EmptyParams',
        'EmptyResponse',
        'TradeFlowDataRequest',
        'GetTradeFlowsResponse',
        'GetLocationVolumeResponse',
        'LocationVolume',
        'GetTradeFlowAggregationResponse',
        'AggregationGroup',
        'AggregationRow',
        'GetTradeFlowTimeseriesResponse',
        'TimeseriesGroup',
        'TimeseriesRow',
        'GeoPoint',
        'TradeFlow',
        'GetTradeFlowHistogramResponse',
        'HistogramGroup',
    },
)


class GetTradeLaneMetricsResponse(proto.Message):
    r"""

    Attributes:
        grouping_variable (str):

        number_of_groups (int):

        trade_lane_metrics (MutableSequence[oceanbolt.com.tradeflows_v3.types.TradeLaneMetric]):

    """

    grouping_variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    number_of_groups: int = proto.Field(
        proto.INT32,
        number=2,
    )
    trade_lane_metrics: MutableSequence['TradeLaneMetric'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='TradeLaneMetric',
    )


class TradeLaneMetric(proto.Message):
    r"""

    Attributes:
        group (str):

        avg_days_at_sea (float):

        avg_load_port_days_waiting (float):

        avg_load_port_days_berthed (float):

        avg_discharge_port_days_waiting (float):

        avg_discharge_port_days_berthed (float):

        avg_voyage_durations_days (float):

        avg_speed (float):

        avg_volume (float):

        avg_distance_nm (float):

        avg_distance_calculated_nm (float):

        median_days_at_sea (float):

        median_load_port_days_waiting (float):

        median_load_port_days_berthed (float):

        median_discharge_port_days_waiting (float):

        median_discharge_port_days_berthed (float):

        median_volume (float):

        median_distance_nm (float):

        number_of_voyages (int):

        sum_of_volume (float):

        unique_vessels (int):

        unique_load_ports (int):

        unique_discharge_ports (int):

    """

    group: str = proto.Field(
        proto.STRING,
        number=9,
    )
    avg_days_at_sea: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    avg_load_port_days_waiting: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    avg_load_port_days_berthed: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    avg_discharge_port_days_waiting: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )
    avg_discharge_port_days_berthed: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    avg_voyage_durations_days: float = proto.Field(
        proto.DOUBLE,
        number=17,
    )
    avg_speed: float = proto.Field(
        proto.DOUBLE,
        number=18,
    )
    avg_volume: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    avg_distance_nm: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    avg_distance_calculated_nm: float = proto.Field(
        proto.DOUBLE,
        number=19,
    )
    median_days_at_sea: float = proto.Field(
        proto.DOUBLE,
        number=16,
    )
    median_load_port_days_waiting: float = proto.Field(
        proto.DOUBLE,
        number=10,
    )
    median_load_port_days_berthed: float = proto.Field(
        proto.DOUBLE,
        number=11,
    )
    median_discharge_port_days_waiting: float = proto.Field(
        proto.DOUBLE,
        number=12,
    )
    median_discharge_port_days_berthed: float = proto.Field(
        proto.DOUBLE,
        number=13,
    )
    median_volume: float = proto.Field(
        proto.DOUBLE,
        number=14,
    )
    median_distance_nm: float = proto.Field(
        proto.DOUBLE,
        number=15,
    )
    number_of_voyages: int = proto.Field(
        proto.INT32,
        number=20,
    )
    sum_of_volume: float = proto.Field(
        proto.DOUBLE,
        number=21,
    )
    unique_vessels: int = proto.Field(
        proto.INT32,
        number=22,
    )
    unique_load_ports: int = proto.Field(
        proto.INT32,
        number=23,
    )
    unique_discharge_ports: int = proto.Field(
        proto.INT32,
        number=24,
    )


class EmptyParams(proto.Message):
    r"""
    """


class EmptyResponse(proto.Message):
    r"""
    """


class TradeFlowDataRequest(proto.Message):
    r"""Trade flow data requests object. This is shared between all
    trade flows queries

    Attributes:
        frequency (str):
            Frequency determines the granularity/period grouping of the
            timeseries. Allowed values are: **["daily", "weekly",
            "monthly","quarterly", "yearly"]**. Default value is
            "monthly". This parameter only applies to the
            **/tradeflows/timeseries** endpoint.
        commodity (MutableSequence[str]):
            List of commodities to get data for (get a list of all
            commodities from **/entities/commodities**).
        commodity_group (MutableSequence[str]):
            List of commodity groups to get data for (get a list of all
            commodity groups from **/entities/commodities**).
        flow_direction (str):
            This controls whether to group the date by export
            date/import date. Allowed values are \**["export","import"].
            Default value is "export". This parameter only applies to
            the **/tradeflows/timeseries** endpoint.
        imo (MutableSequence[int]):
            List of unique vessel identifiers (IMO numbers). This allows
            filtering to show data only for a subset of vessels.
            Example: [1234567,7654321].
        load_port_id (MutableSequence[int]):
            Oceanbolt database identifier of the load
            port.
        load_port_unlocode (MutableSequence[str]):
            List of five letter UNLOCODEs for load
            (export) ports to filter on.
        load_berth_id (MutableSequence[int]):
            Oceanbolt database identifier of the load
            berth/terminal.
        discharge_port_id (MutableSequence[int]):
            Oceanbolt database identifier of the
            discharge port.
        discharge_port_unlocode (MutableSequence[str]):
            List of five letter UNLOCODEs for discharge
            (import) ports to filter on.
        discharge_berth_id (MutableSequence[int]):
            Oceanbolt database identifier of the
            discharge berth/terminal.
        segment (MutableSequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
        load_country_code (MutableSequence[str]):
            List of two letter ISO country codes for
            loading (export) countries to filter on.
        discharge_country_code (MutableSequence[str]):
            List of two letter ISO country codes for
            discharge (import) countries to filter on.
        load_region (MutableSequence[str]):
            List of loading regions to filter on. Allowed values can be
            obtained from the **/entities/regions** endpoint.
        discharge_region (MutableSequence[str]):
            List of discharge regions to filter on. Allowed values can
            be obtained from the **/entities/regions** endpoint.
        status (MutableSequence[str]):

        exclude_intra_country (bool):
            Determines whether to include/exclude intra
            country voyages. Default is to include.
        exclude_unknown_destinations (bool):
            Determines whether to include/exclude voyages
            with unknown destination. Default is to include.
        exclude_missing_load_berth (bool):
            Determines whether to include/exclude voyages with that have
            a missing load_berth_id. Default is to include.
        exclude_missing_discharge_berth (bool):
            Determines whether to include/exclude voyages with that have
            a missing discharge_berth_id. Default is to include.
        next_token (str):
            The pagination token specifying which page of
            results to return in the response. If no token
            is provided, the default page is the first page.
        max_results (int):
            An optional limit for the number of resources
            returned in a single call.
        format_ (str):
            The return format of the data ["csv", "json", "xlsx"].
            Default is "json".
        group_by (str):
            Determines the grouping of the timeseries data. This
            parameter only applies to the **/tradeflows/timeseries**
            endpoint.
        pivot_by (str):
            Not implemented.
        tall_format (bool):
            Not implemented.
        metric (str):
            The metric to retrieve for timeseries aggregations. Allowed
            values:
            ["volume","count","ton_mile_calculated","ton_mile_actual","average_haul","average_speed",
            "volume_times_duration"]. Default is "volume".
        parceling (MutableSequence[str]):
            List of parceling statuses to retrieve. Allowed values are:
            ["include","exclude","only"].
        limit_groups (bool):
            Flag to indicate whether grouped timeseries
            should be limited to top N entries. If the
            parameter is present, the endpoint will only
            return the top N groups, and the remaining
            entries will be grouped into others.
        last_n_days (int):
            Short hand parameter for quickly getting data for the last N
            days. Cannot be supplied along either start_date or
            end_date.
        sort (str):
            Specifies whether results should be sorted in ascending or
            descending order. Allowed values: ["asc","desc"].
        dwt (MutableSequence[float]):
            DWT range to filter on. Example: [60000,90000] - this would
            filter only to only include dwt between 60k and 90k (both
            values inclusive).
        category (str):
            Specifies the base category for aggregation
            queries. This parameter only has effect on the
            GetTradeFlowAggregation method (REST endpoint:
            /tradeflows/aggregation).
        vessel_filter (oceanbolt.com.ptypes.filters.vessel_filter_pb2.VesselFilter):
            Specifies vessel parameters to filter on.
    """

    frequency: str = proto.Field(
        proto.STRING,
        number=1,
    )
    commodity: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    commodity_group: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=30,
    )
    flow_direction: str = proto.Field(
        proto.STRING,
        number=3,
    )
    imo: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=4,
    )
    load_port_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=19,
    )
    load_port_unlocode: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )
    load_berth_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=5,
    )
    discharge_port_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=20,
    )
    discharge_port_unlocode: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=29,
    )
    discharge_berth_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=18,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=27,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=7,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=8,
    )
    load_country_code: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    discharge_country_code: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    load_region: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    discharge_region: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    status: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=32,
    )
    exclude_intra_country: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    exclude_unknown_destinations: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    exclude_missing_load_berth: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    exclude_missing_discharge_berth: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    next_token: str = proto.Field(
        proto.STRING,
        number=15,
    )
    max_results: int = proto.Field(
        proto.INT32,
        number=16,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=17,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=21,
    )
    pivot_by: str = proto.Field(
        proto.STRING,
        number=34,
    )
    tall_format: bool = proto.Field(
        proto.BOOL,
        number=35,
    )
    metric: str = proto.Field(
        proto.STRING,
        number=22,
    )
    parceling: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=26,
    )
    limit_groups: bool = proto.Field(
        proto.BOOL,
        number=31,
    )
    last_n_days: int = proto.Field(
        proto.INT32,
        number=33,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=36,
    )
    dwt: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=37,
    )
    category: str = proto.Field(
        proto.STRING,
        number=38,
    )
    vessel_filter: vessel_filter_pb2.VesselFilter = proto.Field(
        proto.MESSAGE,
        number=39,
        message=vessel_filter_pb2.VesselFilter,
    )


class GetTradeFlowsResponse(proto.Message):
    r"""Response object for trade flow queries

    Attributes:
        data (MutableSequence[oceanbolt.com.tradeflows_v3.types.TradeFlow]):
            List of trade flows.
        next_token (str):
            Pagination token indicating the presence of
            additional further results.
        prev_token (str):
            Pagination token indicating the presence of
            additional previous results.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    data: MutableSequence['TradeFlow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='TradeFlow',
    )
    next_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    prev_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    csv: str = proto.Field(
        proto.STRING,
        number=8,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=9,
    )


class GetLocationVolumeResponse(proto.Message):
    r"""

    Attributes:
        data (MutableSequence[oceanbolt.com.tradeflows_v3.types.LocationVolume]):
            List of locations.
    """

    data: MutableSequence['LocationVolume'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='LocationVolume',
    )


class LocationVolume(proto.Message):
    r"""

    Attributes:
        location_name (str):
            Name of the location.
        location_id (str):
            Oceanbolt identifier of the location.
        location_type (str):
            Type of the location.
        country_code (str):
            ISO 2-letter country code.
        value (google.protobuf.wrappers_pb2.DoubleValue):
            Aggregated value for the location.
        coords (oceanbolt.com.tradeflows_v3.types.GeoPoint):
            Coordinates for the location.
    """

    location_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=6,
    )
    value: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.DoubleValue,
    )
    coords: 'GeoPoint' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='GeoPoint',
    )


class GetTradeFlowAggregationResponse(proto.Message):
    r"""

    Attributes:
        data (MutableSequence[oceanbolt.com.tradeflows_v3.types.AggregationGroup]):
            List of aggregation rows.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    data: MutableSequence['AggregationGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='AggregationGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=8,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=9,
    )


class AggregationGroup(proto.Message):
    r"""

    Attributes:
        group (str):
            Name of the aggregation group.
        rows (MutableSequence[oceanbolt.com.tradeflows_v3.types.AggregationRow]):
            List of categories within the group.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['AggregationRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='AggregationRow',
    )


class AggregationRow(proto.Message):
    r"""

    Attributes:
        category (str):
            Category name for the aggregation row.
        value (google.protobuf.wrappers_pb2.DoubleValue):
            Value of the aggregation row.
    """

    category: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.DoubleValue,
    )


class GetTradeFlowTimeseriesResponse(proto.Message):
    r"""Response object for trade flow timeseries queries

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tradeflows_v3.types.TimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries: MutableSequence['TimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='TimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=4,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=5,
    )


class TimeseriesGroup(proto.Message):
    r"""Trade flow timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        group_value (google.protobuf.wrappers_pb2.DoubleValue):
            Helper variable to calculate top groups. Not
            returned.
        rows (MutableSequence[oceanbolt.com.tradeflows_v3.types.TimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    group_value: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.DoubleValue,
    )
    rows: MutableSequence['TimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='TimeseriesRow',
    )


class TimeseriesRow(proto.Message):
    r"""Trade flow timeseries row

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        value (google.protobuf.wrappers_pb2.DoubleValue):
            The value of the timeseries row.
    """

    date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.DoubleValue,
    )


class GeoPoint(proto.Message):
    r"""

    Attributes:
        lat (float):
            Latitude.
        lon (float):
            Longitude.
    """

    lat: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    lon: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class TradeFlow(proto.Message):
    r"""Trade flow object

    Attributes:
        voyage_id (str):
            Unique ID for the voyage. This can be shared
            across multiple flows in the case of parceling
            voyages.
        flow_id (str):
            Unique ID for the trade flow. This will
            always be unique to the flow.
        imo (int):
            IMO number of the vessel.
        vessel_name (str):
            Name of the vessel.
        segment (str):
            Segment of the vessel.
        sub_segment (str):
            Sub segment of the vessel.
        dwt (float):
            DWT of the vessel.
        commodity (str):
            Name of the commodity.
        commodity_value (str):
            Database friendly name of the commodity.
        commodity_group (str):
            Name of the commodity group.
        volume (float):
            Volume loaded in metric tons.
        load_port_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the load
            port.
        load_port_name (str):
            Name of the load port.
        load_port_unlocode (str):
            UNLOCODE of the load port.
        load_berth_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the load
            berth/load terminal.
        load_berth_name (str):
            Name of the load berth/load terminal.
        load_country_code (str):
            ISO 2-letter country code of the load
            country.
        load_country (str):
            Name of the load country.
        load_region (str):
            Name of the load region.
        load_port_arrived_at (str):
            UTC timestamp for when the vessel arrived at
            the load port.
        load_port_berthed_at (str):
            UTC timestamp for when the vessel berthed in
            the load port.
        load_port_unberthed_at (str):
            UTC timestamp for when the vessel left the
            berth the load port.
        load_port_departed_at (str):
            UTC timestamp for when the vessel departed
            the load port.
        load_port_days_total (google.protobuf.wrappers_pb2.DoubleValue):
            Total duration of the load port call (in
            days).
        load_port_days_berthed (google.protobuf.wrappers_pb2.DoubleValue):
            Number of days the vessel was at berth in the
            load port.
        load_port_days_waiting (google.protobuf.wrappers_pb2.DoubleValue):
            Number of days the vessel was waiting at the
            load port before shifting to berth.
        discharge_port_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the load
            berth/load terminal.
        discharge_port_name (str):
            Name of the load port.
        discharge_port_unlocode (str):
            UNLOCODE of the load port.
        discharge_berth_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the load
            berth/load terminal.
        discharge_berth_name (str):
            Name of the load berth/load terminal.
        discharge_country_code (str):
            ISO 2-letter country code of the load
            country.
        discharge_country (str):
            Name of the load country.
        discharge_region (str):
            Name of the load region.
        discharge_port_arrived_at (str):
            UTC timestamp for when the vessel arrived at
            the discharge port.
        discharge_port_berthed_at (str):
            UTC timestamp for when the vessel berthed in
            the discharge port.
        discharge_port_unberthed_at (str):
            UTC timestamp for when the vessel left the
            berth the discharge port.
        discharge_port_departed_at (str):
            UTC timestamp for when the vessel departed
            the discharge port.
        discharge_port_days_total (google.protobuf.wrappers_pb2.DoubleValue):
            Total duration of the load port call (in
            days).
        discharge_port_days_berthed (google.protobuf.wrappers_pb2.DoubleValue):
            Number of days the vessel was at berth in the
            discharge port.
        discharge_port_days_waiting (google.protobuf.wrappers_pb2.DoubleValue):
            Number of days the vessel was waiting at the
            discharge port before shifting to berth.
        days_steaming (google.protobuf.wrappers_pb2.DoubleValue):
            Number of days the vessel was steaming (the
            time from when it left the discharge port until
            it arrived at the discharge port).
        days_total_duration (google.protobuf.wrappers_pb2.DoubleValue):
            Total duration of the voyage (in days).
        distance_calculated (google.protobuf.wrappers_pb2.DoubleValue):
            Calculated distance in nautical miles between
            load port and discharge port. Based on port
            distance tables.
        distance_actual (google.protobuf.wrappers_pb2.DoubleValue):
            Actual distance sailed in nautical miles
            between load port and discharge port. Based on
            AIS tracks.
        eta (str):
            Captain's Reported ETA.
        destination (str):
            Captain's Reported Destination.
        status (str):
            Status of the trade flow.
        parceling (bool):
            Flag indicating whether the trade flow was
            part of a parceling voyage or a single voyage.
        ballast_started_at (str):
            UTC timestamp for when the vessel started
            ballasting from the last discharge port.
        ballast_port_name (str):
            Name of the port where the vessel ballasted
            from.
        ballast_port_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier for the port
            where the vessel ballasted from.
        ballast_port_unlocode (str):

        ballast_country (str):
            Name of the ballast country.
        ballast_country_code (str):
            ISO 2-letter country code of the ballast
            country.
        ballast_region (str):
            Name of the ballast region.
    """

    voyage_id: str = proto.Field(
        proto.STRING,
        number=52,
    )
    flow_id: str = proto.Field(
        proto.STRING,
        number=51,
    )
    imo: int = proto.Field(
        proto.INT32,
        number=1,
    )
    vessel_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    segment: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sub_segment: str = proto.Field(
        proto.STRING,
        number=49,
    )
    dwt: float = proto.Field(
        proto.DOUBLE,
        number=37,
    )
    commodity: str = proto.Field(
        proto.STRING,
        number=4,
    )
    commodity_value: str = proto.Field(
        proto.STRING,
        number=5,
    )
    commodity_group: str = proto.Field(
        proto.STRING,
        number=6,
    )
    volume: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    load_port_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.Int32Value,
    )
    load_port_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    load_port_unlocode: str = proto.Field(
        proto.STRING,
        number=35,
    )
    load_berth_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=10,
        message=wrappers_pb2.Int32Value,
    )
    load_berth_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    load_country_code: str = proto.Field(
        proto.STRING,
        number=12,
    )
    load_country: str = proto.Field(
        proto.STRING,
        number=13,
    )
    load_region: str = proto.Field(
        proto.STRING,
        number=14,
    )
    load_port_arrived_at: str = proto.Field(
        proto.STRING,
        number=15,
    )
    load_port_berthed_at: str = proto.Field(
        proto.STRING,
        number=17,
    )
    load_port_unberthed_at: str = proto.Field(
        proto.STRING,
        number=31,
    )
    load_port_departed_at: str = proto.Field(
        proto.STRING,
        number=18,
    )
    load_port_days_total: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=46,
        message=wrappers_pb2.DoubleValue,
    )
    load_port_days_berthed: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=47,
        message=wrappers_pb2.DoubleValue,
    )
    load_port_days_waiting: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=48,
        message=wrappers_pb2.DoubleValue,
    )
    discharge_port_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=21,
        message=wrappers_pb2.Int32Value,
    )
    discharge_port_name: str = proto.Field(
        proto.STRING,
        number=22,
    )
    discharge_port_unlocode: str = proto.Field(
        proto.STRING,
        number=36,
    )
    discharge_berth_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=53,
        message=wrappers_pb2.Int32Value,
    )
    discharge_berth_name: str = proto.Field(
        proto.STRING,
        number=23,
    )
    discharge_country_code: str = proto.Field(
        proto.STRING,
        number=24,
    )
    discharge_country: str = proto.Field(
        proto.STRING,
        number=25,
    )
    discharge_region: str = proto.Field(
        proto.STRING,
        number=26,
    )
    discharge_port_arrived_at: str = proto.Field(
        proto.STRING,
        number=27,
    )
    discharge_port_berthed_at: str = proto.Field(
        proto.STRING,
        number=29,
    )
    discharge_port_unberthed_at: str = proto.Field(
        proto.STRING,
        number=32,
    )
    discharge_port_departed_at: str = proto.Field(
        proto.STRING,
        number=30,
    )
    discharge_port_days_total: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=40,
        message=wrappers_pb2.DoubleValue,
    )
    discharge_port_days_berthed: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=41,
        message=wrappers_pb2.DoubleValue,
    )
    discharge_port_days_waiting: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=42,
        message=wrappers_pb2.DoubleValue,
    )
    days_steaming: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=43,
        message=wrappers_pb2.DoubleValue,
    )
    days_total_duration: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=50,
        message=wrappers_pb2.DoubleValue,
    )
    distance_calculated: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=44,
        message=wrappers_pb2.DoubleValue,
    )
    distance_actual: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=45,
        message=wrappers_pb2.DoubleValue,
    )
    eta: str = proto.Field(
        proto.STRING,
        number=33,
    )
    destination: str = proto.Field(
        proto.STRING,
        number=34,
    )
    status: str = proto.Field(
        proto.STRING,
        number=38,
    )
    parceling: bool = proto.Field(
        proto.BOOL,
        number=39,
    )
    ballast_started_at: str = proto.Field(
        proto.STRING,
        number=54,
    )
    ballast_port_name: str = proto.Field(
        proto.STRING,
        number=55,
    )
    ballast_port_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=56,
        message=wrappers_pb2.Int32Value,
    )
    ballast_port_unlocode: str = proto.Field(
        proto.STRING,
        number=57,
    )
    ballast_country: str = proto.Field(
        proto.STRING,
        number=58,
    )
    ballast_country_code: str = proto.Field(
        proto.STRING,
        number=59,
    )
    ballast_region: str = proto.Field(
        proto.STRING,
        number=61,
    )


class GetTradeFlowHistogramResponse(proto.Message):
    r"""

    Attributes:
        grouping_variable (str):
            Name of the varible that results have been
            grouped by.
        number_of_groups (int):
            The number of groups returned.
        groups (MutableSequence[oceanbolt.com.tradeflows_v3.types.HistogramGroup]):
            List of histogram groups.
    """

    grouping_variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    number_of_groups: int = proto.Field(
        proto.INT32,
        number=3,
    )
    groups: MutableSequence['HistogramGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='HistogramGroup',
    )


class HistogramGroup(proto.Message):
    r"""

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        number_of_values (int):
            Number of observations within the group.
        values (MutableSequence[float]):
            Array of the observed values.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    number_of_values: int = proto.Field(
        proto.INT32,
        number=3,
    )
    values: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
