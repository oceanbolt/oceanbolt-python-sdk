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
import os
import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule


from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import path_template
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.oauth2 import service_account
from google.protobuf import wrappers_pb2  # type: ignore
from oceanbolt.com.fleetmanagement_v3.services.fleet_management_service import FleetManagementServiceAsyncClient
from oceanbolt.com.fleetmanagement_v3.services.fleet_management_service import FleetManagementServiceClient
from oceanbolt.com.fleetmanagement_v3.services.fleet_management_service import transports
from oceanbolt.com.fleetmanagement_v3.types import service
import google.auth


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return "foo.googleapis.com" if ("localhost" in client.DEFAULT_ENDPOINT) else client.DEFAULT_ENDPOINT


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert FleetManagementServiceClient._get_default_mtls_endpoint(None) is None
    assert FleetManagementServiceClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert FleetManagementServiceClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    assert FleetManagementServiceClient._get_default_mtls_endpoint(sandbox_endpoint) == sandbox_mtls_endpoint
    assert FleetManagementServiceClient._get_default_mtls_endpoint(sandbox_mtls_endpoint) == sandbox_mtls_endpoint
    assert FleetManagementServiceClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize("client_class", [
    FleetManagementServiceClient,
    FleetManagementServiceAsyncClient,
])
def test_fleet_management_service_client_from_service_account_info(client_class):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == 'api.oceanbolt.com:443'


@pytest.mark.parametrize("transport_class,transport_name", [
    (transports.FleetManagementServiceGrpcTransport, "grpc"),
    (transports.FleetManagementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
def test_fleet_management_service_client_service_account_always_use_jwt(transport_class, transport_name):
    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize("client_class", [
    FleetManagementServiceClient,
    FleetManagementServiceAsyncClient,
])
def test_fleet_management_service_client_from_service_account_file(client_class):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == 'api.oceanbolt.com:443'


def test_fleet_management_service_client_get_transport_class():
    transport = FleetManagementServiceClient.get_transport_class()
    available_transports = [
        transports.FleetManagementServiceGrpcTransport,
    ]
    assert transport in available_transports

    transport = FleetManagementServiceClient.get_transport_class("grpc")
    assert transport == transports.FleetManagementServiceGrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (FleetManagementServiceClient, transports.FleetManagementServiceGrpcTransport, "grpc"),
    (FleetManagementServiceAsyncClient, transports.FleetManagementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
@mock.patch.object(FleetManagementServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(FleetManagementServiceClient))
@mock.patch.object(FleetManagementServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(FleetManagementServiceAsyncClient))
def test_fleet_management_service_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(FleetManagementServiceClient, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(FleetManagementServiceClient, 'get_transport_class') as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,use_client_cert_env", [
    (FleetManagementServiceClient, transports.FleetManagementServiceGrpcTransport, "grpc", "true"),
    (FleetManagementServiceAsyncClient, transports.FleetManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", "true"),
    (FleetManagementServiceClient, transports.FleetManagementServiceGrpcTransport, "grpc", "false"),
    (FleetManagementServiceAsyncClient, transports.FleetManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", "false"),
])
@mock.patch.object(FleetManagementServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(FleetManagementServiceClient))
@mock.patch.object(FleetManagementServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(FleetManagementServiceAsyncClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_fleet_management_service_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        options = client_options.ClientOptions(client_cert_source=client_cert_source_callback)
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
                with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=client_cert_source_callback):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch("google.auth.transport.mtls.has_default_client_cert_source", return_value=False):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                )


@pytest.mark.parametrize("client_class", [
    FleetManagementServiceClient, FleetManagementServiceAsyncClient
])
@mock.patch.object(FleetManagementServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(FleetManagementServiceClient))
@mock.patch.object(FleetManagementServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(FleetManagementServiceAsyncClient))
def test_fleet_management_service_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=False):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
            with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_client_cert_source):
                api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (FleetManagementServiceClient, transports.FleetManagementServiceGrpcTransport, "grpc"),
    (FleetManagementServiceAsyncClient, transports.FleetManagementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
def test_fleet_management_service_client_client_options_scopes(client_class, transport_class, transport_name):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (FleetManagementServiceClient, transports.FleetManagementServiceGrpcTransport, "grpc", grpc_helpers),
    (FleetManagementServiceAsyncClient, transports.FleetManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_fleet_management_service_client_client_options_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

def test_fleet_management_service_client_client_options_from_dict():
    with mock.patch('oceanbolt.com.fleetmanagement_v3.services.fleet_management_service.transports.FleetManagementServiceGrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = FleetManagementServiceClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (FleetManagementServiceClient, transports.FleetManagementServiceGrpcTransport, "grpc", grpc_helpers),
    (FleetManagementServiceAsyncClient, transports.FleetManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_fleet_management_service_client_create_channel_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "api.oceanbolt.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
),
            scopes=None,
            default_host="api.oceanbolt.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("request_type", [
  service.EmptyParams,
  dict,
])
def test_list_fleets(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_fleets),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Fleets(
        )
        response = client.list_fleets(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleets)


def test_list_fleets_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_fleets),
            '__call__') as call:
        client.list_fleets()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.EmptyParams()


@pytest.mark.asyncio
async def test_list_fleets_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_fleets),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Fleets(
        ))
        response = await client.list_fleets(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleets)


@pytest.mark.asyncio
async def test_list_fleets_async_from_dict():
    await test_list_fleets_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.CreateFleetRequest,
  dict,
])
def test_create_fleet(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        )
        response = client.create_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


def test_create_fleet_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_fleet),
            '__call__') as call:
        client.create_fleet()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateFleetRequest()


@pytest.mark.asyncio
async def test_create_fleet_async(transport: str = 'grpc_asyncio', request_type=service.CreateFleetRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))
        response = await client.create_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_create_fleet_async_from_dict():
    await test_create_fleet_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.DeleteFleetRequest,
  dict,
])
def test_delete_fleet(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.EmptyResponse(
        )
        response = client.delete_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


def test_delete_fleet_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_fleet),
            '__call__') as call:
        client.delete_fleet()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteFleetRequest()


@pytest.mark.asyncio
async def test_delete_fleet_async(transport: str = 'grpc_asyncio', request_type=service.DeleteFleetRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))
        response = await client.delete_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_delete_fleet_async_from_dict():
    await test_delete_fleet_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.GetFleetRequest,
  dict,
])
def test_describe_fleet(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        )
        response = client.describe_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


def test_describe_fleet_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_fleet),
            '__call__') as call:
        client.describe_fleet()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetRequest()


@pytest.mark.asyncio
async def test_describe_fleet_async(transport: str = 'grpc_asyncio', request_type=service.GetFleetRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))
        response = await client.describe_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_describe_fleet_async_from_dict():
    await test_describe_fleet_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.RenameFleetRequest,
  dict,
])
def test_rename_fleet(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.rename_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        )
        response = client.rename_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.RenameFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


def test_rename_fleet_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.rename_fleet),
            '__call__') as call:
        client.rename_fleet()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.RenameFleetRequest()


@pytest.mark.asyncio
async def test_rename_fleet_async(transport: str = 'grpc_asyncio', request_type=service.RenameFleetRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.rename_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))
        response = await client.rename_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.RenameFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_rename_fleet_async_from_dict():
    await test_rename_fleet_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.ShareFleetRequest,
  dict,
])
def test_share_fleet(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        )
        response = client.share_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


def test_share_fleet_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_fleet),
            '__call__') as call:
        client.share_fleet()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareFleetRequest()


@pytest.mark.asyncio
async def test_share_fleet_async(transport: str = 'grpc_asyncio', request_type=service.ShareFleetRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))
        response = await client.share_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_share_fleet_async_from_dict():
    await test_share_fleet_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.ShareFleetRequest,
  dict,
])
def test_unshare_fleet(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        )
        response = client.unshare_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


def test_unshare_fleet_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_fleet),
            '__call__') as call:
        client.unshare_fleet()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareFleetRequest()


@pytest.mark.asyncio
async def test_unshare_fleet_async(transport: str = 'grpc_asyncio', request_type=service.ShareFleetRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_fleet),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Fleet(
            fleet_id='fleet_id_value',
            fleet_name='fleet_name_value',
            platform='platform_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))
        response = await client.unshare_fleet(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareFleetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Fleet)
    assert response.fleet_id == 'fleet_id_value'
    assert response.fleet_name == 'fleet_name_value'
    assert response.platform == 'platform_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_unshare_fleet_async_from_dict():
    await test_unshare_fleet_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.ListVesselsRequest,
  dict,
])
def test_list_vessels(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Vessels(
            vessels_in_fleet=1706,
        )
        response = client.list_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessels)
    assert response.vessels_in_fleet == 1706


def test_list_vessels_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_vessels),
            '__call__') as call:
        client.list_vessels()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListVesselsRequest()


@pytest.mark.asyncio
async def test_list_vessels_async(transport: str = 'grpc_asyncio', request_type=service.ListVesselsRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Vessels(
            vessels_in_fleet=1706,
        ))
        response = await client.list_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessels)
    assert response.vessels_in_fleet == 1706


@pytest.mark.asyncio
async def test_list_vessels_async_from_dict():
    await test_list_vessels_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.ListVesselsWithStatusRequest,
  dict,
])
def test_list_vessels_with_status(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_vessels_with_status),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Vessels(
            vessels_in_fleet=1706,
        )
        response = client.list_vessels_with_status(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListVesselsWithStatusRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessels)
    assert response.vessels_in_fleet == 1706


def test_list_vessels_with_status_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_vessels_with_status),
            '__call__') as call:
        client.list_vessels_with_status()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListVesselsWithStatusRequest()


@pytest.mark.asyncio
async def test_list_vessels_with_status_async(transport: str = 'grpc_asyncio', request_type=service.ListVesselsWithStatusRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_vessels_with_status),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Vessels(
            vessels_in_fleet=1706,
        ))
        response = await client.list_vessels_with_status(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListVesselsWithStatusRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessels)
    assert response.vessels_in_fleet == 1706


@pytest.mark.asyncio
async def test_list_vessels_with_status_async_from_dict():
    await test_list_vessels_with_status_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.AddVesselRequest,
  dict,
])
def test_add_vessel(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_vessel),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Vessel(
            imo=325,
            dwt=0.335,
            built=544,
            vessel_name='vessel_name_value',
            segment='segment_value',
            sub_segment='sub_segment_value',
            flag_code='flag_code_value',
            ex_name='ex_name_value',
            type_='type__value',
        )
        response = client.add_vessel(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.AddVesselRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessel)
    assert response.imo == 325
    assert math.isclose(response.dwt, 0.335, rel_tol=1e-6)
    assert response.built == 544
    assert response.vessel_name == 'vessel_name_value'
    assert response.segment == 'segment_value'
    assert response.sub_segment == 'sub_segment_value'
    assert response.flag_code == 'flag_code_value'
    assert response.ex_name == 'ex_name_value'
    assert response.type_ == 'type__value'


def test_add_vessel_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_vessel),
            '__call__') as call:
        client.add_vessel()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.AddVesselRequest()


@pytest.mark.asyncio
async def test_add_vessel_async(transport: str = 'grpc_asyncio', request_type=service.AddVesselRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_vessel),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Vessel(
            imo=325,
            dwt=0.335,
            built=544,
            vessel_name='vessel_name_value',
            segment='segment_value',
            sub_segment='sub_segment_value',
            flag_code='flag_code_value',
            ex_name='ex_name_value',
            type_='type__value',
        ))
        response = await client.add_vessel(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.AddVesselRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessel)
    assert response.imo == 325
    assert math.isclose(response.dwt, 0.335, rel_tol=1e-6)
    assert response.built == 544
    assert response.vessel_name == 'vessel_name_value'
    assert response.segment == 'segment_value'
    assert response.sub_segment == 'sub_segment_value'
    assert response.flag_code == 'flag_code_value'
    assert response.ex_name == 'ex_name_value'
    assert response.type_ == 'type__value'


@pytest.mark.asyncio
async def test_add_vessel_async_from_dict():
    await test_add_vessel_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.UpdateVesselRequest,
  dict,
])
def test_update_vessel(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_vessel),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Vessel(
            imo=325,
            dwt=0.335,
            built=544,
            vessel_name='vessel_name_value',
            segment='segment_value',
            sub_segment='sub_segment_value',
            flag_code='flag_code_value',
            ex_name='ex_name_value',
            type_='type__value',
        )
        response = client.update_vessel(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateVesselRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessel)
    assert response.imo == 325
    assert math.isclose(response.dwt, 0.335, rel_tol=1e-6)
    assert response.built == 544
    assert response.vessel_name == 'vessel_name_value'
    assert response.segment == 'segment_value'
    assert response.sub_segment == 'sub_segment_value'
    assert response.flag_code == 'flag_code_value'
    assert response.ex_name == 'ex_name_value'
    assert response.type_ == 'type__value'


def test_update_vessel_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_vessel),
            '__call__') as call:
        client.update_vessel()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateVesselRequest()


@pytest.mark.asyncio
async def test_update_vessel_async(transport: str = 'grpc_asyncio', request_type=service.UpdateVesselRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_vessel),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.Vessel(
            imo=325,
            dwt=0.335,
            built=544,
            vessel_name='vessel_name_value',
            segment='segment_value',
            sub_segment='sub_segment_value',
            flag_code='flag_code_value',
            ex_name='ex_name_value',
            type_='type__value',
        ))
        response = await client.update_vessel(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateVesselRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Vessel)
    assert response.imo == 325
    assert math.isclose(response.dwt, 0.335, rel_tol=1e-6)
    assert response.built == 544
    assert response.vessel_name == 'vessel_name_value'
    assert response.segment == 'segment_value'
    assert response.sub_segment == 'sub_segment_value'
    assert response.flag_code == 'flag_code_value'
    assert response.ex_name == 'ex_name_value'
    assert response.type_ == 'type__value'


@pytest.mark.asyncio
async def test_update_vessel_async_from_dict():
    await test_update_vessel_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.DeleteVesselRequest,
  dict,
])
def test_delete_vessel(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_vessel),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.EmptyResponse(
        )
        response = client.delete_vessel(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteVesselRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


def test_delete_vessel_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_vessel),
            '__call__') as call:
        client.delete_vessel()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteVesselRequest()


@pytest.mark.asyncio
async def test_delete_vessel_async(transport: str = 'grpc_asyncio', request_type=service.DeleteVesselRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_vessel),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))
        response = await client.delete_vessel(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteVesselRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_delete_vessel_async_from_dict():
    await test_delete_vessel_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.BatchVesselsRequest,
  dict,
])
def test_batch_add_vessels(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.EmptyResponse(
        )
        response = client.batch_add_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


def test_batch_add_vessels_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_vessels),
            '__call__') as call:
        client.batch_add_vessels()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchVesselsRequest()


@pytest.mark.asyncio
async def test_batch_add_vessels_async(transport: str = 'grpc_asyncio', request_type=service.BatchVesselsRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))
        response = await client.batch_add_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_batch_add_vessels_async_from_dict():
    await test_batch_add_vessels_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.BatchVesselsRequest,
  dict,
])
def test_replace_vessels(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.EmptyResponse(
        )
        response = client.replace_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


def test_replace_vessels_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_vessels),
            '__call__') as call:
        client.replace_vessels()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchVesselsRequest()


@pytest.mark.asyncio
async def test_replace_vessels_async(transport: str = 'grpc_asyncio', request_type=service.BatchVesselsRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))
        response = await client.replace_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_replace_vessels_async_from_dict():
    await test_replace_vessels_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.DropVesselsRequest,
  dict,
])
def test_drop_vessels(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.EmptyResponse(
        )
        response = client.drop_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DropVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


def test_drop_vessels_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_vessels),
            '__call__') as call:
        client.drop_vessels()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DropVesselsRequest()


@pytest.mark.asyncio
async def test_drop_vessels_async(transport: str = 'grpc_asyncio', request_type=service.DropVesselsRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))
        response = await client.drop_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DropVesselsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_drop_vessels_async_from_dict():
    await test_drop_vessels_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.GetFleetLiveMapRequest,
  dict,
])
def test_get_fleet_live_map(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_fleet_live_map),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.GetFleetLiveMapResponse(
            map_image='map_image_value',
        )
        response = client.get_fleet_live_map(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetLiveMapRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.GetFleetLiveMapResponse)
    assert response.map_image == 'map_image_value'


def test_get_fleet_live_map_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_fleet_live_map),
            '__call__') as call:
        client.get_fleet_live_map()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetLiveMapRequest()


@pytest.mark.asyncio
async def test_get_fleet_live_map_async(transport: str = 'grpc_asyncio', request_type=service.GetFleetLiveMapRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_fleet_live_map),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.GetFleetLiveMapResponse(
            map_image='map_image_value',
        ))
        response = await client.get_fleet_live_map(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetLiveMapRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.GetFleetLiveMapResponse)
    assert response.map_image == 'map_image_value'


@pytest.mark.asyncio
async def test_get_fleet_live_map_async_from_dict():
    await test_get_fleet_live_map_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.GetFleetListRequest,
  dict,
])
def test_upload_fleet_list(request_type, transport: str = 'grpc'):
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.upload_fleet_list),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.EmptyResponse(
        )
        response = client.upload_fleet_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetListRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


def test_upload_fleet_list_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.upload_fleet_list),
            '__call__') as call:
        client.upload_fleet_list()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetListRequest()


@pytest.mark.asyncio
async def test_upload_fleet_list_async(transport: str = 'grpc_asyncio', request_type=service.GetFleetListRequest):
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.upload_fleet_list),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))
        response = await client.upload_fleet_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetFleetListRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_upload_fleet_list_async_from_dict():
    await test_upload_fleet_list_async(request_type=dict)


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.FleetManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FleetManagementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.FleetManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FleetManagementServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.FleetManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = FleetManagementServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = FleetManagementServiceClient(
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.FleetManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FleetManagementServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.FleetManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = FleetManagementServiceClient(transport=transport)
    assert client.transport is transport

def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.FleetManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.FleetManagementServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

@pytest.mark.parametrize("transport_class", [
    transports.FleetManagementServiceGrpcTransport,
    transports.FleetManagementServiceGrpcAsyncIOTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, 'default') as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()

def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.FleetManagementServiceGrpcTransport,
    )

def test_fleet_management_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.FleetManagementServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_fleet_management_service_base_transport():
    # Instantiate the base transport.
    with mock.patch('oceanbolt.com.fleetmanagement_v3.services.fleet_management_service.transports.FleetManagementServiceTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.FleetManagementServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'list_fleets',
        'create_fleet',
        'delete_fleet',
        'describe_fleet',
        'rename_fleet',
        'share_fleet',
        'unshare_fleet',
        'list_vessels',
        'list_vessels_with_status',
        'add_vessel',
        'update_vessel',
        'delete_vessel',
        'batch_add_vessels',
        'replace_vessels',
        'drop_vessels',
        'get_fleet_live_map',
        'upload_fleet_list',
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()


def test_fleet_management_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(google.auth, 'load_credentials_from_file', autospec=True) as load_creds, mock.patch('oceanbolt.com.fleetmanagement_v3.services.fleet_management_service.transports.FleetManagementServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.FleetManagementServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json",
            scopes=None,
            default_scopes=(
),
            quota_project_id="octopus",
        )


def test_fleet_management_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc, mock.patch('oceanbolt.com.fleetmanagement_v3.services.fleet_management_service.transports.FleetManagementServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.FleetManagementServiceTransport()
        adc.assert_called_once()


def test_fleet_management_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        FleetManagementServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.FleetManagementServiceGrpcTransport,
        transports.FleetManagementServiceGrpcAsyncIOTransport,
    ],
)
def test_fleet_management_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.FleetManagementServiceGrpcTransport, grpc_helpers),
        (transports.FleetManagementServiceGrpcAsyncIOTransport, grpc_helpers_async)
    ],
)
def test_fleet_management_service_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(
            quota_project_id="octopus",
            scopes=["1", "2"]
        )

        create_channel.assert_called_with(
            "api.oceanbolt.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
),
            scopes=["1", "2"],
            default_host="api.oceanbolt.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("transport_class", [transports.FleetManagementServiceGrpcTransport, transports.FleetManagementServiceGrpcAsyncIOTransport])
def test_fleet_management_service_grpc_transport_client_cert_source_for_mtls(
    transport_class
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert,
                private_key=expected_key
            )


def test_fleet_management_service_host_no_port():
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com'),
    )
    assert client.transport._host == 'api.oceanbolt.com:443'


def test_fleet_management_service_host_with_port():
    client = FleetManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com:8000'),
    )
    assert client.transport._host == 'api.oceanbolt.com:8000'

def test_fleet_management_service_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.FleetManagementServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_fleet_management_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.FleetManagementServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.FleetManagementServiceGrpcTransport, transports.FleetManagementServiceGrpcAsyncIOTransport])
def test_fleet_management_service_transport_channel_mtls_with_client_cert_source(
    transport_class
):
    with mock.patch("grpc.ssl_channel_credentials", autospec=True) as grpc_ssl_channel_cred:
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, 'default') as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.FleetManagementServiceGrpcTransport, transports.FleetManagementServiceGrpcAsyncIOTransport])
def test_fleet_management_service_transport_channel_mtls_with_adc(
    transport_class
):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(billing_account=billing_account, )
    actual = FleetManagementServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = FleetManagementServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = FleetManagementServiceClient.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(folder=folder, )
    actual = FleetManagementServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = FleetManagementServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = FleetManagementServiceClient.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(organization=organization, )
    actual = FleetManagementServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = FleetManagementServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = FleetManagementServiceClient.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(project=project, )
    actual = FleetManagementServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = FleetManagementServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = FleetManagementServiceClient.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = FleetManagementServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = FleetManagementServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = FleetManagementServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.FleetManagementServiceTransport, '_prep_wrapped_messages') as prep:
        client = FleetManagementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.FleetManagementServiceTransport, '_prep_wrapped_messages') as prep:
        transport_class = FleetManagementServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


@pytest.mark.asyncio
async def test_transport_close_async():
    client = FleetManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    with mock.patch.object(type(getattr(client.transport, "grpc_channel")), "close") as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()

def test_transport_close():
    transports = {
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = FleetManagementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        with mock.patch.object(type(getattr(client.transport, close_name)), "close") as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()

def test_client_ctx():
    transports = [
        'grpc',
    ]
    for transport in transports:
        client = FleetManagementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()

@pytest.mark.parametrize("client_class,transport_class", [
    (FleetManagementServiceClient, transports.FleetManagementServiceGrpcTransport),
    (FleetManagementServiceAsyncClient, transports.FleetManagementServiceGrpcAsyncIOTransport),
])
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )
