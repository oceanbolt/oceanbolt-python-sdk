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
    },
)


class GetPortCallsRequest(proto.Message):
    r"""Port calls data requests object. This is shared between all
    port calls queries

    Attributes:
        imo (Sequence[int]):
            List of unique vessel identifiers (IMO numbers). This allows
            filtering to show data only for a subset of vessels.
            Example: [1234567,7654321].
        port_id (Sequence[int]):
            List of Oceanbolt port ids to filter on.
        berth_id (Sequence[int]):
            List of Oceanbolt berth ids to filter on.
        unlocode (Sequence[str]):
            List of five letter UNLOCODEs of ports to
            filter on.
        country_code (Sequence[str]):
            List of two letter ISO country codes to
            filter on.
        region (Sequence[str]):
            List of regions to filter on. Allowed values can be obtained
            from the **/entities/regions** endpoint.
        basin (Sequence[str]):
            List of basins to filter on. Allowed values are:
            ["atlantic","indian_ocean","pacific_americas","pacific_asia"]
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
        segment (Sequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment
        sub_segment (Sequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment
        start_date (str):
            The UTC start date of the date filter
        end_date (str):
            The UTC end date of the date filter
        commodity (Sequence[str]):
            List of commodities to get data for (get a list of all
            commodities from **/entities/commodities**).
        commodity_group (Sequence[str]):
            List of commodity groups to get data for (get a list of all
            commodity groups from **/entities/commodities**).
        operation (Sequence[str]):
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
    """

    imo = proto.RepeatedField(proto.INT32, number=1)

    port_id = proto.RepeatedField(proto.INT32, number=2)

    berth_id = proto.RepeatedField(proto.INT32, number=3)

    unlocode = proto.RepeatedField(proto.STRING, number=7)

    country_code = proto.RepeatedField(proto.STRING, number=8)

    region = proto.RepeatedField(proto.STRING, number=9)

    basin = proto.RepeatedField(proto.STRING, number=10)

    latest_only = proto.Field(proto.BOOL, number=6)

    next_token = proto.Field(proto.STRING, number=15)

    max_results = proto.Field(proto.INT32, number=16)

    format_ = proto.Field(proto.STRING, number=5)

    segment = proto.RepeatedField(proto.STRING, number=11)

    sub_segment = proto.RepeatedField(proto.STRING, number=27)

    start_date = proto.Field(proto.STRING, number=12)

    end_date = proto.Field(proto.STRING, number=13)

    commodity = proto.RepeatedField(proto.STRING, number=17)

    commodity_group = proto.RepeatedField(proto.STRING, number=30)

    operation = proto.RepeatedField(proto.STRING, number=20)

    sort = proto.Field(proto.STRING, number=18)

    group_by = proto.Field(proto.STRING, number=19)

    frequency = proto.Field(proto.STRING, number=21)

    limit_groups = proto.Field(proto.BOOL, number=31)


class GetPortCallsResponse(proto.Message):
    r"""Response object for port call queries

    Attributes:
        previous_token (str):

        next_token (str):

        data (Sequence[oceanbolt.com.portcalls_v3.types.PortCall]):

        csv (str):

        xlsx (str):

    """

    previous_token = proto.Field(proto.STRING, number=2)

    next_token = proto.Field(proto.STRING, number=3)

    data = proto.RepeatedField(proto.MESSAGE, number=7,
        message='PortCall',
    )

    csv = proto.Field(proto.STRING, number=8)

    xlsx = proto.Field(proto.STRING, number=9)


class PortCall(proto.Message):
    r"""Port call object

    Attributes:
        voyage_id (str):

        port_call_id (str):

        imo (int):

        vessel_name (str):

        port_name (str):
            int32 port_id = 3;
        segment (str):

        sub_segment (str):

        unlocode (str):

        berth_name (str):

        anchorage_name (str):

        arrived_at (str):

        berthed_at (str):

        departed_at (str):

        days_in_port (float):

        days_waiting (float):

        days_at_berth (float):

        country_code (str):

        operation (str):

        voyage_type (str):

        commodity (str):

        commodity_value (str):

        commodity_group (str):

        volume (float):

        port_visited (bool):
            bool speed_below2_observed = 15;
    """

    voyage_id = proto.Field(proto.STRING, number=16)

    port_call_id = proto.Field(proto.STRING, number=15)

    imo = proto.Field(proto.INT32, number=1)

    vessel_name = proto.Field(proto.STRING, number=2)

    port_name = proto.Field(proto.STRING, number=4)

    segment = proto.Field(proto.STRING, number=18)

    sub_segment = proto.Field(proto.STRING, number=19)

    unlocode = proto.Field(proto.STRING, number=25)

    berth_name = proto.Field(proto.STRING, number=5)

    anchorage_name = proto.Field(proto.STRING, number=6)

    arrived_at = proto.Field(proto.STRING, number=7)

    berthed_at = proto.Field(proto.STRING, number=8)

    departed_at = proto.Field(proto.STRING, number=9)

    days_in_port = proto.Field(proto.DOUBLE, number=10)

    days_waiting = proto.Field(proto.DOUBLE, number=11)

    days_at_berth = proto.Field(proto.DOUBLE, number=12)

    country_code = proto.Field(proto.STRING, number=13)

    operation = proto.Field(proto.STRING, number=14)

    voyage_type = proto.Field(proto.STRING, number=17)

    commodity = proto.Field(proto.STRING, number=20)

    commodity_value = proto.Field(proto.STRING, number=21)

    commodity_group = proto.Field(proto.STRING, number=22)

    volume = proto.Field(proto.DOUBLE, number=23)

    port_visited = proto.Field(proto.BOOL, number=24)


class EmptyParams(proto.Message):
    r""""""


class EmptyResponse(proto.Message):
    r""""""


class GetPortParticularsRequest(proto.Message):
    r"""Particulars

    Attributes:
        start_date (str):

        end_date (str):

        port_id (int):

        berth_id (int):

        unlocode (str):

        last_n_days (int):

    """

    start_date = proto.Field(proto.STRING, number=1)

    end_date = proto.Field(proto.STRING, number=2)

    port_id = proto.Field(proto.INT32, number=3)

    berth_id = proto.Field(proto.INT32, number=4)

    unlocode = proto.Field(proto.STRING, number=5)

    last_n_days = proto.Field(proto.INT32, number=6)


class Statistic(proto.Message):
    r"""

    Attributes:
        min_ (float):

        max_ (float):

        percentile_10 (float):

        percentile_50 (float):

        percentile_90 (float):

        percentile_95 (float):

        percentile_99 (float):

        mean (float):

    """

    min_ = proto.Field(proto.DOUBLE, number=1)

    max_ = proto.Field(proto.DOUBLE, number=2)

    percentile_10 = proto.Field(proto.DOUBLE, number=3)

    percentile_50 = proto.Field(proto.DOUBLE, number=8)

    percentile_90 = proto.Field(proto.DOUBLE, number=10)

    percentile_95 = proto.Field(proto.DOUBLE, number=11)

    percentile_99 = proto.Field(proto.DOUBLE, number=13)

    mean = proto.Field(proto.DOUBLE, number=12)


class GetPortParticularsResponse(proto.Message):
    r"""

    Attributes:
        number_of_port_calls (int):

        loa (oceanbolt.com.portcalls_v3.types.Statistic):

        beam (oceanbolt.com.portcalls_v3.types.Statistic):

        max_draught (oceanbolt.com.portcalls_v3.types.Statistic):

        reported_draught (oceanbolt.com.portcalls_v3.types.Statistic):

        dwt (oceanbolt.com.portcalls_v3.types.Statistic):

        air_draught (oceanbolt.com.portcalls_v3.types.Statistic):

    """

    number_of_port_calls = proto.Field(proto.INT32, number=7)

    loa = proto.Field(proto.MESSAGE, number=1,
        message='Statistic',
    )

    beam = proto.Field(proto.MESSAGE, number=2,
        message='Statistic',
    )

    max_draught = proto.Field(proto.MESSAGE, number=3,
        message='Statistic',
    )

    reported_draught = proto.Field(proto.MESSAGE, number=4,
        message='Statistic',
    )

    dwt = proto.Field(proto.MESSAGE, number=5,
        message='Statistic',
    )

    air_draught = proto.Field(proto.MESSAGE, number=6,
        message='Statistic',
    )


class GetPortCallTimeseriesResponse(proto.Message):
    r"""Response object for port call timeseries queries

    Attributes:
        timeseries (Sequence[oceanbolt.com.portcalls_v3.types.TimeseriesGroup]):
            Timeseries data groups
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='TimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=4)

    xlsx = proto.Field(proto.STRING, number=5)


class TimeseriesGroup(proto.Message):
    r"""Port call timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        group_value (google.protobuf.wrappers_pb2.DoubleValue):
            Helper variable to calculate top groups. Not
            returned.
        rows (Sequence[oceanbolt.com.portcalls_v3.types.TimeseriesRow]):
            Rows of timeseries data
    """

    group = proto.Field(proto.STRING, number=1)

    group_value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )

    rows = proto.RepeatedField(proto.MESSAGE, number=3,
        message='TimeseriesRow',
    )


class TimeseriesRow(proto.Message):
    r"""Port call timeseries row

    Attributes:
        date (str):

        value (google.protobuf.wrappers_pb2.DoubleValue):

    """

    date = proto.Field(proto.STRING, number=1)

    value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
