from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas, pb_timeseries_to_pandas)

class FleetManagement:

    def __init__(self, client: APIClient):
        self.client = client._fleet_client()

    def create_fleet(self, **kwargs):
        return self.client.create_fleet(kwargs)

    def describe_fleet(self, **kwargs):
        return self.client.describe_fleet(kwargs)

    def list_fleets(self, **kwargs):
        return self.client.list_fleets(kwargs)

    def delete_fleet(self, **kwargs):
        return self.client.delete_fleet(kwargs)

    def share_fleet(self, **kwargs):
        return self.client.share_fleet(kwargs)

    def unshare_fleet(self, **kwargs):
        return self.client.unshare_fleet(kwargs)

    def rename_fleet(self, **kwargs):
        return self.client.rename_fleet(kwargs)

    def drop_vessels(self, **kwargs):
        return self.client.drop_vessels(kwargs)

    def batch_add_vessels(self, **kwargs):
        return self.client.batch_add_vessels(kwargs)

    def replace_vessels(self, **kwargs):
        return self.client.replace_vessels(kwargs)

    def add_vessel(self, **kwargs):
        return self.client.add_vessel(kwargs)

    def delete_vessel(self, **kwargs):
        return self.client.delete_vessel(kwargs)

    def update_vessel(self, **kwargs):
        return self.client.update_vessel(kwargs)