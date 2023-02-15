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

from oceanbolt.com.polygonmanagement_v3.types import resources


__protobuf__ = proto.module(
    package='oceanbolt.com.polygonmanagement.v3',
    manifest={
        'ListLayersRequest',
        'CreateLayerRequest',
        'DeleteLayerRequest',
        'CopyLayerRequest',
        'GetLayerRequest',
        'ListPolygonsRequest',
        'ShareLayerRequest',
        'DropPolygonsRequest',
        'BatchAddPolygonsRequest',
        'BatchAddPolygonsResponse',
        'ReplacePolygonsRequest',
        'ListLayersResponse',
        'AddPolygonRequest',
        'DeletePolygonRequest',
        'UpdatePolygonRequest',
        'ListPolygonsResponse',
    },
)


class ListLayersRequest(proto.Message):
    r"""LayerManagement requests and responses
    """


class CreateLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CopyLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        new_layer_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    new_layer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPolygonsRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ShareLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DropPolygonsRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchAddPolygonsRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygons (MutableSequence[oceanbolt.com.polygonmanagement_v3.types.Polygon]):

        upsert (bool):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    polygons: MutableSequence[resources.Polygon] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=resources.Polygon,
    )
    upsert: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class BatchAddPolygonsResponse(proto.Message):
    r"""

    Attributes:
        errors (MutableSequence[str]):

    """

    errors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ReplacePolygonsRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygons (MutableSequence[oceanbolt.com.polygonmanagement_v3.types.Polygon]):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    polygons: MutableSequence[resources.Polygon] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=resources.Polygon,
    )


class ListLayersResponse(proto.Message):
    r"""

    Attributes:
        layers (MutableSequence[oceanbolt.com.polygonmanagement_v3.types.Layer]):

    """

    layers: MutableSequence[resources.Layer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Layer,
    )


class AddPolygonRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygon_id (str):

        payload (oceanbolt.com.polygonmanagement_v3.types.Polygon):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    polygon_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    payload: resources.Polygon = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Polygon,
    )


class DeletePolygonRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygon_id (str):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    polygon_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdatePolygonRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygon_id (str):

        payload (oceanbolt.com.polygonmanagement_v3.types.Polygon):

        upsert (bool):

    """

    layer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    polygon_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    payload: resources.Polygon = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Polygon,
    )
    upsert: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListPolygonsResponse(proto.Message):
    r"""

    Attributes:
        polygons (MutableSequence[oceanbolt.com.polygonmanagement_v3.types.Polygon]):

    """

    polygons: MutableSequence[resources.Polygon] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Polygon,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
