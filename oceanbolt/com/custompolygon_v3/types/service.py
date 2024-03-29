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


__protobuf__ = proto.module(
    package='oceanbolt.com.custompolygon.v3',
    manifest={
        'CustomPolygonRequest',
        'CustomPolygonResponse',
        'TimeseriesGroup',
        'TimeseriesRow',
    },
)


class CustomPolygonRequest(proto.Message):
    r"""Request object for GetPolygonCounts

    Attributes:
        geojson (str):
            GeoJSON formatted string with polygon data
        laden_status (MutableSequence[str]):
            Laden status to filter on. Allowed values are ['laden',
            'ballast']
        segment (MutableSequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment
        start_date (str):
            The UTC start date of the date filter
        end_date (str):
            The UTC end date of the date filter
    """

    geojson: str = proto.Field(
        proto.STRING,
        number=1,
    )
    laden_status: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=4,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CustomPolygonResponse(proto.Message):
    r"""Response object for GetPolygonCounts

    Attributes:
        timeseries (MutableSequence[oceanbolt.com.custompolygon_v3.types.TimeseriesGroup]):
            Timeseries rows
    """

    timeseries: MutableSequence['TimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='TimeseriesGroup',
    )


class TimeseriesGroup(proto.Message):
    r"""Generic tonnage timeseries group

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.custompolygon_v3.types.TimeseriesRow]):
            Rows of timeseries data
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
            UTC date timestamp of the timeseries row
        value (google.protobuf.wrappers_pb2.DoubleValue):
            Value of the timeseries row
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


__all__ = tuple(sorted(__protobuf__.manifest))
