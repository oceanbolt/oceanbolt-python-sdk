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
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1
from google.api_core import grpc_helpers_async
from google.auth import credentials as ga_credentials   # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc                        # type: ignore
from grpc.experimental import aio  # type: ignore

from oceanbolt.com.fleetmanagement_v3.types import service
from .base import FleetManagementServiceTransport, DEFAULT_CLIENT_INFO
from .grpc import FleetManagementServiceGrpcTransport


class FleetManagementServiceGrpcAsyncIOTransport(FleetManagementServiceTransport):
    """gRPC AsyncIO backend transport for FleetManagementService.

    FleetManagement provides service to manage fleets for clients

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(cls,
                       host: str = 'api.oceanbolt.com',
                       credentials: ga_credentials.Credentials = None,
                       credentials_file: Optional[str] = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    def __init__(self, *,
            host: str = 'api.oceanbolt.com',
            credentials: ga_credentials.Credentials = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            channel: aio.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id=None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def list_fleets(self) -> Callable[
            [service.EmptyParams],
            Awaitable[service.Fleets]]:
        r"""Return a callable for the list fleets method over gRPC.

        Lists Fleets for the current user (or fleets that are
        shared with the current user)

        Returns:
            Callable[[~.EmptyParams],
                    Awaitable[~.Fleets]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_fleets' not in self._stubs:
            self._stubs['list_fleets'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/ListFleets',
                request_serializer=service.EmptyParams.serialize,
                response_deserializer=service.Fleets.deserialize,
            )
        return self._stubs['list_fleets']

    @property
    def create_fleet(self) -> Callable[
            [service.CreateFleetRequest],
            Awaitable[service.Fleet]]:
        r"""Return a callable for the create fleet method over gRPC.

        Creates a new Fleet for the current user.

        Returns:
            Callable[[~.CreateFleetRequest],
                    Awaitable[~.Fleet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_fleet' not in self._stubs:
            self._stubs['create_fleet'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/CreateFleet',
                request_serializer=service.CreateFleetRequest.serialize,
                response_deserializer=service.Fleet.deserialize,
            )
        return self._stubs['create_fleet']

    @property
    def delete_fleet(self) -> Callable[
            [service.DeleteFleetRequest],
            Awaitable[service.EmptyResponse]]:
        r"""Return a callable for the delete fleet method over gRPC.

        Deletes a Fleet for the current user.

        Returns:
            Callable[[~.DeleteFleetRequest],
                    Awaitable[~.EmptyResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_fleet' not in self._stubs:
            self._stubs['delete_fleet'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/DeleteFleet',
                request_serializer=service.DeleteFleetRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['delete_fleet']

    @property
    def describe_fleet(self) -> Callable[
            [service.GetFleetRequest],
            Awaitable[service.Fleet]]:
        r"""Return a callable for the describe fleet method over gRPC.

        Retrieves fleet by Fleet id.

        Returns:
            Callable[[~.GetFleetRequest],
                    Awaitable[~.Fleet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'describe_fleet' not in self._stubs:
            self._stubs['describe_fleet'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/DescribeFleet',
                request_serializer=service.GetFleetRequest.serialize,
                response_deserializer=service.Fleet.deserialize,
            )
        return self._stubs['describe_fleet']

    @property
    def rename_fleet(self) -> Callable[
            [service.RenameFleetRequest],
            Awaitable[service.Fleet]]:
        r"""Return a callable for the rename fleet method over gRPC.

        Changes the name of a Fleet.

        Returns:
            Callable[[~.RenameFleetRequest],
                    Awaitable[~.Fleet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'rename_fleet' not in self._stubs:
            self._stubs['rename_fleet'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/RenameFleet',
                request_serializer=service.RenameFleetRequest.serialize,
                response_deserializer=service.Fleet.deserialize,
            )
        return self._stubs['rename_fleet']

    @property
    def share_fleet(self) -> Callable[
            [service.ShareFleetRequest],
            Awaitable[service.Fleet]]:
        r"""Return a callable for the share fleet method over gRPC.

        Sets the shared status of the Fleet to be shared.

        Returns:
            Callable[[~.ShareFleetRequest],
                    Awaitable[~.Fleet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'share_fleet' not in self._stubs:
            self._stubs['share_fleet'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/ShareFleet',
                request_serializer=service.ShareFleetRequest.serialize,
                response_deserializer=service.Fleet.deserialize,
            )
        return self._stubs['share_fleet']

    @property
    def unshare_fleet(self) -> Callable[
            [service.ShareFleetRequest],
            Awaitable[service.Fleet]]:
        r"""Return a callable for the unshare fleet method over gRPC.

        Sets the shared status of the Fleet to be not shared.

        Returns:
            Callable[[~.ShareFleetRequest],
                    Awaitable[~.Fleet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'unshare_fleet' not in self._stubs:
            self._stubs['unshare_fleet'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/UnshareFleet',
                request_serializer=service.ShareFleetRequest.serialize,
                response_deserializer=service.Fleet.deserialize,
            )
        return self._stubs['unshare_fleet']

    @property
    def list_vessels(self) -> Callable[
            [service.ListVesselsRequest],
            Awaitable[service.Vessels]]:
        r"""Return a callable for the list vessels method over gRPC.

        Retrieves list of vessels in a Fleet.

        Returns:
            Callable[[~.ListVesselsRequest],
                    Awaitable[~.Vessels]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_vessels' not in self._stubs:
            self._stubs['list_vessels'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/ListVessels',
                request_serializer=service.ListVesselsRequest.serialize,
                response_deserializer=service.Vessels.deserialize,
            )
        return self._stubs['list_vessels']

    @property
    def list_vessels_with_status(self) -> Callable[
            [service.ListVesselsWithStatusRequest],
            Awaitable[service.Vessels]]:
        r"""Return a callable for the list vessels with status method over gRPC.

        Retrieves list of vessels in a Fleet.

        Returns:
            Callable[[~.ListVesselsWithStatusRequest],
                    Awaitable[~.Vessels]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_vessels_with_status' not in self._stubs:
            self._stubs['list_vessels_with_status'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/ListVesselsWithStatus',
                request_serializer=service.ListVesselsWithStatusRequest.serialize,
                response_deserializer=service.Vessels.deserialize,
            )
        return self._stubs['list_vessels_with_status']

    @property
    def add_vessel(self) -> Callable[
            [service.AddVesselRequest],
            Awaitable[service.Vessel]]:
        r"""Return a callable for the add vessel method over gRPC.

        Adds new vessel to a Fleet. A maximum of 1000 vessels
        can be added to a fleet.

        Returns:
            Callable[[~.AddVesselRequest],
                    Awaitable[~.Vessel]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'add_vessel' not in self._stubs:
            self._stubs['add_vessel'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/AddVessel',
                request_serializer=service.AddVesselRequest.serialize,
                response_deserializer=service.Vessel.deserialize,
            )
        return self._stubs['add_vessel']

    @property
    def update_vessel(self) -> Callable[
            [service.UpdateVesselRequest],
            Awaitable[service.Vessel]]:
        r"""Return a callable for the update vessel method over gRPC.

        Updates existing metadata for a Vessel.

        Returns:
            Callable[[~.UpdateVesselRequest],
                    Awaitable[~.Vessel]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_vessel' not in self._stubs:
            self._stubs['update_vessel'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/UpdateVessel',
                request_serializer=service.UpdateVesselRequest.serialize,
                response_deserializer=service.Vessel.deserialize,
            )
        return self._stubs['update_vessel']

    @property
    def delete_vessel(self) -> Callable[
            [service.DeleteVesselRequest],
            Awaitable[service.EmptyResponse]]:
        r"""Return a callable for the delete vessel method over gRPC.

        Removes a vessel from a Fleet.

        Returns:
            Callable[[~.DeleteVesselRequest],
                    Awaitable[~.EmptyResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_vessel' not in self._stubs:
            self._stubs['delete_vessel'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/DeleteVessel',
                request_serializer=service.DeleteVesselRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['delete_vessel']

    @property
    def batch_add_vessels(self) -> Callable[
            [service.BatchVesselsRequest],
            Awaitable[service.EmptyResponse]]:
        r"""Return a callable for the batch add vessels method over gRPC.

        Batch adds vessels into a Fleet. A maximum of 1000
        vessels can be added to a fleet.

        Returns:
            Callable[[~.BatchVesselsRequest],
                    Awaitable[~.EmptyResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'batch_add_vessels' not in self._stubs:
            self._stubs['batch_add_vessels'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/BatchAddVessels',
                request_serializer=service.BatchVesselsRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['batch_add_vessels']

    @property
    def replace_vessels(self) -> Callable[
            [service.BatchVesselsRequest],
            Awaitable[service.EmptyResponse]]:
        r"""Return a callable for the replace vessels method over gRPC.

        Replaces the existing vessels in a Fleet with a batch
        of new vessels. This is equivalent to first calling
        DropVessels and then calling BatchAddVessels A maximum
        of 1000 vessels can be added to a fleet.

        Returns:
            Callable[[~.BatchVesselsRequest],
                    Awaitable[~.EmptyResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'replace_vessels' not in self._stubs:
            self._stubs['replace_vessels'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/ReplaceVessels',
                request_serializer=service.BatchVesselsRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['replace_vessels']

    @property
    def drop_vessels(self) -> Callable[
            [service.DropVesselsRequest],
            Awaitable[service.EmptyResponse]]:
        r"""Return a callable for the drop vessels method over gRPC.

        Drops all the vessels currently in a fleet.

        Returns:
            Callable[[~.DropVesselsRequest],
                    Awaitable[~.EmptyResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'drop_vessels' not in self._stubs:
            self._stubs['drop_vessels'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/DropVessels',
                request_serializer=service.DropVesselsRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['drop_vessels']

    @property
    def get_fleet_live_map(self) -> Callable[
            [service.GetFleetLiveMapRequest],
            Awaitable[service.GetFleetLiveMapResponse]]:
        r"""Return a callable for the get fleet live map method over gRPC.

        GetFleetLiveMap display static location for vessels
        in a fleet (as static image).

        Returns:
            Callable[[~.GetFleetLiveMapRequest],
                    Awaitable[~.GetFleetLiveMapResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_fleet_live_map' not in self._stubs:
            self._stubs['get_fleet_live_map'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/GetFleetLiveMap',
                request_serializer=service.GetFleetLiveMapRequest.serialize,
                response_deserializer=service.GetFleetLiveMapResponse.deserialize,
            )
        return self._stubs['get_fleet_live_map']

    @property
    def upload_fleet_list(self) -> Callable[
            [service.GetFleetListRequest],
            Awaitable[service.EmptyResponse]]:
        r"""Return a callable for the upload fleet list method over gRPC.

        Uploads file containing fleet data to be parsed into
        a batch of vessels.

        Returns:
            Callable[[~.GetFleetListRequest],
                    Awaitable[~.EmptyResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'upload_fleet_list' not in self._stubs:
            self._stubs['upload_fleet_list'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.fleetmanagement.v3.FleetManagementService/UploadFleetList',
                request_serializer=service.GetFleetListRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['upload_fleet_list']

    def close(self):
        return self.grpc_channel.close()


__all__ = (
    'FleetManagementServiceGrpcAsyncIOTransport',
)
