"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
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

class GeofencePayload(google.protobuf.message.Message):
    """GeofencePayload is a type describing a concrete specific geographical area of interest (such as a polygon or a center with a radius). It can be encoded in a range of different ways."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WKT_FIELD_NUMBER: builtins.int
    GEOJSON_FIELD_NUMBER: builtins.int
    WKB_FIELD_NUMBER: builtins.int
    ESRI_SHAPE_FIELD_NUMBER: builtins.int
    CENTER_RADIUS_FIELD_NUMBER: builtins.int
    POLYGON_LIST_FIELD_NUMBER: builtins.int
    wkt: typing.Text
    """well known text format for geometry encoding, https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry"""

    geojson: typing.Text
    """geojson format for geometry encoding, https://en.wikipedia.org/wiki/GeoJSON"""

    wkb: builtins.bytes
    """well known binary format for geometry encoding, https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary"""

    esri_shape: builtins.bytes
    """ESRI shape binary format for geometry encoding (fastest decoding and encoding for geometry service) https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf"""

    @property
    def center_radius(self) -> global___CenterRadius:
        """center radius format for geometric encoding of circular geofences, consists of a center point and a radius (in meters) around the center point"""
        pass
    @property
    def polygon_list(self) -> global___PolygonList:
        """Polygon format for submitting a geofence as a list of points."""
        pass
    def __init__(self,
        *,
        wkt: typing.Text = ...,
        geojson: typing.Text = ...,
        wkb: builtins.bytes = ...,
        esri_shape: builtins.bytes = ...,
        center_radius: typing.Optional[global___CenterRadius] = ...,
        polygon_list: typing.Optional[global___PolygonList] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["center_radius",b"center_radius","data",b"data","esri_shape",b"esri_shape","geojson",b"geojson","polygon_list",b"polygon_list","wkb",b"wkb","wkt",b"wkt"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["center_radius",b"center_radius","data",b"data","esri_shape",b"esri_shape","geojson",b"geojson","polygon_list",b"polygon_list","wkb",b"wkb","wkt",b"wkt"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["data",b"data"]) -> typing.Optional[typing_extensions.Literal["wkt","geojson","wkb","esri_shape","center_radius","polygon_list"]]: ...
global___GeofencePayload = GeofencePayload

class CenterRadius(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_FIELD_NUMBER: builtins.int
    RADIUS_FIELD_NUMBER: builtins.int
    @property
    def point(self) -> global___Point:
        """Center point"""
        pass
    radius: builtins.float
    """Radius in meters"""

    def __init__(self,
        *,
        point: typing.Optional[global___Point] = ...,
        radius: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["point",b"point","radius",b"radius"]) -> None: ...
global___CenterRadius = CenterRadius

class PolygonList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINTS_FIELD_NUMBER: builtins.int
    @property
    def points(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Point]: ...
    def __init__(self,
        *,
        points: typing.Optional[typing.Iterable[global___Point]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["points",b"points"]) -> None: ...
global___PolygonList = PolygonList

class Point(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LON_FIELD_NUMBER: builtins.int
    LAT_FIELD_NUMBER: builtins.int
    lon: builtins.float
    lat: builtins.float
    def __init__(self,
        *,
        lon: builtins.float = ...,
        lat: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["lat",b"lat","lon",b"lon"]) -> None: ...
global___Point = Point
