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

from oceanbolt.com.tonnage_v3.types import service

from .transports.base import TonnageServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import TonnageServiceGrpcAsyncIOTransport
from .client import TonnageServiceClient


class TonnageServiceAsyncClient:
    """TonnageService provides am API service to get tonnage data"""

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

    from_service_account_info = TonnageServiceClient.from_service_account_info
    from_service_account_file = TonnageServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> TonnageServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            TonnageServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(TonnageServiceClient).get_transport_class, type(TonnageServiceClient))

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, TonnageServiceTransport] = 'grpc_asyncio',
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiate the tonnage service client.

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
            request: service.GetTonnageDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageZoneCountResponse:
        r"""Fetches tonnage counts timeseries.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest`):
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
            request: service.GetTonnageDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetFleetSpeedResponse:
        r"""Fetches fleet speed timeseries.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest`):
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
            request: service.GetTonnageDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetGlobalTonnageStatusResponse:
        r"""Fetches global tonnage status timeseries.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest`):
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
            request: service.GetTonnageFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageFleetStatusResponse:
        r"""Provides fleet status timeseries of how the fleet
        have developed over time. This timeseries shows number
        of active vessels on the water at any given time.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.GetTonnageFleetRequest`):
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
            request: service.GetTonnageFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageFleetGrowthResponse:
        r"""Provides fleet growth timeseries of how the fleet
        have developed over time. This timeseries shows number
        of vessels added to/removed from the fleet during any
        given period.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.GetTonnageFleetRequest`):
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
            request: service.TonnageChineseWatersRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.TonnageChineseWatersResponse:
        r"""Provides chinese waters tonnage timeseries data. This
        timeseries shows the number of Chinese flagged that are
        trading inside and outside of Chinese waters
        respectively.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.TonnageChineseWatersRequest`):
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
            request: service.GetTonnageZoneChangesRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageZoneChangesResponse:
        r"""Provides timeseries data on the number of vessels
        that cross zone boundaries during any given period.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.GetTonnageZoneChangesRequest`):
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
            request: service.GetTonnageBasinRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTonnageBasinResponse:
        r"""Provides timeseries data on the number of vessels
        that are within the four major basins.

        Args:
            request (:class:`oceanbolt.com.tonnage_v3.types.GetTonnageBasinRequest`):
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







try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'oceanbolt-com-tonnage',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    'TonnageServiceAsyncClient',
)
