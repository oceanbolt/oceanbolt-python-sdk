Fleet Growth
============
Find weekly/monthly/annual fleet growth numbers for any vessel segment.

Example questions that can be answered with this endpoint:

- *How many supramax vessels was delivered/scrapped in 2020 on a monthly basis?*
- *What was total annual fleet growth over the past 5 years?*


.. autoclass:: oceanbolt.sdk.data.tonnage.FleetGrowthTimeseries
    :members:

Example
-------
*How many supramax vessels was delivered/scrapped in 2020 on a monthly basis?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.tonnage import FleetGrowthTimeseries
    from datetime import date


    base_client = APIClient()
    df = FleetGrowthTimeseries(base_client).get(
        segment=['supramax'],
        start_date = date(2020,1,1),
        end_date = date(2020,12,31)
    )

Returns:

.. csv-table::
    :header: date,scrapped,delivered,net

    2020-01-06,0,4,4
    2020-01-13,1,3,2
    2020-01-20,0,2,2
    2020-01-27,0,4,4
    2020-02-03,1,1,0
    2020-02-10,1,0,-1
    2020-02-24,1,1,0
    2020-03-02,0,1,1


Arguments
---------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageFleetRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageFleetGrowthResponse
    :members:

.. autoclass:: oceanbolt.com.tonnage_v3.types.FleetGrowthTimeseriesGroup
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.tonnage_v3.types.FleetGrowthTimeseriesRow
    :members:
    :noindex:
