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
    package='oceanbolt.com.fleetmanagement.v3',
    manifest={
        'RenameFleetRequest',
        'CreateFleetRequest',
        'DeleteFleetRequest',
        'GetFleetRequest',
        'ListVesselsRequest',
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
        'EmptyParams',
        'EmptyResponse',
    },
)


class RenameFleetRequest(proto.Message):
    r"""Request object for renaming a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            renamed
        new_fleet_name (str):
            The new name of the Fleet
    """

    fleet_id = proto.Field(proto.STRING, number=1)

    new_fleet_name = proto.Field(proto.STRING, number=2)


class CreateFleetRequest(proto.Message):
    r"""Request object for creating a Fleet

    Attributes:
        fleet_name (str):
            The new name of the Fleet
    """

    fleet_name = proto.Field(proto.STRING, number=2)


class DeleteFleetRequest(proto.Message):
    r"""Request object for deleting a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            deleted
    """

    fleet_id = proto.Field(proto.STRING, number=1)


class GetFleetRequest(proto.Message):
    r"""Request object for retrieving a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            retrieved
    """

    fleet_id = proto.Field(proto.STRING, number=1)


class ListVesselsRequest(proto.Message):
    r"""Request object for listing Vessels in a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be
            deleted
    """

    fleet_id = proto.Field(proto.STRING, number=1)


class ShareFleetRequest(proto.Message):
    r"""Request object for sharing a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource to be shared
    """

    fleet_id = proto.Field(proto.STRING, number=1)


class DropVesselsRequest(proto.Message):
    r"""Request object for dropping Vessels in a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where
            vessels should be dropped
    """

    fleet_id = proto.Field(proto.STRING, number=1)


class BatchVesselsRequest(proto.Message):
    r"""Request object for batch adding Vessels to a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where
            vessels should be added
        vessels (Sequence[oceanbolt.com.fleetmanagement_v3.types.VesselParams]):
            List of Vessels to be added
    """

    fleet_id = proto.Field(proto.STRING, number=1)

    vessels = proto.RepeatedField(proto.MESSAGE, number=2,
        message='VesselParams',
    )


class Fleets(proto.Message):
    r"""Response object for listing Fleets

    Attributes:
        fleets (Sequence[oceanbolt.com.fleetmanagement_v3.types.Fleet]):
            List of user defined Fleet resources
        organization_fleets (Sequence[oceanbolt.com.fleetmanagement_v3.types.Fleet]):
            List of organizational Fleet resources that
            are shared with the current user
        predefined_fleets (Sequence[oceanbolt.com.fleetmanagement_v3.types.Fleet]):
            List of system level predefined Fleet
            resources
    """

    fleets = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Fleet',
    )

    organization_fleets = proto.RepeatedField(proto.MESSAGE, number=2,
        message='Fleet',
    )

    predefined_fleets = proto.RepeatedField(proto.MESSAGE, number=3,
        message='Fleet',
    )


class Fleet(proto.Message):
    r"""Fleet resource

    Attributes:
        fleet_id (str):
            The Fleet identifier
        fleet_name (str):
            The name of the Fleet
        owner_user_id (str):
            The user id of the Fleet owner (the user who
            has created the Fleet)
        organization (str):
            The organization that the user belongs to
        vessels_in_fleet (google.protobuf.wrappers_pb2.Int32Value):
            The number of vessels in the Fleet
        vessels (Sequence[oceanbolt.com.fleetmanagement_v3.types.Vessel]):
            List of Vessels in the Fleet
        shared_with_org (google.protobuf.wrappers_pb2.BoolValue):
            A flag indicating whether this is a shared
            fleet.
    """

    fleet_id = proto.Field(proto.STRING, number=1)

    fleet_name = proto.Field(proto.STRING, number=2)

    owner_user_id = proto.Field(proto.STRING, number=3)

    organization = proto.Field(proto.STRING, number=6)

    vessels_in_fleet = proto.Field(proto.MESSAGE, number=4,
        message=wrappers.Int32Value,
    )

    vessels = proto.RepeatedField(proto.MESSAGE, number=5,
        message='Vessel',
    )

    shared_with_org = proto.Field(proto.MESSAGE, number=7,
        message=wrappers.BoolValue,
    )


class VesselParams(proto.Message):
    r"""Vessel parameters

    Attributes:
        imo (int):
            Imo of the vessel
        metadata (Sequence[oceanbolt.com.fleetmanagement_v3.types.VesselParams.MetadataEntry]):
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

    imo = proto.Field(proto.INT32, number=2)

    metadata = proto.MapField(proto.STRING, proto.STRING, number=3)


class UpdateVesselParams(proto.Message):
    r"""Parameter object for updating a vessel in a Fleet

    Attributes:
        metadata (Sequence[oceanbolt.com.fleetmanagement_v3.types.UpdateVesselParams.MetadataEntry]):
            New set of metadata information for a Vessel.
            This will overwrite existing keys/values
            currently stored in the metadata object of the
            Vessel.
    """

    metadata = proto.MapField(proto.STRING, proto.STRING, number=3)


class AddVesselRequest(proto.Message):
    r"""Request object for adding a Vessel to a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where
            vessels should be added
        vessel (oceanbolt.com.fleetmanagement_v3.types.VesselParams):
            Vessel params for the vessel that should be
            added
    """

    fleet_id = proto.Field(proto.STRING, number=1)

    vessel = proto.Field(proto.MESSAGE, number=2,
        message='VesselParams',
    )


class UpdateVesselRequest(proto.Message):
    r"""Request object for updating a vessel

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where the
            vessel should be updated
        imo (int):
            IMO number of the vessel to be updated
        vessel (oceanbolt.com.fleetmanagement_v3.types.UpdateVesselParams):
            New metadata object
        upsert (bool):
            Flag indicating whether the vessel should be
            created if it doesnt not already exist. If the
            upsert flag is set to false, and a vessel does
            not already exist, the function will return an
            error
    """

    fleet_id = proto.Field(proto.STRING, number=1)

    imo = proto.Field(proto.INT32, number=3)

    vessel = proto.Field(proto.MESSAGE, number=2,
        message='UpdateVesselParams',
    )

    upsert = proto.Field(proto.BOOL, number=4)


class DeleteVesselRequest(proto.Message):
    r"""Request object for deleting a single Vessel from a Fleet

    Attributes:
        fleet_id (str):
            Identifier of the Fleet resource where the
            vessel should be deleted
        imo (int):
            IMO number of the Vessel to be deleted
    """

    fleet_id = proto.Field(proto.STRING, number=1)

    imo = proto.Field(proto.INT32, number=2)


class Vessels(proto.Message):
    r"""List of Vessel objects

    Attributes:
        vessels (Sequence[oceanbolt.com.fleetmanagement_v3.types.Vessel]):
            List of vessels in Fleet
        vessels_in_fleet (int):
            Number of vessels in a Fleet
    """

    vessels = proto.RepeatedField(proto.MESSAGE, number=1,
        message='Vessel',
    )

    vessels_in_fleet = proto.Field(proto.INT32, number=2)


class Vessel(proto.Message):
    r"""Vessel object

    Attributes:
        imo (int):
            IMO number of the vessel
        dwt (float):
            DWT of the vessel
        built (int):
            The year the vessel was built
        vessel_name (str):
            Current name of the Vessel
        segment (str):
            Name of the segment which the vessel belongs
            to
        sub_segment (str):
            Flag code of the country where the vessel is
            currently registered
        flag_code (str):
            Flag code of the country where the vessel is
            currently registered
        ex_name (str):
            Ex name of the Vessel
        type_ (str):
            The type of the vessel
        metadata (Sequence[oceanbolt.com.fleetmanagement_v3.types.Vessel.MetadataEntry]):
            Metadata object that contains arbitratry data
            fields defined by the user
    """

    imo = proto.Field(proto.INT32, number=1)

    dwt = proto.Field(proto.DOUBLE, number=2)

    built = proto.Field(proto.INT32, number=3)

    vessel_name = proto.Field(proto.STRING, number=4)

    segment = proto.Field(proto.STRING, number=5)

    sub_segment = proto.Field(proto.STRING, number=10)

    flag_code = proto.Field(proto.STRING, number=6)

    ex_name = proto.Field(proto.STRING, number=7)

    type_ = proto.Field(proto.STRING, number=8)

    metadata = proto.MapField(proto.STRING, proto.STRING, number=9)


class EmptyParams(proto.Message):
    r"""Empty request object"""


class EmptyResponse(proto.Message):
    r"""Empty response object"""


__all__ = tuple(sorted(__protobuf__.manifest))
