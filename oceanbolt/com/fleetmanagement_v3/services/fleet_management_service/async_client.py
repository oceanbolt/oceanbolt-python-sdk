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

from google.protobuf import wrappers_pb2 as wrappers  # type: ignore
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

    from_service_account_info = FleetManagementServiceClient.from_service_account_info
    from_service_account_file = FleetManagementServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> FleetManagementServiceTransport:
        """Return the transport used by the client instance.

        Returns:
            FleetManagementServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(FleetManagementServiceClient).get_transport_class, type(FleetManagementServiceClient))

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, FleetManagementServiceTransport] = 'grpc_asyncio',
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiate the fleet management service client.

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
            request: service.EmptyParams = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleets:
        r"""Lists Fleets for the current user (or fleets that are
        shared with the current user)

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.EmptyParams`):
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
            request: service.CreateFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Creates a new Fleet for the current user.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.CreateFleetRequest`):
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
            request: service.DeleteFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Deletes a Fleet for the current user.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.DeleteFleetRequest`):
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
            request: service.GetFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Retrieves fleet by Fleet id.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.GetFleetRequest`):
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
            request: service.RenameFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Changes the name of a Fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.RenameFleetRequest`):
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
            request: service.ShareFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Sets the shared status of the Fleet to be shared.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.ShareFleetRequest`):
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
            request: service.ShareFleetRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Fleet:
        r"""Sets the shared status of the Fleet to be not shared.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.ShareFleetRequest`):
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
            request: service.ListVesselsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessels:
        r"""Retrieves list of vessels in a Fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.ListVesselsRequest`):
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
            request: service.ListVesselsWithStatusRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessels:
        r"""Retrieves list of vessels in a Fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.ListVesselsWithStatusRequest`):
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
            request: service.AddVesselRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessel:
        r"""Adds new vessel to a Fleet. A maximum of 1000 vessels
        can be added to a fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.AddVesselRequest`):
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
            request: service.UpdateVesselRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Vessel:
        r"""Updates existing metadata for a Vessel.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.UpdateVesselRequest`):
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
            request: service.DeleteVesselRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Removes a vessel from a Fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.DeleteVesselRequest`):
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
            request: service.BatchVesselsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Batch adds vessels into a Fleet. A maximum of 1000
        vessels can be added to a fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.BatchVesselsRequest`):
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
            request: service.BatchVesselsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Replaces the existing vessels in a Fleet with a batch
        of new vessels. This is equivalent to first calling
        DropVessels and then calling BatchAddVessels A maximum
        of 1000 vessels can be added to a fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.BatchVesselsRequest`):
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
            request: service.DropVesselsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""Drops all the vessels currently in a fleet.

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.DropVesselsRequest`):
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
            request: service.GetFleetLiveMapRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.GetFleetLiveMapResponse:
        r"""GetFleetLiveMap display static location for vessels
        in a fleet (as static image).

        Args:
            request (:class:`oceanbolt.com.fleetmanagement_v3.types.GetFleetLiveMapRequest`):
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







try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'oceanbolt-com-fleetmanagement',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    'FleetManagementServiceAsyncClient',
)
