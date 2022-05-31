"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import oceanbolt.com.ptypes.enums.platforms_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Vessel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    EX_NAME_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    SEGMENT_FIELD_NUMBER: builtins.int
    SUB_SEGMENT_FIELD_NUMBER: builtins.int
    VESSEL_TYPE_FIELD_NUMBER: builtins.int
    DWT_FIELD_NUMBER: builtins.int
    MAX_DRAUGHT_FIELD_NUMBER: builtins.int
    BUILT_FIELD_NUMBER: builtins.int
    LOA_FIELD_NUMBER: builtins.int
    BEAM_FIELD_NUMBER: builtins.int
    imo: builtins.int
    name: typing.Text
    ex_name: typing.Text
    platform: oceanbolt.com.ptypes.enums.platforms_pb2.Platform.ValueType
    segment: typing.Text
    sub_segment: typing.Text
    vessel_type: typing.Text
    dwt: builtins.float
    max_draught: builtins.float
    built: builtins.int
    loa: builtins.float
    beam: builtins.float
    def __init__(self,
        *,
        imo: builtins.int = ...,
        name: typing.Text = ...,
        ex_name: typing.Text = ...,
        platform: oceanbolt.com.ptypes.enums.platforms_pb2.Platform.ValueType = ...,
        segment: typing.Text = ...,
        sub_segment: typing.Text = ...,
        vessel_type: typing.Text = ...,
        dwt: builtins.float = ...,
        max_draught: builtins.float = ...,
        built: builtins.int = ...,
        loa: builtins.float = ...,
        beam: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["beam",b"beam","built",b"built","dwt",b"dwt","ex_name",b"ex_name","imo",b"imo","loa",b"loa","max_draught",b"max_draught","name",b"name","platform",b"platform","segment",b"segment","sub_segment",b"sub_segment","vessel_type",b"vessel_type"]) -> None: ...
global___Vessel = Vessel
