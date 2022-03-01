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
from oceanbolt.com.polygonmanagement_v3.types import service
from .transports.base import PolygonManagementServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import PolygonManagementServiceGrpcAsyncIOTransport
from .client import PolygonManagementServiceClient


class PolygonManagementServiceAsyncClient:
    """LayerManagement provides service to manage layers for clients"""

    _client: PolygonManagementServiceClient

    DEFAULT_ENDPOINT = PolygonManagementServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PolygonManagementServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(PolygonManagementServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(PolygonManagementServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(PolygonManagementServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(PolygonManagementServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(PolygonManagementServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(PolygonManagementServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(PolygonManagementServiceClient.common_project_path)
    parse_common_project_path = staticmethod(PolygonManagementServiceClient.parse_common_project_path)
    common_location_path = staticmethod(PolygonManagementServiceClient.common_location_path)
    parse_common_location_path = staticmethod(PolygonManagementServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PolygonManagementServiceAsyncClient: The constructed client.
        """
        return PolygonManagementServiceClient.from_service_account_info.__func__(PolygonManagementServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            PolygonManagementServiceAsyncClient: The constructed client.
        """
        return PolygonManagementServiceClient.from_service_account_file.__func__(PolygonManagementServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return PolygonManagementServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> PolygonManagementServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            PolygonManagementServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(PolygonManagementServiceClient).get_transport_class, type(PolygonManagementServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, PolygonManagementServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the polygon management service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PolygonManagementServiceTransport]): The
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
        self._client = PolygonManagementServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def list_layers(self,
            request: Union[service.EmptyParams, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Layers:
        r"""ListLayers lists layers for the current user

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_list_layers():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.EmptyParams(
                )

                # Make the request
                response = client.list_layers(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.EmptyParams, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Layers:

        """
        # Create or coerce a protobuf request object.
        request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_layers,
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

    async def create_layer(self,
            request: Union[service.CreateLayerRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Layer:
        r"""CreateLayer creates new layer for the current user

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_create_layer():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.CreateLayerRequest(
                )

                # Make the request
                response = client.create_layer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.CreateLayerRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Layer:

        """
        # Create or coerce a protobuf request object.
        request = service.CreateLayerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_layer,
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

    async def delete_layer(self,
            request: Union[service.DeleteLayerRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""DeleteLayer deletes layer for the current user

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_delete_layer():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.DeleteLayerRequest(
                )

                # Make the request
                response = client.delete_layer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.DeleteLayerRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.EmptyResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.DeleteLayerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_layer,
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

    async def describe_layer(self,
            request: Union[service.GetLayerRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Layer:
        r"""GetLayer gets fleed by layer id for the current user

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_describe_layer():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.GetLayerRequest(
                )

                # Make the request
                response = client.describe_layer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.GetLayerRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Layer:

        """
        # Create or coerce a protobuf request object.
        request = service.GetLayerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.describe_layer,
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

    async def rename_layer(self,
            request: Union[service.RenameLayerRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Layer:
        r"""RenameLayer changes the name of the layer for the
        current user


        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_rename_layer():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.RenameLayerRequest(
                )

                # Make the request
                response = client.rename_layer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.RenameLayerRequest, dict]):
                The request object.  LayerManagement requests ans
                responses
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Layer:

        """
        # Create or coerce a protobuf request object.
        request = service.RenameLayerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.rename_layer,
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

    async def share_layer(self,
            request: Union[service.ShareLayerRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Layer:
        r"""Sets the shared status of the layer to be either
        shared/not shared


        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_share_layer():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.ShareLayerRequest(
                )

                # Make the request
                response = client.share_layer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.ShareLayerRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Layer:

        """
        # Create or coerce a protobuf request object.
        request = service.ShareLayerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.share_layer,
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

    async def unshare_layer(self,
            request: Union[service.ShareLayerRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Layer:
        r"""Sets the shared status of the layer to be either
        shared/not shared


        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_unshare_layer():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.ShareLayerRequest(
                )

                # Make the request
                response = client.unshare_layer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.ShareLayerRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Layer:

        """
        # Create or coerce a protobuf request object.
        request = service.ShareLayerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.unshare_layer,
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

    async def list_polygons(self,
            request: Union[service.ListPolygonsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Polygons:
        r"""GetLayerPolygons gets layer polygons for the current
        user


        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_list_polygons():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.ListPolygonsRequest(
                )

                # Make the request
                response = client.list_polygons(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.ListPolygonsRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Polygons:

        """
        # Create or coerce a protobuf request object.
        request = service.ListPolygonsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_polygons,
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

    async def add_polygon(self,
            request: Union[service.AddPolygonRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Polygon:
        r"""AddPolygon adds new vessel to user's layer

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_add_polygon():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.AddPolygonRequest(
                )

                # Make the request
                response = client.add_polygon(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.AddPolygonRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Polygon:

        """
        # Create or coerce a protobuf request object.
        request = service.AddPolygonRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.add_polygon,
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

    async def update_polygon(self,
            request: Union[service.UpdatePolygonRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Polygon:
        r"""UpdatePolygon updates existing vessel to user's layer

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_update_polygon():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.UpdatePolygonRequest(
                )

                # Make the request
                response = client.update_polygon(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.UpdatePolygonRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.Polygon:

        """
        # Create or coerce a protobuf request object.
        request = service.UpdatePolygonRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_polygon,
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

    async def delete_polygon(self,
            request: Union[service.DeletePolygonRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""DeletePolygon removes vessel from user's layer

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_delete_polygon():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.DeletePolygonRequest(
                )

                # Make the request
                response = client.delete_polygon(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.DeletePolygonRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.EmptyResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.DeletePolygonRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_polygon,
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

    async def batch_add_polygons(self,
            request: Union[service.BatchPolygonsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_batch_add_polygons():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.BatchPolygonsRequest(
                )

                # Make the request
                response = client.batch_add_polygons(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.BatchPolygonsRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.EmptyResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.BatchPolygonsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_add_polygons,
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

    async def replace_polygons(self,
            request: Union[service.BatchPolygonsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_replace_polygons():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.BatchPolygonsRequest(
                )

                # Make the request
                response = client.replace_polygons(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.BatchPolygonsRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.EmptyResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.BatchPolygonsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.replace_polygons,
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

    async def drop_polygons(self,
            request: Union[service.DropPolygonsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.EmptyResponse:
        r"""

        .. code-block:: python

            from oceanbolt.com import polygonmanagement_v3

            def sample_drop_polygons():
                # Create a client
                client = polygonmanagement_v3.PolygonManagementServiceClient()

                # Initialize request argument(s)
                request = polygonmanagement_v3.DropPolygonsRequest(
                )

                # Make the request
                response = client.drop_polygons(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[oceanbolt.com.polygonmanagement_v3.types.DropPolygonsRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            oceanbolt.com.polygonmanagement_v3.types.EmptyResponse:

        """
        # Create or coerce a protobuf request object.
        request = service.DropPolygonsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.drop_polygons,
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
            "oceanbolt-com-polygonmanagement",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "PolygonManagementServiceAsyncClient",
)
