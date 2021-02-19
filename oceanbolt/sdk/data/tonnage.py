from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_timeseries_to_pandas)


class TonnageZoneTimeseries:
    """
    The ``TonnageZoneTimeseries`` returns timeseries on tonnage movements and zone counts.
    """

    RESOURCE_NAME = "tonnage/zone"

    def __init__(self, client: APIClient):
        self.client = client._tonnage_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        df = pb_timeseries_to_pandas(self.client.get_tonnage_zone_count(kwargs).timeseries)
        del df["avg_speed"]
        return df


class FleetSpeedTimeseries:
    """
    The ``FleetSpeedTimeseries`` returns timeseries on fleet speed.
    """

    RESOURCE_NAME = "tonnage/speed"

    def __init__(self, client: APIClient):
        self.client = client._tonnage_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        df = pb_timeseries_to_pandas(self.client.get_tonnage_fleet_speed(kwargs).timeseries)
        del df["vessel_count"]
        del df["vessel_dwt"]
        return df
