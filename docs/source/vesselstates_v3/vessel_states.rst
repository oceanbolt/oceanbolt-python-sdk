Get Vessel States
=================
Retrieve list of vessel states for a given combination of IMO numbers and dates.

.. autoclass:: oceanbolt.sdk.data.vessel_states.VesselStates
    :members:

Example
-------
*Retrive vessel states for Lowlands Tenacity and Lowlands Rise for 2021.*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.vessel_states import VesselStates
    from datetime import date

    base_client = APIClient("<token>")
    df = VesselStates(base_client).get(
        imo=[9583706,9659828],
        start_date=date(2020, 1, 1),
        end_date=date(2020, 12, 31),
    )

Returns:

Arguments
---------
.. autoclass:: oceanbolt.com.vesselstates_v3.types.GetVesselStatesRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.vesselstates_v3.types.VesselStatesResponse
    :members:
    :noindex:


.. autoclass:: oceanbolt.com.vesselstates_v3.types.VesselState
    :members:
    :noindex:
