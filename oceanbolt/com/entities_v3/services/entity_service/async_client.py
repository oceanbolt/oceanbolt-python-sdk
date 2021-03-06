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

from oceanbolt.com.entities_v3.types import service

from .transports.base import EntityServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import EntityServiceGrpcAsyncIOTransport
from .client import EntityServiceClient


class EntityServiceAsyncClient:
    """TradeflowService provides service to get tradeflow data."""

    _client: EntityServiceClient

    DEFAULT_ENDPOINT = EntityServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = EntityServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(EntityServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(EntityServiceClient.parse_common_billing_account_path)

    common_folder_path = staticmethod(EntityServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(EntityServiceClient.parse_common_folder_path)

    common_organization_path = staticmethod(EntityServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(EntityServiceClient.parse_common_organization_path)

    common_project_path = staticmethod(EntityServiceClient.common_project_path)
    parse_common_project_path = staticmethod(EntityServiceClient.parse_common_project_path)

    common_location_path = staticmethod(EntityServiceClient.common_location_path)
    parse_common_location_path = staticmethod(EntityServiceClient.parse_common_location_path)

    from_service_account_info = EntityServiceClient.from_service_account_info
    from_service_account_file = EntityServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> EntityServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            EntityServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(EntityServiceClient).get_transport_class, type(EntityServiceClient))

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, EntityServiceTransport] = 'grpc_asyncio',
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiate the entity service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.EntityServiceTransport]): The
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

        self._client = EntityServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def list_segments(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListSegmentsResponse:
        r"""ListSegments retrieves all available vessel segments

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListSegmentsResponse:
                ListSegments
        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_segments,
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

    async def list_zones(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListTonnageZonesResponse:
        r"""ListZones retrieves all zones

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListTonnageZonesResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_zones,
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

    async def list_zones_with_polygons(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListTonnageZonesWithPolygonsResponse:
        r"""ListZonesWithPolygons retrieves all zones with
        Polygons

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListTonnageZonesWithPolygonsResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_zones_with_polygons,
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

    async def list_regions(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListRegionsResponse:
        r"""ListRegions retrives all regions

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListRegionsResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_regions,
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

    async def list_commodities(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListCommoditiesResponse:
        r"""ListCommodities retrives all commodities

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListCommoditiesResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_commodities,
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

    async def list_countries(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListCountriesResponse:
        r"""ListCountries retrives all countries

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListCountriesResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_countries,
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

    async def list_regions_with_polygons(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListRegionsWithPolygonResponse:
        r"""ListRegionsWithPolygons retrives all regions with geo
        polygons

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListRegionsWithPolygonResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_regions_with_polygons,
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

    async def list_ports(self,
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListPortsResponse:
        r"""ListPorts retrieves all ports

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.EmptyParams`):
                The request object.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.ListPortsResponse:
                List Ports
        """
        # Create or coerce a protobuf request object.

        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_ports,
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

    async def search_polygons(self,
            request: service.SearchRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.SearchPolygonsResponse:
        r"""

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.SearchRequest`):
                The request object. Search

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.SearchPolygonsResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.SearchRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_polygons,
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

    async def search_vessels(self,
            request: service.SearchRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.SearchVesselsResponse:
        r"""

        Args:
            request (:class:`oceanbolt.com.entities_v3.types.SearchRequest`):
                The request object. Search

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.entities_v3.types.SearchVesselsResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.SearchRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_vessels,
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
            'oceanbolt-com-entities',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    'EntityServiceAsyncClient',
)
