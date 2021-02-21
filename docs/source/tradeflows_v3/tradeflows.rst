List Trade Flows
================
Retrieve list of trade flows between countries, regions, for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *Which vessels loaded coal in Richards Bay in 2020?*
- *Which vessels discharged Australian coal into China in the past 30 days?*
- *Which vessels are currently loading fertilizers from the Arabian Gulf?*

.. autoclass:: oceanbolt.sdk.data.trade_flows.TradeFlows
    :members:

Example
-------
*Which vessels discharged Australian coal into China in the past 30 days?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.trade_flows import TradeFlowTimeseries
    from datetime import date, timedelta

    base_client = APIClient("<token>")
    df = TradeFlowTimeseries(base_client).get(
        load_country_code=['AU'],
        discharge_country_code=['CN'],
        commodity_group=['coal'],
        start_date=date.today() - timedelta(days=7),
        flow_direction="import", #Specified to filter and group on import date
    )

Returns:

TBD


Arguments
---------
.. autoclass:: oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.tradeflows_v3.types.GetTradeFlowsResponse
    :members:

.. autoclass:: oceanbolt.com.tradeflows_v3.types.TradeFlow
    :members:

