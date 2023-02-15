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
    package='oceanbolt.com.congestion.v3',
    manifest={
        'EmptyParams',
        'EmptyResponse',
        'GetCongestionRequest',
        'CongestionTimeseriesGroup',
        'CongestionTimeseriesRow',
        'CongestionResponse',
        'CongestionSplitRow',
        'CongestionStay',
    },
)


class EmptyParams(proto.Message):
    r"""
    """


class EmptyResponse(proto.Message):
    r"""
    """


class GetCongestionRequest(proto.Message):
    r"""Congestion request object.

    Attributes:
        port_id (MutableSequence[int]):
            List of Oceanbolt port ids to filter on.
            This filters on the port where the vessel is
            currently congested.
        port_unlocode (MutableSequence[str]):
            List of five letter UNLOCODEs for to filter
            on.
        country_code (MutableSequence[str]):
            The list of 2-letter ISO countries to get
            congestion data for. This filters on the country
            where the vessel is currently congested. Country
            code can be obtained either from the
            /entities/countries endpoint.
        region_id (MutableSequence[str]):
            The list of regionIds to get congestion data
            for. This filters on the region where the vessel
            is currently congested. Region Id can be
            obtained either from the /entities/regions
            endpoint.
        operation (MutableSequence[str]):
            List of port call operation types to filter on. Allowed
            values are: \**["load","discharge";"yard","unknown"].
        commodity (MutableSequence[str]):
            List of commodities to get data for (get a list of all
            commodities from **/entities/commodities**).
        commodity_group (MutableSequence[str]):
            List of commodity groups to get data for (get a list of all
            commodity groups from **/entities/commodities**).
        laden_status (MutableSequence[str]):
            Laden status to filter on. Allowed values are ['laden',
            'ballast'].
        imo (MutableSequence[int]):
            List of IMO numbers to include in the
            congestion data results.
        segment (MutableSequence[str]):
            List of vessel segments to filter on. Allowed values can be
            obtained from the **/entities/segments** endpoint. Cannot be
            supplied alongside subSegment.
        sub_segment (MutableSequence[str]):
            List of vessel sub segments to filter on. Allowed values can
            be obtained from the **/entities/segments** endpoint. Cannot
            be supplied alongside segment.
        group_by (str):
            Determines the grouping of the timeseries data. This
            parameter only applies to the **/portcalls/timeseries**
            endpoint.
        frequency (str):
            Not implemented.
        last_load_country_code (MutableSequence[str]):
            The list of 2-letter ISO countries to get
            congestion data for. This filters on the country
            where the vessel loaded its prior cargo. Country
            code can be obtained either from the
            /entities/countries endpoint.
        last_load_port_id (MutableSequence[int]):
            List of Oceanbolt port ids to filter on.
            This filters on the ports where the vessel
            loaded its prior cargo.
        exclude (int):
            Specifies whether to exclude congestion stays that have a
            longer duration than N (in days). For example if a value of
            ``exlude=60``'\` is specified then all congestion stays that
            lasted longer than 60 days will be excluded from the
            returned data.
        max_stay_length (int):
            Specifies whether to exclude congestion stays that have a
            longer duration than N (in days). For example if a value of
            ``max_stay_length=60``'\` is specified then all congestion
            stays that lasted longer than 60 days will be excluded from
            the returned data.
        include_vessels_currently_at_berth (bool):
            Flag to indicate whether vessels that are
            currently at berth should be included in
            congestion statistics.
        include_vessels_previously_berthed (bool):
            Flag to indicate whether vessels that have
            already visited a berth (but are not currently
            in a berth) as part of the current Port Call
            should be included in congestion statistics.
        format_ (str):
            The return format of the data ["csv","json", "xlsx"].
            Default is "json".
        start_date (str):
            The UTC start date of the date filter.
        end_date (str):
            The UTC end date of the date filter.
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
            applicable to the CongestionVessels method.
        dwt (MutableSequence[float]):
            DWT range to filter on. Example: [60000,90000] - this would
            filter only to only include dwt between 60k and 90k (both
            values inclusive).
        vessel_filter (oceanbolt.com.ptypes.filters.vessel_filter_pb2.VesselFilter):
            Specifies vessel parameters to filter on.
    """

    port_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    port_unlocode: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=18,
    )
    country_code: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    region_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    operation: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    commodity: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    commodity_group: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    laden_status: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=19,
    )
    imo: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=26,
    )
    segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    sub_segment: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=10,
    )
    frequency: str = proto.Field(
        proto.STRING,
        number=11,
    )
    last_load_country_code: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    last_load_port_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=13,
    )
    exclude: int = proto.Field(
        proto.INT32,
        number=14,
    )
    max_stay_length: int = proto.Field(
        proto.INT32,
        number=23,
    )
    include_vessels_currently_at_berth: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    include_vessels_previously_berthed: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=15,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=16,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=17,
    )
    last_n_days: int = proto.Field(
        proto.INT32,
        number=20,
    )
    sort: str = proto.Field(
        proto.STRING,
        number=21,
    )
    display_date: str = proto.Field(
        proto.STRING,
        number=22,
    )
    dwt: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=33,
    )
    vessel_filter: vessel_filter_pb2.VesselFilter = proto.Field(
        proto.MESSAGE,
        number=34,
        message=vessel_filter_pb2.VesselFilter,
    )


class CongestionTimeseriesGroup(proto.Message):
    r"""Congestion timeseries group object.

    Attributes:
        group (str):
            Name of the group. This will be "default", if
            no grouping was specified in the query.
        rows (MutableSequence[oceanbolt.com.congestion_v3.types.CongestionTimeseriesRow]):
            Rows of timeseries data.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rows: MutableSequence['CongestionTimeseriesRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='CongestionTimeseriesRow',
    )


class CongestionTimeseriesRow(proto.Message):
    r"""Congestion timeseries row object.

    Attributes:
        date (str):
            UTC date timestamp of the timeseries row.
        vessel_count (google.protobuf.wrappers_pb2.Int32Value):
            Number of vessels that were congested on the
            date.
        vessel_dwt (google.protobuf.wrappers_pb2.DoubleValue):
            Sum of DWT that were congested on the date.
        avg_waiting_days (google.protobuf.wrappers_pb2.DoubleValue):
            Average waiting days of vessels that were
            congested on the date.
        median_waiting_days (google.protobuf.wrappers_pb2.DoubleValue):
            Median waiting days of vessels that were
            congested on the date.
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


class CongestionResponse(proto.Message):
    r"""Congestion responseobject.

    Attributes:
        number_of_current_vessels (int):
            Number of vessels currently congested.
        current_top_ports (MutableSequence[oceanbolt.com.congestion_v3.types.CongestionSplitRow]):
            List of top ports by amount of congested.
        current_top_sub_segments (MutableSequence[oceanbolt.com.congestion_v3.types.CongestionSplitRow]):
            List of top segments by amount of congested.
        current_top_commodity_groups (MutableSequence[oceanbolt.com.congestion_v3.types.CongestionSplitRow]):
            List of top commodities by amount of
            congested.
        current_top_load_countries (MutableSequence[oceanbolt.com.congestion_v3.types.CongestionSplitRow]):
            List of top countries by amount of congested.
        timeseriesDefault (oceanbolt.com.congestion_v3.types.CongestionTimeseriesGroup):
            Ungrouped timeseries response.
        current_vessels (MutableSequence[oceanbolt.com.congestion_v3.types.CongestionStay]):
            List of vessels currently congested.
        timeseries (MutableSequence[oceanbolt.com.congestion_v3.types.CongestionTimeseriesGroup]):
            Congestion timeseries response.
        csv (str):
            Link to download csv file, if format was
            specified to be "csv".
        xlsx (str):
            Link to download excel file, if format was
            specified to be "xlsx".
    """

    number_of_current_vessels: int = proto.Field(
        proto.INT32,
        number=3,
    )
    current_top_ports: MutableSequence['CongestionSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='CongestionSplitRow',
    )
    current_top_sub_segments: MutableSequence['CongestionSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message='CongestionSplitRow',
    )
    current_top_commodity_groups: MutableSequence['CongestionSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message='CongestionSplitRow',
    )
    current_top_load_countries: MutableSequence['CongestionSplitRow'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='CongestionSplitRow',
    )
    timeseriesDefault: 'CongestionTimeseriesGroup' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='CongestionTimeseriesGroup',
    )
    current_vessels: MutableSequence['CongestionStay'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='CongestionStay',
    )
    timeseries: MutableSequence['CongestionTimeseriesGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='CongestionTimeseriesGroup',
    )
    csv: str = proto.Field(
        proto.STRING,
        number=8,
    )
    xlsx: str = proto.Field(
        proto.STRING,
        number=10,
    )


class CongestionSplitRow(proto.Message):
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
        number=4,
        message=wrappers_pb2.Int32Value,
    )
    dwt: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.DoubleValue,
    )
    count_percent: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.DoubleValue,
    )
    dwt_percent: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.DoubleValue,
    )


class CongestionStay(proto.Message):
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
        current_port_id (str):
            The Oceanbolt port id where the vessel is
            currently congested.
        current_port_name (str):
            The name of the port where the vessel is
            currently congested.
        current_country (str):
            The name of the country where the vessel is
            currently congested.
        current_country_code (str):
            The 2-letter ISO code of the country where
            the vessel is currently congested.
        arrived_at (str):
            The UTC timestamp of when the vessel arrived
            at the current port.
        waiting_time_days (float):
            The waiting time in days that the vessel has
            waiting up until today.
        last_load_country (str):
            The name of the country where the vessel
            loaded its prior cargo.
        last_load_country_code (str):
            The 2-letter ISO code of the country where
            the vessel loaded its prior cargo.
        last_load_port_name (str):
            The name of the port where the vessel loaded
            its prior cargo.
        last_load_berth_name (str):
            The name of the terminal where the vessel
            loaded its prior cargo.
        last_port_departed_at (str):
            The UTC timestamp of when the vessel departed
            its prior load port.
        last_load_port_id (int):
            The Oceanbolt port id of the port where the
            vessel loaded its prior cargo.
        commodity_group (str):
            Name of the commodity group.
        commodity (str):
            Name of the commodity.
        volume (float):
            Volume of the cargo onboard the vessel.
        lat (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
        lng (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
        course (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
        speed (google.protobuf.wrappers_pb2.DoubleValue):
            Not implemented.
        laden_status (str):
            Current laden status of the vessel (laden or
            ballast).
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
        number=6,
    )
    sub_segment: str = proto.Field(
        proto.STRING,
        number=7,
    )
    dwt: float = proto.Field(
        proto.DOUBLE,
        number=21,
    )
    current_port_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    current_port_name: str = proto.Field(
        proto.STRING,
        number=18,
    )
    current_country: str = proto.Field(
        proto.STRING,
        number=17,
    )
    current_country_code: str = proto.Field(
        proto.STRING,
        number=20,
    )
    arrived_at: str = proto.Field(
        proto.STRING,
        number=3,
    )
    waiting_time_days: float = proto.Field(
        proto.DOUBLE,
        number=10,
    )
    last_load_country: str = proto.Field(
        proto.STRING,
        number=8,
    )
    last_load_country_code: str = proto.Field(
        proto.STRING,
        number=15,
    )
    last_load_port_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    last_load_berth_name: str = proto.Field(
        proto.STRING,
        number=16,
    )
    last_port_departed_at: str = proto.Field(
        proto.STRING,
        number=14,
    )
    last_load_port_id: int = proto.Field(
        proto.INT32,
        number=9,
    )
    commodity_group: str = proto.Field(
        proto.STRING,
        number=4,
    )
    commodity: str = proto.Field(
        proto.STRING,
        number=5,
    )
    volume: float = proto.Field(
        proto.DOUBLE,
        number=19,
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
    laden_status: str = proto.Field(
        proto.STRING,
        number=26,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
