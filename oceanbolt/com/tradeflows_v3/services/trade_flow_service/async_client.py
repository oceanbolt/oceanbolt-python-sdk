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

from oceanbolt.com.tradeflows_v3.types import service

from .transports.base import TradeFlowServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import TradeFlowServiceGrpcAsyncIOTransport
from .client import TradeFlowServiceClient


class TradeFlowServiceAsyncClient:
    """TradeFlowService provides service to get tradeflow data."""

    _client: TradeFlowServiceClient

    DEFAULT_ENDPOINT = TradeFlowServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = TradeFlowServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(TradeFlowServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(TradeFlowServiceClient.parse_common_billing_account_path)

    common_folder_path = staticmethod(TradeFlowServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(TradeFlowServiceClient.parse_common_folder_path)

    common_organization_path = staticmethod(TradeFlowServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(TradeFlowServiceClient.parse_common_organization_path)

    common_project_path = staticmethod(TradeFlowServiceClient.common_project_path)
    parse_common_project_path = staticmethod(TradeFlowServiceClient.parse_common_project_path)

    common_location_path = staticmethod(TradeFlowServiceClient.common_location_path)
    parse_common_location_path = staticmethod(TradeFlowServiceClient.parse_common_location_path)

    from_service_account_info = TradeFlowServiceClient.from_service_account_info
    from_service_account_file = TradeFlowServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> TradeFlowServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            TradeFlowServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(TradeFlowServiceClient).get_transport_class, type(TradeFlowServiceClient))

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, TradeFlowServiceTransport] = 'grpc_asyncio',
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiate the trade flow service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.TradeFlowServiceTransport]): The
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

        self._client = TradeFlowServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def get_trade_flows(self,
            request: service.TradeFlowDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowsResponse:
        r"""GetVoyages retrieves all the individual voyages for
        the given filter parameters. Response is paginated, and
        endpoint accepts a paging parameter to specify which
        page to return. It is also possible to set the number of
        voyages to return per query.

        Args:
            request (:class:`oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest`):
                The request object. Trade flow data requests object.
                This is shared between all trade flows queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tradeflows_v3.types.GetTradeFlowsResponse:
                Response object for trade flow
                queries

        """
        # Create or coerce a protobuf request object.

        request = service.TradeFlowDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_trade_flows,
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

    async def get_trade_flow_aggregation(self,
            request: service.TradeFlowDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowAggregationResponse:
        r"""Aggregates tradeflow data across multiple dimensions.

        Args:
            request (:class:`oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest`):
                The request object. Trade flow data requests object.
                This is shared between all trade flows queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tradeflows_v3.types.GetTradeFlowAggregationResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.TradeFlowDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_trade_flow_aggregation,
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

    async def get_trade_flow_timeseries(self,
            request: service.TradeFlowDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowTimeseriesResponse:
        r"""Gets aggregated trade flow timeseries by period.

        Args:
            request (:class:`oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest`):
                The request object. Trade flow data requests object.
                This is shared between all trade flows queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tradeflows_v3.types.GetTradeFlowTimeseriesResponse:
                Response object for trade flow
                timeseries queries

        """
        # Create or coerce a protobuf request object.

        request = service.TradeFlowDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_trade_flow_timeseries,
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

    async def get_trade_flow_on_the_water(self,
            request: service.TradeFlowDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowTimeseriesResponse:
        r"""Gets aggregated trade flow timeseries (on the water)
        by period.

        Args:
            request (:class:`oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest`):
                The request object. Trade flow data requests object.
                This is shared between all trade flows queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tradeflows_v3.types.GetTradeFlowTimeseriesResponse:
                Response object for trade flow
                timeseries queries

        """
        # Create or coerce a protobuf request object.

        request = service.TradeFlowDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_trade_flow_on_the_water,
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

    async def get_trade_flow_histogram(self,
            request: service.TradeFlowDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowHistogramResponse:
        r"""GetTradeFlowHistogramValues gets trade flow histogram
        values by grouping.

        Args:
            request (:class:`oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest`):
                The request object. Trade flow data requests object.
                This is shared between all trade flows queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tradeflows_v3.types.GetTradeFlowHistogramResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.TradeFlowDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_trade_flow_histogram,
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

    async def get_location_volume(self,
            request: service.TradeFlowDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetLocationVolumeResponse:
        r"""GetLocationVolume gets location
        (port/berth/country/region) flow stats for the given
        filter parameters

        Args:
            request (:class:`oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest`):
                The request object. Trade flow data requests object.
                This is shared between all trade flows queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tradeflows_v3.types.GetLocationVolumeResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.TradeFlowDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_location_volume,
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

    async def get_trade_lane_metrics(self,
            request: service.TradeFlowDataRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeLaneMetricsResponse:
        r"""GetTradeflowModelVoyage gets trade flow model voyage
        values by grouping

        Args:
            request (:class:`oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest`):
                The request object. Trade flow data requests object.
                This is shared between all trade flows queries

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.tradeflows_v3.types.GetTradeLaneMetricsResponse:

        """
        # Create or coerce a protobuf request object.

        request = service.TradeFlowDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_trade_lane_metrics,
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
            'oceanbolt-com-tradeflows',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    'TradeFlowServiceAsyncClient',
)
