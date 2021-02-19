Commodities
===========
Retrieve list of commodities

.. autoclass:: oceanbolt.sdk.data.entities.Commodities
    :members:

Example
-------
.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.entities import Commodities

    base_client = APIClient("<token>")
    df = Commodities(base_client).get()

Returns:

tbd

Arguments
---------

None

Response
--------
.. autoclass:: oceanbolt.com.entities_v3.types.ListCommoditiesResponse
    :members:

.. autoclass:: oceanbolt.com.entities_v3.types.Commodity
    :members:
