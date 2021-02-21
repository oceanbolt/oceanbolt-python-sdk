Zones
=====
Retrieve list of tonnage zones

.. autoclass:: oceanbolt.sdk.data.entities.Zones
    :members:

Example
-------
.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.entities import Zones

    base_client = APIClient("<token>")
    df = Zones(base_client).get()

Arguments
---------

None

Response
--------
.. autoclass:: oceanbolt.com.entities_v3.types.ListTonnageZonesResponse
    :members:

.. autoclass:: oceanbolt.com.entities_v3.types.Zone
    :members:
