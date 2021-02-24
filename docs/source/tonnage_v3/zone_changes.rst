Zone Changes
============
Find timeseries data on the number of zone changes (zone crossings) during a given period, while filtering on zone id or vessel segment.

Example questions that can be answered with this endpoint:

- *How many panamax vessels have crossed from the Indian Ocean into the Atlantic on a weekly basis in the past 3 months?*
- *How many vessels have entered the Mediterranean in the past 7 days*


.. autoclass:: oceanbolt.sdk.data.tonnage.ZoneChangesTimeseries
    :members:

Example
-------
*How many panamax vessels have crossed from the Indian Ocean into the Atlantic on a weekly basis in the past 3 months?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.tonnage import ZoneChangesTimeseries
    from datetime import date

    base_client = APIClient()
    df = ZoneChangesTimeseries(base_client).get(
        start_date=date.today() - timedelta(days=90),
        frequency="weekly",
        segment=["panamax"],
        from_zone_id=[22, 13, 97, 96, 8], # zones corresponding to the indian ocean
        to_zone_id=[9, 58, 42, 7, 15], # zones corresponding to the atlantic
    )

Returns:

.. csv-table::
    :header: date,value

    2020-11-23,25
    2020-11-30,27
    2020-12-07,40
    2020-12-14,20
    2020-12-21,26
    2020-12-28,26
    2021-01-04,31
    2021-01-11,30
    2021-01-18,51
    2021-01-25,45
    2021-02-01,61
    2021-02-08,64
    2021-02-15,50
    2021-02-22,21


Arguments
---------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageZoneChangesRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageZoneChangesResponse
    :members:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesRow
    :members:
    :noindex:
