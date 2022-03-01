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

from oceanbolt.com.tonnage_v3.types import service
from .transports.base import TonnageServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import TonnageServiceGrpcAsyncIOTransport
from .client import TonnageServiceClient


class TonnageServiceAsyncClient:
    """TonnageService provides an API service to get tonnage data"""

    _client: TonnageServiceClient

    DEFAULT_ENDPOINT = TonnageServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = TonnageServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(TonnageServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(TonnageServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(TonnageServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(TonnageServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(TonnageServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(TonnageServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(TonnageServiceClient.common_project_path)
    parse_common_project_path = staticmethod(TonnageServiceClient.parse_common_project_path)
    common_location_path = staticmethod(TonnageServiceClient.common_location_path)
    parse_common_location_path = staticmethod(TonnageServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TonnageServiceAsyncClient: The constructed client.
        """
        return TonnageServiceClient.from_service_account_info.__func__(TonnageServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            TonnageServiceAsyncClient: The constructed client.
        """
        return TonnageServiceClient.from_service_account_file.__func__(TonnageServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return TonnageServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> TonnageServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            TonnageServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(TonnageServiceClient).get_transport_class, type(TonnageServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, TonnageServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the tonnage service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.TonnageServiceTransport]): The
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
        self._client = TonnageServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def get_tonnage_zone_count(self,
            request: Union[service.GetTonnageDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageZoneCountResponse:
        r"""Fetches tonnage counts timeseries.

        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_tonnage_zone_count():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.GetTonnageDataRequest(
                )

                # Make the request
                response = client.get_tonnage_zone_count(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest, dict]):
                The request object. Request object for getting tonnage
                zone data and fleet speed data.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.GetTonnageZoneCountResponse:
                Response object for tonnage zone
                counts

        """
        # Create or coerce a protobuf request object.
        request = service.GetTonnageDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tonnage_zone_count,
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

    async def get_tonnage_fleet_speed(self,
            request: Union[service.GetTonnageDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetFleetSpeedResponse:
        r"""Fetches fleet speed timeseries.

        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_tonnage_fleet_speed():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.GetTonnageDataRequest(
                )

                # Make the request
                response = client.get_tonnage_fleet_speed(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest, dict]):
                The request object. Request object for getting tonnage
                zone data and fleet speed data.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.GetFleetSpeedResponse:
                Response object for FleetSpeed
        """
        # Create or coerce a protobuf request object.
        request = service.GetTonnageDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tonnage_fleet_speed,
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

    async def get_global_tonnage_status(self,
            request: Union[service.GetTonnageDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetGlobalTonnageStatusResponse:
        r"""Fetches global tonnage status timeseries.

        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_global_tonnage_status():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.GetTonnageDataRequest(
                )

                # Make the request
                response = client.get_global_tonnage_status(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest, dict]):
                The request object. Request object for getting tonnage
                zone data and fleet speed data.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.GetGlobalTonnageStatusResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.GetTonnageDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_global_tonnage_status,
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

    async def get_tonnage_fleet_status(self,
            request: Union[service.GetTonnageFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageFleetStatusResponse:
        r"""Provides fleet status timeseries of how the fleet
        have developed over time. This timeseries shows number
        of active vessels on the water at any given time.


        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_tonnage_fleet_status():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.GetTonnageFleetRequest(
                )

                # Make the request
                response = client.get_tonnage_fleet_status(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.GetTonnageFleetRequest, dict]):
                The request object. Request object for
                GetTonnageFleetStatus and GetTonnageFleetGrowth
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.GetTonnageFleetStatusResponse:
                Response object for
                GetTonnageFleetStatus

        """
        # Create or coerce a protobuf request object.
        request = service.GetTonnageFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tonnage_fleet_status,
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

    async def get_tonnage_fleet_growth(self,
            request: Union[service.GetTonnageFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageFleetGrowthResponse:
        r"""Provides fleet growth timeseries of how the fleet
        have developed over time. This timeseries shows number
        of vessels added to/removed from the fleet during any
        given period.


        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_tonnage_fleet_growth():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.GetTonnageFleetRequest(
                )

                # Make the request
                response = client.get_tonnage_fleet_growth(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.GetTonnageFleetRequest, dict]):
                The request object. Request object for
                GetTonnageFleetStatus and GetTonnageFleetGrowth
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.GetTonnageFleetGrowthResponse:
                Response object for
                GetTonnageFleetGrowth

        """
        # Create or coerce a protobuf request object.
        request = service.GetTonnageFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tonnage_fleet_growth,
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

    async def get_tonnage_chinese_waters(self,
            request: Union[service.TonnageChineseWatersRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.TonnageChineseWatersResponse:
        r"""Provides chinese waters tonnage timeseries data. This
        timeseries shows the number of Chinese flagged that are
        trading inside and outside of Chinese waters
        respectively.


        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_tonnage_chinese_waters():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.TonnageChineseWatersRequest(
                )

                # Make the request
                response = client.get_tonnage_chinese_waters(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.TonnageChineseWatersRequest, dict]):
                The request object. Request object for
                TonnageChineseWaters
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.TonnageChineseWatersResponse:
                Response object for
                TonnageChineseWaters

        """
        # Create or coerce a protobuf request object.
        request = service.TonnageChineseWatersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tonnage_chinese_waters,
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

    async def get_tonnage_zone_changes(self,
            request: Union[service.GetTonnageZoneChangesRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageZoneChangesResponse:
        r"""Provides timeseries data on the number of vessels
        that cross zone boundaries during any given period.


        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_tonnage_zone_changes():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.GetTonnageZoneChangesRequest(
                )

                # Make the request
                response = client.get_tonnage_zone_changes(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.GetTonnageZoneChangesRequest, dict]):
                The request object. Request object for TonnageZoneChange
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.GetTonnageZoneChangesResponse:
                Response object for TonnageZoneChange
        """
        # Create or coerce a protobuf request object.
        request = service.GetTonnageZoneChangesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tonnage_zone_changes,
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

    async def get_tonnage_basin_count(self,
            request: Union[service.GetTonnageBasinRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageBasinResponse:
        r"""Provides timeseries data on the number of vessels
        that are within the four major basins.


        .. code-block:: python

            from oceanbolt.com import tonnage_v3

            def sample_get_tonnage_basin_count():
                # Create a client
                client = tonnage_v3.TonnageServiceClient()

                # Initialize request argument(s)
                request = tonnage_v3.GetTonnageBasinRequest(
                )

                # Make the request
                response = client.get_tonnage_basin_count(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tonnage_v3.types.GetTonnageBasinRequest, dict]):
                The request object. GetTonnageBasin
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tonnage_v3.types.GetTonnageBasinResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.GetTonnageBasinRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tonnage_basin_count,
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
            "oceanbolt-com-tonnage",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "TonnageServiceAsyncClient",
)
