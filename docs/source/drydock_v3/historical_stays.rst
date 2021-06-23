Historical Drydock Stays
========================
Retrieve list of historical drydock stays for specific vessels or ports.

Example questions that can be answered with this endpoint:

- *When did vessel XYZ last visit a dry dock?*

.. autoclass:: oceanbolt.sdk.data.dry_dock.DryDockHistoricalStays
    :members:

Example
-------
*When did vessel XYZ last visit a dry dock?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.dry_dock import DryDockHistoricalStays


    base_client = APIClient("<token>")
    df = DryDockHistoricalStays(base_client).get(
        imo=[9515644],
    )


Returns:

.. csv-table::
    :header: shipyardStayId,imo,vesselName,segment,subsegment,dwt,portId,portName,portUnlocode,countryCode,region,shipyardName,shipyardId,arrivedAt,departedAt,durationDays

    9515644#2016-06-27T09:39:58Z,9515644,POAVOSA WISDOM,Handysize,Large Handysize (27-43k),28324,154,Chittagong,BDCGP,BD,ECINDIA,Chittagong Shipyard,13378,2016-06-27 09:39:58+00,2016-07-01 03:29:50+00,3.7429629629166663
    9515644#2017-06-22T07:57:08Z,9515644,POAVOSA WISDOM,Handysize,Large Handysize (27-43k),28324,2259,Tuzla,TRTUZ,TR,EASTMED,Tuzla Shipyard,6130,2017-06-22 07:57:08+00,2017-07-02 20:55:16+00,10.540370370324075
    9515644#2019-04-28T09:57:55Z,9515644,POAVOSA WISDOM,Handysize,Large Handysize (27-43k),28324,403,Kemen Port,CNLNJ,CN,FAREAST,Kemen Shipyard,9253,2019-04-28 09:57:55+00,2019-05-11 04:35:31+00,12.776111111064814


Arguments
---------
.. autoclass:: oceanbolt.com.drydock_v3.types.GetDryDockStaysRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.drydock_v3.types.GetDryDockStaysResponse
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.drydock_v3.types.ShipyardStay
    :members:


