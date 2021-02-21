Countries
=========
Retrieve list of countries

.. autoclass:: oceanbolt.sdk.data.entities.Countries
    :members:

Example
-------
.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.entities import Countries

    base_client = APIClient("<token>")
    df = Countries(base_client).get()

Arguments
---------

None

Response
--------
.. autoclass:: oceanbolt.com.entities_v3.types.ListCountriesResponse
    :members:

.. autoclass:: oceanbolt.com.entities_v3.types.Country
    :members:
