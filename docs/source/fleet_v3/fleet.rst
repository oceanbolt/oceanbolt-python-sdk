Create Fleet
============
Retrieve list of port calls in different countries or regions, while filtering for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *Which vessels have called the port of Santos in the past year?*
- *Which vessels have loaded bauxite in Guinea in the past month?*

.. autoclass:: oceanbolt.sdk.fleet.FleetManagement
    :members:

Example
-------
*Which vessels have loaded bauxite in Guinea in the past month?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.fleet import FleetManagement


    base_client = APIClient("<token>")
    df = FleetManagement(base_client).create_fleet(
        fleet_name="my fleet"
    )

Arguments
---------
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.CreateFleetRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Fleet
    :members:
