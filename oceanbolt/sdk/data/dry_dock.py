from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas, pb_timeseries_to_pandas)


class DryDockCurrentVessels:
    """
    The ``DryDockCurrentVessels`` returns list of currently active dry dock stays.
    """

    RESOURCE_NAME = "drydock/currentvessels"

    def __init__(self, client: APIClient):
        self.client = client._drydock_client()

    def get(self, **kwargs):
        """Retrieves currently active dry dock data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.get_dry_dock_vessels(kwargs).current_vessels)


class DryDockHistoricalStays:
    """
    The ``DryDockHistoricalStays`` returns list of historical dry dock stays.
    """

    RESOURCE_NAME = "drydock/liststays"

    def __init__(self, client: APIClient):
        self.client = client._drydock_client()

    def get(self, **kwargs):
        """Retrieves historical dry dock data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.get_dry_dock_stays(kwargs).data)


class DryDockTimeseries:
    """
   The ``DryDockTimeseries`` returns a timeseries of historical dry dock stays.
   """

    RESOURCE_NAME = "drydock/timeseries"

    def __init__(self, client: APIClient):
        self.client = client._drydock_client()

    def get(self, **kwargs):
        """Retrieves dry dock timeseries data as a pandas.DataFrame"""
        return pb_timeseries_to_pandas(self.client.get_dry_dock_timeseries(kwargs).timeseries)
