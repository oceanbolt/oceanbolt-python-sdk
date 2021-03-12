Searching for Vessels/Polygons
==============================
Allows for searching for vessels/polygons in the Oceanbolt Data Platform.

.. autoclass:: oceanbolt.sdk.data.entities.Search
    :members:

Example
-------
.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.entities import Search

    base_client = APIClient("<token>")
    vessels_result = Search(base_client).search_vessels("tenacity")

    base_client = APIClient("<token>")
    vessels_result = Search(base_client).search_vessels("tenacity")

Arguments
---------

.. autoclass:: oceanbolt.sdk.data.entities.Search.search_vessels()
    :members:
    :noindex:

.. autoclass:: oceanbolt.sdk.data.entities.Search.search_polygons()
    :members:
    :noindex:

Response
--------

**Vessels search:**

.. autoclass:: oceanbolt.com.entities_v3.types.Vessel
    :members:

**Polygons search:**

.. autoclass:: oceanbolt.com.entities_v3.types.Polygon
    :members:
