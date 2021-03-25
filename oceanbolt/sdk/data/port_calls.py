from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.helpers import (validate, pb_list_to_pandas, pb_timeseries_to_pandas)


class PortCalls:
    """
    The ``PortCalls`` returns a lists of port calls.
    """

    RESOURCE_NAME = "portcalls/listportcalls"

    def __init__(self, client: APIClient):
        self.client = client._portcalls_client()

    def get(self, **kwargs):
        """Retrieves port calls data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_list_to_pandas(self.client.get_port_calls(kwargs).data)

    def get_raw(self, **kwargs):
        kwargs = validate(kwargs)
        return self.client.get_port_calls(kwargs)


class PortCallTimeseries:
    """
    The ``PortCallTimeseries`` returns a timeseries data on historical number of port calls.
    """

    RESOURCE_NAME = "portcalls/timeseries"

    def __init__(self, client: APIClient):
        self.client = client._portcalls_client()

    def get(self, **kwargs):
        """Retrieves timeseries data as a pandas.DataFrame"""
        kwargs = validate(kwargs)
        return pb_timeseries_to_pandas(self.client.get_port_call_timeseries(kwargs).timeseries)

    def get_raw(self, **kwargs):
        kwargs = validate(kwargs)
        return self.client.get_port_call_timeseries(kwargs)


class PortParticulars:
    """
    The ``PortParticulars`` returns data about port particulars (max beam, max loa, max draught etc) based on the physical characteristics of the most recent port calls.
    """

    RESOURCE_NAME = "portcalls/portparticulars"

    def __init__(self, client: APIClient):
        self.client = client._portcalls_client()

    def get_raw(self, **kwargs):
        """Retrieves port particular data as a python class"""
        return self.client.get_port_particulars(kwargs)
