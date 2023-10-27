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


__protobuf__ = proto.module(
    package='oceanbolt.com.entities.v3',
    manifest={
        'ListSegmentsRequest',
        'ListSegmentsResponse',
        'Segment',
        'ListPortsRequest',
        'ListPortsResponse',
        'Port',
        'ListZonesRequest',
        'ListTonnageZonesWithPolygonsResponse',
        'ZoneWithPolygon',
        'Zone',
        'ListTonnageZonesResponse',
        'ListRegionsRequest',
        'Region',
        'ListRegionsResponse',
        'RegionWithPolygon',
        'ListRegionsWithPolygonResponse',
        'ListCountriesRequest',
        'Country',
        'ListCountriesResponse',
        'ListCommoditiesRequest',
        'Commodity',
        'ListCommoditiesResponse',
        'SearchRequest',
        'SearchPolygonsResponse',
        'Polygon',
        'SearchVesselsResponse',
        'Vessel',
        'ListShipyardsRequest',
        'ListShipyardsResponse',
        'Shipyard',
    },
)


class ListSegmentsRequest(proto.Message):
    r"""ListSegments
    """


class ListSegmentsResponse(proto.Message):
    r"""

    Attributes:
        segments (MutableSequence[oceanbolt.com.entities_v3.types.Segment]):

    """

    segments: MutableSequence['Segment'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Segment',
    )


class Segment(proto.Message):
    r"""

    Attributes:
        segment (str):

        segment_key (str):

        sub_segment (str):

        segment_int (int):

        sub_segment_int (int):

        sub_segment_key (str):

        cutoff_low_dwt (float):

        cutoff_high_dwt (float):

        cutoff_low_cbm (float):

        cutoff_high_cbm (float):

        platform (str):

        highlevel_type (str):

    """

    segment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    segment_key: str = proto.Field(
        proto.STRING,
        number=6,
    )
    sub_segment: str = proto.Field(
        proto.STRING,
        number=2,
    )
    segment_int: int = proto.Field(
        proto.INT32,
        number=3,
    )
    sub_segment_int: int = proto.Field(
        proto.INT32,
        number=4,
    )
    sub_segment_key: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cutoff_low_dwt: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    cutoff_high_dwt: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    cutoff_low_cbm: float = proto.Field(
        proto.DOUBLE,
        number=11,
    )
    cutoff_high_cbm: float = proto.Field(
        proto.DOUBLE,
        number=12,
    )
    platform: str = proto.Field(
        proto.STRING,
        number=9,
    )
    highlevel_type: str = proto.Field(
        proto.STRING,
        number=10,
    )


class ListPortsRequest(proto.Message):
    r"""Response object for ListPorts
    """


class ListPortsResponse(proto.Message):
    r"""

    Attributes:
        ports (MutableSequence[oceanbolt.com.entities_v3.types.Port]):

    """

    ports: MutableSequence['Port'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Port',
    )


class Port(proto.Message):
    r"""Port entity in the Oceanbolt data model.

    Attributes:
        port_id (int):

        port_name (str):

        country_code (str):

        region (str):

        unlocode (str):

        unlocode_alias (MutableSequence[str]):

        port_name_alias (MutableSequence[str]):

        longitude (float):

        latitude (float):

    """

    port_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    port_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    region: str = proto.Field(
        proto.STRING,
        number=4,
    )
    unlocode: str = proto.Field(
        proto.STRING,
        number=5,
    )
    unlocode_alias: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    port_name_alias: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    longitude: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    latitude: float = proto.Field(
        proto.DOUBLE,
        number=9,
    )


class ListZonesRequest(proto.Message):
    r"""ListTonnageZonesWithPolygons
    """


class ListTonnageZonesWithPolygonsResponse(proto.Message):
    r"""

    Attributes:
        zones (MutableSequence[oceanbolt.com.entities_v3.types.ZoneWithPolygon]):

    """

    zones: MutableSequence['ZoneWithPolygon'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='ZoneWithPolygon',
    )


class ZoneWithPolygon(proto.Message):
    r"""

    Attributes:
        zone_id (int):

        zone_name (str):

        zone_basin (str):

        geom_polygon_wkt (str):

        geom_polygon_geojson (str):

        geom_coordinate_wkt (str):

        geom_coordinate_geojson (str):

    """

    zone_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    zone_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zone_basin: str = proto.Field(
        proto.STRING,
        number=3,
    )
    geom_polygon_wkt: str = proto.Field(
        proto.STRING,
        number=4,
    )
    geom_polygon_geojson: str = proto.Field(
        proto.STRING,
        number=5,
    )
    geom_coordinate_wkt: str = proto.Field(
        proto.STRING,
        number=6,
    )
    geom_coordinate_geojson: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Zone(proto.Message):
    r"""ListZones

    Attributes:
        zone_id (int):

        zone_name (str):

    """

    zone_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    zone_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTonnageZonesResponse(proto.Message):
    r"""

    Attributes:
        zones (MutableSequence[oceanbolt.com.entities_v3.types.Zone]):

    """

    zones: MutableSequence['Zone'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Zone',
    )


class ListRegionsRequest(proto.Message):
    r"""ListRegions
    """


class Region(proto.Message):
    r"""

    Attributes:
        region_id (str):

        region_name (str):

    """

    region_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListRegionsResponse(proto.Message):
    r"""

    Attributes:
        regions (MutableSequence[oceanbolt.com.entities_v3.types.Region]):

    """

    regions: MutableSequence['Region'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Region',
    )


class RegionWithPolygon(proto.Message):
    r"""ListRegionsWithPolygon

    Attributes:
        region_id (str):

        region_name (str):

        geojson (str):

    """

    region_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    geojson: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListRegionsWithPolygonResponse(proto.Message):
    r"""

    Attributes:
        regions (MutableSequence[oceanbolt.com.entities_v3.types.RegionWithPolygon]):

    """

    regions: MutableSequence['RegionWithPolygon'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='RegionWithPolygon',
    )


class ListCountriesRequest(proto.Message):
    r"""ListCountries
    """


class Country(proto.Message):
    r"""

    Attributes:
        country (str):

        country_code (str):

    """

    country: str = proto.Field(
        proto.STRING,
        number=1,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListCountriesResponse(proto.Message):
    r"""

    Attributes:
        countries (MutableSequence[oceanbolt.com.entities_v3.types.Country]):

    """

    countries: MutableSequence['Country'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Country',
    )


class ListCommoditiesRequest(proto.Message):
    r"""ListCommodities
    """


class Commodity(proto.Message):
    r"""

    Attributes:
        commodity (str):

        commodity_id (int):

        commodity_value (str):

        commodity_group (str):

        platform (str):

    """

    commodity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    commodity_id: int = proto.Field(
        proto.INT32,
        number=4,
    )
    commodity_value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    commodity_group: str = proto.Field(
        proto.STRING,
        number=3,
    )
    platform: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCommoditiesResponse(proto.Message):
    r"""

    Attributes:
        commodities (MutableSequence[oceanbolt.com.entities_v3.types.Commodity]):

    """

    commodities: MutableSequence['Commodity'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Commodity',
    )


class SearchRequest(proto.Message):
    r"""Search

    Attributes:
        q (str):

    """

    q: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchPolygonsResponse(proto.Message):
    r"""

    Attributes:
        polygons (MutableSequence[oceanbolt.com.entities_v3.types.Polygon]):

    """

    polygons: MutableSequence['Polygon'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Polygon',
    )


class Polygon(proto.Message):
    r"""

    Attributes:
        berth_id (int):

        port_id (int):

        port_name (str):

        berth_name (str):

        country_code (str):

        unlocode (str):

        entity_type (str):

        alias (str):
            string geom_point = 8; double mbc_radius = 9;
    """

    berth_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    port_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    port_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    berth_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    unlocode: str = proto.Field(
        proto.STRING,
        number=6,
    )
    entity_type: str = proto.Field(
        proto.STRING,
        number=7,
    )
    alias: str = proto.Field(
        proto.STRING,
        number=10,
    )


class SearchVesselsResponse(proto.Message):
    r"""

    Attributes:
        vessels (MutableSequence[oceanbolt.com.entities_v3.types.Vessel]):

    """

    vessels: MutableSequence['Vessel'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Vessel',
    )


class Vessel(proto.Message):
    r"""

    Attributes:
        imo (int):

        highlevel_type (str):

        segment (str):

        sub_segment (str):

        dwt (float):

        max_draught (float):

        name (str):

        ex_name (str):

        built (int):

        type_ (str):

        mpv (bool):

        loa (float):

        beam (float):

        holds_total (float):

    """

    imo: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    highlevel_type: str = proto.Field(
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
    max_draught: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    ex_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    built: int = proto.Field(
        proto.UINT32,
        number=9,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=10,
    )
    mpv: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    loa: float = proto.Field(
        proto.DOUBLE,
        number=12,
    )
    beam: float = proto.Field(
        proto.DOUBLE,
        number=13,
    )
    holds_total: float = proto.Field(
        proto.DOUBLE,
        number=14,
    )


class ListShipyardsRequest(proto.Message):
    r"""Request object for ListShipyards
    """


class ListShipyardsResponse(proto.Message):
    r"""Response object for ListShipyards

    Attributes:
        shipyards (MutableSequence[oceanbolt.com.entities_v3.types.Shipyard]):

    """

    shipyards: MutableSequence['Shipyard'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Shipyard',
    )


class Shipyard(proto.Message):
    r"""Shipyard entity in the Oceanbolt data model.

    Attributes:
        shipyard_id (int):

        shipyard_name (str):

        port_id (int):

    """

    shipyard_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    shipyard_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port_id: int = proto.Field(
        proto.INT32,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
