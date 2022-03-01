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

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TradeFlowServiceAsyncClient: The constructed client.
        """
        return TradeFlowServiceClient.from_service_account_info.__func__(TradeFlowServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            TradeFlowServiceAsyncClient: The constructed client.
        """
        return TradeFlowServiceClient.from_service_account_file.__func__(TradeFlowServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return TradeFlowServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> TradeFlowServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            TradeFlowServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(TradeFlowServiceClient).get_transport_class, type(TradeFlowServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, TradeFlowServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the trade flow service client.

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
            request: Union[service.TradeFlowDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowsResponse:
        r"""GetVoyages retrieves all the individual voyages for
        the given filter parameters. Response is paginated, and
        endpoint accepts a paging parameter to specify which
        page to return. It is also possible to set the number of
        voyages to return per query.


        .. code-block:: python

            from oceanbolt.com import tradeflows_v3

            def sample_get_trade_flows():
                # Create a client
                client = tradeflows_v3.TradeFlowServiceClient()

                # Initialize request argument(s)
                request = tradeflows_v3.TradeFlowDataRequest(
                )

                # Make the request
                response = client.get_trade_flows(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest, dict]):
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
            request: Union[service.TradeFlowDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowAggregationResponse:
        r"""Aggregates tradeflow data across multiple dimensions.

        .. code-block:: python

            from oceanbolt.com import tradeflows_v3

            def sample_get_trade_flow_aggregation():
                # Create a client
                client = tradeflows_v3.TradeFlowServiceClient()

                # Initialize request argument(s)
                request = tradeflows_v3.TradeFlowDataRequest(
                )

                # Make the request
                response = client.get_trade_flow_aggregation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest, dict]):
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
            request: Union[service.TradeFlowDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowTimeseriesResponse:
        r"""Gets aggregated trade flow timeseries by period.

        .. code-block:: python

            from oceanbolt.com import tradeflows_v3

            def sample_get_trade_flow_timeseries():
                # Create a client
                client = tradeflows_v3.TradeFlowServiceClient()

                # Initialize request argument(s)
                request = tradeflows_v3.TradeFlowDataRequest(
                )

                # Make the request
                response = client.get_trade_flow_timeseries(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest, dict]):
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
            request: Union[service.TradeFlowDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowTimeseriesResponse:
        r"""Gets aggregated trade flow timeseries (on the water)
        by period.


        .. code-block:: python

            from oceanbolt.com import tradeflows_v3

            def sample_get_trade_flow_on_the_water():
                # Create a client
                client = tradeflows_v3.TradeFlowServiceClient()

                # Initialize request argument(s)
                request = tradeflows_v3.TradeFlowDataRequest(
                )

                # Make the request
                response = client.get_trade_flow_on_the_water(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest, dict]):
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
            request: Union[service.TradeFlowDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeFlowHistogramResponse:
        r"""GetTradeFlowHistogramValues gets trade flow histogram
        values by grouping.


        .. code-block:: python

            from oceanbolt.com import tradeflows_v3

            def sample_get_trade_flow_histogram():
                # Create a client
                client = tradeflows_v3.TradeFlowServiceClient()

                # Initialize request argument(s)
                request = tradeflows_v3.TradeFlowDataRequest(
                )

                # Make the request
                response = client.get_trade_flow_histogram(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest, dict]):
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
            request: Union[service.TradeFlowDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetLocationVolumeResponse:
        r"""GetLocationVolume gets location
        (port/berth/country/region) flow stats for the given
        filter parameters


        .. code-block:: python

            from oceanbolt.com import tradeflows_v3

            def sample_get_location_volume():
                # Create a client
                client = tradeflows_v3.TradeFlowServiceClient()

                # Initialize request argument(s)
                request = tradeflows_v3.TradeFlowDataRequest(
                )

                # Make the request
                response = client.get_location_volume(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest, dict]):
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
            request: Union[service.TradeFlowDataRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetTradeLaneMetricsResponse:
        r"""GetTradeflowModelVoyage gets trade flow model voyage
        values by grouping


        .. code-block:: python

            from oceanbolt.com import tradeflows_v3

            def sample_get_trade_lane_metrics():
                # Create a client
                client = tradeflows_v3.TradeFlowServiceClient()

                # Initialize request argument(s)
                request = tradeflows_v3.TradeFlowDataRequest(
                )

                # Make the request
                response = client.get_trade_lane_metrics(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest, dict]):
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

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "oceanbolt-com-tradeflows",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "TradeFlowServiceAsyncClient",
)
