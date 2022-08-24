from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (pb_list_to_pandas)


class Ports:
    """
    The ``Ports`` returns a list ports.
    """

    RESOURCE_NAME = "entities/ports"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()
        self.metadata = client.metadata

    def get(self):
        """Retrieves list of ports as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_ports(metadata=self.metadata).ports)


class Zones:
    """
    The ``Zones`` returns a list zones.
    """

    RESOURCE_NAME = "entities/zones"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()
        self.metadata = client.metadata

    def get(self):
        """Retrieves list of zones as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_zones(metadata=self.metadata).zones)


class Regions:
    """
    The ``Regions`` returns a list regions.
    """

    RESOURCE_NAME = "entities/regions"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()
        self.metadata = client.metadata

    def get(self):
        """Retrieves list of regions as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_regions(metadata=self.metadata).regions)


class Countries:
    """
    The ``Countries`` returns a list countries.
    """

    RESOURCE_NAME = "entities/countries"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()
        self.metadata = client.metadata

    def get(self):
        return pb_list_to_pandas(self.client.list_countries(metadata=self.metadata).countries)


class Commodities:
    """
    The ``Commodities`` returns a list commodities.
    """

    RESOURCE_NAME = "entities/commodities"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()
        self.metadata = client.metadata

    def get(self):
        """Retrieves list of commodites as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_commodities(metadata=self.metadata).commodities)


class Segments:
    """
    The ``Segments`` returns a list segments.
    """

    RESOURCE_NAME = "entities/segments"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()
        self.metadata = client.metadata

    def get(self):
        """Retrieves list of segments as a pandas.DataFrame"""
        return pb_list_to_pandas(self.client.list_segments(metadata=self.metadata).segments)


class Search:
    """
    The ``Search`` instance allows for searching polygons and vessels.
    """

    RESOURCE_NAME = "entities/segments"

    def __init__(self, client: APIClient):
        self.client = client._entities_client()
        self.metadata = client.metadata

    def search_polygons(self, q):
        r"""
        Searches for polygons (ports/terminals) in the Oceanbolt Database

        Args:
            q (str): The search query
        """
        return pb_list_to_pandas(self.client.search_polygons(request={"q": q}, metadata=self.metadata).polygons)

    def search_vessels(self, q):
        r"""
        Searches for vessels in the Oceanbolt Database

        Args:
            q (str): The search query
        """
        return pb_list_to_pandas(self.client.search_vessels(request={"q": q}, metadata=self.metadata).vessels)
