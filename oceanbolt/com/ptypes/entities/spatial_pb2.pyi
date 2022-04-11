"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Port(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PORT_ID_FIELD_NUMBER: builtins.int
    PORT_NAME_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    COUNTRY_CODE_FIELD_NUMBER: builtins.int
    LAT_FIELD_NUMBER: builtins.int
    LON_FIELD_NUMBER: builtins.int
    port_id: builtins.int
    port_name: typing.Text
    region: typing.Text
    country_code: typing.Text
    lat: builtins.float
    lon: builtins.float
    def __init__(self,
        *,
        port_id: builtins.int = ...,
        port_name: typing.Text = ...,
        region: typing.Text = ...,
        country_code: typing.Text = ...,
        lat: builtins.float = ...,
        lon: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["country_code",b"country_code","lat",b"lat","lon",b"lon","port_id",b"port_id","port_name",b"port_name","region",b"region"]) -> None: ...
global___Port = Port

class Region(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___Region = Region