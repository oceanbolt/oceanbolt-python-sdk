Trade Flow Timeseries
=====================
Find aggregate trade flows between countries, regions, for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *How many tons of iron ore has been imported into China each day over the last year?*
- *How many tonnes of alumina did Hydro export from its Alunorte Facility each week over the last 3 years?*
- *How have average haul (nautical miles/ton) for capesize vessels changed over time?*

.. autoclass:: oceanbolt.sdk.data.trade_flows.TradeFlowTimeseries
    :members:

Example
-------
*What was the monthly export of iron ore from Port Hedland over the last year?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.trade_flows import TradeFlowTimeseries
    from datetime import date


    base_client = APIClient("<token>")
    df = TradeFlowTimeseries(base_client).get(
        frequency="monthly",
        load_port_unlocode=['AUPHE'],
        commodity_group=['iron_ore'],
        start_date=date(2020, 1, 1),
        end_date=date(2020, 12, 31),
    )

Returns:

.. csv-table::
    :header: "date","value"

    "2020-01-01", "40386200.0"
    "2020-02-01", "38528300.0"
    "2020-03-01", "46603900.0"
    "2020-04-01", "44728400.0"
    "2020-05-01", "47670900.0"
    "2020-06-01", "50618500.0"
    "2020-07-01", "44668200.0"
    "2020-08-01", "47672900.0"
    "2020-09-01", "44929400.0"
    "2020-10-01", "45641300.0"
    "2020-11-01", "41011600.0"
    "2020-12-01", "46966000.0"

Arguments
---------
.. autoclass:: oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.tradeflows_v3.types.GetTradeFlowTimeseriesResponse
    :members:

.. autoclass:: oceanbolt.com.tradeflows_v3.types.TimeseriesGroup
    :members:

.. autoclass:: oceanbolt.com.tradeflows_v3.types.TimeseriesRow
    :members: