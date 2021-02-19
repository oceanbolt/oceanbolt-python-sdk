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
        'GetTonnageFleetDevelopmentResponse',
        'FleetTimeseriesGroup',
        'FleetDevelopmentTimeseriesRow',
        'TimeseriesRow',
        'TonnageChineseWatersRequest',
        'TonnageChineseWatersResponse',
        'ChineseWatersTimeseriesGroup',
        'ChineseWatersTimeseriesRow',
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
            be supplied alongside segment
        direction (Sequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        laden_status (Sequence[str]):
            The list of directions to get tonnage data for. The
            following directions are allowed:
            **["NNE","ENE","ESE","SSE","SSW","WSW","WNW","NNW"]**.
            Directions can also be obtained from the interactive
            direction selector found at app.oceanbolt.com.
        port_status (Sequence[str]):
            The port status to get tonnage data for. The following
            values are allowed: **["in_port","at_sea"]**.
        group_by (str):

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
            Timeseries data groups
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


class TonnageTimeseriesGroup(proto.Message):
    r"""Tonnage zone timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (Sequence[oceanbolt.com.tonnage_v3.types.TonnageTimeseriesRow]):
            Rows of timeseries data
    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
        message='TonnageTimeseriesRow',
    )


class TonnageTimeseriesRow(proto.Message):
    r"""

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row
        vessel_count (google.protobuf.wrappers_pb2.Int32Value):
            The number of vessels for the timeseries row
        vessel_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            The sum of dwt for the timeseries row
        avg_speed (google.protobuf.wrappers_pb2.DoubleValue):
            The average speed in knots for the timeseries
            row
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

        sort (str):

    """

    direction = proto.RepeatedField(proto.STRING, number=1)

    format_ = proto.Field(proto.STRING, number=2)

    laden_status = proto.RepeatedField(proto.STRING, number=3)

    period = proto.Field(proto.INT32, number=4)

    segment = proto.RepeatedField(proto.STRING, number=5)

    sort = proto.Field(proto.STRING, number=6)


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

        year (google.protobuf.wrappers_pb2.Int32Value):

        unified_date (str):

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

    year = proto.Field(proto.MESSAGE, number=7,
        message=wrappers.Int32Value,
    )

    unified_date = proto.Field(proto.STRING, number=8)


class GetTonnageFleetRequest(proto.Message):
    r"""GetTonnageFleet

    Attributes:
        range_ (str):

        segment (Sequence[str]):

        sub_segment (Sequence[str]):

        group (str):

        metric (str):

        format_ (str):

        excludeMpv (bool):

        sort (str):

    """

    range_ = proto.Field(proto.STRING, number=1)

    segment = proto.RepeatedField(proto.STRING, number=2)

    sub_segment = proto.RepeatedField(proto.STRING, number=6)

    group = proto.Field(proto.STRING, number=3)

    metric = proto.Field(proto.STRING, number=4)

    format_ = proto.Field(proto.STRING, number=5)

    excludeMpv = proto.Field(proto.BOOL, number=7)

    sort = proto.Field(proto.STRING, number=8)


class GetTonnageFleetStatusResponse(proto.Message):
    r"""

    Attributes:
        data (Sequence[oceanbolt.com.tonnage_v3.types.TimeseriesRow]):

        csv (str):

        xlsx (str):

    """

    data = proto.RepeatedField(proto.MESSAGE, number=1,
        message='TimeseriesRow',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class GetTonnageFleetDevelopmentResponse(proto.Message):
    r"""

    Attributes:
        data (Sequence[oceanbolt.com.tonnage_v3.types.FleetTimeseriesGroup]):

        csv (str):

        xlsx (str):

    """

    data = proto.RepeatedField(proto.MESSAGE, number=1,
        message='FleetTimeseriesGroup',
    )

    csv = proto.Field(proto.STRING, number=2)

    xlsx = proto.Field(proto.STRING, number=3)


class FleetTimeseriesGroup(proto.Message):
    r"""

    Attributes:
        group (str):

        rows (Sequence[oceanbolt.com.tonnage_v3.types.FleetDevelopmentTimeseriesRow]):

    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
        message='FleetDevelopmentTimeseriesRow',
    )


class FleetDevelopmentTimeseriesRow(proto.Message):
    r"""

    Attributes:
        date (str):

        scrapped (google.protobuf.wrappers_pb2.DoubleValue):

        delivered (google.protobuf.wrappers_pb2.DoubleValue):

        net (google.protobuf.wrappers_pb2.DoubleValue):

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


class TimeseriesRow(proto.Message):
    r"""

    Attributes:
        date (str):

        value (google.protobuf.wrappers_pb2.DoubleValue):

        group (str):

    """

    date = proto.Field(proto.STRING, number=1)

    value = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )

    group = proto.Field(proto.STRING, number=3)


class TonnageChineseWatersRequest(proto.Message):
    r"""Tonnage Chinese Waters

    Attributes:
        start_date (str):

        end_date (str):

        segment (Sequence[str]):

        sub_segment (Sequence[str]):

        group_by (str):

        sort (str):

        format_ (str):

    """

    start_date = proto.Field(proto.STRING, number=1)

    end_date = proto.Field(proto.STRING, number=2)

    segment = proto.RepeatedField(proto.STRING, number=3)

    sub_segment = proto.RepeatedField(proto.STRING, number=4)

    group_by = proto.Field(proto.STRING, number=5)

    sort = proto.Field(proto.STRING, number=6)

    format_ = proto.Field(proto.STRING, number=7)


class TonnageChineseWatersResponse(proto.Message):
    r"""

    Attributes:
        timeseries (Sequence[oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesGroup]):

        csv (str):

        xlsx (str):

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

        rows (Sequence[oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesRow]):

    """

    group = proto.Field(proto.STRING, number=1)

    rows = proto.RepeatedField(proto.MESSAGE, number=2,
        message='ChineseWatersTimeseriesRow',
    )


class ChineseWatersTimeseriesRow(proto.Message):
    r"""

    Attributes:
        date (str):

        inside_chinese_waters_count (google.protobuf.wrappers_pb2.Int32Value):

        inside_chinese_waters_dwt (google.protobuf.wrappers_pb2.DoubleValue):

        outside_chinese_waters_count (google.protobuf.wrappers_pb2.Int32Value):

        outside_chinese_waters_dwt (google.protobuf.wrappers_pb2.DoubleValue):

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


class EmptyParams(proto.Message):
    r""""""


class EmptyResponse(proto.Message):
    r""""""


__all__ = tuple(sorted(__protobuf__.manifest))
