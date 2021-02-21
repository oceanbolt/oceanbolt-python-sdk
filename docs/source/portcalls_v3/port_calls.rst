List Port Calls
=====================
Retrieve list of port calls in different countries or regions, while filtering for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *Which vessels have called the port of Santos in the past year?*
- *Which vessels have loaded bauxite in Guinea in the past month?*

.. autoclass:: oceanbolt.sdk.data.port_calls.PortCalls
    :members:

Example
-------
*Which vessels have loaded bauxite in Guinea in the past month?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.port_calls import PortCalls
    from datetime import date,timedelta


    base_client = APIClient("<token>")
    df = PortCalls(base_client).get(
        country_code=['GN'],
        commodity_group = ['bauxite'],
        start_date=date.today() - timedelta(days=30),
    )

Returns:

.. csv-table::
    :header: ﻿voyage_id,port_call_id,imo,vessel_name,port_id,port_name,segment,sub_segment,unlocode,berth_id,berth_name,anchorage_id,anchorage_name,arrived_at,berthed_at,unberthed_at,departed_at,days_in_port,days_waiting,days_at_berth,country_code,operation,voyage_type,commodity,commodity_value,commodity_group,volume,port_visited

    22f5c4b1c13ffd56aa6179614b78cdf0,b2894d359ccb34bbd008ab61bd1259dd,9262730,AGIOS CHARALAMBOS,998,Port Kamsar,Capesize,Large Capesize (180-250k),GNKMR,10171,Port Kamsar Bauxite Loading Anchorage,,,2021-02-21T13:48:55Z,2021-02-21T13:48:55Z,,,,0.0,,GN,Load,Part of Laden Leg,Bauxite,bauxite,Bauxite,181100.0,False
    b9b237384e1ec8a7cc5869da60602754,a1667ce115d3f46952b739547620b168,9165516,CAPE OSPREY,998,Port Kamsar,Capesize,Capesize (140-180k),GNKMR,10171,Port Kamsar Bauxite Loading Anchorage,,,2021-02-20T16:45:36Z,2021-02-20T16:45:36Z,,,,0.0,,GN,Load,Part of Laden Leg,Bauxite,bauxite,Bauxite,168400.0,False
    6ce296f896c8c16fa60aa8ee72879587,536cda0f3344512eac7d793d75423927,9844588,CL HUANGPU RIVER,998,Port Kamsar,Capesize,Large Capesize (180-250k),GNKMR,10171,Port Kamsar Bauxite Loading Anchorage,,,2021-02-19T17:13:47Z,2021-02-19T17:13:47Z,,,,0.0,,GN,Load,Part of Laden Leg,Bauxite,bauxite,Bauxite,203800.0,False
    0664d6d6310b18a09f386ce1a09b4e2c,252c092f7075dd75c95e3ff17e4807c4,9279393,WINNING EXCELLENCE,998,Port Kamsar,Capesize,Large Capesize (180-250k),GNKMR,10171,Port Kamsar Bauxite Loading Anchorage,,,2021-02-18T15:39:05Z,2021-02-18T15:39:05Z,,,,0.0,,GN,Load,Part of Laden Leg,Bauxite,bauxite,Bauxite,151300.0,False
    16091932b47134794bc9518b20a05a6b,5e43bdd5d33ccb7a8b18d0348a09ae27,9607289,YELLOW FIN,998,Port Kamsar,Supramax,Supramax (50-60k),GNKMR,10171,Port Kamsar Bauxite Loading Anchorage,,,2021-02-16T11:46:33Z,2021-02-16T11:46:33Z,,,,0.0,,GN,Load,Part of Laden Leg,Bauxite,bauxite,Bauxite,55600.0,False

Arguments
---------
.. autoclass:: oceanbolt.com.portcalls_v3.types.GetPortCallsRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.portcalls_v3.types.GetPortCallsResponse
    :members:

.. autoclass:: oceanbolt.com.portcalls_v3.types.PortCall
    :members:
