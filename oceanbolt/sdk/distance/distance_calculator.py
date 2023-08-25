from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (pb_list_to_pandas, wrapPoints)


class DistanceCalculator:
    r"""DistanceCalculator provides an interface to calculate shortest route between ports/vessels

    Methods:
        distance(): Calculates the shortest distance between a list of locations.
        duration(): Calculates expected duration for a voyage between a list of locations,
            given a speed provided by the user.
        shortest_route(): Calculates the shortest route between a list of locations, and returns the route as a pandas
            dataframe of lat/lons.
        get_raw(): Provides access to the raw response from the API, which includes breakdown by individual legs,
            in case of a waypoint route calculation.
        batch_distance(): Batch calculates the shortest distance between a list of locations.
        batch_duration(): Batch calculates expected duration for a voyage between a list of locations,
            given a speed provided by the user.
        batch_shortest_route(): Batch calculates the shortest route between a list of locations,
            and returns the route as pandas dataframes of lat/lons.
        batch_get_raw(): Provides access to the raw response from the API, which includes breakdown by individual legs,
            in case of a waypoint route calculation.
    """

    def __init__(self, client: APIClient):
        self.client = client._distance_client()
        self.metadata = client.metadata

    def shortest_route(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return pb_list_to_pandas(self.client.calculate_distance(request=kwargs, metadata=self.metadata).total_shortest_path)

    def distance(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return self.client.calculate_distance(request=kwargs, metadata=self.metadata).total_distance

    def duration(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        if kwargs.get("speed") <= 0:
            raise ValueError("Speed cannot be negative in duration call.")
        return self.client.calculate_distance(request=kwargs, metadata=self.metadata).total_duration_hours

    def get_raw(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return self.client.calculate_distance(request=kwargs, metadata=self.metadata)

    def batch_shortest_route(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return [pb_list_to_pandas(o.total_shortest_path) for o in self.client.batch_calculate_distance(request=kwargs, metadata=self.metadata).responses]

    def batch_distance(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return [o.total_distance for o in self.client.batch_calculate_distance(request=kwargs, metadata=self.metadata).responses]

    def batch_duration(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        if any(["speed" in o and o.get("speed") <= 0 for o in kwargs.get("requests")]):
            raise ValueError("Speed cannot be negative in batch duration call.")
        return [o.total_duration_hours for o in self.client.batch_calculate_distance(request=kwargs, metadata=self.metadata).responses]

    def batch_get_raw(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return self.client.batch_calculate_distance(request=kwargs, metadata=self.metadata).responses
