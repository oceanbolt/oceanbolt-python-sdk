Port Call Timeseries
=====================
Find aggregate counts of port calls in different countries or regions, while filtering for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *How many vessels have called the port of Santos in the past year grouped by segment?*
- *How many port calls have been completed in the Atlantic vs the Pacific each week over the last 3 years?*
- *How many panamax vessels have discharged coal in China in the past month?*

.. autoclass:: oceanbolt.sdk.data.port_calls.PortCallTimeseries
    :members:

Example
-------
*How many handysize vessels have called the port of Santos on a weekly basis in the past year?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.port_calls import PortCallTimeseries
    from datetime import date


    base_client = APIClient("<token>")
    df = PortCallTimeseries(base_client).get(
        frequency="weekly",
        group_by="segment",
        unlocode=['BRSSZ'],
        start_date=date(2020, 1, 1),
        end_date=date(2020, 12, 31),
    )

Returns:

.. csv-table::
    :header: "date","group","value"

    2019-12-30,Panamax,4
    2020-01-06,Panamax,8
    2020-01-13,Panamax,7
    2020-01-20,Panamax,11
    2020-01-27,Panamax,14
    2020-02-03,Panamax,14
    2020-02-10,Panamax,24
    2020-02-17,Panamax,21
    2020-02-24,Panamax,16
    2019-12-30,Supramax,7
    2020-01-06,Supramax,16
    2020-01-13,Supramax,8
    2020-01-20,Supramax,10
    2020-01-27,Supramax,11
    2020-02-03,Supramax,6
    2020-02-10,Supramax,15
    2020-02-17,Supramax,7
    2020-02-24,Supramax,5
    2019-12-30,Handysize,3
    2020-01-06,Handysize,5
    2020-01-13,Handysize,9
    2020-01-20,Handysize,8
    2020-01-27,Handysize,6
    2020-02-03,Handysize,11
    2020-02-10,Handysize,6
    2020-02-17,Handysize,7
    2020-02-24,Handysize,5

Arguments
---------
.. autoclass:: oceanbolt.com.portcalls_v3.types.GetPortCallsRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.portcalls_v3.types.GetPortCallTimeseriesResponse
    :members:

.. autoclass:: oceanbolt.com.portcalls_v3.types.TimeseriesGroup
    :members:

.. autoclass:: oceanbolt.com.portcalls_v3.types.TimeseriesRow
    :members: