List Vessels
============
Retrieve list of vessels in the Oceanbolt DatabasePlatform while filering on various criteria.

Example questions that can be answered with this endpoint:

- *Which vessels are currently carrying fertilizer?*
- *Which vessels are classified as supramaxes?*

.. autoclass:: oceanbolt.sdk.data.vessels.Vessels
    :members:

Example
-------
*Which vessels have loaded bauxite in Guinea in the past month?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.vessels import Vessels
    from datetime import date,timedelta


    base_client = APIClient("<token>")
    df = Vessels(base_client).get(
        segment=['supramax'],
    )

Returns:

.. csv-table::
    :header: "vesselName","imo","lastPositionReceived","lastStaticReceived","dwt","segment","subSegment","zoneId","cargoStatus","ladenStatus","ladenStatusDraught","destination","destinationRegion","destinationCountryCode","eta","navigationalStatus","lastPortName","lastCountryCode","lastRegion","portCallStatus","commodityGroup","commodityName","direction","zoneName","portId","portName","berthId","berthName","relatedPortId","relatedPortName","speed","destinationPortName"

    "ABDUL HAMID",9329837,"2021-09-14T10:05:30Z","2021-08-16T07:34:12Z",56011,"Supramax","Supramax (50-60k)",40,"L","L","B","TG PEMANCINGAN","NWAFRICA","TG","2021-07-15T02:00:00Z",1,"Muara Satui Loading Anchorage","ID","SEA","in_berth","Coal","Coal (unclassified)","SSE","South East Asia",1643,"Muara Satui Loading Anchorage",2874,"Muara Satui Coal Loading Anchorage",1643,"Muara Satui Loading Anchorage",,
    "ABDULLAH",9132923,"2021-09-14T13:56:47Z","2021-09-08T06:33:28Z",45653,"Supramax","Handymax (43-50k)",22,"D","L","L","CHATTOGRAM",,,"2021-09-05T16:00:00Z",1,"Chittagong","BD","ECINDIA","in_berth","Cement and Clinker","Cement","WSW","Bay of Bengal",154,"Chittagong",15437,"Chittagon Multibulk Loading Anchorage 1",154,"Chittagong",0.1,
    "ABDUL M",9144055,"2021-09-14T09:41:16Z","2021-09-12T14:59:09Z",46570,"Supramax","Handymax (43-50k)",9,"B","B","B","BR SSZ","ECSA","BR","2021-09-24T12:00:00Z",2,"Monrovia","LR","NWAFRICA","not_in_port",,,"ENE","East Atlantic Ocean (Africa)",,,,,,,1.9,"Santos"
    "ABILITY",9908281,"2021-09-14T13:40:00Z","2021-09-07T16:17:47Z",63800,"Supramax","Ultramax (60-68k)",40,"D","L","L","US LOG PH MNL","SEA","PH","2021-09-02T20:00:00Z",1,"Manila","PH","SEA","in_berth","Grains","Wheat","WNW","South East Asia",,,15891,"Manila Loading Anchorage",2030,"Manila",,


Arguments
---------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListVesselsRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.vessels_v3.types.ListVesselsResponse
    :members:

.. autoclass:: oceanbolt.com.vessels_v3.types.Vessel
    :members:
