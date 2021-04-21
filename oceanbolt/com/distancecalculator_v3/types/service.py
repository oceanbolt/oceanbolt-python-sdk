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
    package='oceanbolt.com.distancecalculator.v3',
    manifest={
        'Location',
        'DistanceRequest',
        'Leg',
        'DistanceResponse',
        'Point',
    },
)


class Location(proto.Message):
    r"""Locatation data object.
    Locations can be specified using either raw lon/lat coordinates,
    unlocodes, Oceanbolt portIds or by specifying IMO number of a
    vessel. If an IMO is specified, routing will be calculated from
    the vessels current location.

    Attributes:
        imo (int):
            IMO number to include in the routing
            calculation. The current location of the vessel
            will be used in routing calculations.
        unlocode (str):
            UNLOCODE of a port to be included in routing
            calculation.
        point (oceanbolt.com.distancecalculator_v3.types.Point):
            Raw lon/lat point to be included in routing
            calculation.
        port_id (int):
            Oceanbolt port identifier to be included in
            routing calculation.
    """

    imo = proto.Field(proto.UINT32, number=1, oneof='Data')

    unlocode = proto.Field(proto.STRING, number=2, oneof='Data')

    point = proto.Field(proto.MESSAGE, number=3, oneof='Data',
        message='Point',
    )

    port_id = proto.Field(proto.UINT32, number=4, oneof='Data')


class DistanceRequest(proto.Message):
    r"""Request object for CalculateDistance method

    Attributes:
        locations (Sequence[oceanbolt.com.distancecalculator_v3.types.Location]):
            List of locations to calculate the shortest
            route between. If more than 2 locations are
            specified, then routing will be calculated
            through all locations, using intermediary
            locations as waypoints. The routing order of the
            locations will be based on the order of the
            locations in the request body.
        speed (float):
            An optional speed parameter. If this is
            supplied, then the API will return an estimate
            of the total duration of the voyage, based on
            the supplied speed. Speed parameter should be
            supplied in knots.
        transform (str):
            Specifies a transformation to be applied to the returned
            shortest path. Allowed values are [great_circle].
        longitude_adjustment (str):
            Specifies whether the resulting points/lines crossing the
            antimeridian should be adjusted to form a continuous line
            for plotting. Allowed values are [antimeridian,none].
            Default value is 'antimeridian.
    """

    locations = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Location',
    )

    speed = proto.Field(proto.DOUBLE, number=2)

    transform = proto.Field(proto.STRING, number=3)

    longitude_adjustment = proto.Field(proto.STRING, number=4)


class Leg(proto.Message):
    r"""Individual leg

    Attributes:
        distance (float):
            Distance of the leg in nautical miles.
        duration_hours (float):
            Expected duration of the leg, given a certain
            speed supplied by the user.
        shortest_path (Sequence[oceanbolt.com.distancecalculator_v3.types.Point]):
            The calculated shortest path between the
            start/end point of the leg.
        starting_point_modified (google.protobuf.wrappers_pb2.BoolValue):
            Flag indicating whether the original starting
            point was modified. This can happen if the
            original point supplied was over land.
    """

    distance = proto.Field(proto.DOUBLE, number=1)

    duration_hours = proto.Field(proto.DOUBLE, number=2)

    shortest_path = proto.RepeatedField(proto.MESSAGE, number=3,
        message='Point',
    )

    starting_point_modified = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.BoolValue,
    )


class DistanceResponse(proto.Message):
    r"""Response object for CalculateDistance method

    Attributes:
        total_distance (float):
            Total distance of the entire voyage in
            nautical miles.
        total_duration_hours (float):
            Total expected duration of the entire voyage,
            given a certain speed supplied by the user.
        total_shortest_path (Sequence[oceanbolt.com.distancecalculator_v3.types.Point]):
            The calculated shortest path between the
            start/end point of the entire voyage.
        individual_legs (Sequence[oceanbolt.com.distancecalculator_v3.types.Leg]):
            Array of the individual legs that compose the
            voyage
    """

    total_distance = proto.Field(proto.DOUBLE, number=1)

    total_duration_hours = proto.Field(proto.DOUBLE, number=2)

    total_shortest_path = proto.RepeatedField(proto.MESSAGE, number=3,
        message='Point',
    )

    individual_legs = proto.RepeatedField(proto.MESSAGE, number=4,
        message='Leg',
    )


class Point(proto.Message):
    r"""GeoPoint

    Attributes:
        lon (google.protobuf.wrappers_pb2.DoubleValue):
            Longitude
        lat (google.protobuf.wrappers_pb2.DoubleValue):
            Latitude
    """

    lon = proto.Field(proto.MESSAGE, number=1,
        message=wrappers.DoubleValue,
    )

    lat = proto.Field(proto.MESSAGE, number=2,
        message=wrappers.DoubleValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
