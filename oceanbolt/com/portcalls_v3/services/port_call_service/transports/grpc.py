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
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import gapic_v1
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from oceanbolt.com.portcalls_v3.types import service
from .base import PortCallServiceTransport, DEFAULT_CLIENT_INFO


class PortCallServiceGrpcTransport(PortCallServiceTransport):
    """gRPC backend transport for PortCallService.

    PortCallService provides an API service to get PortCall data

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'api.oceanbolt.com',
            credentials: ga_credentials.Credentials = None,
            credentials_file: str = None,
            scopes: Sequence[str] = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id: Optional[str] = None,
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
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
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
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
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

    @classmethod
    def create_channel(cls,
                       host: str = 'api.oceanbolt.com',
                       credentials: ga_credentials.Credentials = None,
                       credentials_file: str = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
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

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def get_port_calls(self) -> Callable[
            [service.GetPortCallsRequest],
            service.GetPortCallsResponse]:
        r"""Return a callable for the get port calls method over gRPC.

        ListPortCalls retrieves lists all port calls for a
        set of request params. Response is paginated, and
        endpoint accepts a paging parameter to specify which
        page to return. It is also possible to set the number of
        port calls to return per query, default is 50 and
        maximum is 2000.

        Returns:
            Callable[[~.GetPortCallsRequest],
                    ~.GetPortCallsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_port_calls' not in self._stubs:
            self._stubs['get_port_calls'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.portcalls.v3.PortCallService/GetPortCalls',
                request_serializer=service.GetPortCallsRequest.serialize,
                response_deserializer=service.GetPortCallsResponse.deserialize,
            )
        return self._stubs['get_port_calls']

    @property
    def get_port_call_timeseries(self) -> Callable[
            [service.GetPortCallsRequest],
            service.GetPortCallTimeseriesResponse]:
        r"""Return a callable for the get port call timeseries method over gRPC.

        GetPortCallTimeseries retrieves aggregated counts for
        port calls for a set of request params.

        Returns:
            Callable[[~.GetPortCallsRequest],
                    ~.GetPortCallTimeseriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_port_call_timeseries' not in self._stubs:
            self._stubs['get_port_call_timeseries'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.portcalls.v3.PortCallService/GetPortCallTimeseries',
                request_serializer=service.GetPortCallsRequest.serialize,
                response_deserializer=service.GetPortCallTimeseriesResponse.deserialize,
            )
        return self._stubs['get_port_call_timeseries']

    @property
    def get_port_particulars(self) -> Callable[
            [service.GetPortParticularsRequest],
            service.GetPortParticularsResponse]:
        r"""Return a callable for the get port particulars method over gRPC.

        ListPortCalls retrieves lists all port calls for a
        given vessel. Response is paginated, and endpoint
        accepts a paging parameter to specify which page to
        return. It is also possible to set the number of port
        calls to return per query, default is 50 and maximum is
        2000.

        Returns:
            Callable[[~.GetPortParticularsRequest],
                    ~.GetPortParticularsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_port_particulars' not in self._stubs:
            self._stubs['get_port_particulars'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.portcalls.v3.PortCallService/GetPortParticulars',
                request_serializer=service.GetPortParticularsRequest.serialize,
                response_deserializer=service.GetPortParticularsResponse.deserialize,
            )
        return self._stubs['get_port_particulars']

    @property
    def get_vessels_in_port(self) -> Callable[
            [service.GetVesselsInPortRequest],
            service.GetVesselsInPortResponse]:
        r"""Return a callable for the get vessels in port method over gRPC.

        GetVesselsInPort lists all vessels that were within a
        port (or related anchorages) at a certain time.

        Returns:
            Callable[[~.GetVesselsInPortRequest],
                    ~.GetVesselsInPortResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_vessels_in_port' not in self._stubs:
            self._stubs['get_vessels_in_port'] = self.grpc_channel.unary_unary(
                '/oceanbolt.com.portcalls.v3.PortCallService/GetVesselsInPort',
                request_serializer=service.GetVesselsInPortRequest.serialize,
                response_deserializer=service.GetVesselsInPortResponse.deserialize,
            )
        return self._stubs['get_vessels_in_port']

    def close(self):
        self.grpc_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = (
    'PortCallServiceGrpcTransport',
)
