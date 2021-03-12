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

from oceanbolt.com.polygonmanagement_v3.types import service


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'oceanbolt-com-polygonmanagement',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

class PolygonManagementServiceTransport(abc.ABC):
    """Abstract transport class for PolygonManagementService."""

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
            self.list_layers: gapic_v1.method.wrap_method(
                self.list_layers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_layer: gapic_v1.method.wrap_method(
                self.create_layer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_layer: gapic_v1.method.wrap_method(
                self.delete_layer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.describe_layer: gapic_v1.method.wrap_method(
                self.describe_layer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_layer: gapic_v1.method.wrap_method(
                self.rename_layer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.share_layer: gapic_v1.method.wrap_method(
                self.share_layer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.unshare_layer: gapic_v1.method.wrap_method(
                self.unshare_layer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_polygons: gapic_v1.method.wrap_method(
                self.list_polygons,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_polygon: gapic_v1.method.wrap_method(
                self.add_polygon,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_polygon: gapic_v1.method.wrap_method(
                self.update_polygon,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_polygon: gapic_v1.method.wrap_method(
                self.delete_polygon,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_add_polygons: gapic_v1.method.wrap_method(
                self.batch_add_polygons,
                default_timeout=None,
                client_info=client_info,
            ),
            self.replace_polygons: gapic_v1.method.wrap_method(
                self.replace_polygons,
                default_timeout=None,
                client_info=client_info,
            ),
            self.drop_polygons: gapic_v1.method.wrap_method(
                self.drop_polygons,
                default_timeout=None,
                client_info=client_info,
            ),

        }

    @property
    def list_layers(self) -> typing.Callable[
            [service.EmptyParams],
            typing.Union[
                service.Layers,
                typing.Awaitable[service.Layers]
            ]]:
        raise NotImplementedError()

    @property
    def create_layer(self) -> typing.Callable[
            [service.CreateLayerRequest],
            typing.Union[
                service.Layer,
                typing.Awaitable[service.Layer]
            ]]:
        raise NotImplementedError()

    @property
    def delete_layer(self) -> typing.Callable[
            [service.DeleteLayerRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def describe_layer(self) -> typing.Callable[
            [service.GetLayerRequest],
            typing.Union[
                service.Layer,
                typing.Awaitable[service.Layer]
            ]]:
        raise NotImplementedError()

    @property
    def rename_layer(self) -> typing.Callable[
            [service.RenameLayerRequest],
            typing.Union[
                service.Layer,
                typing.Awaitable[service.Layer]
            ]]:
        raise NotImplementedError()

    @property
    def share_layer(self) -> typing.Callable[
            [service.ShareLayerRequest],
            typing.Union[
                service.Layer,
                typing.Awaitable[service.Layer]
            ]]:
        raise NotImplementedError()

    @property
    def unshare_layer(self) -> typing.Callable[
            [service.ShareLayerRequest],
            typing.Union[
                service.Layer,
                typing.Awaitable[service.Layer]
            ]]:
        raise NotImplementedError()

    @property
    def list_polygons(self) -> typing.Callable[
            [service.ListPolygonsRequest],
            typing.Union[
                service.Polygons,
                typing.Awaitable[service.Polygons]
            ]]:
        raise NotImplementedError()

    @property
    def add_polygon(self) -> typing.Callable[
            [service.AddPolygonRequest],
            typing.Union[
                service.Polygon,
                typing.Awaitable[service.Polygon]
            ]]:
        raise NotImplementedError()

    @property
    def update_polygon(self) -> typing.Callable[
            [service.UpdatePolygonRequest],
            typing.Union[
                service.Polygon,
                typing.Awaitable[service.Polygon]
            ]]:
        raise NotImplementedError()

    @property
    def delete_polygon(self) -> typing.Callable[
            [service.DeletePolygonRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def batch_add_polygons(self) -> typing.Callable[
            [service.BatchPolygonsRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def replace_polygons(self) -> typing.Callable[
            [service.BatchPolygonsRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def drop_polygons(self) -> typing.Callable[
            [service.DropPolygonsRequest],
            typing.Union[
                service.EmptyResponse,
                typing.Awaitable[service.EmptyResponse]
            ]]:
        raise NotImplementedError()


__all__ = (
    'PolygonManagementServiceTransport',
)
