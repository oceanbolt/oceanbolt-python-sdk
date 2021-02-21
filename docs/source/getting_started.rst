Getting Started
===============

Setup
_____
The SDK supports the following python versions: 3.6, 3.7, 3.8, and 3.9

In order to install, run the following:

    pip install oceanbolt.sdk

In order to upgrade an existing installation, run the following:

    pip install oceanbolt.sdk --update

Setting the API access token
____________________________
The API token is set when creating a base api client class instance.

It can be set in two different ways:

1. Setting the API key from ENV:
    The API can set by specifying the **OCEANBOLT_API_KEY** ENV variable.

    `OCEANBOLT_API_KEY=<your access token>`

    If the API key is set through ENV variable, it will automatically be picked up by the SDK when creating a base API client.

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    base_client = APIClient()


2. Setting the API key manually:
    The API key can also be specified manually when creating an API client.

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    base_client = APIClient("<your access token>")


*If both options are set simultaneously, the manual inputted API key will take precedence.*

Connecting and accessing data
_____________________________

When a api base client has been created, this base client can be used to
connect to the different data endpoints that are provided in the Oceanbolt API.

For example in order to access the TradeFlowTimeseries data endpoint, we would do the following:

.. code-block:: python

    trade_flows = TradeFlowTimeseries(base_client)

Once connection is set up to a data endpoint, data can be access using the `get` method:

.. code-block:: python

    trade_flows.get()

The `get` method accepts a range of different filter arguments to customize and filter the data returned.
All arguments are document on for each of the individual data endpoints. As an example the arguments
allowed for the **TradeFlowTimeseries** is shown here: `python <https://python-sdk.oceanbolt.com/en/latest/tradeflows_v3/timeseries.html#arguments>`_

For example we could add filters to limit the date range we are querying for,
while also changing the frequency of the data to weekly:

.. code-block:: python

    from datetime import date

    df = trade_flows.get(
        start_date=date(2020,1,1)
        end_date=date(2020,12,31)
        frequency="weekly"
    )

The "get" Method
""""""""""""""""
Data is always accessed through the `"get"` method. The `"get"` method is available on all data endpoint classes.
The data is returned as a pandas.DataFrame(),allowing for further data processing in an easy and smooth way.


Full code example
"""""""""""""""""

The full code for the example above:

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.trade_flows import TradeFlowTimeseries
    from datetime import date

    base_client = APIClient(<"your access token>") # here we are using the manual method to specify the token
    trade_flows = TradeFlowTimeseries(base_client)

    df = trade_flows.get(
        start_date=date(2020,1,1)
        end_date=date(2020,12,31)
        frequency="weekly"
    )

or in more compact way:

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.trade_flows import TradeFlowTimeseries
    from datetime import date

    base_client = APIClient(<"your access token>") # here we are using the manual method to specify the token

    df = TradeFlowTimeseries(base_client).get(
        start_date=date(2020,1,1)
        end_date=date(2020,12,31)
        frequency="weekly"
    )