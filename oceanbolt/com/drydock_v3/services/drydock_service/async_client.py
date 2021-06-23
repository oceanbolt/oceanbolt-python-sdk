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

from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions # type: ignore
from google.api_core import exceptions                 # type: ignore
from google.api_core import gapic_v1                   # type: ignore
from google.api_core import retry as retries           # type: ignore
from google.auth import credentials                    # type: ignore
from google.oauth2 import service_account              # type: ignore

from oceanbolt.com.drydock_v3.types import service

from .transports.base import DrydockServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import DrydockServiceGrpcAsyncIOTransport
from .client import DrydockServiceClient


class DrydockServiceAsyncClient:
    """DryDockService provides service to get dry dock data"""

    _client: DrydockServiceClient

    DEFAULT_ENDPOINT = DrydockServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DrydockServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(DrydockServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(DrydockServiceClient.parse_common_billing_account_path)

    common_folder_path = staticmethod(DrydockServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(DrydockServiceClient.parse_common_folder_path)

    common_organization_path = staticmethod(DrydockServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(DrydockServiceClient.parse_common_organization_path)

    common_project_path = staticmethod(DrydockServiceClient.common_project_path)
    parse_common_project_path = staticmethod(DrydockServiceClient.parse_common_project_path)

    common_location_path = staticmethod(DrydockServiceClient.common_location_path)
    parse_common_location_path = staticmethod(DrydockServiceClient.parse_common_location_path)

    from_service_account_info = DrydockServiceClient.from_service_account_info
    from_service_account_file = DrydockServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> DrydockServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            DrydockServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(DrydockServiceClient).get_transport_class, type(DrydockServiceClient))

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, DrydockServiceTransport] = 'grpc_asyncio',
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiate the drydock service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DrydockServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """

        self._client = DrydockServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def get_dry_dock_stays(self,
            request: service.GetDryDockStaysRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetDryDockStaysResponse:
        r"""GetDryDockStays retrives individual historical dry
        dock stays

        Args:
            request (:class:`oceanbolt.com.drydock_v3.types.GetDryDockStaysRequest`):
                The request object. DryDockstays

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.drydock_v3.types.GetDryDockStaysResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.GetDryDockStaysRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_dry_dock_stays,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_dry_dock_timeseries(self,
            request: service.GetDryDockRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.DryDockResponse:
        r"""GetDryDockTimeseries retrieves dry dock timeseries data for a
        specified list of port_ids/segments

        Args:
            request (:class:`oceanbolt.com.drydock_v3.types.GetDryDockRequest`):
                The request object. DryDock request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.drydock_v3.types.DryDockResponse:
                DryDock responseobject.
        """
        # Create or coerce a protobuf request object.

        request = service.GetDryDockRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_dry_dock_timeseries,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_dry_dock_web(self,
            request: service.GetDryDockRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.DryDockResponse:
        r"""GetDryDockWeb retrieves current and live dry dock data for a
        specified list of port_ids/segments

        Args:
            request (:class:`oceanbolt.com.drydock_v3.types.GetDryDockRequest`):
                The request object. DryDock request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.drydock_v3.types.DryDockResponse:
                DryDock responseobject.
        """
        # Create or coerce a protobuf request object.

        request = service.GetDryDockRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_dry_dock_web,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_dry_dock_vessels(self,
            request: service.GetDryDockRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.DryDockResponse:
        r"""GetDryDockVessels retrieves list of currently active dry dock
        stays for a specified list of port_ids/segments

        Args:
            request (:class:`oceanbolt.com.drydock_v3.types.GetDryDockRequest`):
                The request object. DryDock request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.drydock_v3.types.DryDockResponse:
                DryDock responseobject.
        """
        # Create or coerce a protobuf request object.

        request = service.GetDryDockRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_dry_dock_vessels,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response







try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'oceanbolt-com-drydock',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    'DrydockServiceAsyncClient',
)
