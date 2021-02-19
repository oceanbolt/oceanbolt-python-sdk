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
        kwargs = validate(kwargs)
        df = pb_list_to_pandas(self.client.get_congestion_vessels(kwargs).current_vessels)
        del df["speed"]
        del df["course"]
        del df["lat"]
        del df["lon"]
        return df


class CongestionTimeseries:
    """
    The ``CongestionTimeseries`` returns timeseries on congestion, including data on number of congested vessels, congested dwt, waiting times etc.
    """

    RESOURCE_NAME = "congestion/timeseries"

    def __init__(self, client: APIClient):
        self.client = client._congestion_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        return pb_timeseries_to_pandas(self.client.get_congestion_timeseries(kwargs).timeseries)
