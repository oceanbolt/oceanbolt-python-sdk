Congestion Timeseries
=====================
Retrieve timeseries data of how many vessels are congested in different countries or regions, while filtering for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *How many VLOCs are currently congested in Brazil waiting to load?*
- *What is the average waiting time for vessels currently congested in China waiting to discharge Australian coal and how has that changed in the past year?*

.. autoclass:: oceanbolt.sdk.data.congestion.CongestionTimeseries
    :members:

Example
-------
*How many vessels are currently congested in China waiting to discharge Australian coal and how has that changed in the past year?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.congestion import CongestionTimeseries
    from datetime import date

    base_client = APIClient("<token>")
    df = CongestionTimeseries(base_client).get(
        country_code=['CN'],
        last_load_country_code=['AU'],
        commodity_group = ['coal'],
        start_date=date(2020,1,1),
    )


Returns:

.. csv-table::
    :header: ﻿﻿"date","group","vessel_count","vessel_dwt","average_waiting_days","median_waiting_days"

        2021-02-19,default,50,5586544,137.782971,131.122540
        2021-02-18,default,50,5674628,134.318293,130.122540
        2021-02-17,default,50,5674628,136.004659,129.122540
        2021-02-16,default,51,5726315,132.450734,127.651956
        2021-02-15,default,53,6074773,130.864687,126.651956
        2021-02-14,default,51,5811030,134.971958,126.593125
        2021-02-13,default,53,5984440,129.094691,124.651956
        2021-02-12,default,55,6152710,131.408019,124.593125
        2021-02-11,default,54,6101023,132.827528,123.695417
        2021-02-10,default,53,6009144,134.321403,122.797708
        2021-02-09,default,57,6356727,136.738331,122.753090
        2021-02-08,default,58,6449928,135.311120,121.275399
        2021-02-07,default,58,6308928,132.075676,120.275399
        2021-02-06,default,57,6227397,135.695934,119.753090
        2021-02-05,default,58,6407697,132.385083,118.275399
        2021-02-04,default,58,6368678,134.732518,118.046233
        2021-02-03,default,57,6284059,135.497696,117.339375
        2021-02-02,default,57,6284059,136.874849,116.339375
        2021-02-01,default,56,6190825,138.306718,116.255741

Arguments
---------
.. autoclass:: oceanbolt.com.congestion_v3.types.GetCongestionRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.congestion_v3.types.CongestionResponse
    :members:

.. autoclass:: oceanbolt.com.congestion_v3.types.CongestionTimeseriesRow
    :members:

.. autoclass:: oceanbolt.com.congestion_v3.types.CongestionTimeseriesGroup
    :members:


