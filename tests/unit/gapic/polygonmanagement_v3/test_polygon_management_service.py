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
import os
# try/except added for compatibility with python < 3.8
try:
    from unittest import mock
    from unittest.mock import AsyncMock
except ImportError:
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
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service import PolygonManagementServiceAsyncClient
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service import PolygonManagementServiceClient
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service import transports
from oceanbolt.com.polygonmanagement_v3.types import resources
from oceanbolt.com.polygonmanagement_v3.types import service
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

    assert PolygonManagementServiceClient._get_default_mtls_endpoint(None) is None
    assert PolygonManagementServiceClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert PolygonManagementServiceClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    assert PolygonManagementServiceClient._get_default_mtls_endpoint(sandbox_endpoint) == sandbox_mtls_endpoint
    assert PolygonManagementServiceClient._get_default_mtls_endpoint(sandbox_mtls_endpoint) == sandbox_mtls_endpoint
    assert PolygonManagementServiceClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize("client_class,transport_name", [
    (PolygonManagementServiceClient, "grpc"),
    (PolygonManagementServiceAsyncClient, "grpc_asyncio"),
])
def test_polygon_management_service_client_from_service_account_info(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'api.oceanbolt.com:443'
        )


@pytest.mark.parametrize("transport_class,transport_name", [
    (transports.PolygonManagementServiceGrpcTransport, "grpc"),
    (transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
def test_polygon_management_service_client_service_account_always_use_jwt(transport_class, transport_name):
    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize("client_class,transport_name", [
    (PolygonManagementServiceClient, "grpc"),
    (PolygonManagementServiceAsyncClient, "grpc_asyncio"),
])
def test_polygon_management_service_client_from_service_account_file(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'api.oceanbolt.com:443'
        )


def test_polygon_management_service_client_get_transport_class():
    transport = PolygonManagementServiceClient.get_transport_class()
    available_transports = [
        transports.PolygonManagementServiceGrpcTransport,
    ]
    assert transport in available_transports

    transport = PolygonManagementServiceClient.get_transport_class("grpc")
    assert transport == transports.PolygonManagementServiceGrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport, "grpc"),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
@mock.patch.object(PolygonManagementServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PolygonManagementServiceClient))
@mock.patch.object(PolygonManagementServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PolygonManagementServiceAsyncClient))
def test_polygon_management_service_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(PolygonManagementServiceClient, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(PolygonManagementServiceClient, 'get_transport_class') as gtc:
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
            api_audience=None,
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
                api_audience=None,
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
                api_audience=None,
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
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(api_audience="https://language.googleapis.com")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com"
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,use_client_cert_env", [
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport, "grpc", "true"),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", "true"),
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport, "grpc", "false"),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", "false"),
])
@mock.patch.object(PolygonManagementServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PolygonManagementServiceClient))
@mock.patch.object(PolygonManagementServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PolygonManagementServiceAsyncClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_polygon_management_service_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
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
                api_audience=None,
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
                        api_audience=None,
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
                    api_audience=None,
                )


@pytest.mark.parametrize("client_class", [
    PolygonManagementServiceClient, PolygonManagementServiceAsyncClient
])
@mock.patch.object(PolygonManagementServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PolygonManagementServiceClient))
@mock.patch.object(PolygonManagementServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PolygonManagementServiceAsyncClient))
def test_polygon_management_service_client_get_mtls_endpoint_and_cert_source(client_class):
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
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport, "grpc"),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
def test_polygon_management_service_client_client_options_scopes(client_class, transport_class, transport_name):
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
            api_audience=None,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport, "grpc", grpc_helpers),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_polygon_management_service_client_client_options_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
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
            api_audience=None,
        )

def test_polygon_management_service_client_client_options_from_dict():
    with mock.patch('oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.transports.PolygonManagementServiceGrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = PolygonManagementServiceClient(
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
            api_audience=None,
        )


@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport, "grpc", grpc_helpers),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_polygon_management_service_client_create_channel_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
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
            api_audience=None,
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
  service.ListLayersRequest,
  dict,
])
def test_list_layers(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_layers),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListLayersResponse(
        )
        response = client.list_layers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListLayersRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListLayersResponse)


def test_list_layers_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_layers),
            '__call__') as call:
        client.list_layers()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListLayersRequest()

@pytest.mark.asyncio
async def test_list_layers_async(transport: str = 'grpc_asyncio', request_type=service.ListLayersRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_layers),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.ListLayersResponse(
        ))
        response = await client.list_layers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListLayersRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListLayersResponse)


@pytest.mark.asyncio
async def test_list_layers_async_from_dict():
    await test_list_layers_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.CreateLayerRequest,
  dict,
])
def test_create_layer(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        )
        response = client.create_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


def test_create_layer_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_layer),
            '__call__') as call:
        client.create_layer()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateLayerRequest()

@pytest.mark.asyncio
async def test_create_layer_async(transport: str = 'grpc_asyncio', request_type=service.CreateLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        ))
        response = await client.create_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


@pytest.mark.asyncio
async def test_create_layer_async_from_dict():
    await test_create_layer_async(request_type=dict)


@pytest.mark.parametrize("request_type", [
  service.DeleteLayerRequest,
  dict,
])
def test_delete_layer(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteLayerRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_layer_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_layer),
            '__call__') as call:
        client.delete_layer()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteLayerRequest()

@pytest.mark.asyncio
async def test_delete_layer_async(transport: str = 'grpc_asyncio', request_type=service.DeleteLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteLayerRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_delete_layer_async_from_dict():
    await test_delete_layer_async(request_type=dict)


def test_delete_layer_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_layer),
            '__call__') as call:
        call.return_value = None
        client.delete_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_delete_layer_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_layer),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.CopyLayerRequest,
  dict,
])
def test_copy_layer(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.copy_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        )
        response = client.copy_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CopyLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


def test_copy_layer_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.copy_layer),
            '__call__') as call:
        client.copy_layer()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CopyLayerRequest()

@pytest.mark.asyncio
async def test_copy_layer_async(transport: str = 'grpc_asyncio', request_type=service.CopyLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.copy_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        ))
        response = await client.copy_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CopyLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


@pytest.mark.asyncio
async def test_copy_layer_async_from_dict():
    await test_copy_layer_async(request_type=dict)


def test_copy_layer_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CopyLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.copy_layer),
            '__call__') as call:
        call.return_value = resources.Layer()
        client.copy_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_copy_layer_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CopyLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.copy_layer),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer())
        await client.copy_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.GetLayerRequest,
  dict,
])
def test_describe_layer(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        )
        response = client.describe_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


def test_describe_layer_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_layer),
            '__call__') as call:
        client.describe_layer()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetLayerRequest()

@pytest.mark.asyncio
async def test_describe_layer_async(transport: str = 'grpc_asyncio', request_type=service.GetLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        ))
        response = await client.describe_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


@pytest.mark.asyncio
async def test_describe_layer_async_from_dict():
    await test_describe_layer_async(request_type=dict)


def test_describe_layer_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_layer),
            '__call__') as call:
        call.return_value = resources.Layer()
        client.describe_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_describe_layer_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.describe_layer),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer())
        await client.describe_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.ShareLayerRequest,
  dict,
])
def test_share_layer(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        )
        response = client.share_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


def test_share_layer_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_layer),
            '__call__') as call:
        client.share_layer()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareLayerRequest()

@pytest.mark.asyncio
async def test_share_layer_async(transport: str = 'grpc_asyncio', request_type=service.ShareLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        ))
        response = await client.share_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


@pytest.mark.asyncio
async def test_share_layer_async_from_dict():
    await test_share_layer_async(request_type=dict)


def test_share_layer_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ShareLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_layer),
            '__call__') as call:
        call.return_value = resources.Layer()
        client.share_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_share_layer_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ShareLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.share_layer),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer())
        await client.share_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.ShareLayerRequest,
  dict,
])
def test_unshare_layer(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        )
        response = client.unshare_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


def test_unshare_layer_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_layer),
            '__call__') as call:
        client.unshare_layer()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareLayerRequest()

@pytest.mark.asyncio
async def test_unshare_layer_async(transport: str = 'grpc_asyncio', request_type=service.ShareLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer(
            name='name_value',
            layer_id='layer_id_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
            polygons_in_layer=1837,
            shared_with_org=True,
        ))
        response = await client.unshare_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Layer)
    assert response.name == 'name_value'
    assert response.layer_id == 'layer_id_value'
    assert response.owner_user_id == 'owner_user_id_value'
    assert response.organization == 'organization_value'
    assert response.polygons_in_layer == 1837
    assert response.shared_with_org is True


@pytest.mark.asyncio
async def test_unshare_layer_async_from_dict():
    await test_unshare_layer_async(request_type=dict)


def test_unshare_layer_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ShareLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_layer),
            '__call__') as call:
        call.return_value = resources.Layer()
        client.unshare_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_unshare_layer_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ShareLayerRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.unshare_layer),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.Layer())
        await client.unshare_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.ListPolygonsRequest,
  dict,
])
def test_list_polygons(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListPolygonsResponse(
        )
        response = client.list_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListPolygonsResponse)


def test_list_polygons_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_polygons),
            '__call__') as call:
        client.list_polygons()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListPolygonsRequest()

@pytest.mark.asyncio
async def test_list_polygons_async(transport: str = 'grpc_asyncio', request_type=service.ListPolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.ListPolygonsResponse(
        ))
        response = await client.list_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListPolygonsResponse)


@pytest.mark.asyncio
async def test_list_polygons_async_from_dict():
    await test_list_polygons_async(request_type=dict)


def test_list_polygons_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListPolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_polygons),
            '__call__') as call:
        call.return_value = service.ListPolygonsResponse()
        client.list_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_list_polygons_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListPolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_polygons),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListPolygonsResponse())
        await client.list_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.AddPolygonRequest,
  dict,
])
def test_add_polygon(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_polygon),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Polygon(
            name='name_value',
            polygon_id='polygon_id_value',
            geojson='geojson_value',
        )
        response = client.add_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.AddPolygonRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Polygon)
    assert response.name == 'name_value'
    assert response.polygon_id == 'polygon_id_value'
    assert response.geojson == 'geojson_value'


def test_add_polygon_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_polygon),
            '__call__') as call:
        client.add_polygon()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.AddPolygonRequest()

@pytest.mark.asyncio
async def test_add_polygon_async(transport: str = 'grpc_asyncio', request_type=service.AddPolygonRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_polygon),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(resources.Polygon(
            name='name_value',
            polygon_id='polygon_id_value',
            geojson='geojson_value',
        ))
        response = await client.add_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.AddPolygonRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Polygon)
    assert response.name == 'name_value'
    assert response.polygon_id == 'polygon_id_value'
    assert response.geojson == 'geojson_value'


@pytest.mark.asyncio
async def test_add_polygon_async_from_dict():
    await test_add_polygon_async(request_type=dict)


def test_add_polygon_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.AddPolygonRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_polygon),
            '__call__') as call:
        call.return_value = resources.Polygon()
        client.add_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_add_polygon_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.AddPolygonRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.add_polygon),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.Polygon())
        await client.add_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.UpdatePolygonRequest,
  dict,
])
def test_update_polygon(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_polygon),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Polygon(
            name='name_value',
            polygon_id='polygon_id_value',
            geojson='geojson_value',
        )
        response = client.update_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdatePolygonRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Polygon)
    assert response.name == 'name_value'
    assert response.polygon_id == 'polygon_id_value'
    assert response.geojson == 'geojson_value'


def test_update_polygon_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_polygon),
            '__call__') as call:
        client.update_polygon()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdatePolygonRequest()

@pytest.mark.asyncio
async def test_update_polygon_async(transport: str = 'grpc_asyncio', request_type=service.UpdatePolygonRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_polygon),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(resources.Polygon(
            name='name_value',
            polygon_id='polygon_id_value',
            geojson='geojson_value',
        ))
        response = await client.update_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdatePolygonRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Polygon)
    assert response.name == 'name_value'
    assert response.polygon_id == 'polygon_id_value'
    assert response.geojson == 'geojson_value'


@pytest.mark.asyncio
async def test_update_polygon_async_from_dict():
    await test_update_polygon_async(request_type=dict)


def test_update_polygon_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdatePolygonRequest()

    request.layer_id = 'layer_id_value'
    request.polygon_id = 'polygon_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_polygon),
            '__call__') as call:
        call.return_value = resources.Polygon()
        client.update_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value&polygon_id=polygon_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_update_polygon_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdatePolygonRequest()

    request.layer_id = 'layer_id_value'
    request.polygon_id = 'polygon_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.update_polygon),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.Polygon())
        await client.update_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value&polygon_id=polygon_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.DeletePolygonRequest,
  dict,
])
def test_delete_polygon(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_polygon),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeletePolygonRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_polygon_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_polygon),
            '__call__') as call:
        client.delete_polygon()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeletePolygonRequest()

@pytest.mark.asyncio
async def test_delete_polygon_async(transport: str = 'grpc_asyncio', request_type=service.DeletePolygonRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_polygon),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeletePolygonRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_delete_polygon_async_from_dict():
    await test_delete_polygon_async(request_type=dict)


def test_delete_polygon_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeletePolygonRequest()

    request.layer_id = 'layer_id_value'
    request.polygon_id = 'polygon_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_polygon),
            '__call__') as call:
        call.return_value = None
        client.delete_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value&polygon_id=polygon_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_delete_polygon_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeletePolygonRequest()

    request.layer_id = 'layer_id_value'
    request.polygon_id = 'polygon_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_polygon),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value&polygon_id=polygon_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.BatchAddPolygonsRequest,
  dict,
])
def test_batch_add_polygons(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.BatchAddPolygonsResponse(
            errors=['errors_value'],
        )
        response = client.batch_add_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchAddPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.BatchAddPolygonsResponse)
    assert response.errors == ['errors_value']


def test_batch_add_polygons_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_polygons),
            '__call__') as call:
        client.batch_add_polygons()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchAddPolygonsRequest()

@pytest.mark.asyncio
async def test_batch_add_polygons_async(transport: str = 'grpc_asyncio', request_type=service.BatchAddPolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(service.BatchAddPolygonsResponse(
            errors=['errors_value'],
        ))
        response = await client.batch_add_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.BatchAddPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.BatchAddPolygonsResponse)
    assert response.errors == ['errors_value']


@pytest.mark.asyncio
async def test_batch_add_polygons_async_from_dict():
    await test_batch_add_polygons_async(request_type=dict)


def test_batch_add_polygons_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.BatchAddPolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_polygons),
            '__call__') as call:
        call.return_value = service.BatchAddPolygonsResponse()
        client.batch_add_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_batch_add_polygons_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.BatchAddPolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.batch_add_polygons),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.BatchAddPolygonsResponse())
        await client.batch_add_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.ReplacePolygonsRequest,
  dict,
])
def test_replace_polygons(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.replace_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ReplacePolygonsRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_replace_polygons_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_polygons),
            '__call__') as call:
        client.replace_polygons()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ReplacePolygonsRequest()

@pytest.mark.asyncio
async def test_replace_polygons_async(transport: str = 'grpc_asyncio', request_type=service.ReplacePolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.replace_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ReplacePolygonsRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_replace_polygons_async_from_dict():
    await test_replace_polygons_async(request_type=dict)


def test_replace_polygons_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ReplacePolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_polygons),
            '__call__') as call:
        call.return_value = None
        client.replace_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_replace_polygons_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ReplacePolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.replace_polygons),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.replace_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  service.DropPolygonsRequest,
  dict,
])
def test_drop_polygons(request_type, transport: str = 'grpc'):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.drop_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DropPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_drop_polygons_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_polygons),
            '__call__') as call:
        client.drop_polygons()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DropPolygonsRequest()

@pytest.mark.asyncio
async def test_drop_polygons_async(transport: str = 'grpc_asyncio', request_type=service.DropPolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.drop_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DropPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_drop_polygons_async_from_dict():
    await test_drop_polygons_async(request_type=dict)


def test_drop_polygons_field_headers():
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DropPolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_polygons),
            '__call__') as call:
        call.return_value = None
        client.drop_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_drop_polygons_field_headers_async():
    client = PolygonManagementServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DropPolygonsRequest()

    request.layer_id = 'layer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.drop_polygons),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.drop_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'layer_id=layer_id_value',
    ) in kw['metadata']


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = PolygonManagementServiceClient(transport=transport)
    assert client.transport is transport

def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.PolygonManagementServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

@pytest.mark.parametrize("transport_class", [
    transports.PolygonManagementServiceGrpcTransport,
    transports.PolygonManagementServiceGrpcAsyncIOTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, 'default') as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()

@pytest.mark.parametrize("transport_name", [
    "grpc",
])
def test_transport_kind(transport_name):
    transport = PolygonManagementServiceClient.get_transport_class(transport_name)(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert transport.kind == transport_name

def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.PolygonManagementServiceGrpcTransport,
    )

def test_polygon_management_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.PolygonManagementServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_polygon_management_service_base_transport():
    # Instantiate the base transport.
    with mock.patch('oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.transports.PolygonManagementServiceTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.PolygonManagementServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'list_layers',
        'create_layer',
        'delete_layer',
        'copy_layer',
        'describe_layer',
        'share_layer',
        'unshare_layer',
        'list_polygons',
        'add_polygon',
        'update_polygon',
        'delete_polygon',
        'batch_add_polygons',
        'replace_polygons',
        'drop_polygons',
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Catch all for all remaining methods and properties
    remainder = [
        'kind',
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_polygon_management_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(google.auth, 'load_credentials_from_file', autospec=True) as load_creds, mock.patch('oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.transports.PolygonManagementServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.PolygonManagementServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json",
            scopes=None,
            default_scopes=(
),
            quota_project_id="octopus",
        )


def test_polygon_management_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc, mock.patch('oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.transports.PolygonManagementServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.PolygonManagementServiceTransport()
        adc.assert_called_once()


def test_polygon_management_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        PolygonManagementServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.PolygonManagementServiceGrpcTransport,
        transports.PolygonManagementServiceGrpcAsyncIOTransport,
    ],
)
def test_polygon_management_service_transport_auth_adc(transport_class):
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
    "transport_class",
    [
        transports.PolygonManagementServiceGrpcTransport,
        transports.PolygonManagementServiceGrpcAsyncIOTransport,
    ],
)
def test_polygon_management_service_transport_auth_gdch_credentials(transport_class):
    host = 'https://language.com'
    api_audience_tests = [None, 'https://language2.com']
    api_audience_expect = [host, 'https://language2.com']
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, 'default', autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(return_value=gdch_mock)
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(
                e
            )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.PolygonManagementServiceGrpcTransport, grpc_helpers),
        (transports.PolygonManagementServiceGrpcAsyncIOTransport, grpc_helpers_async)
    ],
)
def test_polygon_management_service_transport_create_channel(transport_class, grpc_helpers):
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


@pytest.mark.parametrize("transport_class", [transports.PolygonManagementServiceGrpcTransport, transports.PolygonManagementServiceGrpcAsyncIOTransport])
def test_polygon_management_service_grpc_transport_client_cert_source_for_mtls(
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


@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
])
def test_polygon_management_service_host_no_port(transport_name):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com'),
         transport=transport_name,
    )
    assert client.transport._host == (
        'api.oceanbolt.com:443'
    )

@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
])
def test_polygon_management_service_host_with_port(transport_name):
    client = PolygonManagementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com:8000'),
        transport=transport_name,
    )
    assert client.transport._host == (
        'api.oceanbolt.com:8000'
    )

def test_polygon_management_service_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.PolygonManagementServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_polygon_management_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.PolygonManagementServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.PolygonManagementServiceGrpcTransport, transports.PolygonManagementServiceGrpcAsyncIOTransport])
def test_polygon_management_service_transport_channel_mtls_with_client_cert_source(
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
@pytest.mark.parametrize("transport_class", [transports.PolygonManagementServiceGrpcTransport, transports.PolygonManagementServiceGrpcAsyncIOTransport])
def test_polygon_management_service_transport_channel_mtls_with_adc(
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
    actual = PolygonManagementServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = PolygonManagementServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = PolygonManagementServiceClient.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(folder=folder, )
    actual = PolygonManagementServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = PolygonManagementServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = PolygonManagementServiceClient.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(organization=organization, )
    actual = PolygonManagementServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = PolygonManagementServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = PolygonManagementServiceClient.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(project=project, )
    actual = PolygonManagementServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = PolygonManagementServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = PolygonManagementServiceClient.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = PolygonManagementServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = PolygonManagementServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = PolygonManagementServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.PolygonManagementServiceTransport, '_prep_wrapped_messages') as prep:
        client = PolygonManagementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.PolygonManagementServiceTransport, '_prep_wrapped_messages') as prep:
        transport_class = PolygonManagementServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

@pytest.mark.asyncio
async def test_transport_close_async():
    client = PolygonManagementServiceAsyncClient(
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
        client = PolygonManagementServiceClient(
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
        client = PolygonManagementServiceClient(
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
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport),
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
                api_audience=None,
            )
