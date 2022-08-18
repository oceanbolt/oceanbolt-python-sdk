"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _NavigationalStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _NavigationalStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NavigationalStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_NAVIGATIONAL_STATUS: _NavigationalStatus.ValueType  # 0
    UNDER_WAY_USING_ENGINE: _NavigationalStatus.ValueType  # 100
    AT_ANCHOR: _NavigationalStatus.ValueType  # 1
    NOT_UNDER_COMMAND: _NavigationalStatus.ValueType  # 2
    RESTRICTED_MANOEUVRABILITY: _NavigationalStatus.ValueType  # 3
    CONSTRAINED_BY_DRAUGHT: _NavigationalStatus.ValueType  # 4
    MOORED: _NavigationalStatus.ValueType  # 5
    AGROUND: _NavigationalStatus.ValueType  # 6
    ENGAGED_IN_FISHING: _NavigationalStatus.ValueType  # 7
    ENGAGED_IN_SAILING: _NavigationalStatus.ValueType  # 8
    POWER_DRIVEN_VESSEL_TOWING_ASTERN: _NavigationalStatus.ValueType  # 11
    POWER_DRIVEN_VESSEL_PUSHING_AHEAD_OR_TOWING_ALONGSIDE: _NavigationalStatus.ValueType  # 12
    UNDEFINED: _NavigationalStatus.ValueType  # 15
class NavigationalStatus(_NavigationalStatus, metaclass=_NavigationalStatusEnumTypeWrapper):
    pass

UNKNOWN_NAVIGATIONAL_STATUS: NavigationalStatus.ValueType  # 0
UNDER_WAY_USING_ENGINE: NavigationalStatus.ValueType  # 100
AT_ANCHOR: NavigationalStatus.ValueType  # 1
NOT_UNDER_COMMAND: NavigationalStatus.ValueType  # 2
RESTRICTED_MANOEUVRABILITY: NavigationalStatus.ValueType  # 3
CONSTRAINED_BY_DRAUGHT: NavigationalStatus.ValueType  # 4
MOORED: NavigationalStatus.ValueType  # 5
AGROUND: NavigationalStatus.ValueType  # 6
ENGAGED_IN_FISHING: NavigationalStatus.ValueType  # 7
ENGAGED_IN_SAILING: NavigationalStatus.ValueType  # 8
POWER_DRIVEN_VESSEL_TOWING_ASTERN: NavigationalStatus.ValueType  # 11
POWER_DRIVEN_VESSEL_PUSHING_AHEAD_OR_TOWING_ALONGSIDE: NavigationalStatus.ValueType  # 12
UNDEFINED: NavigationalStatus.ValueType  # 15
global___NavigationalStatus = NavigationalStatus

