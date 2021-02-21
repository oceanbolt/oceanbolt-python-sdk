Fleet Speed
===========
Find aggregated average fleet speed for various vessels segments, various laden status, various directions or various zones.

Example questions that can be answered with this endpoint:

- *How many ballast ultramax or supramax vessels are currently in the Indian Ocean?*
- *How many panamaxes are currently in the atlantic vs the pacific and how has this changed over time?*


.. autoclass:: oceanbolt.sdk.data.tonnage.FleetSpeedTimeseries
    :members:

Example
-------
*What is the average speed of all ballast panamaxes and capesizes currently in the Indian Ocean?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.tonnage import FleetSpeedTimeseries
    from datetime import date


    base_client = APIClient("<token>")
    df = FleetSpeedTimeseries(base_client).get(
        segment=['panamax','capesize'],
        laden_status=["ballast"],
        zone_id=[22, 13, 97, 96, 8], #Zone Ids can be obtained from the zone selector map in the Oceanbolt App or from the entities/zones endpoint.

    )

Returns:

.. csv-table::
    :header: "date","avg_speed"

        "2021-02-01","11.820454597473145"
        "2021-02-02","11.539999961853027"
        "2021-02-03","11.881817817687988"
        "2021-02-04","11.872941017150879"
        "2021-02-05","11.676087379455566"
        "2021-02-06","11.892473220825195"
        "2021-02-07","11.985262870788574"
        "2021-02-08","11.77934741973877"
        "2021-02-09","11.592308044433594"
        "2021-02-10","12.045000076293945"
        "2021-02-11","11.79594612121582"
        "2021-02-12","11.716666221618652"
        "2021-02-13","11.979220390319824"
        "2021-02-14","12.097015380859375"
        "2021-02-15","11.929333686828613"
        "2021-02-16","11.353408813476562"
        "2021-02-17","11.669511795043945"
        "2021-02-18","11.818181991577148"
        "2021-02-19","11.818181991577148"


Arguments
---------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetFleetSpeedResponse
    :members:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesRow
    :members:
    :noindex:
