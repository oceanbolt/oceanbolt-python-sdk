from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas)


class Vessels:
    """    The ``Vessels`` returns a list of vessels.    """

    RESOURCE_NAME = "vessels/listvessels"

    def __init__(self, client: APIClient):
        self.client = client._vessels_client()

    def get(self, **kwargs):
        """Retrieves trade flow data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.list_vessels(kwargs).vessels)


class StoppageEvents:
    """The ``StoppageEvents`` returns list of historical stoppage events."""

    RESOURCE_NAME = "vessels/stoppageevents"

    def __init__(self, client: APIClient):
        self.client = client._vessels_client()

    def get(self, **kwargs):
        """Retrieves timeseries data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.list_stoppage_events(kwargs).stoppage_events)
