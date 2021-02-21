# Oceanbolt Python SDK
The Oceanbolt Python SDK provides access to Oceanbolt data. It is a python wrapper around the Oceanbolt Data API (REST).

It can be easily integrated existing tools such as jupyter notebooks, scripts, and applications.

Data is returned in the form of pandas.DataFrame, which allows for easy manipulation and further data processing. 

The python SDK is available to all Oceanbolt API clients (API authentication token required in order to get access). API tokens can be generated in the Oceanbolt App (app.oceanbolt.com)

## Setup

The SDK supports the following python versions: 3.6, 3.7, 3.8, and 3.9

In order to install, run the following:

    pip install oceanbolt.sdk

In order to upgrade an existing installation, run the following:

    pip install oceanbolt.sdk --update

## Docs
Documentation : https://python-sdk.oceanbolt.com

## Quick Example

````python
from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.data.port_calls import PortCalls
from datetime import date, timedelta

# Create the base API client using your token. Tokens can be created in the Oceanbolt App (app.oceanbolt.com)
base_client = APIClient("<your API access token>")

# Connect to one of the Oceanbolt's data endpoints using the base client object, ie: PortCalls
port_calls_client = PortCalls(base_client)

# Get a list of Port Hedland exports over the last week
hedland_portcalls = port_calls_client.get(
    start_date=date.today() - timedelta(days=7),
    segment=["capesize"],
    unlocode=["AUPHE"],
)

````

