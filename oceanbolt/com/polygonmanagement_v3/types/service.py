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


from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.polygonmanagement.v3',
    manifest={
        'RenameLayerRequest',
        'CreateLayerRequest',
        'DeleteLayerRequest',
        'CopyLayerRequest',
        'GetLayerRequest',
        'ListPolygonsRequest',
        'ShareLayerRequest',
        'DropPolygonsRequest',
        'BatchPolygonsRequest',
        'Layers',
        'Layer',
        'PolygonParams',
        'AddPolygonRequest',
        'DeletePolygonRequest',
        'UpdatePolygonRequest',
        'Polygons',
        'Polygon',
        'EmptyParams',
        'EmptyResponse',
    },
)


class RenameLayerRequest(proto.Message):
    r"""LayerManagement requests ans responses

    Attributes:
        layer_id (str):

        new_layer_name (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)

    new_layer_name = proto.Field(proto.STRING, number=2)


class CreateLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_name (str):

    """

    layer_name = proto.Field(proto.STRING, number=2)


class DeleteLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)


class CopyLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)


class GetLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)


class ListPolygonsRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)


class ShareLayerRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)


class DropPolygonsRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)


class BatchPolygonsRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygons (Sequence[oceanbolt.com.polygonmanagement_v3.types.PolygonParams]):

        upsert (bool):

    """

    layer_id = proto.Field(proto.STRING, number=1)

    polygons = proto.RepeatedField(proto.MESSAGE, number=2,
        message='PolygonParams',
    )

    upsert = proto.Field(proto.BOOL, number=4)


class Layers(proto.Message):
    r"""

    Attributes:
        layers (Sequence[oceanbolt.com.polygonmanagement_v3.types.Layer]):

        predefined_layers (Sequence[oceanbolt.com.polygonmanagement_v3.types.Layer]):

    """

    layers = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Layer',
    )

    predefined_layers = proto.RepeatedField(proto.MESSAGE, number=2,
        message='Layer',
    )


class Layer(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        layer_name (str):

        owner_user_id (str):

        organization (str):

        polygons_in_layer (google.protobuf.wrappers_pb2.Int32Value):

        polygons (Sequence[oceanbolt.com.polygonmanagement_v3.types.Polygon]):

        shared_with_org (google.protobuf.wrappers_pb2.BoolValue):

    """

    layer_id = proto.Field(proto.STRING, number=1)

    layer_name = proto.Field(proto.STRING, number=2)

    owner_user_id = proto.Field(proto.STRING, number=3)

    organization = proto.Field(proto.STRING, number=6)

    polygons_in_layer = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.Int32Value,
    )

    polygons = proto.RepeatedField(proto.MESSAGE, number=5,
        message='Polygon',
    )

    shared_with_org = proto.Field(proto.MESSAGE, number=7,
        message=wrappers.BoolValue,
    )


class PolygonParams(proto.Message):
    r"""

    Attributes:
        polygon_name (str):

        geojson (str):
            geojson format for geometry encoding,
            https://en.wikipedia.org/wiki/GeoJSON
        metadata (Sequence[oceanbolt.com.polygonmanagement_v3.types.PolygonParams.MetadataEntry]):

    """

    polygon_name = proto.Field(proto.STRING, number=2)

    geojson = proto.Field(proto.STRING, number=11)

    metadata = proto.MapField(proto.STRING, proto.STRING, number=3)


class AddPolygonRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygon (oceanbolt.com.polygonmanagement_v3.types.PolygonParams):

    """

    layer_id = proto.Field(proto.STRING, number=1)

    polygon = proto.Field(proto.MESSAGE, number=2,
        message='PolygonParams',
    )


class DeletePolygonRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygon_id (str):

    """

    layer_id = proto.Field(proto.STRING, number=1)

    polygon_id = proto.Field(proto.STRING, number=2)


class UpdatePolygonRequest(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygon_id (str):

        polygon (oceanbolt.com.polygonmanagement_v3.types.PolygonParams):

        upsert (bool):

    """

    layer_id = proto.Field(proto.STRING, number=1)

    polygon_id = proto.Field(proto.STRING, number=2)

    polygon = proto.Field(proto.MESSAGE, number=3,
        message='PolygonParams',
    )

    upsert = proto.Field(proto.BOOL, number=4)


class Polygons(proto.Message):
    r"""

    Attributes:
        polygons (Sequence[oceanbolt.com.polygonmanagement_v3.types.Polygon]):

        polygons_in_layer (int):

    """

    polygons = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Polygon',
    )

    polygons_in_layer = proto.Field(proto.INT32, number=2)


class Polygon(proto.Message):
    r"""

    Attributes:
        layer_id (str):

        polygon_id (str):

        polygon_name (str):

        metadata (Sequence[oceanbolt.com.polygonmanagement_v3.types.Polygon.MetadataEntry]):

    """

    layer_id = proto.Field(proto.STRING, number=4)

    polygon_id = proto.Field(proto.STRING, number=1)

    polygon_name = proto.Field(proto.STRING, number=2)

    metadata = proto.MapField(proto.STRING, proto.STRING, number=3)


class EmptyParams(proto.Message):
    r""""""


class EmptyResponse(proto.Message):
    r""""""


__all__ = tuple(sorted(__protobuf__.manifest))
