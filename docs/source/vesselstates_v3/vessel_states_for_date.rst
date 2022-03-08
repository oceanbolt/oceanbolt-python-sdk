Get Vessel States For Date
==========================
Retrieve list of vessel states for the entire fleet for a single date.

.. autoclass:: oceanbolt.sdk.data.vessel_states.VesselStatesForDate
    :members:

Example
-------
*Retrive vessel states for the entire fleet for the 1st of january 2020.*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.vessel_states import VesselStatesForDate
    from datetime import date

    base_client = APIClient("<token>")
    df = VesselStatesForDate(base_client).get(
        date=date(2020, 1, 1),
    )

Returns:

Arguments
---------
.. autoclass:: oceanbolt.com.vesselstates_v3.types.GetVesselStatesForDateRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.vesselstates_v3.types.VesselStatesResponse
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.vesselstates_v3.types.VesselState
    :members:
    :noindex: