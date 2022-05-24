"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import oceanbolt.com.ptypes.enums.direction_pb2
import oceanbolt.com.ptypes.enums.polygon_status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PositionFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COURSE_FIELD_NUMBER: builtins.int
    HEADING_FIELD_NUMBER: builtins.int
    SPEED_FIELD_NUMBER: builtins.int
    DRAUGHT_METERS_FIELD_NUMBER: builtins.int
    DRAUGHT_PERCENTAGE_FIELD_NUMBER: builtins.int
    POLYGON_STATUS_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    @property
    def course(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Course range to filter on. Example: [0,45] (both values inclusive)."""
        pass
    @property
    def heading(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Heading range to filter on. Example: [0,45] (both values inclusive)."""
        pass
    @property
    def speed(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Speed range to filter on. Example: [0,12] (both values inclusive)."""
        pass
    @property
    def draught_meters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Draught range to filter on (value in meters). Example: [0,8] (both values inclusive)."""
        pass
    @property
    def draught_percentage(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Draught percentage range to filter on (value in percentage). Example: [0.6,1] (both values inclusive)."""
        pass
    @property
    def polygon_status(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[ptypes.enums.polygon_status_pb2.PolygonStatus.ValueType]:
        """Polygon statuses to filter on. See oceanbolt.com.ptypes.enumspb.v1.PolygonStatus for list of valid values."""
        pass
    @property
    def direction(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[ptypes.enums.direction_pb2.Direction.ValueType]:
        """Directions to filter on. See oceanbolt.com.ptypes.enumspb.v1.Directions for list of valid values."""
        pass
    def __init__(self,
        *,
        course: typing.Optional[typing.Iterable[builtins.float]] = ...,
        heading: typing.Optional[typing.Iterable[builtins.float]] = ...,
        speed: typing.Optional[typing.Iterable[builtins.float]] = ...,
        draught_meters: typing.Optional[typing.Iterable[builtins.float]] = ...,
        draught_percentage: typing.Optional[typing.Iterable[builtins.float]] = ...,
        polygon_status: typing.Optional[typing.Iterable[ptypes.enums.polygon_status_pb2.PolygonStatus.ValueType]] = ...,
        direction: typing.Optional[typing.Iterable[ptypes.enums.direction_pb2.Direction.ValueType]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["course",b"course","direction",b"direction","draught_meters",b"draught_meters","draught_percentage",b"draught_percentage","heading",b"heading","polygon_status",b"polygon_status","speed",b"speed"]) -> None: ...
global___PositionFilter = PositionFilter
