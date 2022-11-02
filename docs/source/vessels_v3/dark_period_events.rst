List Dark Period Events
=======================
Retrieve list of dark period events for vessels. Stoppage Events are defined as events where vessels do not emit AIS data for a period of 48 hours or longer. See methodology for more details.
Currently this API only supports filtering by IMO numbers.

Example questions that can be answered with this endpoint:

- *Have vesel XYZ have any prolonged periods of missing AIS data?*
- *When was the last time vessel XYZ went for a long time without sending AIS data?*

.. autoclass:: oceanbolt.sdk.data.vessels.DarkPeriodEvents
    :members:

Example
-------
*List the most recent dark period events for vessel CHARMEY (9583706)?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.vessels import DarkPeriodEvents
    from datetime import date,timedelta


    base_client = APIClient("<token>")
    df = DarkPeriodEvents(base_client).get(
        imo=[9583706],
    )

Returns:

.. csv-table::
    :header: IMO,Started At,Ended At,Start Zone ID,Start Zone Name,End Zone ID,End Zone Name,Duration Hours,Start Latitude,Start Longitude,End Latitude,End Longitude

    8706686,2022-05-02T23:36:03Z,2022-05-09T04:26:23Z,23,North Pacific Ocean (North America),23,North Pacific Ocean (North America),148.84,32.6294,-117.2429,32.7424,-117.3415
    8706686,2022-05-09T15:47:50Z,2022-06-09T12:56:48Z,23,North Pacific Ocean (North America),23,North Pacific Ocean (North America),741.15,32.6849,-117.1346,32.6849,-117.1346
    8706686,2022-06-09T23:57:13Z,2022-07-01T20:57:35Z,23,North Pacific Ocean (North America),23,North Pacific Ocean (North America),525.01,32.7050,-117.1845,32.7056,-117.1839
    8706686,2022-07-02T22:55:09Z,2022-07-09T07:10:18Z,23,North Pacific Ocean (North America),32,Pacific Ocean (Central America),152.25,32.6283,-117.2510,22.2102,-155.6228
    8706686,2022-07-11T02:55:09Z,2022-07-16T17:59:47Z,32,Pacific Ocean (Central America),32,Pacific Ocean (Central America),135.08,21.2880,-157.9508,20.4843,-159.5273
    8706686,2022-07-17T02:19:20Z,2022-07-19T16:59:31Z,32,Pacific Ocean (Central America),32,Pacific Ocean (Central America),62.67,20.3386,-158.5557,21.2437,-158.0200
    8706686,2022-07-20T03:40:08Z,2022-07-23T15:59:56Z,32,Pacific Ocean (Central America),32,Pacific Ocean (Central America),84.33,21.2684,-157.9577,20.5171,-159.6679
    8706686,2022-07-25T05:21:55Z,2022-08-03T18:43:58Z,32,Pacific Ocean (Central America),32,Pacific Ocean (Central America),229.37,21.2614,-157.9593,20.7158,-158.9186
    8706686,2022-08-06T03:40:32Z,2022-08-11T16:35:32Z,32,Pacific Ocean (Central America),32,Pacific Ocean (Central America),132.92,21.2385,-157.9369,23.4235,-152.8382
    8706686,2022-08-11T16:35:32Z,2022-08-16T15:55:32Z,32,Pacific Ocean (Central America),23,North Pacific Ocean (North America),119.33,23.4235,-152.8382,32.6184,-118.4935
    8706686,2022-08-19T00:08:33Z,2022-08-21T22:59:51Z,23,North Pacific Ocean (North America),23,North Pacific Ocean (North America),70.85,32.6304,-117.3040,32.6104,-117.2461
    8706686,2022-10-24T10:32:15Z,2022-11-01T16:55:44Z,23,North Pacific Ocean (North America),23,North Pacific Ocean (North America),198.39,38.0978,-122.2661,38.0978,-122.2661

Arguments
---------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListDarkPeriodEventsRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListDarkPeriodEventsResponse
    :members:

.. autoclass:: oceanbolt.com.vessels_v3.types.DarkPeriodEvent
    :members:
