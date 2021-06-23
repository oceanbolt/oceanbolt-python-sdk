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

import abc
import typing
import pkg_resources

from google import auth  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1    # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore

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

    def __init__(
            self, *,
            host: str = 'api.oceanbolt.com',
            credentials: credentials.Credentials = None,
            credentials_file: typing.Optional[str] = None,
            scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
            quota_project_id: typing.Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                                credentials_file,
                                scopes=scopes,
                                quota_project_id=quota_project_id
                            )

        elif credentials is None:
            credentials, _ = auth.default(scopes=scopes, quota_project_id=quota_project_id)

        # Save the credentials.
        self._credentials = credentials

        # Lifted into its own function so it can be stubbed out during tests.
        self._prep_wrapped_messages(client_info)

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

        }

    @property
    def list_fleets(self) -> typing.Callable[
            [service.EmptyParams],
            typing.Union[
                service.Fleets,
                typing.Awaitable[service.Fleets]
            ]]:
        raise NotImplementedError()

    @property
    def create_fleet(self) -> typing.Callable[
            [service.CreateFleetRequest],
            typing.Union[
                service.Fleet,
                typing.Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def delete_fleet(self) -> typing.Callable[
            [service.DeleteFleetRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def describe_fleet(self) -> typing.Callable[
            [service.GetFleetRequest],
            typing.Union[
                service.Fleet,
                typing.Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def rename_fleet(self) -> typing.Callable[
            [service.RenameFleetRequest],
            typing.Union[
                service.Fleet,
                typing.Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def share_fleet(self) -> typing.Callable[
            [service.ShareFleetRequest],
            typing.Union[
                service.Fleet,
                typing.Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def unshare_fleet(self) -> typing.Callable[
            [service.ShareFleetRequest],
            typing.Union[
                service.Fleet,
                typing.Awaitable[service.Fleet]
            ]]:
        raise NotImplementedError()

    @property
    def list_vessels(self) -> typing.Callable[
            [service.ListVesselsRequest],
            typing.Union[
                service.Vessels,
                typing.Awaitable[service.Vessels]
            ]]:
        raise NotImplementedError()

    @property
    def list_vessels_with_status(self) -> typing.Callable[
            [service.ListVesselsWithStatusRequest],
            typing.Union[
                service.Vessels,
                typing.Awaitable[service.Vessels]
            ]]:
        raise NotImplementedError()

    @property
    def add_vessel(self) -> typing.Callable[
            [service.AddVesselRequest],
            typing.Union[
                service.Vessel,
                typing.Awaitable[service.Vessel]
            ]]:
        raise NotImplementedError()

    @property
    def update_vessel(self) -> typing.Callable[
            [service.UpdateVesselRequest],
            typing.Union[
                service.Vessel,
                typing.Awaitable[service.Vessel]
            ]]:
        raise NotImplementedError()

    @property
    def delete_vessel(self) -> typing.Callable[
            [service.DeleteVesselRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def batch_add_vessels(self) -> typing.Callable[
            [service.BatchVesselsRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def replace_vessels(self) -> typing.Callable[
            [service.BatchVesselsRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def drop_vessels(self) -> typing.Callable[
            [service.DropVesselsRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_fleet_live_map(self) -> typing.Callable[
            [service.GetFleetLiveMapRequest],
            typing.Union[
                service.GetFleetLiveMapResponse,
                typing.Awaitable[service.GetFleetLiveMapResponse]
            ]]:
        raise NotImplementedError()


__all__ = (
    'FleetManagementServiceTransport',
)
