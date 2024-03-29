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
    package='oceanbolt.com.drydock.v3',
    manifest={
        'EmptyParams',
        'EmptyResponse',
        'GetDryDockStaysRequest',
        'GetDryDockStaysResponse',
        'HistoricalDryDockStay',
        'GetDryDockRequest',
        'DryDockTimeseriesGroup',
        'DryDockTimeseriesRow',
        'DryDockResponse',
        'DryDockSplitRow',
        'DryDockStay',
    },
)


class EmptyParams(proto.Message):
    r"""
    """


class EmptyResponse(proto.Message):
    r"""
    """


class GetDryDockStaysRequest(proto.Message):
    r"""DryDockstays

    Attributes:
        imo (MutableSequence[int]):
            List of unique vessel identifiers (IMO numbers). This allows
            filtering to show data only for a subset of vessels.
            Example: [1234567,7654321].
        port_id (MutableSequence[int]):
            This filters on the port where the vessel is
            currently in dry dock.
        shipyard_id (MutableSequence[int]):
            List of Oceanbolt shipyard ids to filter on.
        unlocode (MutableSequence[str]):
            UNLOCODE of the port.
        segment (MutableSequence[str]):
            List of vessel segments to filter on.
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on.
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

    imo: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    port_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=2,
    )
    shipyard_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=3,
    )
    unlocode: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=8,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=9,
    )
    latest_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=4,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=7,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=12,
    )


class GetDryDockStaysResponse(proto.Message):
    r"""

    Attributes:
        data (MutableSequence[oceanbolt.com.drydock_v3.types.HistoricalDryDockStay]):

        csv (str):

        xlsx (str):

        previous_token (str):

        next_token (str):

        max_results (int):

    """

    data: MutableSequence['HistoricalDryDockStay'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='HistoricalDryDockStay',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=2,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=3,
    )
    previous_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    next_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    max_results: int = proto.Field(
        proto.INT32,
        number=6,
    )


class HistoricalDryDockStay(proto.Message):
    r"""

    Attributes:
        shipyard_stay_id (str):
            Unique ID for the dry dock stay. This will
            always be unique to the port call.
        imo (int):
            IMO number of the vessel.
        mmsi (int):
            MMSI number of the vessel.
        vessel_name (str):
            Name of the vessel.
        segment (str):
            Segment of the vessel.
        subsegment (str):
            Sub segment of the vessel.
        dwt (float):
            DWT of the vessel
        port_id (int):
            Oceanbolt database identifier of the port.
        port_name (str):
            Name of the port.
        unlocode (str):
            UNLOCODE of the port.
        country_code (str):
            Country code of the port.
        region (str):
            Region of the port.
        shipyard_name (str):
            Name of the shipyard
        shipyard_id (int):
            Oceanbolt database identifier of the
            shipyard.
        arrived_at (str):
            UTC timestamp for when the vessel arrived at
            the port.
        departed_at (str):
            UTC timestamp for when the vessel left the
            port.
        duration_days (google.protobuf.wrappers_pb2.DoubleValue):
            Duration of the dry dock stay (in days).
    """

    shipyard_stay_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    imo: int = proto.Field(
        proto.INT32,
        number=2,
    )
    mmsi: int = proto.Field(
        proto.INT32,
        number=3,
    )
    vessel_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    segment: str = proto.Field(
        proto.STRING,
        number=5,
    )
    subsegment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    dwt: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    port_id: int = proto.Field(
        proto.INT32,
        number=8,
    )
    port_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    unlocode: str = proto.Field(
        proto.STRING,
        number=10,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=11,
    )
    region: str = proto.Field(
        proto.STRING,
        number=12,
    )
    shipyard_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    shipyard_id: int = proto.Field(
        proto.INT32,
        number=14,
    )
    arrived_at: str = proto.Field(
        proto.STRING,
        number=15,
    )
    departed_at: str = proto.Field(
        proto.STRING,
        number=16,
    )
    duration_days: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=18,
        message=wrappers_pb2.DoubleValue,
    )


class GetDryDockRequest(proto.Message):
    r"""DryDock request object.

    Attributes:
        port_id (MutableSequence[int]):
            List of Oceanbolt port ids to filter on.
            This filters on the port where the vessel is
            currently in dry dock.
        port_unlocode (MutableSequence[str]):
            List of five letter UNLOCODEs for to filter
            on.
        shipyard_id (MutableSequence[int]):
            List of Oceanbolt shipyard ids to filter on.
            This filters on the shipyard where the vessel is
            currently in dry dock.
        country_code (MutableSequence[str]):
            The list of 2-letter ISO countries to get
            congestion data for. This filters on the country
            where the vessel is currently congested. Country
            code can be obtained either from the
            /entities/countries endpoint.
        region_id (MutableSequence[str]):
            The list of region IDs to get dry dock data
            for. Region ID can be obtained either from the
            /entities/regions endpoint.
        segment (MutableSequence[str]):
            Cannot be supplied alongside subSegment
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment
        group_by (str):
            Determines the grouping of the timeseries data. This
            parameter only applies to the **/drydock/timeseries**
            endpoint.
        exclude (int):
            60 days will be excluded from the returned
            data.
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
        start_date (str):
            The UTC start date of the date filter
        end_date (str):
            The UTC end date of the date filter
        last_n_days (int):
            Short hand parameter for quickly getting data for the last N
            days. Cannot be supplied along either start_date or
            end_date.
        sort (str):
            Specifies whether results should be sorted in ascending or
            descing order. Allowed values: ["asc","desc"].
        display_date (str):
            Parameter used to display historical vessel
            lists for congested vessels. It is only
            applicable to the DryDockVessels method.
    """

    port_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    port_unlocode: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    shipyard_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=3,
    )
    country_code: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    region_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=8,
    )
    exclude: int = proto.Field(
        proto.INT32,
        number=9,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=10,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=11,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=12,
    )
    last_n_days: int = proto.Field(
        proto.INT32,
        number=13,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=14,
    )
    display_date: str = proto.Field(
        proto.STRING,
        number=15,
    )


class DryDockTimeseriesGroup(proto.Message):
    r"""DryDock timeseries group object.

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.drydock_v3.types.DryDockTimeseriesRow]):
            Rows of timeseries data
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['DryDockTimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='DryDockTimeseriesRow',
    )


class DryDockTimeseriesRow(proto.Message):
    r"""DryDock timeseries row object.

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row
        vessel_count (google.protobuf.wrappers_pb2.Int32Value):
            Number of vessels that were congested on the
            date
        vessel_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            Sum of DWT that were congested on the date
        avg_waiting_days (google.protobuf.wrappers_pb2.DoubleValue):
            Average waiting days of vessels that were
            congested on the date
        median_waiting_days (google.protobuf.wrappers_pb2.DoubleValue):
            Median waiting days of vessels that were
            congested on the date
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
    avg_waiting_days: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.DoubleValue,
    )
    median_waiting_days: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.DoubleValue,
    )


class DryDockResponse(proto.Message):
    r"""DryDock responseobject.

    Attributes:
        number_of_current_vessels (int):
            Number of vessels currently congested
        current_top_ports (MutableSequence[oceanbolt.com.drydock_v3.types.DryDockSplitRow]):
            List of top ports by amount of congested
        current_top_sub_segments (MutableSequence[oceanbolt.com.drydock_v3.types.DryDockSplitRow]):
            List of top segments by amount of congested
        current_top_countries (MutableSequence[oceanbolt.com.drydock_v3.types.DryDockSplitRow]):
            List of top countries by amount of congested
        current_top_shipyards (MutableSequence[oceanbolt.com.drydock_v3.types.DryDockSplitRow]):
            List of top countries by amount of congested
        timeseriesDefault (oceanbolt.com.drydock_v3.types.DryDockTimeseriesGroup):
            Ungrouped timeseries response.
        current_vessels (MutableSequence[oceanbolt.com.drydock_v3.types.DryDockStay]):
            List of vessels currently congested.
        timeseries (MutableSequence[oceanbolt.com.drydock_v3.types.DryDockTimeseriesGroup]):
            DryDock timeseries response.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    number_of_current_vessels: int = proto.Field(
        proto.INT32,
        number=1,
    )
    current_top_ports: MutableSequence['DryDockSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='DryDockSplitRow',
    )
    current_top_sub_segments: MutableSequence['DryDockSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='DryDockSplitRow',
    )
    current_top_countries: MutableSequence['DryDockSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='DryDockSplitRow',
    )
    current_top_shipyards: MutableSequence['DryDockSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message='DryDockSplitRow',
    )
    timeseriesDefault: 'DryDockTimeseriesGroup' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='DryDockTimeseriesGroup',
    )
    current_vessels: MutableSequence['DryDockStay'] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message='DryDockStay',
    )
    timeseries: MutableSequence['DryDockTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='DryDockTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=8,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=9,
    )


class DryDockSplitRow(proto.Message):
    r"""

    Attributes:
        item (str):

        count (google.protobuf.wrappers_pb2.Int32Value):

        dwt (google.protobuf.wrappers_pb2.DoubleValue):

        count_percent (google.protobuf.wrappers_pb2.DoubleValue):

        dwt_percent (google.protobuf.wrappers_pb2.DoubleValue):

    """

    item: str = proto.Field(
        proto.STRING,
        number=1,
    )
    count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )
    dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.DoubleValue,
    )
    count_percent: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.DoubleValue,
    )
    dwt_percent: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.DoubleValue,
    )


class DryDockStay(proto.Message):
    r"""

    Attributes:
        imo (int):
            IMO number of the vessel.
        vessel_name (str):
            Name of the vessel.
        segment (str):
            The vessel segment (handysize, supramax,
            panamax etc.).
        sub_segment (str):
            The vessel sub segment (large capesize,
            kamsarmax, vloc etc.).
        dwt (float):
            The DWT of the vessel.
        port_id (int):
            The Oceanbolt port id where the vessel is
            currently docked.
        port_name (str):
            The name of the port where the vessel is
            currently docked.
        shipyard_id (int):
            The Oceanbolt shipyard id where the vessel is
            currently docked.
        shipyard_name (str):
            The name of the shipyard where the vessel is
            currently docked.
        country_name (str):
            The name of the country where the vessel is
            currently docked.
        country_code (str):
            The 2-letter ISO code of the country where
            the vessel is currently docked.
        current_country_code (str):
            OLD FIELD - WILL BE DEPRECATED!!! (The
            2-letter ISO code of the country where the
            vessel is currently docked.)
        arrived_at (str):
            The UTC timestamp of when the vessel arrived
            at the current port.
        waiting_time_days (float):
            The duration in days that the vessel has been
            dry docked up until today.
        lat (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
        lng (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
        course (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
        speed (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
    """

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
        number=4,
    )
    dwt: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )
    port_id: int = proto.Field(
        proto.INT32,
        number=6,
    )
    port_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    shipyard_id: int = proto.Field(
        proto.INT32,
        number=11,
    )
    shipyard_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    country_name: str = proto.Field(
        proto.STRING,
        number=26,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=27,
    )
    current_country_code: str = proto.Field(
        proto.STRING,
        number=8,
    )
    arrived_at: str = proto.Field(
        proto.STRING,
        number=9,
    )
    waiting_time_days: float = proto.Field(
        proto.DOUBLE,
        number=10,
    )
    lat: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=22,
        message=wrappers_pb2.DoubleValue,
    )
    lng: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=23,
        message=wrappers_pb2.DoubleValue,
    )
    course: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=25,
        message=wrappers_pb2.DoubleValue,
    )
    speed: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=24,
        message=wrappers_pb2.DoubleValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
