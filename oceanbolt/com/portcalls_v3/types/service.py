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

from google.protobuf import timestamp_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore
from oceanbolt.com.ptypes.filters import vessel_filter_pb2  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.portcalls.v3',
    manifest={
        'GetPortCallsRequest',
        'GetPortCallsResponse',
        'PortCall',
        'EmptyParams',
        'EmptyResponse',
        'GetPortParticularsRequest',
        'Statistic',
        'GetPortParticularsResponse',
        'GetPortCallTimeseriesResponse',
        'TimeseriesGroup',
        'TimeseriesRow',
        'GetVesselsInPortRequest',
        'GetVesselsInPortResponse',
        'VesselInPort',
        'BerthStay',
        'AnchorageStay',
    },
)


class GetPortCallsRequest(proto.Message):
    r"""Port calls data requests object. This is shared between all
    port calls queries

    Attributes:
        imo (MutableSequence[int]):
            List of unique vessel identifiers (IMO numbers). This allows
            filtering to show data only for a subset of vessels.
            Example: [1234567,7654321].
        port_id (MutableSequence[int]):
            List of Oceanbolt port ids to filter on.
        berth_id (MutableSequence[int]):
            List of Oceanbolt berth ids to filter on.
        unlocode (MutableSequence[str]):
            List of five letter UNLOCODEs of ports to
            filter on.
        country_code (MutableSequence[str]):
            List of two letter ISO country codes to
            filter on.
        region (MutableSequence[str]):
            List of regions to filter on. Allowed values can be obtained
            from the **/entities/regions** endpoint.
        basin (MutableSequence[str]):
            List of basins to filter on. Allowed values are:
            ["atlantic","indian_ocean","pacific_americas","pacific_asia"].
        latest_only (bool):
            Flat to indiciate whether only the latest
            port call should be included on an IMO basis. If
            this is enabled, only the latest port call for
            each imo passing the filter will be returned.
        next_token (str):
            The pagination token specifying which page of
            results to return in the response. If no token
            is provided, the default page is the first page.
        max_results (int):
            An optional limit for the number of resources
            returned in a single call.
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
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
        commodity (MutableSequence[str]):
            List of commodities to get data for (get a list of all
            commodities from **/entities/commodities**).
        commodity_group (MutableSequence[str]):
            List of commodity groups to get data for (get a list of all
            commodity groups from **/entities/commodities**).
        operation (MutableSequence[str]):
            List of port call operation types to filter on. Allowed
            values are: \**["D","Dx";"L","Lx","B","Y","U"].
        sort (str):
            Specifies whether results should be sorted in ascending or
            descing order. Allowed values: ["asc","desc"].
        group_by (str):
            Determines the grouping of the timeseries data. This
            parameter only applies to the **/portcalls/timeseries**
            endpoint.
        frequency (str):
            Frequency determines the granularity/period grouping of the
            timeseries. Allowed values are: **["daily", "weekly",
            "monthly","quarterly "yearly"]**. Default value is
            "monthly". This parameter only applies to the
            **/portcalls/timeseries** endpoint.
        limit_groups (bool):
            Flag to indicate whether grouped timeseries
            should be limited to top N entries. If the
            parameter is present, the endpoint will only
            return the top N groups, and the remaining
            entries will be grouped into others.
        dwt (MutableSequence[float]):
            DWT range to filter on. Example: [60000,90000] - this would
            filter only to only include dwt between 60k and 90k (both
            values inclusive).
        vessel_filter (oceanbolt.com.ptypes.filters.vessel_filter_pb2.VesselFilter):
            Specifies vessel parameters to filter on.
    """

    imo: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    port_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=2,
    )
    berth_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=3,
    )
    unlocode: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    country_code: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    region: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    basin: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    latest_only: bool = proto.Field(
        proto.BOOL,
        number=6,
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
        number=5,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=27,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=12,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=13,
    )
    commodity: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    commodity_group: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=30,
    )
    operation: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=20,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=18,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=19,
    )
    frequency: str = proto.Field(
        proto.STRING,
        number=21,
    )
    limit_groups: bool = proto.Field(
        proto.BOOL,
        number=31,
    )
    dwt: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=37,
    )
    vessel_filter: vessel_filter_pb2.VesselFilter = proto.Field(
        proto.MESSAGE,
        number=38,
        message=vessel_filter_pb2.VesselFilter,
    )


class GetPortCallsResponse(proto.Message):
    r"""Response object for port call queries

    Attributes:
        prev_token (str):
            Pagination token indicating the presence of
            additional previous results.
        next_token (str):
            Pagination token indicating the presence of
            additional further results.
        data (MutableSequence[oceanbolt.com.portcalls_v3.types.PortCall]):
            List of port calls.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    prev_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    next_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data: MutableSequence['PortCall'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='PortCall',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=8,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=9,
    )


class PortCall(proto.Message):
    r"""Port call object

    Attributes:
        voyage_id (str):
            Unique ID for the voyage. This can be shared
            across multiple port calls in the case of
            parceling voyages.
        port_call_id (str):
            Unique ID for the port call. This will always
            be unique to the port call.
        imo (int):
            IMO number of the vessel.
        vessel_name (str):
            Name of the vessel.
        port_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the port.
        port_name (str):
            Name of the port.
        segment (str):
            Segment of the vessel.
        sub_segment (str):
            Sub segment of the vessel.
        unlocode (str):
            UNLOCODE of the port.
        berth_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the primary
            berth/terminal visited during the port call.
        berth_name (str):
            Name of the primary berth/terminal visited
            during the port call.
        anchorage_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the
            anchorage.
        anchorage_name (str):
            Name of the anchorage.
        arrived_at (str):
            UTC timestamp for when the vessel arrived at
            the port.
        berthed_at (str):
            UTC timestamp for when the vessel berthed in
            the port.
        unberthed_at (str):
            UTC timestamp for when the vessel left the
            berth/terminal.
        departed_at (str):
            UTC timestamp for when the vessel left the
            port.
        days_in_port (google.protobuf.wrappers_pb2.DoubleValue):
            Total duration of the port call (in days).
        days_waiting (google.protobuf.wrappers_pb2.DoubleValue):
            Number of days the vessel was waiting at
            anchor before shifting to berth.
        days_at_berth (google.protobuf.wrappers_pb2.DoubleValue):
            Number of days the vessel was at berth in
            during the duration of the port call.
        country_code (str):
            ISO 2-letter country code of the load
            country.
        operation (str):
            Operation type of the port call.
        voyage_type (str):
            The type of the voyage.
        commodity (str):
            Name of the commodity.
        commodity_value (str):
            Database friendly name of the commodity.
        commodity_group (str):
            Name of the commodity group.
        volume (google.protobuf.wrappers_pb2.DoubleValue):
            Volume loaded in metric tons.
        port_visited (bool):
            Flag to indicate whether the vessel has
            visited the port interior. If the flag is false
            the vessels only visited an anchorage.
    """

    voyage_id: str = proto.Field(
        proto.STRING,
        number=16,
    )
    port_call_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    imo: int = proto.Field(
        proto.INT32,
        number=1,
    )
    vessel_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int32Value,
    )
    port_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    segment: str = proto.Field(
        proto.STRING,
        number=18,
    )
    sub_segment: str = proto.Field(
        proto.STRING,
        number=19,
    )
    unlocode: str = proto.Field(
        proto.STRING,
        number=25,
    )
    berth_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=27,
        message=wrappers_pb2.Int32Value,
    )
    berth_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    anchorage_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=28,
        message=wrappers_pb2.Int32Value,
    )
    anchorage_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    arrived_at: str = proto.Field(
        proto.STRING,
        number=7,
    )
    berthed_at: str = proto.Field(
        proto.STRING,
        number=8,
    )
    unberthed_at: str = proto.Field(
        proto.STRING,
        number=26,
    )
    departed_at: str = proto.Field(
        proto.STRING,
        number=9,
    )
    days_in_port: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=10,
        message=wrappers_pb2.DoubleValue,
    )
    days_waiting: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=11,
        message=wrappers_pb2.DoubleValue,
    )
    days_at_berth: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=12,
        message=wrappers_pb2.DoubleValue,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=13,
    )
    operation: str = proto.Field(
        proto.STRING,
        number=14,
    )
    voyage_type: str = proto.Field(
        proto.STRING,
        number=17,
    )
    commodity: str = proto.Field(
        proto.STRING,
        number=20,
    )
    commodity_value: str = proto.Field(
        proto.STRING,
        number=21,
    )
    commodity_group: str = proto.Field(
        proto.STRING,
        number=22,
    )
    volume: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=23,
        message=wrappers_pb2.DoubleValue,
    )
    port_visited: bool = proto.Field(
        proto.BOOL,
        number=24,
    )


class EmptyParams(proto.Message):
    r"""
    """


class EmptyResponse(proto.Message):
    r"""
    """


class GetPortParticularsRequest(proto.Message):
    r"""Request object for GetPortParticulars

    Attributes:
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
        port_id (int):
            Oceanbolt port identifier to filter on.
        berth_id (int):
            Oceanbolt berth identifier to filter on.
        unlocode (str):
            Unlocode port identifier to filter on.
        last_n_days (int):
            Alternative way of specifying date filter. If
            specified, then data will only be based on port
            calls in last X days.
    """

    start_date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port_id: int = proto.Field(
        proto.INT32,
        number=3,
    )
    berth_id: int = proto.Field(
        proto.INT32,
        number=4,
    )
    unlocode: str = proto.Field(
        proto.STRING,
        number=5,
    )
    last_n_days: int = proto.Field(
        proto.INT32,
        number=6,
    )


class Statistic(proto.Message):
    r"""

    Attributes:
        min_ (float):
            Minimum observed value.
        max_ (float):
            Maximum observed value.
        percentile_10 (float):
            10th percentile of observed values.
        percentile_50 (float):
            50th percentile of observed values (same as
            median).
        percentile_90 (float):
            90th percentile of observed values.
        percentile_95 (float):
            95th percentile of observed values.
        percentile_99 (float):
            99th percentile of observed values.
        mean (float):
            mean of observed values.
    """

    min_: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    max_: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    percentile_10: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    percentile_50: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    percentile_90: float = proto.Field(
        proto.DOUBLE,
        number=10,
    )
    percentile_95: float = proto.Field(
        proto.DOUBLE,
        number=11,
    )
    percentile_99: float = proto.Field(
        proto.DOUBLE,
        number=13,
    )
    mean: float = proto.Field(
        proto.DOUBLE,
        number=12,
    )


class GetPortParticularsResponse(proto.Message):
    r"""Response object for GetPortParticulars

    Attributes:
        number_of_port_calls (int):
            Number of port calls which forms the basis of
            the statistical aggregates.
        loa (oceanbolt.com.portcalls_v3.types.Statistic):
            Summary statistics for LOA.
        beam (oceanbolt.com.portcalls_v3.types.Statistic):
            Summary statistics for Beam.
        max_draught (oceanbolt.com.portcalls_v3.types.Statistic):
            Summary statistics for Maximum Design
            Draught.
        reported_draught (oceanbolt.com.portcalls_v3.types.Statistic):
            Summary statistics for Vessel Reported
            Draught.
        dwt (oceanbolt.com.portcalls_v3.types.Statistic):
            Summary statistics for DWT.
        air_draught (oceanbolt.com.portcalls_v3.types.Statistic):
            Summary statistics for Air Draught (if
            available).
    """

    number_of_port_calls: int = proto.Field(
        proto.INT32,
        number=7,
    )
    loa: 'Statistic' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Statistic',
    )
    beam: 'Statistic' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Statistic',
    )
    max_draught: 'Statistic' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Statistic',
    )
    reported_draught: 'Statistic' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='Statistic',
    )
    dwt: 'Statistic' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='Statistic',
    )
    air_draught: 'Statistic' = proto.Field(
        proto.MESSAGE,
        number=6,
        message='Statistic',
    )


class GetPortCallTimeseriesResponse(proto.Message):
    r"""Response object for port call timeseries queries

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.portcalls_v3.types.TimeseriesGroup]):
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
    r"""Port call timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        group_value (google.protobuf.wrappers_pb2.DoubleValue):
            Helper variable to calculate top groups. Not
            returned.
        rows (MutableSequence[oceanbolt.com.portcalls_v3.types.TimeseriesRow]):
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
    r"""Port call timeseries row

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


class GetVesselsInPortRequest(proto.Message):
    r"""Request object for GetVesselsInPort

    Attributes:
        port_id (int):
            Database id of the port to filter on
        unlocode (str):
            UNLOCODE of the port to filter on
        vessel_filter (oceanbolt.com.ptypes.filters.vessel_filter_pb2.VesselFilter):
            Specifies vessel parameters to filter on.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp to generate the vessel in port list
            for. This allows to generate historical
            snapshots of the vessels that were inside a port
            at a given time in history. If left blank, then
            it the vessel list will default to be generated
            for the current time.
        merge_sequential_polygon_stays (bool):
            Flag to indicate whether to merge sequential
            berth stays in same berth (if the stays are
            within the merge threshold). Default is false,
            meaning that by default berth stays will not be
            merged.
        merge_threshold_hours (float):
            The threshold in hours for a merge to take
            place for multiple consequtive stays. If the
            time from when the vessel left the berth until
            it reentered into the same berth is above the
            threshold, the polygon stays will not be merged.
            Default value is 6 hours.
    """

    port_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    unlocode: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vessel_filter: vessel_filter_pb2.VesselFilter = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vessel_filter_pb2.VesselFilter,
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    merge_sequential_polygon_stays: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    merge_threshold_hours: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )


class GetVesselsInPortResponse(proto.Message):
    r"""Response object for GetVesselsInPort

    Attributes:
        vessels_in_port (int):
            The number of vessels in port
        data (MutableSequence[oceanbolt.com.portcalls_v3.types.VesselInPort]):
            List of vessels in port at the requested
            time.
    """

    vessels_in_port: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    data: MutableSequence['VesselInPort'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='VesselInPort',
    )


class VesselInPort(proto.Message):
    r"""VesselInPort object

    Attributes:
        voyage_id (str):
            Unique ID for the voyage. This can be shared
            across multiple port calls in the case of
            parceling voyages.
        port_call_id (str):
            Unique ID for the port call. This will always
            be unique to the port call.
        imo (int):
            IMO number of the vessel.
        vessel_name (str):
            Name of the vessel.
        port_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the port.
        port_name (str):
            Name of the port.
        unlocode (str):
            UNLOCODE of the port.
        segment (str):
            Segment of the vessel.
        sub_segment (str):
            Sub segment of the vessel.
        dwt (float):
            DWT of the vessel
        berth_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the primary
            berth/terminal visited during the port call.
        berth_name (str):
            Name of the primary berth/terminal visited
            during the port call.
        anchorage_id (google.protobuf.wrappers_pb2.Int32Value):
            Oceanbolt database identifier of the
            anchorage.
        anchorage_name (str):
            Name of the anchorage.
        arrived_at (str):
            UTC timestamp for when the vessel arrived at
            the port.
        departed_at (str):
            UTC timestamp for when the vessel left the
            port (only applies for historical snapshot
            views), if blank, then the vessel is still
            inside the port.
        days_in_port (google.protobuf.wrappers_pb2.DoubleValue):
            Total duration of the port call (in days).
        country_code (str):
            ISO 2-letter country code of the load
            country.
        operation (str):
            Predicted operation type of the port call.
        voyage_type (str):
            Predicted the type of the voyage.
        commodity (str):
            Name of the predicted commodity.
        commodity_value (str):
            Database friendly name of the predicted
            commodity.
        commodity_group (str):
            Name of the predicted commodity group.
        volume (google.protobuf.wrappers_pb2.DoubleValue):
            Volume loaded in metric tons.
        port_visited (bool):
            Flag to indicate whether the vessel has
            visited the port interior. If the flag is false
            the vessels only visited an anchorage or a
            berth.
        berth_stays (MutableSequence[oceanbolt.com.portcalls_v3.types.BerthStay]):
            List of all berths that the vessel visited
            during the port call
        anchorage_stays (MutableSequence[oceanbolt.com.portcalls_v3.types.AnchorageStay]):
            List of all anchorages that the vessel
            visited during the port call
        vessel_status (str):
            Current Vessel status
    """

    voyage_id: str = proto.Field(
        proto.STRING,
        number=16,
    )
    port_call_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    imo: int = proto.Field(
        proto.INT32,
        number=1,
    )
    vessel_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int32Value,
    )
    port_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    unlocode: str = proto.Field(
        proto.STRING,
        number=25,
    )
    segment: str = proto.Field(
        proto.STRING,
        number=18,
    )
    sub_segment: str = proto.Field(
        proto.STRING,
        number=19,
    )
    dwt: float = proto.Field(
        proto.DOUBLE,
        number=26,
    )
    berth_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=27,
        message=wrappers_pb2.Int32Value,
    )
    berth_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    anchorage_id: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=28,
        message=wrappers_pb2.Int32Value,
    )
    anchorage_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    arrived_at: str = proto.Field(
        proto.STRING,
        number=7,
    )
    departed_at: str = proto.Field(
        proto.STRING,
        number=9,
    )
    days_in_port: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=10,
        message=wrappers_pb2.DoubleValue,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=13,
    )
    operation: str = proto.Field(
        proto.STRING,
        number=14,
    )
    voyage_type: str = proto.Field(
        proto.STRING,
        number=17,
    )
    commodity: str = proto.Field(
        proto.STRING,
        number=20,
    )
    commodity_value: str = proto.Field(
        proto.STRING,
        number=21,
    )
    commodity_group: str = proto.Field(
        proto.STRING,
        number=22,
    )
    volume: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=23,
        message=wrappers_pb2.DoubleValue,
    )
    port_visited: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    berth_stays: MutableSequence['BerthStay'] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message='BerthStay',
    )
    anchorage_stays: MutableSequence['AnchorageStay'] = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message='AnchorageStay',
    )
    vessel_status: str = proto.Field(
        proto.STRING,
        number=31,
    )


class BerthStay(proto.Message):
    r"""BerthStay object

    Attributes:
        berth_id (int):
            Berth id of the berth
        berth_name (str):
            Name of the berth
        berth_type (str):
            Type of the berth
        arrived_at (str):
            Timestamp of when the vessel arrived at the
            berth
        departed_at (str):
            Timestamp of when the vessel departed from
            the berth
        draught_in (float):
            The draught when the vessel arrived at the
            berth
        draught_out (float):
            The draught when the vessel departed from the
            berth
        hours_in_berth (float):
            The duration of the stay in the berth in
            hours.
    """

    berth_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    berth_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    berth_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    arrived_at: str = proto.Field(
        proto.STRING,
        number=4,
    )
    departed_at: str = proto.Field(
        proto.STRING,
        number=5,
    )
    draught_in: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    draught_out: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    hours_in_berth: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )


class AnchorageStay(proto.Message):
    r"""AnchorageStay object

    Attributes:
        anchorage_id (int):
            Anchorage id of the anchorage
        anchorage_name (str):
            Name of the anchorage
        arrived_at (str):
            Timestamp of when the vessel arrived at the
            anchorage
        departed_at (str):
            Timestamp of when the vessel departed from
            the anchorage
        hours_in_anchorage (float):
            The duration of the stay in the anchorage in
            hours.
    """

    anchorage_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    anchorage_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    arrived_at: str = proto.Field(
        proto.STRING,
        number=3,
    )
    departed_at: str = proto.Field(
        proto.STRING,
        number=4,
    )
    hours_in_anchorage: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
