from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas)


class DryDockStays:
    """
    The ``DryDockStays`` returns list of historical dry dock stays.
    """

    RESOURCE_NAME = "drydock/liststays"

    def __init__(self, client: APIClient):
        self.client = client._drydock_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.get_tonnage_dry_dock(kwargs).timeseries)

# class DryDockTimeseries:
#    """
#    The ``DryDockTimeseries`` returns a timeseries of historical dry dock stays.
#    """
#
#    RESOURCE_NAME = "drydock/timeseries"
#
#    def __init__(self, client: APIClient):
#        self.client = client._congestion_client()
#
#    def get(self, **kwargs):
#        return pb_list_to_pandas(self.client.get_congestion_vessels(kwargs).current_vessels)
