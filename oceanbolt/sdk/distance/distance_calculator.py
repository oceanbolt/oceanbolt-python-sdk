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
    """

    def __init__(self, client: APIClient):
        self.client = client._distance_client()

    def shortest_route(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return pb_list_to_pandas(self.client.calculate_distance(request=kwargs, metadata=(('x-ob-platform', 'bulk'),)).total_shortest_path)

    def distance(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return self.client.calculate_distance(kwargs).total_distance

    def duration(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        if kwargs.get("speed") <= 0:
            raise ValueError("Speed cannot be negative in duration call.")
        return self.client.calculate_distance(kwargs).total_duration_hours

    def get_raw(self, **kwargs):
        kwargs = wrapPoints(kwargs)
        return self.client.calculate_distance(kwargs)
