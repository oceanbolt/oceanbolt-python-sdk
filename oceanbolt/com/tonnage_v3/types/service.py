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
    package='oceanbolt.com.tonnage.v3',
    manifest={
        'GetTonnageDataRequest',
        'GetTonnageZoneCountResponse',
        'GetFleetSpeedResponse',
        'TonnageTimeseriesGroup',
        'TonnageTimeseriesRow',
        'GetGlobalTonnageStatusRequest',
        'GetGlobalTonnageStatusResponse',
        'GlobalTonnageZoneCount',
        'GetTonnageFleetRequest',
        'GetTonnageFleetStatusResponse',
        'GetTonnageFleetGrowthResponse',
        'FleetGrowthTimeseriesGroup',
        'FleetGrowthTimeseriesRow',
        'TimeseriesGroup',
        'TimeseriesRow',
        'TonnageChineseWatersRequest',
        'TonnageChineseWatersResponse',
        'ChineseWatersTimeseriesGroup',
        'ChineseWatersTimeseriesRow',
        'GetTonnageZoneChangesRequest',
        'GetTonnageZoneChangesResponse',
        'ZoneChangesTimeseriesGroup',
        'ZoneChangesTimeseriesRow',
        'GetTonnageBasinRequest',
        'GetTonnageBasinResponse',
        'TonnageBasinTimeseriesGroup',
        'TonnageBasinTimeseriesRow',
        'EmptyParams',
        'EmptyResponse',
    },
)


class GetTonnageDataRequest(proto.Message):
    r"""Request object for getting tonnage zone data and fleet speed
    data.

    Attributes:
        zone_id (MutableSequence[int]):
            List of zones ids to filter on.
            Allowed values can be obtained from the
            /entities/zones endpoint.
        segment (MutableSequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        direction (MutableSequence[str]):
            The list of directions to get tonnage data for. The
            following directions are allowed:
            **["NNE","ENE","ESE","SSE","SSW","WSW","WNW","NNW"]**.
            Directions can also be obtained from the interactive
            direction selector found at app.oceanbolt.com.
        laden_status (MutableSequence[str]):
            The laden status to get tonnage data for. The following
            values are allowed: **["laden","ballast"]**.
        port_status (MutableSequence[str]):
            The port status to get tonnage data for. The following
            values are allowed: **["in_port","at_sea"]**.
        group_by (str):
            Not Implemented Yet //TODO
        exclude_mpv (bool):
            Flag to specify whether or not MPV vessels
            should be included/excluded. Default is to
            include.
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
        last_n_days (int):
            Short hand parameter for quickly getting data
            for the last N days.
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
        sort (str):
            Specifies whether results should be sorted in ascending or
            descing order. Allowed values: ["asc","desc"].
    """

    zone_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    direction: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    laden_status: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    port_status: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=13,
    )
    exclude_mpv: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=9,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=10,
    )
    last_n_days: int = proto.Field(
        proto.INT32,
        number=11,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=5,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=12,
    )


class GetTonnageZoneCountResponse(proto.Message):
    r"""Response object for tonnage zone counts

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries: MutableSequence['TonnageTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='TonnageTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetFleetSpeedResponse(proto.Message):
    r"""Response object for FleetSpeed

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries: MutableSequence['TonnageTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='TonnageTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TonnageTimeseriesGroup(proto.Message):
    r"""Tonnage zone/fleet speed timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['TonnageTimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='TonnageTimeseriesRow',
    )


class TonnageTimeseriesRow(proto.Message):
    r"""Tonnage zone/fleet speed timeseries row.

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        vessel_count (google.protobuf.wrappers_pb2.Int32Value):
            The number of vessels for the timeseries row.
        vessel_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            The sum of dwt for the timeseries row.
        avg_speed (google.protobuf.wrappers_pb2.DoubleValue):
            The average speed in knots for the timeseries
            row.
    """

    date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vessel_count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )
    vessel_dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.DoubleValue,
    )
    avg_speed: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.DoubleValue,
    )


class GetGlobalTonnageStatusRequest(proto.Message):
    r"""GetGlobalTonnageStatus

    Attributes:
        direction (MutableSequence[str]):

        format_ (str):

        laden_status (MutableSequence[str]):

        period (int):

        segment (MutableSequence[str]):

        sub_segment (MutableSequence[str]):

        sort (str):

        start_date (str):

        end_date (str):

    """

    direction: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    laden_status: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    period: int = proto.Field(
        proto.INT32,
        number=4,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=6,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=8,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=9,
    )


class GetGlobalTonnageStatusResponse(proto.Message):
    r"""

    Attributes:
        global_tonnage_zone_counts (MutableSequence[oceanbolt.com.tonnage_v3.types.GlobalTonnageZoneCount]):

        csv (str):

        xlsx (str):

    """

    global_tonnage_zone_counts: MutableSequence['GlobalTonnageZoneCount'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='GlobalTonnageZoneCount',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GlobalTonnageZoneCount(proto.Message):
    r"""

    Attributes:
        date (str):

        zone_id (int):

        zone_name (str):

        vessel_count (google.protobuf.wrappers_pb2.Int32Value):

        vessel_dwt (google.protobuf.wrappers_pb2.DoubleValue):

        avg_speed (google.protobuf.wrappers_pb2.DoubleValue):

    """

    date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone_id: int = proto.Field(
        proto.INT32,
        number=2,
    )
    zone_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vessel_count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int32Value,
    )
    vessel_dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.DoubleValue,
    )
    avg_speed: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.DoubleValue,
    )


class GetTonnageFleetRequest(proto.Message):
    r"""Request object for GetTonnageFleetStatus and
    GetTonnageFleetGrowth

    Attributes:
        frequency (str):
            Frequency determines the granularity/period grouping of the
            timeseries. Allowed values are: **["daily", "weekly",
            "monthly","quarterly "yearly"]**. Default value is
            "monthly".
        segment (MutableSequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        group_by (str):
            Determines the grouping of the timeseries
            data.
        metric (str):
            The metric to retrieve for timeseries aggregations. Allowed
            values: ["count","dwt"]. Default is "count".
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
        exclude_mpv (bool):
            Flag to specify whether or not MPV vessels
            should be included/excluded. Default is to
            include.
        sort (str):
            Specifies whether results should be sorted in ascending or
            descing order. Allowed values: ["asc","desc"].
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
    """

    frequency: str = proto.Field(
        proto.STRING,
        number=1,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    metric: str = proto.Field(
        proto.STRING,
        number=4,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=5,
    )
    exclude_mpv: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=8,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=9,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=10,
    )


class GetTonnageFleetStatusResponse(proto.Message):
    r"""Response object for GetTonnageFleetStatus

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tonnage_v3.types.TimeseriesGroup]):
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
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetTonnageFleetGrowthResponse(proto.Message):
    r"""Response object for GetTonnageFleetGrowth

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tonnage_v3.types.FleetGrowthTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries: MutableSequence['FleetGrowthTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='FleetGrowthTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class FleetGrowthTimeseriesGroup(proto.Message):
    r"""Fleet growth timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.tonnage_v3.types.FleetGrowthTimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['FleetGrowthTimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='FleetGrowthTimeseriesRow',
    )


class FleetGrowthTimeseriesRow(proto.Message):
    r"""Fleet growth timeseries row

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        scrapped (google.protobuf.wrappers_pb2.DoubleValue):
            Number of vessels (or sum of DWT) that was
            scrapped during this period.
        delivered (google.protobuf.wrappers_pb2.DoubleValue):
            Number of vessels (or sum of DWT) that was
            delivered during this period.
        net (google.protobuf.wrappers_pb2.DoubleValue):
            Net number of vessels (or sum of DWT) that
            was added to/removed from the fleet during this
            period.
    """

    date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scrapped: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.DoubleValue,
    )
    delivered: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.DoubleValue,
    )
    net: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.DoubleValue,
    )


class TimeseriesGroup(proto.Message):
    r"""Generic tonnage timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.tonnage_v3.types.TimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['TimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='TimeseriesRow',
    )


class TimeseriesRow(proto.Message):
    r"""Generic tonnage timeseries row

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        value (google.protobuf.wrappers_pb2.DoubleValue):
            Value of the timeseries row.
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


class TonnageChineseWatersRequest(proto.Message):
    r"""Request object for TonnageChineseWaters

    Attributes:
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
        segment (MutableSequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        group_by (str):
            Determines the grouping of the timeseries
            data.
        sort (str):
            Specifies whether results should be sorted in ascending or
            descing order. Allowed values: ["asc","desc"].
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
    """

    start_date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=2,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=6,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=7,
    )


class TonnageChineseWatersResponse(proto.Message):
    r"""Response object for TonnageChineseWaters

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries: MutableSequence['ChineseWatersTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='ChineseWatersTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ChineseWatersTimeseriesGroup(proto.Message):
    r"""

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['ChineseWatersTimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='ChineseWatersTimeseriesRow',
    )


class ChineseWatersTimeseriesRow(proto.Message):
    r"""

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        inside_chinese_waters_count (google.protobuf.wrappers_pb2.Int32Value):
            Number of Chinese flagged vessels inside
            Chinese waters.
        inside_chinese_waters_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            Sum of DWT of Chinese flagged vessels inside
            Chinese waters.
        outside_chinese_waters_count (google.protobuf.wrappers_pb2.Int32Value):
            Number of Chinese flagged vessels outside
            Chinese waters.
        outside_chinese_waters_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            Sum of DWT of Chinese flagged vessels outside
            Chinese waters.
    """

    date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inside_chinese_waters_count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )
    inside_chinese_waters_dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.DoubleValue,
    )
    outside_chinese_waters_count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int32Value,
    )
    outside_chinese_waters_dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.DoubleValue,
    )


class GetTonnageZoneChangesRequest(proto.Message):
    r"""Request object for TonnageZoneChange

    Attributes:
        from_zone_id (MutableSequence[int]):

        to_zone_id (MutableSequence[int]):

        segment (MutableSequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        laden_status (MutableSequence[str]):
            The laden status to get tonnage data for. The following
            values are allowed: **["laden","ballast"]**.
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
        group_by (str):
            Determines the grouping of the timeseries
            data.
        sort (str):
            Specifies whether results should be sorted in ascending or
            descing order. Allowed values: ["asc","desc"].
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
        frequency (str):
            Frequency determines the granularity/period grouping of the
            timeseries. Allowed values are: **["daily", "weekly",
            "monthly","quarterly "yearly"]**. Default value is
            "monthly".
        vessel_filter (oceanbolt.com.ptypes.filters.vessel_filter_pb2.VesselFilter):
            Specifies vessel parameters to filter on.
    """

    from_zone_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    to_zone_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=2,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    laden_status: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=6,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=7,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=8,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=9,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=10,
    )
    frequency: str = proto.Field(
        proto.STRING,
        number=11,
    )
    vessel_filter: vessel_filter_pb2.VesselFilter = proto.Field(
        proto.MESSAGE,
        number=12,
        message=vessel_filter_pb2.VesselFilter,
    )


class GetTonnageZoneChangesResponse(proto.Message):
    r"""Response object for TonnageZoneChange

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tonnage_v3.types.ZoneChangesTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries: MutableSequence['ZoneChangesTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='ZoneChangesTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ZoneChangesTimeseriesGroup(proto.Message):
    r"""Tonnage zone/fleet speed timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.tonnage_v3.types.ZoneChangesTimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['ZoneChangesTimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='ZoneChangesTimeseriesRow',
    )


class ZoneChangesTimeseriesRow(proto.Message):
    r"""Tonnage zone/fleet speed timeseries row.

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        vessel_count (google.protobuf.wrappers_pb2.Int32Value):
            The number of vessels for the timeseries row.
        vessel_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            The sum of dwt for the timeseries row.
    """

    date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vessel_count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )
    vessel_dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.DoubleValue,
    )


class GetTonnageBasinRequest(proto.Message):
    r"""GetTonnageBasin

    Attributes:
        basin (MutableSequence[str]):

        segment (MutableSequence[str]):

        sub_segment (MutableSequence[str]):

        start_date (str):

        end_date (str):

        exclude_mpv (bool):

        last_n_days (int):

        format_ (str):

    """

    basin: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=4,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=5,
    )
    exclude_mpv: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    last_n_days: int = proto.Field(
        proto.INT32,
        number=7,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GetTonnageBasinResponse(proto.Message):
    r"""

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup]):

        csv (str):

        xlsx (str):

    """

    timeseries: MutableSequence['TonnageTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='TonnageTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TonnageBasinTimeseriesGroup(proto.Message):
    r"""Tonnage zone/fleet speed timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.tonnage_v3.types.TonnageBasinTimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['TonnageBasinTimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='TonnageBasinTimeseriesRow',
    )


class TonnageBasinTimeseriesRow(proto.Message):
    r"""

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        vessel_count (google.protobuf.wrappers_pb2.Int32Value):
            The number of vessels for the timeseries row.
        vessel_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            The sum of dwt for the timeseries row.
    """

    date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vessel_count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )
    vessel_dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.DoubleValue,
    )


class EmptyParams(proto.Message):
    r"""Empty params
    """


class EmptyResponse(proto.Message):
    r"""Empty response
    """


__all__ = tuple(sorted(__protobuf__.manifest))
