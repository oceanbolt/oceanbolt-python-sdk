from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (pb_list_to_pandas)


class Ports:
    """
    The ``Ports`` returns a list ports.
    """

    RESOURCE_NAME = "entities/ports"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()

    def get(self):
        """Retrieves list of ports as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_ports().ports)


class Zones:
    """
    The ``Zones`` returns a list zones.
    """

    RESOURCE_NAME = "entities/zones"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()

    def get(self):
        """Retrieves list of zones as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_zones().zones)


class Regions:
    """
    The ``Regions`` returns a list regions.
    """

    RESOURCE_NAME = "entities/regions"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()

    def get(self):
        """Retrieves list of regions as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_regions().regions)


class Countries:
    """
    The ``Countries`` returns a list countries.
    """

    RESOURCE_NAME = "entities/countries"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()

    def get(self):
        return pb_list_to_pandas(self.client.list_countries().countries)


class Commodities:
    """
    The ``Commodities`` returns a list commodities.
    """

    RESOURCE_NAME = "entities/commodities"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()

    def get(self):
        """Retrieves list of commodites as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_commodities().commodities)


class Segments:
    """
    The ``Segments`` returns a list segments.
    """

    RESOURCE_NAME = "entities/segments"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()

    def get(self):
        """Retrieves list of segments as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_segments().segments)


class Search:
    """
    The ``Search`` instance allows for searching polygons and vessels.
    """

    RESOURCE_NAME = "entities/segments"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()

    def search_polygons(self, q):
        r"""
        Searches for polygons (ports/terminals) in the Oceanbolt Database

        Args:
            q (str): The search query
        """
        return pb_list_to_pandas(self.client.search_polygons({"q": q}).polygons)

    def search_vessels(self, q):
        r"""
        Searches for vessels in the Oceanbolt Database

        Args:
            q (str): The search query
        """
        return pb_list_to_pandas(self.client.search_vessels({"q": q}).vessels)
