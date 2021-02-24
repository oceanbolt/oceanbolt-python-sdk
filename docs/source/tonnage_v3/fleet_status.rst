Fleet Status
============
Find the development of the number of vessels on the water for any vessel segment.

Example questions that can be answered with this endpoint:

- *What is the current size of the "on the water dry bulk fleet split by segment?*
- *How has the number of capesize vessels on the water developed over the past 5 years?*


.. autoclass:: oceanbolt.sdk.data.tonnage.FleetStatusTimeseries
    :members:

Example
-------
*How has the number of capesize vessels on the water developed over the past 4 years?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.tonnage import FleetStatusTimeseries
    from datetime import date

    base_client = APIClient()
    df = FleetStatusTimeseries(base_client).get(
        segment = ["capesize"],
        group_by = "segment",
        start_date = date(2016,1,1),
        end_date = date(2020,12,31),
    )

Returns:

.. csv-table::
    :header: group,date,value

    Capesize,2016-01-01,1548
    Capesize,2016-01-02,1548
    Capesize,2016-01-03,1548
    Capesize,2016-01-04,1548
    Capesize,2016-01-05,1550
    Capesize,2016-01-06,1550
    Capesize,2016-01-07,1552
    Capesize,2016-01-08,1554

Arguments
---------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageFleetRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageFleetStatusResponse
    :members:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesRow
    :members:
    :noindex:
