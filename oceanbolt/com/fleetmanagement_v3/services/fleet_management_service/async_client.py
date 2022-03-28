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

from google.protobuf import wrappers_pb2  # type: ignore
from oceanbolt.com.fleetmanagement_v3.types import service
from .transports.base import FleetManagementServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import FleetManagementServiceGrpcAsyncIOTransport
from .client import FleetManagementServiceClient


class FleetManagementServiceAsyncClient:
    """FleetManagement provides service to manage fleets for clients"""

    _client: FleetManagementServiceClient

    DEFAULT_ENDPOINT = FleetManagementServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = FleetManagementServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(FleetManagementServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(FleetManagementServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(FleetManagementServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(FleetManagementServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(FleetManagementServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(FleetManagementServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(FleetManagementServiceClient.common_project_path)
    parse_common_project_path = staticmethod(FleetManagementServiceClient.parse_common_project_path)
    common_location_path = staticmethod(FleetManagementServiceClient.common_location_path)
    parse_common_location_path = staticmethod(FleetManagementServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            FleetManagementServiceAsyncClient: The constructed client.
        """
        return FleetManagementServiceClient.from_service_account_info.__func__(FleetManagementServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            FleetManagementServiceAsyncClient: The constructed client.
        """
        return FleetManagementServiceClient.from_service_account_file.__func__(FleetManagementServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return FleetManagementServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> FleetManagementServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            FleetManagementServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(FleetManagementServiceClient).get_transport_class, type(FleetManagementServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, FleetManagementServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the fleet management service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.FleetManagementServiceTransport]): The
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
        self._client = FleetManagementServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def list_fleets(self,
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleets:
        r"""Lists Fleets for the current user (or fleets that are
        shared with the current user)


        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_list_fleets():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.EmptyParams(
                )

                # Make the request
                response = client.list_fleets(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.EmptyParams, dict]):
                The request object. Empty request object
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Fleets:
                Response object for listing Fleets
        """
        # Create or coerce a protobuf request object.
        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_fleets,
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

    async def create_fleet(self,
            request: Union[service.CreateFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Creates a new Fleet for the current user.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_create_fleet():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.CreateFleetRequest(
                )

                # Make the request
                response = client.create_fleet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.CreateFleetRequest, dict]):
                The request object. Request object for creating a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Fleet:
                Fleet resource
        """
        # Create or coerce a protobuf request object.
        request = service.CreateFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_fleet,
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

    async def delete_fleet(self,
            request: Union[service.DeleteFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Deletes a Fleet for the current user.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_delete_fleet():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.DeleteFleetRequest(
                )

                # Make the request
                response = client.delete_fleet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.DeleteFleetRequest, dict]):
                The request object. Request object for deleting a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.EmptyResponse:
                Empty response object
        """
        # Create or coerce a protobuf request object.
        request = service.DeleteFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_fleet,
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

    async def describe_fleet(self,
            request: Union[service.GetFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Retrieves fleet by Fleet id.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_describe_fleet():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.GetFleetRequest(
                )

                # Make the request
                response = client.describe_fleet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.GetFleetRequest, dict]):
                The request object. Request object for retrieving a
                Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Fleet:
                Fleet resource
        """
        # Create or coerce a protobuf request object.
        request = service.GetFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.describe_fleet,
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

    async def rename_fleet(self,
            request: Union[service.RenameFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Changes the name of a Fleet.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_rename_fleet():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.RenameFleetRequest(
                )

                # Make the request
                response = client.rename_fleet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.RenameFleetRequest, dict]):
                The request object. Request object for renaming a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Fleet:
                Fleet resource
        """
        # Create or coerce a protobuf request object.
        request = service.RenameFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.rename_fleet,
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

    async def share_fleet(self,
            request: Union[service.ShareFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Sets the shared status of the Fleet to be shared.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_share_fleet():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.ShareFleetRequest(
                )

                # Make the request
                response = client.share_fleet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.ShareFleetRequest, dict]):
                The request object. Request object for sharing a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Fleet:
                Fleet resource
        """
        # Create or coerce a protobuf request object.
        request = service.ShareFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.share_fleet,
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

    async def unshare_fleet(self,
            request: Union[service.ShareFleetRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Sets the shared status of the Fleet to be not shared.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_unshare_fleet():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.ShareFleetRequest(
                )

                # Make the request
                response = client.unshare_fleet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.ShareFleetRequest, dict]):
                The request object. Request object for sharing a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Fleet:
                Fleet resource
        """
        # Create or coerce a protobuf request object.
        request = service.ShareFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.unshare_fleet,
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

    async def list_vessels(self,
            request: Union[service.ListVesselsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessels:
        r"""Retrieves list of vessels in a Fleet.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_list_vessels():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.ListVesselsRequest(
                )

                # Make the request
                response = client.list_vessels(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.ListVesselsRequest, dict]):
                The request object. Request object for listing Vessels
                in a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Vessels:
                List of Vessel objects
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

    async def list_vessels_with_status(self,
            request: Union[service.ListVesselsWithStatusRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessels:
        r"""Retrieves list of vessels in a Fleet.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_list_vessels_with_status():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.ListVesselsWithStatusRequest(
                )

                # Make the request
                response = client.list_vessels_with_status(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.ListVesselsWithStatusRequest, dict]):
                The request object. Request object for listing Fleet
                Vessels with status (live state) data and speed events
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Vessels:
                List of Vessel objects
        """
        # Create or coerce a protobuf request object.
        request = service.ListVesselsWithStatusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_vessels_with_status,
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

    async def add_vessel(self,
            request: Union[service.AddVesselRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessel:
        r"""Adds new vessel to a Fleet. A maximum of 1000 vessels
        can be added to a fleet.


        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_add_vessel():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.AddVesselRequest(
                )

                # Make the request
                response = client.add_vessel(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.AddVesselRequest, dict]):
                The request object. Request object for adding a Vessel
                to a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Vessel:
                Vessel object
        """
        # Create or coerce a protobuf request object.
        request = service.AddVesselRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.add_vessel,
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

    async def update_vessel(self,
            request: Union[service.UpdateVesselRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessel:
        r"""Updates existing metadata for a Vessel.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_update_vessel():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.UpdateVesselRequest(
                )

                # Make the request
                response = client.update_vessel(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.UpdateVesselRequest, dict]):
                The request object. Request object for updating a vessel
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.Vessel:
                Vessel object
        """
        # Create or coerce a protobuf request object.
        request = service.UpdateVesselRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_vessel,
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

    async def delete_vessel(self,
            request: Union[service.DeleteVesselRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Removes a vessel from a Fleet.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_delete_vessel():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.DeleteVesselRequest(
                )

                # Make the request
                response = client.delete_vessel(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.DeleteVesselRequest, dict]):
                The request object. Request object for deleting a single
                Vessel from a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.EmptyResponse:
                Empty response object
        """
        # Create or coerce a protobuf request object.
        request = service.DeleteVesselRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_vessel,
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

    async def batch_add_vessels(self,
            request: Union[service.BatchVesselsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Batch adds vessels into a Fleet. A maximum of 1000
        vessels can be added to a fleet.


        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_batch_add_vessels():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.BatchVesselsRequest(
                )

                # Make the request
                response = client.batch_add_vessels(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.BatchVesselsRequest, dict]):
                The request object. Request object for batch adding
                Vessels to a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.EmptyResponse:
                Empty response object
        """
        # Create or coerce a protobuf request object.
        request = service.BatchVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_add_vessels,
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

    async def replace_vessels(self,
            request: Union[service.BatchVesselsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Replaces the existing vessels in a Fleet with a batch
        of new vessels. This is equivalent to first calling
        DropVessels and then calling BatchAddVessels A maximum
        of 1000 vessels can be added to a fleet.


        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_replace_vessels():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.BatchVesselsRequest(
                )

                # Make the request
                response = client.replace_vessels(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.BatchVesselsRequest, dict]):
                The request object. Request object for batch adding
                Vessels to a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.EmptyResponse:
                Empty response object
        """
        # Create or coerce a protobuf request object.
        request = service.BatchVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.replace_vessels,
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

    async def drop_vessels(self,
            request: Union[service.DropVesselsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Drops all the vessels currently in a fleet.

        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_drop_vessels():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.DropVesselsRequest(
                )

                # Make the request
                response = client.drop_vessels(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.DropVesselsRequest, dict]):
                The request object. Request object for dropping Vessels
                in a Fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.EmptyResponse:
                Empty response object
        """
        # Create or coerce a protobuf request object.
        request = service.DropVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.drop_vessels,
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

    async def get_fleet_live_map(self,
            request: Union[service.GetFleetLiveMapRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetFleetLiveMapResponse:
        r"""GetFleetLiveMap display static location for vessels
        in a fleet (as static image).


        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_get_fleet_live_map():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.GetFleetLiveMapRequest(
                )

                # Make the request
                response = client.get_fleet_live_map(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.GetFleetLiveMapRequest, dict]):
                The request object. GetFleetLiveMapRequest request
                object for getting static fleet map
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.GetFleetLiveMapResponse:
                GetFleetLiveMapRequest request object
                for getting static fleet map

        """
        # Create or coerce a protobuf request object.
        request = service.GetFleetLiveMapRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_fleet_live_map,
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

    async def upload_fleet_list(self,
            request: Union[service.GetFleetListRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Uploads file containing fleet data to be parsed into
        a batch of vessels.


        .. code-block:: python

            from oceanbolt.com import fleetmanagement_v3

            def sample_upload_fleet_list():
                # Create a client
                client = fleetmanagement_v3.FleetManagementServiceClient()

                # Initialize request argument(s)
                request = fleetmanagement_v3.GetFleetListRequest(
                )

                # Make the request
                response = client.upload_fleet_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.fleetmanagement_v3.types.GetFleetListRequest, dict]):
                The request object. Request object for parsing a file
                into a fleet
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.fleetmanagement_v3.types.EmptyResponse:
                Empty response object
        """
        # Create or coerce a protobuf request object.
        request = service.GetFleetListRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.upload_fleet_list,
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
            "oceanbolt-com-fleetmanagement",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "FleetManagementServiceAsyncClient",
)
