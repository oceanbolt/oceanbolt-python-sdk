"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Platform:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PlatformEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Platform.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNDEFINED_PLATFORM: _Platform.ValueType  # 0
    DRY_BULK: _Platform.ValueType  # 1
    TANKER: _Platform.ValueType  # 2
    CONTAINER: _Platform.ValueType  # 3
    RORO: _Platform.ValueType  # 4
    AUXILIARY: _Platform.ValueType  # 5

class Platform(_Platform, metaclass=_PlatformEnumTypeWrapper): ...

UNDEFINED_PLATFORM: Platform.ValueType  # 0
DRY_BULK: Platform.ValueType  # 1
TANKER: Platform.ValueType  # 2
CONTAINER: Platform.ValueType  # 3
RORO: Platform.ValueType  # 4
AUXILIARY: Platform.ValueType  # 5
global___Platform = Platform
