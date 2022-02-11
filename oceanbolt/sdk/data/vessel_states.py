from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas)


class VesselStates:
    """    The ``VesselStates`` returns a list for VesselStates for the given dates and imo numbers requested.    """

    RESOURCE_NAME = "vesselstates"

    def __init__(self, client: APIClient):
        self.client = client._vessel_states_client()

    def get(self, **kwargs):
        """Retrieves trade flow data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.get_vessel_states(kwargs).vessel_states)


class VesselStatesForDate:
    """The ``VesselStatesForDate`` returns list of VesselStates for the entire fleet for the date specified.   """

    RESOURCE_NAME = "vesselstatesfordate"

    def __init__(self, client: APIClient):
        self.client = client._vessel_states_client()

    def get(self, **kwargs):
        """Retrieves timeseries data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.get_vessel_states_for_date(kwargs).vessel_states)
