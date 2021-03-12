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

from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.async_client import PolygonManagementServiceAsyncClient
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.client import PolygonManagementServiceClient
from oceanbolt.com.polygonmanagement_v3.types.service import AddPolygonRequest
from oceanbolt.com.polygonmanagement_v3.types.service import BatchPolygonsRequest
from oceanbolt.com.polygonmanagement_v3.types.service import CopyLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import CreateLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import DeleteLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import DeletePolygonRequest
from oceanbolt.com.polygonmanagement_v3.types.service import DropPolygonsRequest
from oceanbolt.com.polygonmanagement_v3.types.service import EmptyParams
from oceanbolt.com.polygonmanagement_v3.types.service import EmptyResponse
from oceanbolt.com.polygonmanagement_v3.types.service import GetLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import Layer
from oceanbolt.com.polygonmanagement_v3.types.service import Layers
from oceanbolt.com.polygonmanagement_v3.types.service import ListPolygonsRequest
from oceanbolt.com.polygonmanagement_v3.types.service import Polygon
from oceanbolt.com.polygonmanagement_v3.types.service import PolygonParams
from oceanbolt.com.polygonmanagement_v3.types.service import Polygons
from oceanbolt.com.polygonmanagement_v3.types.service import RenameLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import ShareLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import UpdatePolygonRequest

__all__ = (
    'AddPolygonRequest',
    'BatchPolygonsRequest',
    'CopyLayerRequest',
    'CreateLayerRequest',
    'DeleteLayerRequest',
    'DeletePolygonRequest',
    'DropPolygonsRequest',
    'EmptyParams',
    'EmptyResponse',
    'GetLayerRequest',
    'Layer',
    'Layers',
    'ListPolygonsRequest',
    'Polygon',
    'PolygonManagementServiceAsyncClient',
    'PolygonManagementServiceClient',
    'PolygonParams',
    'Polygons',
    'RenameLayerRequest',
    'ShareLayerRequest',
    'UpdatePolygonRequest',
)
