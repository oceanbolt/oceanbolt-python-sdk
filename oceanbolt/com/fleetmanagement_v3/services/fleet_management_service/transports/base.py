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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import pkg_resources

import google.auth  # type: ignore
import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore

from oceanbolt.com.fleetmanagement_v3.types import service

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'oceanbolt-com-fleetmanagement',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class FleetManagementServiceTransport(abc.ABC):
    """Abstract transport class for FleetManagementService."""

    AUTH_SCOPES = (
    )

    DEFAULT_HOST: str = 'api.oceanbolt.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: ga_credentials.Credentials = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )
        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(api_audience if api_audience else host)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_fleets: gapic_v1.method.wrap_method(
                self.list_fleets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_fleet: gapic_v1.method.wrap_method(
                self.create_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_fleet: gapic_v1.method.wrap_method(
                self.delete_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.describe_fleet: gapic_v1.method.wrap_method(
                self.describe_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_fleet: gapic_v1.method.wrap_method(
                self.rename_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.share_fleet: gapic_v1.method.wrap_method(
                self.share_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.unshare_fleet: gapic_v1.method.wrap_method(
                self.unshare_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_vessels: gapic_v1.method.wrap_method(
                self.list_vessels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_vessels_with_status: gapic_v1.method.wrap_method(
                self.list_vessels_with_status,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_vessel: gapic_v1.method.wrap_method(
                self.add_vessel,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_vessel: gapic_v1.method.wrap_method(
                self.update_vessel,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_vessel: gapic_v1.method.wrap_method(
                self.delete_vessel,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_add_vessels: gapic_v1.method.wrap_method(
                self.batch_add_vessels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.replace_vessels: gapic_v1.method.wrap_method(
                self.replace_vessels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.drop_vessels: gapic_v1.method.wrap_method(
                self.drop_vessels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_fleet_live_map: gapic_v1.method.wrap_method(
                self.get_fleet_live_map,
                default_timeout=None,
                client_info=client_info,
            ),
            self.upload_fleet_list: gapic_v1.method.wrap_method(
                self.upload_fleet_list,
                default_timeout=None,
                client_info=client_info,
            ),
         }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def list_fleets(self) -> Callable[
            [service.EmptyParams],
            Union[
                service.Fleets,
                Awaitable[service.Fleets]
            ]]:
        raise NotImplementedError()

    @property
    def create_fleet(self) -> Callable[
            [service.CreateFleetRequest],
            Union[
                service.Fleet,
                Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def delete_fleet(self) -> Callable[
            [service.DeleteFleetRequest],
            Union[
                service.EmptyResponse,
                Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def describe_fleet(self) -> Callable[
            [service.GetFleetRequest],
            Union[
                service.Fleet,
                Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def rename_fleet(self) -> Callable[
            [service.RenameFleetRequest],
            Union[
                service.Fleet,
                Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def share_fleet(self) -> Callable[
            [service.ShareFleetRequest],
            Union[
                service.Fleet,
                Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def unshare_fleet(self) -> Callable[
            [service.ShareFleetRequest],
            Union[
                service.Fleet,
                Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def list_vessels(self) -> Callable[
            [service.ListVesselsRequest],
            Union[
                service.Vessels,
                Awaitable[service.Vessels]
            ]]:
        raise NotImplementedError()

    @property
    def list_vessels_with_status(self) -> Callable[
            [service.ListVesselsWithStatusRequest],
            Union[
                service.Vessels,
                Awaitable[service.Vessels]
            ]]:
        raise NotImplementedError()

    @property
    def add_vessel(self) -> Callable[
            [service.AddVesselRequest],
            Union[
                service.Vessel,
                Awaitable[service.Vessel]
            ]]:
        raise NotImplementedError()

    @property
    def update_vessel(self) -> Callable[
            [service.UpdateVesselRequest],
            Union[
                service.Vessel,
                Awaitable[service.Vessel]
            ]]:
        raise NotImplementedError()

    @property
    def delete_vessel(self) -> Callable[
            [service.DeleteVesselRequest],
            Union[
                service.EmptyResponse,
                Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def batch_add_vessels(self) -> Callable[
            [service.BatchVesselsRequest],
            Union[
                service.EmptyResponse,
                Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def replace_vessels(self) -> Callable[
            [service.BatchVesselsRequest],
            Union[
                service.EmptyResponse,
                Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def drop_vessels(self) -> Callable[
            [service.DropVesselsRequest],
            Union[
                service.EmptyResponse,
                Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_fleet_live_map(self) -> Callable[
            [service.GetFleetLiveMapRequest],
            Union[
                service.GetFleetLiveMapResponse,
                Awaitable[service.GetFleetLiveMapResponse]
            ]]:
        raise NotImplementedError()

    @property
    def upload_fleet_list(self) -> Callable[
            [service.GetFleetListRequest],
            Union[
                service.EmptyResponse,
                Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'FleetManagementServiceTransport',
)
