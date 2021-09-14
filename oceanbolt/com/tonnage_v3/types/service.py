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
        zone_id (Sequence[int]):
            List of zones ids to filter on.
            Allowed values can be obtained from the
            /entities/zones endpoint.
        segment (Sequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (Sequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        direction (Sequence[str]):
            The list of directions to get tonnage data for. The
            following directions are allowed:
            **["NNE","ENE","ESE","SSE","SSW","WSW","WNW","NNW"]**.
            Directions can also be obtained from the interactive
            direction selector found at app.oceanbolt.com.
        laden_status (Sequence[str]):
            The laden status to get tonnage data for. The following
            values are allowed: **["laden","ballast"]**.
        port_status (Sequence[str]):
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

    zone_id = proto.RepeatedField(proto.INT32, number=1)

    segment = proto.RepeatedField(proto.STRING, number=2)

    sub_segment = proto.RepeatedField(proto.STRING, number=7)

    direction = proto.RepeatedField(proto.STRING, number=3)

    laden_status = proto.RepeatedField(proto.STRING, number=4)

    port_status = proto.RepeatedField(proto.STRING, number=6)

    group_by = proto.Field(proto.STRING, number=13)

    exclude_mpv = proto.Field(proto.BOOL, number=8)

    start_date = proto.Field(proto.STRING, number=9)

    end_date = proto.Field(proto.STRING, number=10)

    last_n_days = proto.Field(proto.INT32, number=11)

    format_ = proto.Field(proto.STRING, number=5)

    sort = proto.Field(proto.STRING, number=12)


class GetTonnageZoneCountResponse(proto.Message):
    r"""Response object for tonnage zone counts

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='TonnageTimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class GetFleetSpeedResponse(proto.Message):
    r"""Response object for FleetSpeed

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='TonnageTimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class TonnageTimeseriesGroup(proto.Message):
    r"""Tonnage zone/fleet speed timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (Sequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesRow]):
            Rows of timeseries data.
    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
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

    date = proto.Field(proto.STRING, number=1)

    vessel_count = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.Int32Value,
    )

    vessel_dwt = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.DoubleValue,
    )

    avg_speed = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.DoubleValue,
    )


class GetGlobalTonnageStatusRequest(proto.Message):
    r"""GetGlobalTonnageStatus

    Attributes:
        direction (Sequence[str]):

        format_ (str):

        laden_status (Sequence[str]):

        period (int):

        segment (Sequence[str]):

        sub_segment (Sequence[str]):

        sort (str):

        start_date (str):

        end_date (str):

    """

    direction = proto.RepeatedField(proto.STRING, number=1)

    format_ = proto.Field(proto.STRING, number=2)

    laden_status = proto.RepeatedField(proto.STRING, number=3)

    period = proto.Field(proto.INT32, number=4)

    segment = proto.RepeatedField(proto.STRING, number=5)

    sub_segment = proto.RepeatedField(proto.STRING, number=7)

    sort = proto.Field(proto.STRING, number=6)

    start_date = proto.Field(proto.STRING, number=8)

    end_date = proto.Field(proto.STRING, number=9)


class GetGlobalTonnageStatusResponse(proto.Message):
    r"""

    Attributes:
        global_tonnage_zone_counts (Sequence[oceanbolt.com.tonnage_v3.types.GlobalTonnageZoneCount]):

        csv (str):

        xlsx (str):

    """

    global_tonnage_zone_counts = proto.RepeatedField(proto.MESSAGE, number=1,
        message='GlobalTonnageZoneCount',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


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

    date = proto.Field(proto.STRING, number=1)

    zone_id = proto.Field(proto.INT32, number=2)

    zone_name = proto.Field(proto.STRING, number=3)

    vessel_count = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.Int32Value,
    )

    vessel_dwt = proto.Field(proto.MESSAGE, number=5,
        message=wrappers.DoubleValue,
    )

    avg_speed = proto.Field(proto.MESSAGE, number=6,
        message=wrappers.DoubleValue,
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
        segment (Sequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (Sequence[str]):
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

    frequency = proto.Field(proto.STRING, number=1)

    segment = proto.RepeatedField(proto.STRING, number=2)

    sub_segment = proto.RepeatedField(proto.STRING, number=6)

    group_by = proto.Field(proto.STRING, number=3)

    metric = proto.Field(proto.STRING, number=4)

    format_ = proto.Field(proto.STRING, number=5)

    exclude_mpv = proto.Field(proto.BOOL, number=7)

    sort = proto.Field(proto.STRING, number=8)

    start_date = proto.Field(proto.STRING, number=9)

    end_date = proto.Field(proto.STRING, number=10)


class GetTonnageFleetStatusResponse(proto.Message):
    r"""Response object for GetTonnageFleetStatus

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.TimeseriesGroup]):
            Timeseries data groups.
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

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class GetTonnageFleetGrowthResponse(proto.Message):
    r"""Response object for GetTonnageFleetGrowth

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.FleetGrowthTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='FleetGrowthTimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class FleetGrowthTimeseriesGroup(proto.Message):
    r"""Fleet growth timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (Sequence[oceanbolt.com.tonnage_v3.types.FleetGrowthTimeseriesRow]):
            Rows of timeseries data.
    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
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

    date = proto.Field(proto.STRING, number=1)

    scrapped = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )

    delivered = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.DoubleValue,
    )

    net = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.DoubleValue,
    )


class TimeseriesGroup(proto.Message):
    r"""Generic tonnage timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (Sequence[oceanbolt.com.tonnage_v3.types.TimeseriesRow]):
            Rows of timeseries data.
    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
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

    date = proto.Field(proto.STRING, number=1)

    value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )


class TonnageChineseWatersRequest(proto.Message):
    r"""Request object for TonnageChineseWaters

    Attributes:
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
        segment (Sequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (Sequence[str]):
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

    start_date = proto.Field(proto.STRING, number=1)

    end_date = proto.Field(proto.STRING, number=2)

    segment = proto.RepeatedField(proto.STRING, number=3)

    sub_segment = proto.RepeatedField(proto.STRING, number=4)

    group_by = proto.Field(proto.STRING, number=5)

    sort = proto.Field(proto.STRING, number=6)

    format_ = proto.Field(proto.STRING, number=7)


class TonnageChineseWatersResponse(proto.Message):
    r"""Response object for TonnageChineseWaters

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='ChineseWatersTimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class ChineseWatersTimeseriesGroup(proto.Message):
    r"""

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (Sequence[oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesRow]):
            Rows of timeseries data.
    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
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

    date = proto.Field(proto.STRING, number=1)

    inside_chinese_waters_count = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.Int32Value,
    )

    inside_chinese_waters_dwt = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.DoubleValue,
    )

    outside_chinese_waters_count = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.Int32Value,
    )

    outside_chinese_waters_dwt = proto.Field(proto.MESSAGE, number=5,
        message=wrappers.DoubleValue,
    )


class GetTonnageZoneChangesRequest(proto.Message):
    r"""Request object for TonnageZoneChange

    Attributes:
        from_zone_id (Sequence[int]):

        to_zone_id (Sequence[int]):

        segment (Sequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (Sequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        laden_status (Sequence[str]):
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
    """

    from_zone_id = proto.RepeatedField(proto.INT32, number=1)

    to_zone_id = proto.RepeatedField(proto.INT32, number=2)

    segment = proto.RepeatedField(proto.STRING, number=3)

    sub_segment = proto.RepeatedField(proto.STRING, number=4)

    laden_status = proto.RepeatedField(proto.STRING, number=5)

    start_date = proto.Field(proto.STRING, number=6)

    end_date = proto.Field(proto.STRING, number=7)

    group_by = proto.Field(proto.STRING, number=8)

    sort = proto.Field(proto.STRING, number=9)

    format_ = proto.Field(proto.STRING, number=10)

    frequency = proto.Field(proto.STRING, number=11)


class GetTonnageZoneChangesResponse(proto.Message):
    r"""Response object for TonnageZoneChange

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.ZoneChangesTimeseriesGroup]):
            Timeseries data groups.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='ZoneChangesTimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class ZoneChangesTimeseriesGroup(proto.Message):
    r"""Tonnage zone/fleet speed timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (Sequence[oceanbolt.com.tonnage_v3.types.ZoneChangesTimeseriesRow]):
            Rows of timeseries data.
    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
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

    date = proto.Field(proto.STRING, number=1)

    vessel_count = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.Int32Value,
    )

    vessel_dwt = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.DoubleValue,
    )


class GetTonnageBasinRequest(proto.Message):
    r"""GetTonnageBasin

    Attributes:
        basin (Sequence[str]):

        segment (Sequence[str]):

        sub_segment (Sequence[str]):

        start_date (str):

        end_date (str):

        exclude_mpv (bool):

        last_n_days (int):

        format_ (str):

    """

    basin = proto.RepeatedField(proto.STRING, number=1)

    segment = proto.RepeatedField(proto.STRING, number=2)

    sub_segment = proto.RepeatedField(proto.STRING, number=3)

    start_date = proto.Field(proto.STRING, number=4)

    end_date = proto.Field(proto.STRING, number=5)

    exclude_mpv = proto.Field(proto.BOOL, number=6)

    last_n_days = proto.Field(proto.INT32, number=7)

    format_ = proto.Field(proto.STRING, number=8)


class GetTonnageBasinResponse(proto.Message):
    r"""

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup]):

        csv (str):

        xlsx (str):

    """

    timeseries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='TonnageTimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class TonnageBasinTimeseriesGroup(proto.Message):
    r"""Tonnage zone/fleet speed timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (Sequence[oceanbolt.com.tonnage_v3.types.TonnageBasinTimeseriesRow]):
            Rows of timeseries data.
    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
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

    date = proto.Field(proto.STRING, number=1)

    vessel_count = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.Int32Value,
    )

    vessel_dwt = proto.Field(proto.MESSAGE, number=3,
        message=wrappers.DoubleValue,
    )


class EmptyParams(proto.Message):
    r""""""


class EmptyResponse(proto.Message):
    r""""""


__all__ = tuple(sorted(__protobuf__.manifest))
