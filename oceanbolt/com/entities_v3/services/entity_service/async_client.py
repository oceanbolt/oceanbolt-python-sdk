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
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

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

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EntityServiceAsyncClient: The constructed client.
        """
        return EntityServiceClient.from_service_account_info.__func__(EntityServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EntityServiceAsyncClient: The constructed client.
        """
        return EntityServiceClient.from_service_account_file.__func__(EntityServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return EntityServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> EntityServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            EntityServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(EntityServiceClient).get_transport_class, type(EntityServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, EntityServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the entity service client.

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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListSegmentsResponse:
        r"""ListSegments retrieves all available vessel segments

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_segments():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_segments(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListTonnageZonesResponse:
        r"""ListZones retrieves all zones

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_zones():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_zones(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListTonnageZonesWithPolygonsResponse:
        r"""ListZonesWithPolygons retrieves all zones with
        Polygons


        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_zones_with_polygons():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_zones_with_polygons(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListRegionsResponse:
        r"""ListRegions retrives all regions

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_regions():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_regions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListCommoditiesResponse:
        r"""ListCommodities retrives all commodities

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_commodities():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_commodities(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListCountriesResponse:
        r"""ListCountries retrives all countries

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_countries():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_countries(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListRegionsWithPolygonResponse:
        r"""ListRegionsWithPolygons retrives all regions with geo
        polygons


        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_regions_with_polygons():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_regions_with_polygons(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListPortsResponse:
        r"""ListPorts retrieves all ports

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_list_ports():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.EmptyParams(
                )

                # Make the request
                response = client.list_ports(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.EmptyParams, dict]):
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
            request: Union[service.SearchRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.SearchPolygonsResponse:
        r"""

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_search_polygons():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.SearchRequest(
                )

                # Make the request
                response = client.search_polygons(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.SearchRequest, dict]):
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
            request: Union[service.SearchRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.SearchVesselsResponse:
        r"""

        .. code-block:: python

            from oceanbolt.com import entities_v3

            def sample_search_vessels():
                # Create a client
                client = entities_v3.EntityServiceClient()

                # Initialize request argument(s)
                request = entities_v3.SearchRequest(
                )

                # Make the request
                response = client.search_vessels(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.entities_v3.types.SearchRequest, dict]):
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

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "oceanbolt-com-entities",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "EntityServiceAsyncClient",
)
