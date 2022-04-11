"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class VesselFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMO_FIELD_NUMBER: builtins.int
    DWT_FIELD_NUMBER: builtins.int
    MAX_DRAUGHT_FIELD_NUMBER: builtins.int
    LOA_FIELD_NUMBER: builtins.int
    BEAM_FIELD_NUMBER: builtins.int
    LOG_FITTED_FIELD_NUMBER: builtins.int
    SELF_UNLOADER_FIELD_NUMBER: builtins.int
    GEARED_FIELD_NUMBER: builtins.int
    ICE_CLASSED_FIELD_NUMBER: builtins.int
    MPV_FIELD_NUMBER: builtins.int
    GT_FIELD_NUMBER: builtins.int
    GRAIN_CAPACITY_FIELD_NUMBER: builtins.int
    GAS_CAPACITY_CBM_FIELD_NUMBER: builtins.int
    BUILT_FIELD_NUMBER: builtins.int
    VESSEL_TYPE_FIELD_NUMBER: builtins.int
    FLAG_STATE_FIELD_NUMBER: builtins.int
    @property
    def imo(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """List IMO values to filter on. Example: [1234567,7654321]."""
        pass
    @property
    def dwt(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """DWT range to filter on. Example: [45000,90000] (both values inclusive)."""
        pass
    @property
    def max_draught(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Maximum Draught range to filter on (value in meters). Example: [12,20] (both values inclusive)."""
        pass
    @property
    def loa(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """LOA range to filter on (value in meters). Example: [150,200] (both values inclusive)."""
        pass
    @property
    def beam(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """BEAM range to filter on (value in meters). Example: [10,40] (both values inclusive)."""
        pass
    @property
    def log_fitted(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Flag to specify filtering on whether a vessel is log fitted or not. If left blank, filter will not be applied."""
        pass
    @property
    def self_unloader(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Flag to specify filtering on whether a vessel is classified as a self unloader or not. If left blank, filter will not be applied."""
        pass
    @property
    def geared(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Flag to specify filtering on whether a vessel is geared or not. If left blank, filter will not be applied."""
        pass
    @property
    def ice_classed(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Flag to specify filtering on whether a vessel is ice classed or not. If left blank, filter will not be applied."""
        pass
    @property
    def mpv(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Flag to specify filtering on whether a vessel is classified as an MPV. If left blank, filter will not be applied."""
        pass
    @property
    def gt(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """GT range to filter on. Example: [45000,90000] (both values inclusive)."""
        pass
    @property
    def grain_capacity(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Grain capacity range to filter on (value in cubic meters). Example: [45000,90000] (both values inclusive)."""
        pass
    @property
    def gas_capacity_cbm(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Gas capacity range filter on (value in cubic meters). Example: [45000,90000] (both values inclusive)."""
        pass
    @property
    def built(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Built year range to filter on. Example: [1998,2005] (both values inclusive)."""
        pass
    @property
    def vessel_type(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of vessel type values to filter on. Example: TBD."""
        pass
    @property
    def flag_state(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of flag state values to filter on. Example: [US,CN]."""
        pass
    def __init__(self,
        *,
        imo: typing.Optional[typing.Iterable[builtins.int]] = ...,
        dwt: typing.Optional[typing.Iterable[builtins.float]] = ...,
        max_draught: typing.Optional[typing.Iterable[builtins.float]] = ...,
        loa: typing.Optional[typing.Iterable[builtins.float]] = ...,
        beam: typing.Optional[typing.Iterable[builtins.float]] = ...,
        log_fitted: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        self_unloader: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        geared: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        ice_classed: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        mpv: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        gt: typing.Optional[typing.Iterable[builtins.float]] = ...,
        grain_capacity: typing.Optional[typing.Iterable[builtins.float]] = ...,
        gas_capacity_cbm: typing.Optional[typing.Iterable[builtins.float]] = ...,
        built: typing.Optional[typing.Iterable[builtins.int]] = ...,
        vessel_type: typing.Optional[typing.Iterable[typing.Text]] = ...,
        flag_state: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["geared",b"geared","ice_classed",b"ice_classed","log_fitted",b"log_fitted","mpv",b"mpv","self_unloader",b"self_unloader"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["beam",b"beam","built",b"built","dwt",b"dwt","flag_state",b"flag_state","gas_capacity_cbm",b"gas_capacity_cbm","geared",b"geared","grain_capacity",b"grain_capacity","gt",b"gt","ice_classed",b"ice_classed","imo",b"imo","loa",b"loa","log_fitted",b"log_fitted","max_draught",b"max_draught","mpv",b"mpv","self_unloader",b"self_unloader","vessel_type",b"vessel_type"]) -> None: ...
global___VesselFilter = VesselFilter