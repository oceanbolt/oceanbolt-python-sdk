Current Drydock Stays
=====================
Retrieve list of current drydock stays for vessels in different countries or regions.

Example questions that can be answered with this endpoint:

- *Which Capesize vessels are currently in dry dock in China?*

.. autoclass:: oceanbolt.sdk.data.dry_dock.DryDockCurrentVessels
    :members:

Example
-------
*Which capesize vessels are currently drydocked in China?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.dry_dock import DryDockCurrentVessels


    base_client = APIClient("<token>")
    df = DryDockCurrentVessels(base_client).get(
        country_code=['CN'],
        segment=['capesize']
    )


Returns:

.. csv-table::
    :header: imo,vesselName,segment,subSegment,dwt,portId,portName,currentCountryCode,arrivedAt,waitingTimeDays,shipyardId,shipyardName,lat,lng,speed,course,countryName,countryCode

    9038438,STELLAR GALAXY,Capesize,VLOC (250k+),263130,1525,Matsushima,JP,2020-12-03T03:55:00Z,202.26453669499088,9583,Matsushima Shipyard,0,0,0,0,Japan,JP
    9044229,STELLAR EAGLE,Capesize,VLOC (250k+),278258,348,Guangzhou,CN,2021-01-11T08:55:22Z,163.0559487313819,14363,Guangzhou Shipyard 20,0,0,0,0,China,CN
    9002673,ATLANTIC MERCHANT,Capesize,Large Capesize (180-250k),238818,2143,Singapore,SG,2021-01-12T10:23:07Z,161.99501123148215,750,Singapore Keppel Shipyard,0,0,0,0,Singapore,SG
    9003122,HBIS SUNRISE,Capesize,VLOC (250k+),268132,2143,Singapore,SG,2021-04-14T01:22:57Z,70.37012697228242,750,Singapore Keppel Shipyard,0,0,0,0,Singapore,SG
    9573775,PACIFIC ENDURANCE,Capesize,Large Capesize (180-250k),181458,7627,Changtu Island,CN,2021-04-25T01:42:05Z,59.3568399355469,9361,Changtu Island Shipyard,0,0,0,0,China,CN
    9844100,Sea Victoria,Capesize,VLOC (250k+),325000,356,Chiwan,CN,2021-05-16T12:17:52Z,37.915323731644726,5863,Ximazhou Shipyard Island,0,0,0,0,China,CN
    9488865,EPIC,Capesize,Large Capesize (180-250k),180149,359,Dalian,CN,2021-05-24T04:07:36Z,30.255786694479525,5898,Dalian Shipyard,0,0,0,0,China,CN
    9588457,STAR POLARIS,Capesize,Capesize (140-180k),179678,8355,Shanhaiguan,CN,2021-05-27T04:51:02Z,27.225624657491412,9642,"SHANHAIGUAN SHIPBUILDING INDUSTRY CO.,LTD(CSIC)",0,0,0,0,China,CN
    9589384,JABAL NAFUSA,Capesize,Capesize (140-180k),169097,403,Kemen Port,CN,2021-05-28T05:49:38Z,26.184930213393255,9253,Kemen Shipyard,0,0,0,0,China,CN
    9579781,NEW HYDRA,Capesize,Capesize (140-180k),179258,8355,Shanhaiguan,CN,2021-05-28T08:50:06Z,26.059606139097607,9642,"SHANHAIGUAN SHIPBUILDING INDUSTRY CO.,LTD(CSIC)",0,0,0,0,China,CN
    9456680,LAKE DOLPHIN,Capesize,Capesize (140-180k),179418,442,Shanghai,CN,2021-05-29T09:53:56Z,25.01527743544707,9431,Shanghai Shipyard 3,0,0,0,0,China,CN


Arguments
---------
.. autoclass:: oceanbolt.com.drydock_v3.types.GetDryDockRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.drydock_v3.types.DryDockStay
    :members:


