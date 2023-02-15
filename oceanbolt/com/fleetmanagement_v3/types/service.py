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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import wrappers_pb2  # type: ignore


__protobuf__ = proto.module(
    package='oceanbolt.com.fleetmanagement.v3',
    manifest={
        'RenameFleetRequest',
        'CreateFleetRequest',
        'DeleteFleetRequest',
        'GetFleetRequest',
        'ListVesselsRequest',
        'GetVesselRequest',
        'ListVesselsWithStatusRequest',
        'ShareFleetRequest',
        'DropVesselsRequest',
        'BatchVesselsRequest',
        'Fleets',
        'Fleet',
        'VesselParams',
        'UpdateVesselParams',
        'AddVesselRequest',
        'UpdateVesselRequest',
        'DeleteVesselRequest',
        'Vessels',
        'Vessel',
        'VesselStatus',
        'VesselStoppageEvent',
        'GetFleetLiveMapRequest',
        'GetFleetLiveMapResponse',
        'GetFleetListRequest',
        'EmptyParams',
        'EmptyResponse',
    },
)


class RenameFleetRequest(proto.Message):
    r"""Request object for renaming a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            renamed.
        new_fleet_name (str):
            The new name of the Fleet.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    new_fleet_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateFleetRequest(proto.Message):
    r"""Request object for creating a Fleet

    Attributes:
        fleet_name (str):
            The new name of the Fleet.
    """

    fleet_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteFleetRequest(proto.Message):
    r"""Request object for deleting a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            deleted.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetFleetRequest(proto.Message):
    r"""Request object for retrieving a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            retrieved.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVesselsRequest(proto.Message):
    r"""Request object for listing Vessels in a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource which
            vessels to be retrieved.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetVesselRequest(proto.Message):
    r"""Request object for retrieving a Vessel in a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource which
            vessels to be retrieved.
        imo (int):
            Imo of the vessel.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    imo: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ListVesselsWithStatusRequest(proto.Message):
    r"""Request object for listing Fleet Vessels with status (live
    state) data and speed events

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource which
            vessels to be retrieved.
        last_days (int):
            Number of last days from now for vessel StoppageEvents to be
            retrieved. Cannot be used alongside start_date and end_date.
        start_date (str):
            The UTC start date of the date filter for
            related events (StoppageEvents etc.)
        end_date (str):
            The UTC end date of the date filter for
            related events (StoppageEvents etc.)
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_days: int = proto.Field(
        proto.INT32,
        number=2,
    )
    start_date: str = proto.Field(
        proto.STRING,
        number=3,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ShareFleetRequest(proto.Message):
    r"""Request object for sharing a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            shared.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DropVesselsRequest(proto.Message):
    r"""Request object for dropping Vessels in a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where
            vessels should be dropped.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchVesselsRequest(proto.Message):
    r"""Request object for batch adding Vessels to a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where
            vessels should be added.
        vessels (MutableSequence[oceanbolt.com.fleetmanagement_v3.types.VesselParams]):
            List of Vessels to be added.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vessels: MutableSequence['VesselParams'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='VesselParams',
    )


class Fleets(proto.Message):
    r"""Response object for listing Fleets

    Attributes:
        fleets (MutableSequence[oceanbolt.com.fleetmanagement_v3.types.Fleet]):
            List of user defined Fleet resources.
        organization_fleets (MutableSequence[oceanbolt.com.fleetmanagement_v3.types.Fleet]):
            List of organizational Fleet resources that
            are shared with the current user.
        predefined_fleets (MutableSequence[oceanbolt.com.fleetmanagement_v3.types.Fleet]):
            List of system level predefined Fleet
            resources.
    """

    fleets: MutableSequence['Fleet'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Fleet',
    )
    organization_fleets: MutableSequence['Fleet'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='Fleet',
    )
    predefined_fleets: MutableSequence['Fleet'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='Fleet',
    )


class Fleet(proto.Message):
    r"""Fleet resource

    Attributes:
        fleet_id (str):
            The Fleet identifier.
        fleet_name (str):
            The name of the Fleet.
        platform (str):
            The platform identifier of the fleet
        owner_user_id (str):
            The user id of the Fleet owner (the user who
            has created the Fleet).
        organization (str):
            The organization that the user belongs to.
        vessels_in_fleet (google.protobuf.wrappers_pb2.Int32Value):
            The number of vessels in the Fleet.
        vessels (MutableSequence[oceanbolt.com.fleetmanagement_v3.types.Vessel]):
            List of Vessels in the Fleet.
        shared_with_org (google.protobuf.wrappers_pb2.BoolValue):
            A flag indicating whether this is a shared
            fleet.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fleet_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    platform: str = proto.Field(
        proto.STRING,
        number=8,
    )
    owner_user_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    organization: str = proto.Field(
        proto.STRING,
        number=6,
    )
    vessels_in_fleet: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int32Value,
    )
    vessels: MutableSequence['Vessel'] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message='Vessel',
    )
    shared_with_org: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )


class VesselParams(proto.Message):
    r"""Vessel parameters

    Attributes:
        imo (int):
            Imo of the vessel.
        metadata (MutableMapping[str, str]):
            A dict/map of arbitratry metadata that should
            be added to the vessel in the context of the
            current fleet. This can for example be links to
            internal voyage systems (Vezon/Imoset etc.) it
            can be current voyage related data or similar.
            The metadata is only accessible by the current
            user. If the current user chooses to share the
            fleet, it will also be accesible by users who
            belong to the same organization as the fleet
            owner.
    """

    imo: int = proto.Field(
        proto.INT32,
        number=2,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class UpdateVesselParams(proto.Message):
    r"""Parameter object for updating a vessel in a Fleet

    Attributes:
        metadata (MutableMapping[str, str]):
            New set of metadata information for a Vessel.
            This will overwrite existing keys/values
            currently stored in the metadata object of the
            Vessel.
    """

    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class AddVesselRequest(proto.Message):
    r"""Request object for adding a Vessel to a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where
            vessels should be added.
        vessel (oceanbolt.com.fleetmanagement_v3.types.VesselParams):
            Vessel params for the vessel that should be
            added.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vessel: 'VesselParams' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='VesselParams',
    )


class UpdateVesselRequest(proto.Message):
    r"""Request object for updating a vessel

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where the
            vessel should be updated.
        imo (int):
            IMO number of the vessel to be updated.
        vessel (oceanbolt.com.fleetmanagement_v3.types.UpdateVesselParams):
            New metadata object.
        upsert (bool):
            Flag indicating whether the vessel should be
            created if it doesnt not already exist. If the
            upsert flag is set to false, and a vessel does
            not already exist, the function will return an
            error.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    imo: int = proto.Field(
        proto.INT32,
        number=3,
    )
    vessel: 'UpdateVesselParams' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='UpdateVesselParams',
    )
    upsert: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteVesselRequest(proto.Message):
    r"""Request object for deleting a single Vessel from a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where the
            vessel should be deleted.
        imo (int):
            IMO number of the Vessel to be deleted.
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    imo: int = proto.Field(
        proto.INT32,
        number=2,
    )


class Vessels(proto.Message):
    r"""List of Vessel objects

    Attributes:
        vessels (MutableSequence[oceanbolt.com.fleetmanagement_v3.types.Vessel]):
            List of vessels in Fleet.
        vessels_in_fleet (int):
            Number of vessels in a Fleet.
    """

    vessels: MutableSequence['Vessel'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Vessel',
    )
    vessels_in_fleet: int = proto.Field(
        proto.INT32,
        number=2,
    )


class Vessel(proto.Message):
    r"""Vessel object

    Attributes:
        imo (int):
            IMO number of the vessel.
        dwt (float):
            DWT of the vessel.
        built (int):
            The year the vessel was built.
        vessel_name (str):
            Current name of the Vessel.
        segment (str):
            Name of the segment which the vessel belongs
            to.
        sub_segment (str):
            Flag code of the country where the vessel is
            currently registered.
        flag_code (str):
            Flag code of the country where the vessel is
            currently registered.
        ex_name (str):
            Ex name of the Vessel.
        type_ (str):
            The type of the vessel.
        metadata (MutableMapping[str, str]):
            Metadata object that contains arbitrary data
            fields defined by the user.
        status (oceanbolt.com.fleetmanagement_v3.types.VesselStatus):
            Vessel status (livestate data).
        stoppage_events (MutableSequence[oceanbolt.com.fleetmanagement_v3.types.VesselStoppageEvent]):
            Vessel speed events (stoppage data).
    """

    imo: int = proto.Field(
        proto.INT32,
        number=1,
    )
    dwt: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    built: int = proto.Field(
        proto.INT32,
        number=3,
    )
    vessel_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    segment: str = proto.Field(
        proto.STRING,
        number=5,
    )
    sub_segment: str = proto.Field(
        proto.STRING,
        number=10,
    )
    flag_code: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ex_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=8,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    status: 'VesselStatus' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='VesselStatus',
    )
    stoppage_events: MutableSequence['VesselStoppageEvent'] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message='VesselStoppageEvent',
    )


class VesselStatus(proto.Message):
    r"""

    Attributes:
        laden_status (str):

        cargo_status (str):

        port_call_status (str):

        related_port_name (str):

        draught_percentage (google.protobuf.wrappers_pb2.DoubleValue):

        destination (str):

        destination_port_name (str):

        last_position_received_at (str):

        last_static_received_at (str):

        current_speed (google.protobuf.wrappers_pb2.DoubleValue):

        current_navigational_status (google.protobuf.wrappers_pb2.Int32Value):

        current_commodity_group (str):

    """

    laden_status: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cargo_status: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port_call_status: str = proto.Field(
        proto.STRING,
        number=3,
    )
    related_port_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    draught_percentage: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.DoubleValue,
    )
    destination: str = proto.Field(
        proto.STRING,
        number=6,
    )
    destination_port_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    last_position_received_at: str = proto.Field(
        proto.STRING,
        number=8,
    )
    last_static_received_at: str = proto.Field(
        proto.STRING,
        number=9,
    )
    current_speed: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=10,
        message=wrappers_pb2.DoubleValue,
    )
    current_navigational_status: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=11,
        message=wrappers_pb2.Int32Value,
    )
    current_commodity_group: str = proto.Field(
        proto.STRING,
        number=12,
    )


class VesselStoppageEvent(proto.Message):
    r"""

    Attributes:
        started_at (str):

        ended_at (str):

        port_id (int):

        port_name (str):

        zone_id (int):

        zone_name (str):

        min_speed_observed (google.protobuf.wrappers_pb2.DoubleValue):

        duration_hours (google.protobuf.wrappers_pb2.DoubleValue):

        lat (float):

        lon (float):

        classification (str):

    """

    started_at: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ended_at: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port_id: int = proto.Field(
        proto.INT32,
        number=3,
    )
    port_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    zone_id: int = proto.Field(
        proto.INT32,
        number=5,
    )
    zone_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    min_speed_observed: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.DoubleValue,
    )
    duration_hours: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.DoubleValue,
    )
    lat: float = proto.Field(
        proto.DOUBLE,
        number=9,
    )
    lon: float = proto.Field(
        proto.DOUBLE,
        number=10,
    )
    classification: str = proto.Field(
        proto.STRING,
        number=11,
    )


class GetFleetLiveMapRequest(proto.Message):
    r"""GetFleetLiveMapRequest request object for getting static
    fleet map

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource
        map_theme (str):
            Specifies the map theme. Allowed values are: [light-v10,
            dark-v10, navigation-night-v1, navigation-day-v1,
            outdoors-v11, satellite-v9]
    """

    fleet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    map_theme: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFleetLiveMapResponse(proto.Message):
    r"""GetFleetLiveMapRequest request object for getting static
    fleet map

    Attributes:
        map_image (str):
            Static fleet map image URL
    """

    map_image: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetFleetListRequest(proto.Message):
    r"""Request object for parsing a file into a fleet

    Attributes:
        file_name (str):
            Original file name including file extension
        file (bytes):
            Serialized file data
        fleet_id (str):
            Fleet ID of existing fleet
        fleet_name (str):
            Name of existing fleet
        overwrite (bool):
            Specifies whether an existing fleet should be
            appended or overwritten
    """

    file_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    fleet_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    fleet_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    overwrite: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class EmptyParams(proto.Message):
    r"""Empty request object
    """


class EmptyResponse(proto.Message):
    r"""Empty response object
    """


__all__ = tuple(sorted(__protobuf__.manifest))
