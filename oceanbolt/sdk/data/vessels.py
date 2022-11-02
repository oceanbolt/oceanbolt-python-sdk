from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas)


class Vessels:
    """    The ``Vessels`` returns a list of vessels.    """

    RESOURCE_NAME = "vessels/listvessels"

    def __init__(self, client: APIClient):
        self.client = client._vessels_client()
        self.metadata = client.metadata

    def get(self, **kwargs):
        """Retrieves vessels as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.list_vessels(request=kwargs, metadata=self.metadata).vessels)


class StoppageEvents:
    """The ``StoppageEvents`` returns list of historical stoppage events."""

    RESOURCE_NAME = "vessels/stoppageevents"

    def __init__(self, client: APIClient):
        self.client = client._vessels_client()
        self.metadata = client.metadata

    def get(self, **kwargs):
        """Retrieves data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.list_stoppage_events(request=kwargs, metadata=self.metadata).stoppage_events)

class DarkPeriodEvents:
    """The ``DarkPeriodEvents`` returns list of historical dark period events."""

    RESOURCE_NAME = "vessels/darkperiodevents"

    def __init__(self, client: APIClient):
        self.client = client._vessels_client()
        self.metadata = client.metadata

    def get(self, **kwargs):
        """Retrieves data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.list_dark_period_events(request=kwargs, metadata=self.metadata).dark_period_events)
