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

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers   # type: ignore
from google.api_core import gapic_v1       # type: ignore
from google import auth                    # type: ignore
from google.auth import credentials        # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from oceanbolt.com.polygonmanagement_v3.types import service

from .base import PolygonManagementServiceTransport, DEFAULT_CLIENT_INFO


class PolygonManagementServiceGrpcTransport(PolygonManagementServiceTransport):
    """gRPC backend transport for PolygonManagementService.

    LayerManagement provides service to manage layers for clients

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'api.oceanbolt.com',
            credentials: credentials.Credentials = None,
            credentials_file: str = None,
            scopes: Sequence[str] = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._ssl_channel_credentials = ssl_channel_credentials

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        elif api_mtls_endpoint:
            host = api_mtls_endpoint if ":" in api_mtls_endpoint else api_mtls_endpoint + ":443"

            if credentials is None:
                credentials, _ = auth.default(scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id)

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            self._ssl_channel_credentials = ssl_credentials
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id)

            if client_cert_source_for_mtls and not ssl_channel_credentials:
                cert, key = client_cert_source_for_mtls()
                self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=self._ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        self._stubs = {}  # type: Dict[str, Callable]

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

    @classmethod
    def create_channel(cls,
                       host: str = 'api.oceanbolt.com',
                       credentials: credentials.Credentials = None,
                       credentials_file: str = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def list_layers(self) -> Callable[
            [service.EmptyParams],
            service.Layers]:
        r"""Return a callable for the list layers method over gRPC.

        ListLayers lists layers for the current user

        Returns:
            Callable[[~.EmptyParams],
                    ~.Layers]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_layers' not in self._stubs:
            self._stubs['list_layers'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/ListLayers',
                request_serializer=service.EmptyParams.serialize,
                response_deserializer=service.Layers.deserialize,
            )
        return self._stubs['list_layers']

    @property
    def create_layer(self) -> Callable[
            [service.CreateLayerRequest],
            service.Layer]:
        r"""Return a callable for the create layer method over gRPC.

        CreateLayer creates new layer for the current user

        Returns:
            Callable[[~.CreateLayerRequest],
                    ~.Layer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_layer' not in self._stubs:
            self._stubs['create_layer'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/CreateLayer',
                request_serializer=service.CreateLayerRequest.serialize,
                response_deserializer=service.Layer.deserialize,
            )
        return self._stubs['create_layer']

    @property
    def delete_layer(self) -> Callable[
            [service.DeleteLayerRequest],
            service.EmptyResponse]:
        r"""Return a callable for the delete layer method over gRPC.

        DeleteLayer deletes layer for the current user

        Returns:
            Callable[[~.DeleteLayerRequest],
                    ~.EmptyResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_layer' not in self._stubs:
            self._stubs['delete_layer'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/DeleteLayer',
                request_serializer=service.DeleteLayerRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['delete_layer']

    @property
    def describe_layer(self) -> Callable[
            [service.GetLayerRequest],
            service.Layer]:
        r"""Return a callable for the describe layer method over gRPC.

        GetLayer gets fleed by layer id for the current user

        Returns:
            Callable[[~.GetLayerRequest],
                    ~.Layer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'describe_layer' not in self._stubs:
            self._stubs['describe_layer'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/DescribeLayer',
                request_serializer=service.GetLayerRequest.serialize,
                response_deserializer=service.Layer.deserialize,
            )
        return self._stubs['describe_layer']

    @property
    def rename_layer(self) -> Callable[
            [service.RenameLayerRequest],
            service.Layer]:
        r"""Return a callable for the rename layer method over gRPC.

        RenameLayer changes the name of the layer for the
        current user

        Returns:
            Callable[[~.RenameLayerRequest],
                    ~.Layer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'rename_layer' not in self._stubs:
            self._stubs['rename_layer'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/RenameLayer',
                request_serializer=service.RenameLayerRequest.serialize,
                response_deserializer=service.Layer.deserialize,
            )
        return self._stubs['rename_layer']

    @property
    def share_layer(self) -> Callable[
            [service.ShareLayerRequest],
            service.Layer]:
        r"""Return a callable for the share layer method over gRPC.

        Sets the shared status of the layer to be either
        shared/not shared

        Returns:
            Callable[[~.ShareLayerRequest],
                    ~.Layer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'share_layer' not in self._stubs:
            self._stubs['share_layer'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/ShareLayer',
                request_serializer=service.ShareLayerRequest.serialize,
                response_deserializer=service.Layer.deserialize,
            )
        return self._stubs['share_layer']

    @property
    def unshare_layer(self) -> Callable[
            [service.ShareLayerRequest],
            service.Layer]:
        r"""Return a callable for the unshare layer method over gRPC.

        Sets the shared status of the layer to be either
        shared/not shared

        Returns:
            Callable[[~.ShareLayerRequest],
                    ~.Layer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'unshare_layer' not in self._stubs:
            self._stubs['unshare_layer'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/UnshareLayer',
                request_serializer=service.ShareLayerRequest.serialize,
                response_deserializer=service.Layer.deserialize,
            )
        return self._stubs['unshare_layer']

    @property
    def list_polygons(self) -> Callable[
            [service.ListPolygonsRequest],
            service.Polygons]:
        r"""Return a callable for the list polygons method over gRPC.

        GetLayerPolygons gets layer polygons for the current
        user

        Returns:
            Callable[[~.ListPolygonsRequest],
                    ~.Polygons]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_polygons' not in self._stubs:
            self._stubs['list_polygons'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/ListPolygons',
                request_serializer=service.ListPolygonsRequest.serialize,
                response_deserializer=service.Polygons.deserialize,
            )
        return self._stubs['list_polygons']

    @property
    def add_polygon(self) -> Callable[
            [service.AddPolygonRequest],
            service.Polygon]:
        r"""Return a callable for the add polygon method over gRPC.

        AddPolygon adds new vessel to user's layer

        Returns:
            Callable[[~.AddPolygonRequest],
                    ~.Polygon]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'add_polygon' not in self._stubs:
            self._stubs['add_polygon'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/AddPolygon',
                request_serializer=service.AddPolygonRequest.serialize,
                response_deserializer=service.Polygon.deserialize,
            )
        return self._stubs['add_polygon']

    @property
    def update_polygon(self) -> Callable[
            [service.UpdatePolygonRequest],
            service.Polygon]:
        r"""Return a callable for the update polygon method over gRPC.

        UpdatePolygon updates existing vessel to user's layer

        Returns:
            Callable[[~.UpdatePolygonRequest],
                    ~.Polygon]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_polygon' not in self._stubs:
            self._stubs['update_polygon'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/UpdatePolygon',
                request_serializer=service.UpdatePolygonRequest.serialize,
                response_deserializer=service.Polygon.deserialize,
            )
        return self._stubs['update_polygon']

    @property
    def delete_polygon(self) -> Callable[
            [service.DeletePolygonRequest],
            service.EmptyResponse]:
        r"""Return a callable for the delete polygon method over gRPC.

        DeletePolygon removes vessel from user's layer

        Returns:
            Callable[[~.DeletePolygonRequest],
                    ~.EmptyResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_polygon' not in self._stubs:
            self._stubs['delete_polygon'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/DeletePolygon',
                request_serializer=service.DeletePolygonRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['delete_polygon']

    @property
    def batch_add_polygons(self) -> Callable[
            [service.BatchPolygonsRequest],
            service.EmptyResponse]:
        r"""Return a callable for the batch add polygons method over gRPC.

        Returns:
            Callable[[~.BatchPolygonsRequest],
                    ~.EmptyResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'batch_add_polygons' not in self._stubs:
            self._stubs['batch_add_polygons'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/BatchAddPolygons',
                request_serializer=service.BatchPolygonsRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['batch_add_polygons']

    @property
    def replace_polygons(self) -> Callable[
            [service.BatchPolygonsRequest],
            service.EmptyResponse]:
        r"""Return a callable for the replace polygons method over gRPC.

        Returns:
            Callable[[~.BatchPolygonsRequest],
                    ~.EmptyResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'replace_polygons' not in self._stubs:
            self._stubs['replace_polygons'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/ReplacePolygons',
                request_serializer=service.BatchPolygonsRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['replace_polygons']

    @property
    def drop_polygons(self) -> Callable[
            [service.DropPolygonsRequest],
            service.EmptyResponse]:
        r"""Return a callable for the drop polygons method over gRPC.

        Returns:
            Callable[[~.DropPolygonsRequest],
                    ~.EmptyResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'drop_polygons' not in self._stubs:
            self._stubs['drop_polygons'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.polygonmanagement.v3.PolygonManagementService/DropPolygons',
                request_serializer=service.DropPolygonsRequest.serialize,
                response_deserializer=service.EmptyResponse.deserialize,
            )
        return self._stubs['drop_polygons']


__all__ = (
    'PolygonManagementServiceGrpcTransport',
)
