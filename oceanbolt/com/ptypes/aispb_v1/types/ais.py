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

from google.protobuf import timestamp_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.ptypes.aispb.v1',
    manifest={
        'AisPositionExtended',
    },
)


class AisPositionExtended(proto.Message):
    r"""

    Attributes:
        lon (float):

        lat (float):

        timestamp (google.protobuf.timestamp_pb2.Timestamp):

        speed (google.protobuf.wrappers_pb2.DoubleValue):

        navigational_status (google.protobuf.wrappers_pb2.Int32Value):

        destination (str):

        eta (google.protobuf.timestamp_pb2.Timestamp):

        draught (google.protobuf.wrappers_pb2.DoubleValue):

        course (google.protobuf.wrappers_pb2.DoubleValue):

        heading (google.protobuf.wrappers_pb2.DoubleValue):

        imo (int):

        mmsi (int):

    """

    lon = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    lat = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    speed = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.DoubleValue,
    )
    navigational_status = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int32Value,
    )
    destination = proto.Field(
        proto.STRING,
        number=6,
    )
    eta = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    draught = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.DoubleValue,
    )
    course = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.DoubleValue,
    )
    heading = proto.Field(
        proto.MESSAGE,
        number=12,
        message=wrappers_pb2.DoubleValue,
    )
    imo = proto.Field(
        proto.INT32,
        number=10,
    )
    mmsi = proto.Field(
        proto.INT32,
        number=11,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
