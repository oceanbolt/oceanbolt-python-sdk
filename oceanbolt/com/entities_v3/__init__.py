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
from oceanbolt.com.entities_v3 import gapic_version as package_version

__version__ = package_version.__version__


from .services.entity_service import EntityServiceClient
from .services.entity_service import EntityServiceAsyncClient

from .types.service import Commodity
from .types.service import Country
from .types.service import ListCommoditiesRequest
from .types.service import ListCommoditiesResponse
from .types.service import ListCountriesRequest
from .types.service import ListCountriesResponse
from .types.service import ListPortsRequest
from .types.service import ListPortsResponse
from .types.service import ListRegionsRequest
from .types.service import ListRegionsResponse
from .types.service import ListRegionsWithPolygonResponse
from .types.service import ListSegmentsRequest
from .types.service import ListSegmentsResponse
from .types.service import ListShipyardsRequest
from .types.service import ListShipyardsResponse
from .types.service import ListTonnageZonesResponse
from .types.service import ListTonnageZonesWithPolygonsResponse
from .types.service import ListZonesRequest
from .types.service import Polygon
from .types.service import Port
from .types.service import Region
from .types.service import RegionWithPolygon
from .types.service import SearchPolygonsResponse
from .types.service import SearchRequest
from .types.service import SearchVesselsResponse
from .types.service import Segment
from .types.service import Shipyard
from .types.service import Vessel
from .types.service import Zone
from .types.service import ZoneWithPolygon

__all__ = (
    'EntityServiceAsyncClient',
'Commodity',
'Country',
'EntityServiceClient',
'ListCommoditiesRequest',
'ListCommoditiesResponse',
'ListCountriesRequest',
'ListCountriesResponse',
'ListPortsRequest',
'ListPortsResponse',
'ListRegionsRequest',
'ListRegionsResponse',
'ListRegionsWithPolygonResponse',
'ListSegmentsRequest',
'ListSegmentsResponse',
'ListShipyardsRequest',
'ListShipyardsResponse',
'ListTonnageZonesResponse',
'ListTonnageZonesWithPolygonsResponse',
'ListZonesRequest',
'Polygon',
'Port',
'Region',
'RegionWithPolygon',
'SearchPolygonsResponse',
'SearchRequest',
'SearchVesselsResponse',
'Segment',
'Shipyard',
'Vessel',
'Zone',
'ZoneWithPolygon',
)
