from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (pb_list_to_pandas)


class DistanceCalculator:

    def __init__(self, client: APIClient):
        self.client = client._distance_client()

    def shortest_route(self, **kwargs):
        return pb_list_to_pandas(self.client.calculate_distance(kwargs).total_shortest_path)

    def distance(self, **kwargs):
        return self.client.calculate_distance(kwargs).total_distance

    def duration(self, **kwargs):
        if kwargs.get("speed") <= 0:
            raise ValueError("Speed cannot be negative in duration call.")
        return self.client.calculate_distance(kwargs).total_duration_hours

    def get_raw(self, **kwargs):
        return self.client.calculate_distance(kwargs)
