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
        start_date=date.today() - timedelta(day=30),
    )

Returns:

.. csv-table::
    :header: ﻿"voyage_id","port_call_id","imo","vessel_name","port_name","segment","sub_segment","unlocode","berth_name","anchorage_name","arrived_at","berthed_at","departed_at","days_in_port","days_waiting","days_at_berth","country_code","operation","voyage_type","commodity","commodity_value","commodity_group","volume","port_visited"

    "0664d6d6310b18a09f386ce1a09b4e2c","252c092f7075dd75c95e3ff17e4807c4","9279393","WINNING EXCELLENCE","Port Kamsar","Capesize","Large Capesize (180-250k)","GNKMR","Port Kamsar Bauxite Loading Anchorage","2021-02-18T15:39:05Z","2021-02-18T15:39:05Z","GN","Load","Part of Laden Leg","Bauxite","bauxite","Bauxite","151300","","",""
    "16091932b47134794bc9518b20a05a6b","5e43bdd5d33ccb7a8b18d0348a09ae27","9607289","YELLOW FIN","Port Kamsar","Supramax","Supramax (50-60k)","GNKMR","Port Kamsar Bauxite Loading Anchorage","2021-02-16T11:46:33Z","2021-02-16T11:46:33Z","GN","Load","Part of Laden Leg","Bauxite","bauxite","Bauxite","55600","","",""
    "dddc2675d9b0c8febb317d88d584d21b","bef47b801c99139e45a069738e4a97dd","9289013","SPAR LYRA","Port Kamsar","Supramax","Supramax (50-60k)","GNKMR","Port Kamsar Bauxite Loading Anchorage","2021-02-13T07:14:36Z","2021-02-13T07:14:36Z","GN","Load","Part of Laden Leg","Bauxite","bauxite","Bauxite","52400","","",""
    "46a88f9f4ae0e3c01c26135b670ea70f","f7295e3507709bf7229068f9775ae8dc","9198240","SUNNY BOKE","Port Kamsar","Capesize","Capesize (140-180k)","GNKMR","Port Kamsar Bauxite Loading Anchorage","2021-02-13T02:50:10Z","2021-02-13T02:50:10Z","GN","Load","Part of Laden Leg","Bauxite","bauxite","Bauxite","169000","2021-02-16T23:54:50Z","3.87","3.87"
    "f2da9e9787c3a32a660140d346e4ab32","934e97e665a013fd3750f8928caf222d","9298480","TIAN LU HAI","Bel Air Pier","Capesize","Capesize (140-180k)","","Bel Air Chalco Boffa Mine Bauxite Loading Anchorage","2021-02-12T15:58:51Z","2021-02-12T15:58:51Z","GN","Load","Part of Laden Leg","Bauxite","bauxite","Bauxite","170900","2021-02-16T21:56:33Z","4.24","4.24"


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
