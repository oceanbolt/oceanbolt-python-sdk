List Stoppage Events
====================
Retrieve list of stoppage events for vessels. Stoppage Events are defined as events where vessels have longer period under 8 knots. See methodology for more details.
Currently this API only supports filtering by IMO numbers.

Example questions that can be answered with this endpoint:

- *Have vesel XYZ have any prolonged periods of slow speed?*
- *When was the last time vessel XYZ stopped?*

.. autoclass:: oceanbolt.sdk.data.vessels.StoppageEvents
    :members:

Example
-------
*List the most recent stoppage events for vessel CHARMEY (9583706)?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.vessels import StoppageEvents
    from datetime import date,timedelta


    base_client = APIClient("<token>")
    df = StoppageEvents(base_client).get(
        imo=[9583706],
    )

Returns:

.. csv-table::
    :header: "imo","startedAt","endedAt","portId","portName","zoneId","zoneName","minSpeedObserved","durationHours","lat","lon","classification"

    9583706,"2021-03-25T10:26:15Z","2021-03-25T16:51:33Z",5264,"Mindelo",9,"East Atlantic Ocean (Africa)",0,6.42166666666667,16.89492,-25.01568,"PORT_STAY"
    9583706,"2021-04-02T07:31:55Z","2021-04-12T21:36:00Z",802,"La Pallice",46,"Bay of Biscay",0,254.068055555556,46.15896,-1.23298,"PORT_STAY"
    9583706,"2021-04-13T01:45:33Z","2021-04-14T12:30:35Z",,,46,"Bay of Biscay",1.1,34.7502944444444,46.41442,-2.75874,"AT_SEA"
    9583706,"2021-04-15T19:48:11Z","2021-04-16T10:55:00Z",,,24,"North Atlantic Ocean (Continent)",5.4,15.1136111111111,50.52954,1.02962,"AT_SEA"
    9583706,"2021-04-16T17:55:05Z","2021-04-30T03:50:00Z",156,"Antwerp",24,"North Atlantic Ocean (Continent)",0,321.915277777778,51.32929,4.30511,"PORT_STAY"

Arguments
---------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListStoppageEventsRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListStoppageEventsResponse
    :members:

.. autoclass:: oceanbolt.com.vessels_v3.types.StoppageEvent
    :members:
