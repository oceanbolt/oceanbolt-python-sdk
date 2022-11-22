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
import proto  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.polygonmanagement.v3',
    manifest={
        'Layer',
        'Polygon',
    },
)


class Layer(proto.Message):
    r"""

    Attributes:
        name (str):

        layer_id (str):

        owner_user_id (str):

        organization (str):

        polygons_in_layer (int):

        polygons (Sequence[oceanbolt.com.polygonmanagement_v3.types.Polygon]):

        shared_with_org (bool):

    """

    name = proto.Field(
        proto.STRING,
        number=8,
    )
    layer_id = proto.Field(
        proto.STRING,
        number=1,
    )
    owner_user_id = proto.Field(
        proto.STRING,
        number=3,
    )
    organization = proto.Field(
        proto.STRING,
        number=6,
    )
    polygons_in_layer = proto.Field(
        proto.INT32,
        number=4,
    )
    polygons = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message='Polygon',
    )
    shared_with_org = proto.Field(
        proto.BOOL,
        number=7,
    )


class Polygon(proto.Message):
    r"""

    Attributes:
        name (str):

        polygon_id (str):

        geojson (str):

        metadata (Mapping[str, str]):

    """

    name = proto.Field(
        proto.STRING,
        number=5,
    )
    polygon_id = proto.Field(
        proto.STRING,
        number=1,
    )
    geojson = proto.Field(
        proto.STRING,
        number=2,
    )
    metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
