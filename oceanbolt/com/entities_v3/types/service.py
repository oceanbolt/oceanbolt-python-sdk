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


__protobuf__ = proto.module(
    package='oceanbolt.com.entities.v3',
    manifest={
        'EmptyParams',
        'ListSegmentsResponse',
        'Segment',
        'ListPortsResponse',
        'Port',
        'ZoneWithPolygon',
        'ListTonnageZonesWithPolygonsResponse',
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
        'Commodity',
        'ListCommoditiesResponse',
        'SearchRequest',
        'SearchPolygonsResponse',
        'Polygon',
        'SearchVesselsResponse',
        'Vessel',
    },
)


class EmptyParams(proto.Message):
    r""""""


class ListSegmentsResponse(proto.Message):
    r"""ListSegments

    Attributes:
        segments (Sequence[oceanbolt.com.entities_v3.types.Segment]):

    """

    segments = proto.RepeatedField(proto.MESSAGE, number=1,
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

        cutoff_low (float):

        cutoff_high (float):

        platform (str):

        highlevel_type (str):

    """

    segment = proto.Field(proto.STRING, number=1)

    segment_key = proto.Field(proto.STRING, number=6)

    sub_segment = proto.Field(proto.STRING, number=2)

    segment_int = proto.Field(proto.INT32, number=3)

    sub_segment_int = proto.Field(proto.INT32, number=4)

    sub_segment_key = proto.Field(proto.STRING, number=5)

    cutoff_low = proto.Field(proto.DOUBLE, number=7)

    cutoff_high = proto.Field(proto.DOUBLE, number=8)

    platform = proto.Field(proto.STRING, number=9)

    highlevel_type = proto.Field(proto.STRING, number=10)


class ListPortsResponse(proto.Message):
    r"""List Ports

    Attributes:
        ports (Sequence[oceanbolt.com.entities_v3.types.Port]):

    """

    ports = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Port',
    )


class Port(proto.Message):
    r"""

    Attributes:
        port_id (int):

        port_name (str):

        country_code (str):

        region (str):

        unlocode (str):

        unlocode_alias (Sequence[str]):

        port_name_alias (Sequence[str]):

    """

    port_id = proto.Field(proto.INT32, number=1)

    port_name = proto.Field(proto.STRING, number=2)

    country_code = proto.Field(proto.STRING, number=3)

    region = proto.Field(proto.STRING, number=4)

    unlocode = proto.Field(proto.STRING, number=5)

    unlocode_alias = proto.RepeatedField(proto.STRING, number=6)

    port_name_alias = proto.RepeatedField(proto.STRING, number=7)


class ZoneWithPolygon(proto.Message):
    r"""ListTonnageZonesWithPolygons

    Attributes:
        zone_id (int):

        zone_name (str):

        zone_basin (str):

        geom_polygon_wkt (str):

        geom_polygon_geojson (str):

        geom_coordinate_wkt (str):

        geom_coordinate_geojson (str):

    """

    zone_id = proto.Field(proto.INT32, number=1)

    zone_name = proto.Field(proto.STRING, number=2)

    zone_basin = proto.Field(proto.STRING, number=3)

    geom_polygon_wkt = proto.Field(proto.STRING, number=4)

    geom_polygon_geojson = proto.Field(proto.STRING, number=5)

    geom_coordinate_wkt = proto.Field(proto.STRING, number=6)

    geom_coordinate_geojson = proto.Field(proto.STRING, number=7)


class ListTonnageZonesWithPolygonsResponse(proto.Message):
    r"""

    Attributes:
        zones (Sequence[oceanbolt.com.entities_v3.types.ZoneWithPolygon]):

    """

    zones = proto.RepeatedField(proto.MESSAGE, number=1,
        message='ZoneWithPolygon',
    )


class Zone(proto.Message):
    r"""ListZones

    Attributes:
        zone_id (int):

        zone_name (str):

    """

    zone_id = proto.Field(proto.INT32, number=1)

    zone_name = proto.Field(proto.STRING, number=2)


class ListTonnageZonesResponse(proto.Message):
    r"""

    Attributes:
        zones (Sequence[oceanbolt.com.entities_v3.types.Zone]):

    """

    zones = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Zone',
    )


class ListRegionsRequest(proto.Message):
    r"""ListRegions

    Attributes:
        direction (str):

    """

    direction = proto.Field(proto.STRING, number=1)


class Region(proto.Message):
    r"""

    Attributes:
        region_id (str):

        region_name (str):

    """

    region_id = proto.Field(proto.STRING, number=1)

    region_name = proto.Field(proto.STRING, number=2)


class ListRegionsResponse(proto.Message):
    r"""

    Attributes:
        regions (Sequence[oceanbolt.com.entities_v3.types.Region]):

    """

    regions = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Region',
    )


class RegionWithPolygon(proto.Message):
    r"""ListRegionsWithPolygon

    Attributes:
        region_id (str):

        region_name (str):

        geojson (str):

    """

    region_id = proto.Field(proto.STRING, number=1)

    region_name = proto.Field(proto.STRING, number=2)

    geojson = proto.Field(proto.STRING, number=3)


class ListRegionsWithPolygonResponse(proto.Message):
    r"""

    Attributes:
        regions (Sequence[oceanbolt.com.entities_v3.types.RegionWithPolygon]):

    """

    regions = proto.RepeatedField(proto.MESSAGE, number=1,
        message='RegionWithPolygon',
    )


class ListCountriesRequest(proto.Message):
    r"""ListCountries

    Attributes:
        direction (str):

    """

    direction = proto.Field(proto.STRING, number=1)


class Country(proto.Message):
    r"""

    Attributes:
        country (str):

        country_code (str):

    """

    country = proto.Field(proto.STRING, number=1)

    country_code = proto.Field(proto.STRING, number=2)


class ListCountriesResponse(proto.Message):
    r"""

    Attributes:
        countries (Sequence[oceanbolt.com.entities_v3.types.Country]):

    """

    countries = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Country',
    )


class Commodity(proto.Message):
    r"""ListCommodities

    Attributes:
        commodity (str):

        commodity_id (int):

        commodity_value (str):

        commodity_group (str):

        platform (str):

    """

    commodity = proto.Field(proto.STRING, number=1)

    commodity_id = proto.Field(proto.INT32, number=4)

    commodity_value = proto.Field(proto.STRING, number=2)

    commodity_group = proto.Field(proto.STRING, number=3)

    platform = proto.Field(proto.STRING, number=5)


class ListCommoditiesResponse(proto.Message):
    r"""

    Attributes:
        commodities (Sequence[oceanbolt.com.entities_v3.types.Commodity]):

    """

    commodities = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Commodity',
    )


class SearchRequest(proto.Message):
    r"""Search

    Attributes:
        q (str):

    """

    q = proto.Field(proto.STRING, number=1)


class SearchPolygonsResponse(proto.Message):
    r"""

    Attributes:
        polygons (Sequence[oceanbolt.com.entities_v3.types.Polygon]):

    """

    polygons = proto.RepeatedField(proto.MESSAGE, number=1,
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

    berth_id = proto.Field(proto.UINT32, number=1)

    port_id = proto.Field(proto.UINT32, number=2)

    port_name = proto.Field(proto.STRING, number=3)

    berth_name = proto.Field(proto.STRING, number=4)

    country_code = proto.Field(proto.STRING, number=5)

    unlocode = proto.Field(proto.STRING, number=6)

    entity_type = proto.Field(proto.STRING, number=7)

    alias = proto.Field(proto.STRING, number=10)


class SearchVesselsResponse(proto.Message):
    r"""

    Attributes:
        vessels (Sequence[oceanbolt.com.entities_v3.types.Vessel]):

    """

    vessels = proto.RepeatedField(proto.MESSAGE, number=1,
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

    imo = proto.Field(proto.UINT32, number=1)

    highlevel_type = proto.Field(proto.STRING, number=2)

    segment = proto.Field(proto.STRING, number=3)

    sub_segment = proto.Field(proto.STRING, number=4)

    dwt = proto.Field(proto.DOUBLE, number=5)

    max_draught = proto.Field(proto.DOUBLE, number=6)

    name = proto.Field(proto.STRING, number=7)

    ex_name = proto.Field(proto.STRING, number=8)

    built = proto.Field(proto.UINT32, number=9)

    type_ = proto.Field(proto.STRING, number=10)

    mpv = proto.Field(proto.BOOL, number=11)

    loa = proto.Field(proto.DOUBLE, number=12)

    beam = proto.Field(proto.DOUBLE, number=13)

    holds_total = proto.Field(proto.DOUBLE, number=14)


__all__ = tuple(sorted(__protobuf__.manifest))
