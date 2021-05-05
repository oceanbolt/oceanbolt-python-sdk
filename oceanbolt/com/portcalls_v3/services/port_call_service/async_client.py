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

from oceanbolt.com.portcalls_v3.types import service

from .transports.base import PortCallServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import PortCallServiceGrpcAsyncIOTransport
from .client import PortCallServiceClient


class PortCallServiceAsyncClient:
    """PortCallService provides an API service to get PortCall data"""

    _client: PortCallServiceClient

    DEFAULT_ENDPOINT = PortCallServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PortCallServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(PortCallServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(PortCallServiceClient.parse_common_billing_account_path)

    common_folder_path = staticmethod(PortCallServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(PortCallServiceClient.parse_common_folder_path)

    common_organization_path = staticmethod(PortCallServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(PortCallServiceClient.parse_common_organization_path)

    common_project_path = staticmethod(PortCallServiceClient.common_project_path)
    parse_common_project_path = staticmethod(PortCallServiceClient.parse_common_project_path)

    common_location_path = staticmethod(PortCallServiceClient.common_location_path)
    parse_common_location_path = staticmethod(PortCallServiceClient.parse_common_location_path)

    from_service_account_info = PortCallServiceClient.from_service_account_info
    from_service_account_file = PortCallServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> PortCallServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            PortCallServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(PortCallServiceClient).get_transport_class, type(PortCallServiceClient))

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, PortCallServiceTransport] = 'grpc_asyncio',
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiate the port call service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PortCallServiceTransport]): The
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

        self._client = PortCallServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def get_port_calls(self,
            request: service.GetPortCallsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetPortCallsResponse:
        r"""ListPortCalls retrieves lists all port calls for a
        set of request params. Response is paginated, and
        endpoint accepts a paging parameter to specify which
        page to return. It is also possible to set the number of
        port calls to return per query, default is 50 and
        maximum is 2000.

        Args:
            request (:class:`oceanbolt.com.portcalls_v3.types.GetPortCallsRequest`):
                The request object. Port calls data requests object.
                This is shared between all port calls queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.portcalls_v3.types.GetPortCallsResponse:
                Response object for port call queries
        """
        # Create or coerce a protobuf request object.

        request = service.GetPortCallsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_port_calls,
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

    async def get_port_call_timeseries(self,
            request: service.GetPortCallsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetPortCallTimeseriesResponse:
        r"""GetPortCallTimeseries retrieves aggregated counts for
        port calls for a set of request params.

        Args:
            request (:class:`oceanbolt.com.portcalls_v3.types.GetPortCallsRequest`):
                The request object. Port calls data requests object.
                This is shared between all port calls queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.portcalls_v3.types.GetPortCallTimeseriesResponse:
                Response object for port call
                timeseries queries

        """
        # Create or coerce a protobuf request object.

        request = service.GetPortCallsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_port_call_timeseries,
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

    async def get_port_particulars(self,
            request: service.GetPortParticularsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetPortParticularsResponse:
        r"""ListPortCalls retrieves lists all port calls for a
        given vessel. Response is paginated, and endpoint
        accepts a paging parameter to specify which page to
        return. It is also possible to set the number of port
        calls to return per query, default is 50 and maximum is
        2000.

        Args:
            request (:class:`oceanbolt.com.portcalls_v3.types.GetPortParticularsRequest`):
                The request object. Request object for
                GetPortParticulars

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.portcalls_v3.types.GetPortParticularsResponse:
                Response object for
                GetPortParticulars

        """
        # Create or coerce a protobuf request object.

        request = service.GetPortParticularsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_port_particulars,
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
            'oceanbolt-com-portcalls',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    'PortCallServiceAsyncClient',
)
