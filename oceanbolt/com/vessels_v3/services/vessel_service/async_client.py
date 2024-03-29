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
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union

from oceanbolt.com.vessels_v3 import gapic_version as package_version

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

from google.protobuf import timestamp_pb2  # type: ignore
from oceanbolt.com.vessels_v3.types import service
from .transports.base import VesselServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import VesselServiceGrpcAsyncIOTransport
from .client import VesselServiceClient


class VesselServiceAsyncClient:
    """VesselService provides service to get vessel data"""

    _client: VesselServiceClient

    DEFAULT_ENDPOINT = VesselServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = VesselServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(VesselServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(VesselServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(VesselServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(VesselServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(VesselServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(VesselServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(VesselServiceClient.common_project_path)
    parse_common_project_path = staticmethod(VesselServiceClient.parse_common_project_path)
    common_location_path = staticmethod(VesselServiceClient.common_location_path)
    parse_common_location_path = staticmethod(VesselServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            VesselServiceAsyncClient: The constructed client.
        """
        return VesselServiceClient.from_service_account_info.__func__(VesselServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            VesselServiceAsyncClient: The constructed client.
        """
        return VesselServiceClient.from_service_account_file.__func__(VesselServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        default mTLS endpoint; if the environment variable is "never", use the default API
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
        return VesselServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> VesselServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            VesselServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(VesselServiceClient).get_transport_class, type(VesselServiceClient))

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Union[str, VesselServiceTransport] = "grpc_asyncio",
            client_options: Optional[ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the vessel service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.VesselServiceTransport]): The
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
        self._client = VesselServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def list_vessels(self,
            request: Optional[Union[service.ListVesselsRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListVesselsResponse:
        r"""Vessels gets a list of vessels for the given filter
        parameters

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from oceanbolt.com import vessels_v3

            async def sample_list_vessels():
                # Create a client
                client = vessels_v3.VesselServiceAsyncClient()

                # Initialize request argument(s)
                request = vessels_v3.ListVesselsRequest(
                )

                # Make the request
                response = await client.list_vessels(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[oceanbolt.com.vessels_v3.types.ListVesselsRequest, dict]]):
                The request object. Vessels
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.vessels_v3.types.ListVesselsResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.ListVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_vessels,
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

    async def list_stoppage_events(self,
            request: Optional[Union[service.ListStoppageEventsRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListStoppageEventsResponse:
        r"""Fetches ais based stoppage events for a single vessel

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from oceanbolt.com import vessels_v3

            async def sample_list_stoppage_events():
                # Create a client
                client = vessels_v3.VesselServiceAsyncClient()

                # Initialize request argument(s)
                request = vessels_v3.ListStoppageEventsRequest(
                )

                # Make the request
                response = await client.list_stoppage_events(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[oceanbolt.com.vessels_v3.types.ListStoppageEventsRequest, dict]]):
                The request object. VesselStoppageEvents
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.vessels_v3.types.ListStoppageEventsResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.ListStoppageEventsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_stoppage_events,
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

    async def list_dark_period_events(self,
            request: Optional[Union[service.ListDarkPeriodEventsRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.ListDarkPeriodEventsResponse:
        r"""Fetches ais based dark period events for a single
        vessel. A dark period event, is where a vessel has not
        transmitted AIS data for a period greater than 6 hours.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from oceanbolt.com import vessels_v3

            async def sample_list_dark_period_events():
                # Create a client
                client = vessels_v3.VesselServiceAsyncClient()

                # Initialize request argument(s)
                request = vessels_v3.ListDarkPeriodEventsRequest(
                )

                # Make the request
                response = await client.list_dark_period_events(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[oceanbolt.com.vessels_v3.types.ListDarkPeriodEventsRequest, dict]]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.vessels_v3.types.ListDarkPeriodEventsResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.ListDarkPeriodEventsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_dark_period_events,
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

    async def get_ais_summary(self,
            request: Optional[Union[service.GetAisSummaryRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetAisSummaryResponse:
        r"""Generates summary data regarding AIS received during
        a specific requested period for a single vessel

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from oceanbolt.com import vessels_v3

            async def sample_get_ais_summary():
                # Create a client
                client = vessels_v3.VesselServiceAsyncClient()

                # Initialize request argument(s)
                request = vessels_v3.GetAisSummaryRequest(
                )

                # Make the request
                response = await client.get_ais_summary(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[oceanbolt.com.vessels_v3.types.GetAisSummaryRequest, dict]]):
                The request object. Request object for
                GetAisSummaryRequest
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.vessels_v3.types.GetAisSummaryResponse:
                Request object for
                GetAisSummaryResponse

        """
        # Create or coerce a protobuf request object.
        request = service.GetAisSummaryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_ais_summary,
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

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


__all__ = (
    "VesselServiceAsyncClient",
)
