Drydock Timeseries
==================
Retrieve timeseries data of how many vessels have been drydocked in different ports, countries or regions over time.

Example questions that can be answered with this endpoint:

- *How has the number of dry docked vessels changed over the past year?*

.. autoclass:: oceanbolt.sdk.data.dry_dock.DryDockTimeseries
    :members:

Example
-------
*How has the number of dry docked vessels changed over the past year?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.dry_dock import DryDockTimeseries
    from datetime import date

    base_client = APIClient("<token>")
    df = DryDockTimeseries(base_client).get(
        start_date=date(2020,1,1),
    )


Returns:

.. csv-table::
    :header: date,vesselCount,vesselDwt,avgWaitingDays,medianWaitingDays

    2021-03-15,49,9357994,20.798795138888885,8.826215277777779
    2021-03-16,51,9640308,20.094400190631806,8.920185185185185
    2021-03-17,51,9519327,20.08614764887436,8.777407407407408
    2021-03-18,53,9861875,20.20562631027253,9.663645833333334


Arguments
---------
.. autoclass:: oceanbolt.com.drydock_v3.types.GetDryDockRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.drydock_v3.types.DryDockTimeseriesRow
    :members:

.. autoclass:: oceanbolt.com.drydock_v3.types.DryDockTimeseriesGroup
    :members:


