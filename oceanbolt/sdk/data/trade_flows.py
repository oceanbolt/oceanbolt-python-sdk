from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas, pb_timeseries_to_pandas)


class TradeFlows:
    """    The ``TradeFlows`` returns list of historical voyages.    """

    RESOURCE_NAME = "tradeflows/listflows"

    def __init__(self, client: APIClient):
        self.client = client._trade_flows_client()

    def get(self, **kwargs):
        """Retrieves trade flow data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.get_trade_flows(kwargs).data)


class TradeFlowTimeseries:
    """The ``TradeFlowsTimeseries`` returns list of historical voyages."""

    RESOURCE_NAME = "tradeflows/timeseries"

    def __init__(self, client: APIClient):
        self.client = client._trade_flows_client()

    def get(self, **kwargs):
        """Retrieves timeseries data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_timeseries_to_pandas(self.client.get_trade_flow_timeseries(kwargs).timeseries)
