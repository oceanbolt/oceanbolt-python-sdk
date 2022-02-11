List Vessels
============
Retrieve list of vessel states for a given combination of dates and IMO numbers.

.. autoclass:: oceanbolt.sdk.data.vessel_states.VesselStates
    :members:

Example
-------
*Which vessels have loaded bauxite in Guinea in the past month?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.vessel_states import VesselStates
    from datetime import date,timedelta


    base_client = APIClient("<token>")
    df = VesselStates(base_client).get(
        imo=[9586801],
        start_date=da
    )

Returns:

Arguments
---------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListVesselsRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListVesselsResponse
    :members:

.. autoclass:: oceanbolt.com.vessels_v3.types.Vessel
    :members:
