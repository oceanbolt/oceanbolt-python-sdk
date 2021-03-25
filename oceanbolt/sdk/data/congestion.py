from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas, pb_timeseries_to_pandas)


class CongestionVessels:
    """
    The ``CongestionVessels`` returns a list of either current congested vessels or a list of congested vessels at a prior historical date.
    """

    RESOURCE_NAME = "congestion/listvessels"

    def __init__(self, client: APIClient):
        self.client = client._congestion_client()

    def get(self, **kwargs):
        """Retrieves current congested vessels as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        df = pb_list_to_pandas(self.client.get_congestion_vessels(kwargs).current_vessels)
        if "speed" in df.columns:
            del df["speed"]
        if "course" in df.columns:
            del df["course"]
        if "lat" in df.columns:
            del df["lat"]
        if "lng" in df.columns:
            del df["lng"]
        return df


class CongestionTimeseries:
    """
    The ``CongestionTimeseries`` returns timeseries on congestion, including data on number of congested vessels, congested dwt, waiting times etc.
    """

    RESOURCE_NAME = "congestion/timeseries"

    def __init__(self, client: APIClient):
        self.client = client._congestion_client()

    def get(self, **kwargs):
        """Retrieves congested timeseries as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_timeseries_to_pandas(self.client.get_congestion_timeseries(kwargs).timeseries)
