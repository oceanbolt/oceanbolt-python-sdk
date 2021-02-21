Regions
=======
Retrieve list of regions

.. autoclass:: oceanbolt.sdk.data.entities.Regions
    :members:

Example
-------
.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.entities import Regions

    base_client = APIClient("<token>")
    df = Regions(base_client).get()

Arguments
---------

None

Response
--------
.. autoclass:: oceanbolt.com.entities_v3.types.ListRegionsResponse
    :members:

.. autoclass:: oceanbolt.com.entities_v3.types.Region
    :members:
