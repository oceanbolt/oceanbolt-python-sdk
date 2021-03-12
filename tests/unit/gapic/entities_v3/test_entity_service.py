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
from oceanbolt.com.entities_v3.services.entity_service import EntityServiceAsyncClient
from oceanbolt.com.entities_v3.services.entity_service import EntityServiceClient
from oceanbolt.com.entities_v3.services.entity_service import transports
from oceanbolt.com.entities_v3.types import service


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

    assert EntityServiceClient._get_default_mtls_endpoint(None) is None
    assert EntityServiceClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert EntityServiceClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    assert EntityServiceClient._get_default_mtls_endpoint(sandbox_endpoint) == sandbox_mtls_endpoint
    assert EntityServiceClient._get_default_mtls_endpoint(sandbox_mtls_endpoint) == sandbox_mtls_endpoint
    assert EntityServiceClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


def test_entity_service_client_from_service_account_info():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = EntityServiceClient.from_service_account_info(info)
        assert client.transport._credentials == creds

        assert client.transport._host == 'api.oceanbolt.com:443'


@pytest.mark.parametrize("client_class", [
    EntityServiceClient,
    EntityServiceAsyncClient,
])
def test_entity_service_client_from_service_account_file(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client.transport._credentials == creds

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client.transport._credentials == creds

        assert client.transport._host == 'api.oceanbolt.com:443'


def test_entity_service_client_get_transport_class():
    transport = EntityServiceClient.get_transport_class()
    available_transports = [
        transports.EntityServiceGrpcTransport,
    ]
    assert transport in available_transports

    transport = EntityServiceClient.get_transport_class("grpc")
    assert transport == transports.EntityServiceGrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (EntityServiceClient, transports.EntityServiceGrpcTransport, "grpc"),
    (EntityServiceAsyncClient, transports.EntityServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
@mock.patch.object(EntityServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(EntityServiceClient))
@mock.patch.object(EntityServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(EntityServiceAsyncClient))
def test_entity_service_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(EntityServiceClient, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(EntityServiceClient, 'get_transport_class') as gtc:
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

    (EntityServiceClient, transports.EntityServiceGrpcTransport, "grpc", "true"),
    (EntityServiceAsyncClient, transports.EntityServiceGrpcAsyncIOTransport, "grpc_asyncio", "true"),
    (EntityServiceClient, transports.EntityServiceGrpcTransport, "grpc", "false"),
    (EntityServiceAsyncClient, transports.EntityServiceGrpcAsyncIOTransport, "grpc_asyncio", "false"),

])
@mock.patch.object(EntityServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(EntityServiceClient))
@mock.patch.object(EntityServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(EntityServiceAsyncClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_entity_service_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
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
    (EntityServiceClient, transports.EntityServiceGrpcTransport, "grpc"),
    (EntityServiceAsyncClient, transports.EntityServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
def test_entity_service_client_client_options_scopes(client_class, transport_class, transport_name):
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
    (EntityServiceClient, transports.EntityServiceGrpcTransport, "grpc"),
    (EntityServiceAsyncClient, transports.EntityServiceGrpcAsyncIOTransport, "grpc_asyncio"),
])
def test_entity_service_client_client_options_credentials_file(client_class, transport_class, transport_name):
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


def test_entity_service_client_client_options_from_dict():
    with mock.patch('oceanbolt.com.entities_v3.services.entity_service.transports.EntityServiceGrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = EntityServiceClient(
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


def test_list_segments(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_segments),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListSegmentsResponse(
        )

        response = client.list_segments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListSegmentsResponse)


def test_list_segments_from_dict():
    test_list_segments(request_type=dict)


@pytest.mark.asyncio
async def test_list_segments_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_segments),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListSegmentsResponse(
        ))

        response = await client.list_segments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListSegmentsResponse)


@pytest.mark.asyncio
async def test_list_segments_async_from_dict():
    await test_list_segments_async(request_type=dict)


def test_list_zones(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_zones),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListTonnageZonesResponse(
        )

        response = client.list_zones(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListTonnageZonesResponse)


def test_list_zones_from_dict():
    test_list_zones(request_type=dict)


@pytest.mark.asyncio
async def test_list_zones_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_zones),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListTonnageZonesResponse(
        ))

        response = await client.list_zones(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListTonnageZonesResponse)


@pytest.mark.asyncio
async def test_list_zones_async_from_dict():
    await test_list_zones_async(request_type=dict)


def test_list_zones_with_polygons(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_zones_with_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListTonnageZonesWithPolygonsResponse(
        )

        response = client.list_zones_with_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListTonnageZonesWithPolygonsResponse)


def test_list_zones_with_polygons_from_dict():
    test_list_zones_with_polygons(request_type=dict)


@pytest.mark.asyncio
async def test_list_zones_with_polygons_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_zones_with_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListTonnageZonesWithPolygonsResponse(
        ))

        response = await client.list_zones_with_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListTonnageZonesWithPolygonsResponse)


@pytest.mark.asyncio
async def test_list_zones_with_polygons_async_from_dict():
    await test_list_zones_with_polygons_async(request_type=dict)


def test_list_regions(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_regions),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListRegionsResponse(
        )

        response = client.list_regions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListRegionsResponse)


def test_list_regions_from_dict():
    test_list_regions(request_type=dict)


@pytest.mark.asyncio
async def test_list_regions_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_regions),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListRegionsResponse(
        ))

        response = await client.list_regions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListRegionsResponse)


@pytest.mark.asyncio
async def test_list_regions_async_from_dict():
    await test_list_regions_async(request_type=dict)


def test_list_commodities(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_commodities),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCommoditiesResponse(
        )

        response = client.list_commodities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListCommoditiesResponse)


def test_list_commodities_from_dict():
    test_list_commodities(request_type=dict)


@pytest.mark.asyncio
async def test_list_commodities_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_commodities),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListCommoditiesResponse(
        ))

        response = await client.list_commodities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListCommoditiesResponse)


@pytest.mark.asyncio
async def test_list_commodities_async_from_dict():
    await test_list_commodities_async(request_type=dict)


def test_list_countries(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_countries),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCountriesResponse(
        )

        response = client.list_countries(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListCountriesResponse)


def test_list_countries_from_dict():
    test_list_countries(request_type=dict)


@pytest.mark.asyncio
async def test_list_countries_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_countries),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListCountriesResponse(
        ))

        response = await client.list_countries(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListCountriesResponse)


@pytest.mark.asyncio
async def test_list_countries_async_from_dict():
    await test_list_countries_async(request_type=dict)


def test_list_regions_with_polygons(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_regions_with_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListRegionsWithPolygonResponse(
        )

        response = client.list_regions_with_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListRegionsWithPolygonResponse)


def test_list_regions_with_polygons_from_dict():
    test_list_regions_with_polygons(request_type=dict)


@pytest.mark.asyncio
async def test_list_regions_with_polygons_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_regions_with_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListRegionsWithPolygonResponse(
        ))

        response = await client.list_regions_with_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListRegionsWithPolygonResponse)


@pytest.mark.asyncio
async def test_list_regions_with_polygons_async_from_dict():
    await test_list_regions_with_polygons_async(request_type=dict)


def test_list_ports(transport: str = 'grpc', request_type=service.EmptyParams):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_ports),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListPortsResponse(
        )

        response = client.list_ports(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.ListPortsResponse)


def test_list_ports_from_dict():
    test_list_ports(request_type=dict)


@pytest.mark.asyncio
async def test_list_ports_async(transport: str = 'grpc_asyncio', request_type=service.EmptyParams):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_ports),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.ListPortsResponse(
        ))

        response = await client.list_ports(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.EmptyParams()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ListPortsResponse)


@pytest.mark.asyncio
async def test_list_ports_async_from_dict():
    await test_list_ports_async(request_type=dict)


def test_search_polygons(transport: str = 'grpc', request_type=service.SearchRequest):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.SearchPolygonsResponse(
        )

        response = client.search_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.SearchRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.SearchPolygonsResponse)


def test_search_polygons_from_dict():
    test_search_polygons(request_type=dict)


@pytest.mark.asyncio
async def test_search_polygons_async(transport: str = 'grpc_asyncio', request_type=service.SearchRequest):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_polygons),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.SearchPolygonsResponse(
        ))

        response = await client.search_polygons(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.SearchRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.SearchPolygonsResponse)


@pytest.mark.asyncio
async def test_search_polygons_async_from_dict():
    await test_search_polygons_async(request_type=dict)


def test_search_vessels(transport: str = 'grpc', request_type=service.SearchRequest):
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.SearchVesselsResponse(
        )

        response = client.search_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.SearchRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, service.SearchVesselsResponse)


def test_search_vessels_from_dict():
    test_search_vessels(request_type=dict)


@pytest.mark.asyncio
async def test_search_vessels_async(transport: str = 'grpc_asyncio', request_type=service.SearchRequest):
    client = EntityServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_vessels),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.SearchVesselsResponse(
        ))

        response = await client.search_vessels(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.SearchRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.SearchVesselsResponse)


@pytest.mark.asyncio
async def test_search_vessels_async_from_dict():
    await test_search_vessels_async(request_type=dict)


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.EntityServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EntityServiceClient(
            credentials=credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.EntityServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EntityServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.EntityServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EntityServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.EntityServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = EntityServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.EntityServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.EntityServiceGrpcAsyncIOTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize("transport_class", [
    transports.EntityServiceGrpcTransport,
    transports.EntityServiceGrpcAsyncIOTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.EntityServiceGrpcTransport,
    )


def test_entity_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(exceptions.DuplicateCredentialArgs):
        transport = transports.EntityServiceTransport(
            credentials=credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_entity_service_base_transport():
    # Instantiate the base transport.
    with mock.patch('oceanbolt.com.entities_v3.services.entity_service.transports.EntityServiceTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.EntityServiceTransport(
            credentials=credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'list_segments',
        'list_zones',
        'list_zones_with_polygons',
        'list_regions',
        'list_commodities',
        'list_countries',
        'list_regions_with_polygons',
        'list_ports',
        'search_polygons',
        'search_vessels',
        )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())


def test_entity_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(auth, 'load_credentials_from_file') as load_creds, mock.patch('oceanbolt.com.entities_v3.services.entity_service.transports.EntityServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.EntityServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json", scopes=(
            ),
            quota_project_id="octopus",
        )


def test_entity_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(auth, 'default') as adc, mock.patch('oceanbolt.com.entities_v3.services.entity_service.transports.EntityServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.EntityServiceTransport()
        adc.assert_called_once()


def test_entity_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        EntityServiceClient()
        adc.assert_called_once_with(scopes=(),
            quota_project_id=None,
        )


def test_entity_service_transport_auth_adc():
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transports.EntityServiceGrpcTransport(host="squid.clam.whelk", quota_project_id="octopus")
        adc.assert_called_once_with(scopes=(),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize("transport_class", [transports.EntityServiceGrpcTransport, transports.EntityServiceGrpcAsyncIOTransport])
def test_entity_service_grpc_transport_client_cert_source_for_mtls(
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


def test_entity_service_host_no_port():
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com'),
    )
    assert client.transport._host == 'api.oceanbolt.com:443'


def test_entity_service_host_with_port():
    client = EntityServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='api.oceanbolt.com:8000'),
    )
    assert client.transport._host == 'api.oceanbolt.com:8000'


def test_entity_service_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.EntityServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_entity_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.EntityServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.EntityServiceGrpcTransport, transports.EntityServiceGrpcAsyncIOTransport])
def test_entity_service_transport_channel_mtls_with_client_cert_source(
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
@pytest.mark.parametrize("transport_class", [transports.EntityServiceGrpcTransport, transports.EntityServiceGrpcAsyncIOTransport])
def test_entity_service_transport_channel_mtls_with_adc(
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
    actual = EntityServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
    "billing_account": "clam",

    }
    path = EntityServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = EntityServiceClient.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "whelk"

    expected = "folders/{folder}".format(folder=folder, )
    actual = EntityServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
    "folder": "octopus",

    }
    path = EntityServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = EntityServiceClient.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "oyster"

    expected = "organizations/{organization}".format(organization=organization, )
    actual = EntityServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
    "organization": "nudibranch",

    }
    path = EntityServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = EntityServiceClient.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "cuttlefish"

    expected = "projects/{project}".format(project=project, )
    actual = EntityServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
    "project": "mussel",

    }
    path = EntityServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = EntityServiceClient.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "winkle"
    location = "nautilus"

    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = EntityServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
    "project": "scallop",
    "location": "abalone",

    }
    path = EntityServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = EntityServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_withDEFAULT_CLIENT_INFO():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.EntityServiceTransport, '_prep_wrapped_messages') as prep:
        client = EntityServiceClient(
            credentials=credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.EntityServiceTransport, '_prep_wrapped_messages') as prep:
        transport_class = EntityServiceClient.get_transport_class()
        transport = transport_class(
            credentials=credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)
