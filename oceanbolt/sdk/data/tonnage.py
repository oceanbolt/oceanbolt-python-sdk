from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_timeseries_to_pandas)


class FleetStatusTimeseries:
    """
    The ``FleetStatusTimeseries`` returns timeseries on fleet status (number of vessels active in the fleet).
    """

    RESOURCE_NAME = "tonnage/fleetstatus"

    def __init__(self, client: APIClient):
        self.client = client._tonnage_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        df = pb_timeseries_to_pandas(self.client.get_tonnage_fleet_status(kwargs).timeseries)
        return df


class FleetGrowthTimeseries:
    """
    The ``FleetGrowthTimeseries`` returns timeseries on fleet growth.
    """

    RESOURCE_NAME = "tonnage/fleetgrowth"

    def __init__(self, client: APIClient):
        self.client = client._tonnage_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        df = pb_timeseries_to_pandas(self.client.get_tonnage_fleet_growth(kwargs).timeseries)
        return df


class TonnageZoneTimeseries:
    """
    The ``TonnageZoneTimeseries`` returns timeseries on zone counts.
    """

    RESOURCE_NAME = "tonnage/zone"

    def __init__(self, client: APIClient):
        self.client = client._tonnage_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        df = pb_timeseries_to_pandas(self.client.get_tonnage_zone_count(kwargs).timeseries)
        del df["avg_speed"]
        return df


class ZoneChangesTimeseries:
    """
    The ``TonnageZoneChangesTimeseries`` returns timeseries on tonnage movements and zone crossings.
    """

    RESOURCE_NAME = "tonnage/zonechanges"

    def __init__(self, client: APIClient):
        self.client = client._tonnage_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        df = pb_timeseries_to_pandas(self.client.get_tonnage_zone_changes(kwargs).timeseries)
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
        if 'vessel_count' in df.columns:
            del df["vessel_count"]
        if 'vessel_dwt' in df.columns:
            del df["vessel_dwt"]
        return df


class ChineseWatersTimeseries:
    """
    The ``ChineseVesselsChineseWaters`` returns timeseries on fleet speed.
    """

    RESOURCE_NAME = "tonnage/chinawaters"

    def __init__(self, client: APIClient):
        self.client = client._tonnage_client()

    def get(self, **kwargs):
        kwargs = validate(kwargs)
        return pb_timeseries_to_pandas(self.client.get_tonnage_chinese_waters(kwargs).timeseries)
