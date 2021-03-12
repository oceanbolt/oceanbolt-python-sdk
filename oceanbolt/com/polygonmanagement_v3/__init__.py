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

from .services.polygon_management_service import PolygonManagementServiceClient
from .types.service import AddPolygonRequest
from .types.service import BatchPolygonsRequest
from .types.service import CopyLayerRequest
from .types.service import CreateLayerRequest
from .types.service import DeleteLayerRequest
from .types.service import DeletePolygonRequest
from .types.service import DropPolygonsRequest
from .types.service import EmptyParams
from .types.service import EmptyResponse
from .types.service import GetLayerRequest
from .types.service import Layer
from .types.service import Layers
from .types.service import ListPolygonsRequest
from .types.service import Polygon
from .types.service import PolygonParams
from .types.service import Polygons
from .types.service import RenameLayerRequest
from .types.service import ShareLayerRequest
from .types.service import UpdatePolygonRequest


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
    'PolygonParams',
    'Polygons',
    'RenameLayerRequest',
    'ShareLayerRequest',
    'UpdatePolygonRequest',
'PolygonManagementServiceClient',
)
