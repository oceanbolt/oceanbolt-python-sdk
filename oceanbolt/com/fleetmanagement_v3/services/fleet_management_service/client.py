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
import os
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials             # type: ignore
from google.auth.transport import mtls                            # type: ignore
from google.auth.transport.grpc import SslCredentials             # type: ignore
from google.auth.exceptions import MutualTLSChannelError          # type: ignore
from google.oauth2 import service_account                         # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.protobuf import wrappers_pb2  # type: ignore
from oceanbolt.com.fleetmanagement_v3.types import service
from .transports.base import FleetManagementServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import FleetManagementServiceGrpcTransport
from .transports.grpc_asyncio import FleetManagementServiceGrpcAsyncIOTransport


class FleetManagementServiceClientMeta(type):
    """Metaclass for the FleetManagementService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """
    _transport_registry = OrderedDict()  # type: Dict[str, Type[FleetManagementServiceTransport]]
    _transport_registry["grpc"] = FleetManagementServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = FleetManagementServiceGrpcAsyncIOTransport

    def get_transport_class(cls,
            label: str = None,
        ) -> Type[FleetManagementServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class FleetManagementServiceClient(metaclass=FleetManagementServiceClientMeta):
    """FleetManagement provides service to manage fleets for clients"""

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "api.oceanbolt.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            FleetManagementServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

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
            FleetManagementServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> FleetManagementServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            FleetManagementServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def common_billing_account_path(billing_account: str, ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(billing_account=billing_account, )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str,str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str, ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder, )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str,str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str, ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization, )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str,str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str, ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project, )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str,str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str, ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(project=project, location=location, )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str,str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[client_options_lib.ClientOptions] = None):
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
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError("Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`")
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError("Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`")

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (use_mtls_endpoint == "auto" and client_cert_source):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Union[str, FleetManagementServiceTransport, None] = None,
            client_options: Optional[client_options_lib.ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the fleet management service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, FleetManagementServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
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
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(client_options)

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError("client_options.api_key and credentials are mutually exclusive")

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, FleetManagementServiceTransport):
            # transport is a FleetManagementServiceTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError("When providing a transport instance, "
                                 "provide its credentials directly.")
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(google.auth._default, "get_api_key_credentials"):
                credentials = google.auth._default.get_api_key_credentials(api_key_value)

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
            )

    def list_fleets(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.EmptyParams.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.EmptyParams):
            request = service.EmptyParams(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_fleets]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_fleet(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateFleetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateFleetRequest):
            request = service.CreateFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_fleet]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_fleet(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.DeleteFleetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DeleteFleetRequest):
            request = service.DeleteFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_fleet]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def describe_fleet(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetFleetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetFleetRequest):
            request = service.GetFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.describe_fleet]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def rename_fleet(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.RenameFleetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.RenameFleetRequest):
            request = service.RenameFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.rename_fleet]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def share_fleet(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ShareFleetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ShareFleetRequest):
            request = service.ShareFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.share_fleet]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def unshare_fleet(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ShareFleetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ShareFleetRequest):
            request = service.ShareFleetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.unshare_fleet]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_vessels(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListVesselsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListVesselsRequest):
            request = service.ListVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_vessels]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_vessels_with_status(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListVesselsWithStatusRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListVesselsWithStatusRequest):
            request = service.ListVesselsWithStatusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_vessels_with_status]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def add_vessel(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.AddVesselRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.AddVesselRequest):
            request = service.AddVesselRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_vessel]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_vessel(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateVesselRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateVesselRequest):
            request = service.UpdateVesselRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_vessel]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_vessel(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.DeleteVesselRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DeleteVesselRequest):
            request = service.DeleteVesselRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_vessel]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_add_vessels(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.BatchVesselsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.BatchVesselsRequest):
            request = service.BatchVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_add_vessels]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def replace_vessels(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.BatchVesselsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.BatchVesselsRequest):
            request = service.BatchVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.replace_vessels]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def drop_vessels(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.DropVesselsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DropVesselsRequest):
            request = service.DropVesselsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.drop_vessels]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_fleet_live_map(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetFleetLiveMapRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetFleetLiveMapRequest):
            request = service.GetFleetLiveMapRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_fleet_live_map]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def upload_fleet_list(self,
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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetFleetListRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetFleetListRequest):
            request = service.GetFleetListRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.upload_fleet_list]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()



try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "oceanbolt-com-fleetmanagement",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "FleetManagementServiceClient",
)
