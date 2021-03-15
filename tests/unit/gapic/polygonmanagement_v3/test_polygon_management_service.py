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

from google import auth
from google.api_core import client_options
from google.api_core import exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.auth import credentials
from google.auth.exceptions import MutualTLSChannelError
from google.oauth2 import service_account
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service import PolygonManagementServiceAsyncClient
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service import PolygonManagementServiceClient
from oceanbolt.com.polygonmanagement_v3.services.polygon_management_service import transports
from oceanbolt.com.polygonmanagement_v3.types import service


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


def test_polygon_management_service_client_from_service_account_info():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = PolygonManagementServiceClient.from_service_account_info(info)
        assert client.transport._credentials == creds

        assert client.transport._host == 'api.oceanbolt.com:443'


@pytest.mark.parametrize("client_class", [
    PolygonManagementServiceClient,
    PolygonManagementServiceAsyncClient,
])
def test_polygon_management_service_client_from_service_account_file(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client.transport._credentials == creds

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client.transport._credentials == creds

        assert client.transport._host == 'api.oceanbolt.com:443'


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
            credentials=credentials.AnonymousCredentials()
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
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class()

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        with pytest.raises(ValueError):
            client = client_class()

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
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
            client = client_class(client_options=options)

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
                    client = client_class()
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch("google.auth.transport.mtls.has_default_client_cert_source", return_value=False):
                patched.return_value = None
                client = client_class()
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                )


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
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (PolygonManagementServiceClient, transports.PolygonManagementServiceGrpcTransport, "grpc"),
    (PolygonManagementServiceAsyncClient, transports.PolygonManagementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
def test_polygon_management_service_client_client_options_credentials_file(client_class, transport_class, transport_name):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
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
        )


def test_list_layers(transport: str = 'grpc', request_type=service.EmptyParams):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Layers(
        )

        response = client.list_layers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Layers)


def test_list_layers_from_dict():
    test_list_layers(request_type=dict)


@pytest.mark.asyncio
async def test_list_layers_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Layers(
        ))

        response = await client.list_layers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Layers)


@pytest.mark.asyncio
async def test_list_layers_async_from_dict():
    await test_list_layers_async(request_type=dict)


def test_create_layer(transport: str = 'grpc', request_type=service.CreateLayerRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Layer(
            layer_id='layer_id_value',

            layer_name='layer_name_value',

            owner_user_id='owner_user_id_value',

            organization='organization_value',

        )

        response = client.create_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.CreateLayerRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


def test_create_layer_from_dict():
    test_create_layer(request_type=dict)


@pytest.mark.asyncio
async def test_create_layer_async(transport: str = 'grpc_asyncio', request_type=service.CreateLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Layer(
            layer_id='layer_id_value',
            layer_name='layer_name_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))

        response = await client.create_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.CreateLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_create_layer_async_from_dict():
    await test_create_layer_async(request_type=dict)


def test_delete_layer(transport: str = 'grpc', request_type=service.DeleteLayerRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.EmptyResponse(
        )

        response = client.delete_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DeleteLayerRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.EmptyResponse)


def test_delete_layer_from_dict():
    test_delete_layer(request_type=dict)


@pytest.mark.asyncio
async def test_delete_layer_async(transport: str = 'grpc_asyncio', request_type=service.DeleteLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))

        response = await client.delete_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DeleteLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_delete_layer_async_from_dict():
    await test_delete_layer_async(request_type=dict)


def test_describe_layer(transport: str = 'grpc', request_type=service.GetLayerRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Layer(
            layer_id='layer_id_value',

            layer_name='layer_name_value',

            owner_user_id='owner_user_id_value',

            organization='organization_value',

        )

        response = client.describe_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.GetLayerRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


def test_describe_layer_from_dict():
    test_describe_layer(request_type=dict)


@pytest.mark.asyncio
async def test_describe_layer_async(transport: str = 'grpc_asyncio', request_type=service.GetLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Layer(
            layer_id='layer_id_value',
            layer_name='layer_name_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))

        response = await client.describe_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.GetLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_describe_layer_async_from_dict():
    await test_describe_layer_async(request_type=dict)


def test_rename_layer(transport: str = 'grpc', request_type=service.RenameLayerRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.rename_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Layer(
            layer_id='layer_id_value',

            layer_name='layer_name_value',

            owner_user_id='owner_user_id_value',

            organization='organization_value',

        )

        response = client.rename_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.RenameLayerRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


def test_rename_layer_from_dict():
    test_rename_layer(request_type=dict)


@pytest.mark.asyncio
async def test_rename_layer_async(transport: str = 'grpc_asyncio', request_type=service.RenameLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.rename_layer),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Layer(
            layer_id='layer_id_value',
            layer_name='layer_name_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))

        response = await client.rename_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.RenameLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_rename_layer_async_from_dict():
    await test_rename_layer_async(request_type=dict)


def test_share_layer(transport: str = 'grpc', request_type=service.ShareLayerRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Layer(
            layer_id='layer_id_value',

            layer_name='layer_name_value',

            owner_user_id='owner_user_id_value',

            organization='organization_value',

        )

        response = client.share_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


def test_share_layer_from_dict():
    test_share_layer(request_type=dict)


@pytest.mark.asyncio
async def test_share_layer_async(transport: str = 'grpc_asyncio', request_type=service.ShareLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Layer(
            layer_id='layer_id_value',
            layer_name='layer_name_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))

        response = await client.share_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_share_layer_async_from_dict():
    await test_share_layer_async(request_type=dict)


def test_unshare_layer(transport: str = 'grpc', request_type=service.ShareLayerRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Layer(
            layer_id='layer_id_value',

            layer_name='layer_name_value',

            owner_user_id='owner_user_id_value',

            organization='organization_value',

        )

        response = client.unshare_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


def test_unshare_layer_from_dict():
    test_unshare_layer(request_type=dict)


@pytest.mark.asyncio
async def test_unshare_layer_async(transport: str = 'grpc_asyncio', request_type=service.ShareLayerRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Layer(
            layer_id='layer_id_value',
            layer_name='layer_name_value',
            owner_user_id='owner_user_id_value',
            organization='organization_value',
        ))

        response = await client.unshare_layer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ShareLayerRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Layer)

    assert response.layer_id == 'layer_id_value'

    assert response.layer_name == 'layer_name_value'

    assert response.owner_user_id == 'owner_user_id_value'

    assert response.organization == 'organization_value'


@pytest.mark.asyncio
async def test_unshare_layer_async_from_dict():
    await test_unshare_layer_async(request_type=dict)


def test_list_polygons(transport: str = 'grpc', request_type=service.ListPolygonsRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Polygons(
            polygons_in_layer=1837,

        )

        response = client.list_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ListPolygonsRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Polygons)

    assert response.polygons_in_layer == 1837


def test_list_polygons_from_dict():
    test_list_polygons(request_type=dict)


@pytest.mark.asyncio
async def test_list_polygons_async(transport: str = 'grpc_asyncio', request_type=service.ListPolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Polygons(
            polygons_in_layer=1837,
        ))

        response = await client.list_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ListPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Polygons)

    assert response.polygons_in_layer == 1837


@pytest.mark.asyncio
async def test_list_polygons_async_from_dict():
    await test_list_polygons_async(request_type=dict)


def test_add_polygon(transport: str = 'grpc', request_type=service.AddPolygonRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Polygon(
            layer_id='layer_id_value',

            polygon_id='polygon_id_value',

            polygon_name='polygon_name_value',

        )

        response = client.add_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.AddPolygonRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Polygon)

    assert response.layer_id == 'layer_id_value'

    assert response.polygon_id == 'polygon_id_value'

    assert response.polygon_name == 'polygon_name_value'


def test_add_polygon_from_dict():
    test_add_polygon(request_type=dict)


@pytest.mark.asyncio
async def test_add_polygon_async(transport: str = 'grpc_asyncio', request_type=service.AddPolygonRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Polygon(
            layer_id='layer_id_value',
            polygon_id='polygon_id_value',
            polygon_name='polygon_name_value',
        ))

        response = await client.add_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.AddPolygonRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Polygon)

    assert response.layer_id == 'layer_id_value'

    assert response.polygon_id == 'polygon_id_value'

    assert response.polygon_name == 'polygon_name_value'


@pytest.mark.asyncio
async def test_add_polygon_async_from_dict():
    await test_add_polygon_async(request_type=dict)


def test_update_polygon(transport: str = 'grpc', request_type=service.UpdatePolygonRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.Polygon(
            layer_id='layer_id_value',

            polygon_id='polygon_id_value',

            polygon_name='polygon_name_value',

        )

        response = client.update_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.UpdatePolygonRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.Polygon)

    assert response.layer_id == 'layer_id_value'

    assert response.polygon_id == 'polygon_id_value'

    assert response.polygon_name == 'polygon_name_value'


def test_update_polygon_from_dict():
    test_update_polygon(request_type=dict)


@pytest.mark.asyncio
async def test_update_polygon_async(transport: str = 'grpc_asyncio', request_type=service.UpdatePolygonRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Polygon(
            layer_id='layer_id_value',
            polygon_id='polygon_id_value',
            polygon_name='polygon_name_value',
        ))

        response = await client.update_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.UpdatePolygonRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Polygon)

    assert response.layer_id == 'layer_id_value'

    assert response.polygon_id == 'polygon_id_value'

    assert response.polygon_name == 'polygon_name_value'


@pytest.mark.asyncio
async def test_update_polygon_async_from_dict():
    await test_update_polygon_async(request_type=dict)


def test_delete_polygon(transport: str = 'grpc', request_type=service.DeletePolygonRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.EmptyResponse(
        )

        response = client.delete_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DeletePolygonRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.EmptyResponse)


def test_delete_polygon_from_dict():
    test_delete_polygon(request_type=dict)


@pytest.mark.asyncio
async def test_delete_polygon_async(transport: str = 'grpc_asyncio', request_type=service.DeletePolygonRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))

        response = await client.delete_polygon(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DeletePolygonRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_delete_polygon_async_from_dict():
    await test_delete_polygon_async(request_type=dict)


def test_batch_add_polygons(transport: str = 'grpc', request_type=service.BatchPolygonsRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.EmptyResponse(
        )

        response = client.batch_add_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.BatchPolygonsRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.EmptyResponse)


def test_batch_add_polygons_from_dict():
    test_batch_add_polygons(request_type=dict)


@pytest.mark.asyncio
async def test_batch_add_polygons_async(transport: str = 'grpc_asyncio', request_type=service.BatchPolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))

        response = await client.batch_add_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.BatchPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_batch_add_polygons_async_from_dict():
    await test_batch_add_polygons_async(request_type=dict)


def test_replace_polygons(transport: str = 'grpc', request_type=service.BatchPolygonsRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.EmptyResponse(
        )

        response = client.replace_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.BatchPolygonsRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.EmptyResponse)


def test_replace_polygons_from_dict():
    test_replace_polygons(request_type=dict)


@pytest.mark.asyncio
async def test_replace_polygons_async(transport: str = 'grpc_asyncio', request_type=service.BatchPolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))

        response = await client.replace_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.BatchPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_replace_polygons_async_from_dict():
    await test_replace_polygons_async(request_type=dict)


def test_drop_polygons(transport: str = 'grpc', request_type=service.DropPolygonsRequest):
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = service.EmptyResponse(
        )

        response = client.drop_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DropPolygonsRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.EmptyResponse)


def test_drop_polygons_from_dict():
    test_drop_polygons(request_type=dict)


@pytest.mark.asyncio
async def test_drop_polygons_async(transport: str = 'grpc_asyncio', request_type=service.DropPolygonsRequest):
    client = PolygonManagementServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
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
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.EmptyResponse(
        ))

        response = await client.drop_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DropPolygonsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.EmptyResponse)


@pytest.mark.asyncio
async def test_drop_polygons_async_from_dict():
    await test_drop_polygons_async(request_type=dict)


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            credentials=credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PolygonManagementServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = PolygonManagementServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PolygonManagementServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.PolygonManagementServiceGrpcAsyncIOTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize("transport_class", [
    transports.PolygonManagementServiceGrpcTransport,
    transports.PolygonManagementServiceGrpcAsyncIOTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.PolygonManagementServiceGrpcTransport,
    )


def test_polygon_management_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(exceptions.DuplicateCredentialArgs):
        transport = transports.PolygonManagementServiceTransport(
            credentials=credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_polygon_management_service_base_transport():
    # Instantiate the base transport.
    with mock.patch('oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.transports.PolygonManagementServiceTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.PolygonManagementServiceTransport(
            credentials=credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'list_layers',
        'create_layer',
        'delete_layer',
        'describe_layer',
        'rename_layer',
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


def test_polygon_management_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(auth, 'load_credentials_from_file') as load_creds, mock.patch('oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.transports.PolygonManagementServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.PolygonManagementServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json", scopes=(
            ),
            quota_project_id="octopus",
        )


def test_polygon_management_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(auth, 'default') as adc, mock.patch('oceanbolt.com.polygonmanagement_v3.services.polygon_management_service.transports.PolygonManagementServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.PolygonManagementServiceTransport()
        adc.assert_called_once()


def test_polygon_management_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        PolygonManagementServiceClient()
        adc.assert_called_once_with(scopes=(),
            quota_project_id=None,
        )


def test_polygon_management_service_transport_auth_adc():
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transports.PolygonManagementServiceGrpcTransport(host="squid.clam.whelk", quota_project_id="octopus")
        adc.assert_called_once_with(scopes=(),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize("transport_class", [transports.PolygonManagementServiceGrpcTransport, transports.PolygonManagementServiceGrpcAsyncIOTransport])
def test_polygon_management_service_grpc_transport_client_cert_source_for_mtls(
    transport_class
):
    cred = credentials.AnonymousCredentials()

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
            scopes=(
            ),
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


def test_polygon_management_service_host_no_port():
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com'),
    )
    assert client.transport._host == 'api.oceanbolt.com:443'


def test_polygon_management_service_host_with_port():
    client = PolygonManagementServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com:8000'),
    )
    assert client.transport._host == 'api.oceanbolt.com:8000'


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

            cred = credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(auth, 'default') as adc:
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
                scopes=(
                ),
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
                scopes=(
                ),
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


def test_client_withDEFAULT_CLIENT_INFO():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.PolygonManagementServiceTransport, '_prep_wrapped_messages') as prep:
        client = PolygonManagementServiceClient(
            credentials=credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.PolygonManagementServiceTransport, '_prep_wrapped_messages') as prep:
        transport_class = PolygonManagementServiceClient.get_transport_class()
        transport = transport_class(
            credentials=credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)
