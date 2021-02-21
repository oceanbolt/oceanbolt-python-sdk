List Congested Vessels
======================
Retrieve list of congested vessels in different countries or regions, while filtering for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *Which VLOCs are currently congested in Brazil waiting to load?*
- *Which vessels are currently congested in China waiting to discharge Australian coal?*

.. autoclass:: oceanbolt.sdk.data.congestion.CongestionVessels
    :members:

Example
-------
*Which vessels are currently congested in China waiting to discharge Australian coal?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.congestion import CongestionVessels


    base_client = APIClient("<token>")
    df = CongestionVessels(base_client).get(
        country_code=['CN'],
        last_load_country_code=['AU'],
        commodity_group = ['coal'],
    )


Returns:

.. csv-table::
    :header: ﻿﻿"imo","vesselName","segment","subSegment","dwt","currentPortName","currentCountry","currentCountryCode","arrivedAt","waitingTimeDays","lastLoadCountry","lastLoadCountryCode","lastLoadPortName","lastLoadBerthName","lastPortDepartedAt","commodityGroup","commodity","volume"

    "9693422","FRATERNELLE","Panamax","Kamsarmax (80-90k)","82086","Bayuquan","China","CN","2020-09-11T14:50:51Z","160.94841746067797","Australia","AU","Hay Point","Hay Point DBCT Management Coal Berths","2020-08-26T15:59:55Z","Coal","Coal (unclassified)","80400"
    "9501071","PELOPIDAS","Capesize","Capesize (140-180k)","176006","Bayuquan","China","CN","2020-09-13T23:56:56Z","158.56919292613023","Australia","AU","Hay Point","Hay Point DBCT Management Coal Berths","2020-08-29T13:59:53Z","Coal","Coal (unclassified)","172400"
    "9719941","KSL SAKURA","Capesize","Large Capesize (180-250k)","181062","Zhanjiang","China","CN","2020-10-05T03:49:38Z","137.40759569984374","Australia","AU","Newcastle","Newcastle PWCS Kooragang Coal Terminal Berths #4 to 7","2020-09-20T16:57:11Z","Coal","Coal (unclassified)","175500"
    "9510694","OLYMPIC GLORY","Panamax","Kamsarmax (80-90k)","84091","Donggang","China","CN","2020-10-06T00:51:55Z","136.53101005195037","Australia","AU","Hay Point","Hay Point BHP Billiton Mitsubishi Alliance Coal Berths","2020-09-18T03:44:27Z","Coal","Coking Coal","82400"
    "9442768","FAR EASTERN JUPITER","Panamax","Kamsarmax (80-90k)","82655","Bayuquan","China","CN","2020-10-06T03:56:16Z","136.4029892226362","Australia","AU","Hay Point","Hay Point DBCT Management Coal Berths","2020-09-21T02:58:14Z","Coal","Coal (unclassified)","81000"


Arguments
---------
.. autoclass:: oceanbolt.com.congestion_v3.types.GetCongestionRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.congestion_v3.types.CongestionResponse
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.congestion_v3.types.CongestionStay
    :members:


