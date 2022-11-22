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

from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.client import PolygonManagementServiceClient
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.async_client import PolygonManagementServiceAsyncClient

from oceanbolt.com.polygonmanagement_v3.types.resources import Layer
from oceanbolt.com.polygonmanagement_v3.types.resources import Polygon
from oceanbolt.com.polygonmanagement_v3.types.service import AddPolygonRequest
from oceanbolt.com.polygonmanagement_v3.types.service import BatchAddPolygonsRequest
from oceanbolt.com.polygonmanagement_v3.types.service import BatchAddPolygonsResponse
from oceanbolt.com.polygonmanagement_v3.types.service import CopyLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import CreateLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import DeleteLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import DeletePolygonRequest
from oceanbolt.com.polygonmanagement_v3.types.service import DropPolygonsRequest
from oceanbolt.com.polygonmanagement_v3.types.service import GetLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import ListLayersRequest
from oceanbolt.com.polygonmanagement_v3.types.service import ListLayersResponse
from oceanbolt.com.polygonmanagement_v3.types.service import ListPolygonsRequest
from oceanbolt.com.polygonmanagement_v3.types.service import ListPolygonsResponse
from oceanbolt.com.polygonmanagement_v3.types.service import ReplacePolygonsRequest
from oceanbolt.com.polygonmanagement_v3.types.service import ShareLayerRequest
from oceanbolt.com.polygonmanagement_v3.types.service import UpdatePolygonRequest

__all__ = ('PolygonManagementServiceClient',
    'PolygonManagementServiceAsyncClient',
    'Layer',
    'Polygon',
    'AddPolygonRequest',
    'BatchAddPolygonsRequest',
    'BatchAddPolygonsResponse',
    'CopyLayerRequest',
    'CreateLayerRequest',
    'DeleteLayerRequest',
    'DeletePolygonRequest',
    'DropPolygonsRequest',
    'GetLayerRequest',
    'ListLayersRequest',
    'ListLayersResponse',
    'ListPolygonsRequest',
    'ListPolygonsResponse',
    'ReplacePolygonsRequest',
    'ShareLayerRequest',
    'UpdatePolygonRequest',
)
