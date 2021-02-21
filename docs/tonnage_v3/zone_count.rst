Tonnage Zone Counts
===================
Find aggregated vessel counts for various vessels segments, various laden status, various directions or various zones.

Example questions that can be answered with this endpoint:

- *How many ballast ultramax or supramax vessels are currently in the Indian Ocean?*
- *How many panamaxes are currently in the atlantic vs the pacific and how has this changed over time?*


.. autoclass:: oceanbolt.sdk.data.tonnage.TonnageZoneTimeseries
    :members:

Example
-------
*How many ballast ultramax or supramax vessels are currently in the Indian Ocean?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.tonnage import TonnageZoneTimeseries
    from datetime import date


    base_client = APIClient("<token>")
    df = TonnageZoneTimeseries(base_client).get(
        sub_segment=['ultramax','supramax'],
        laden_status=["ballast"],
        zone_id=[22, 13, 97, 96, 8], #Zone Ids can be obtained from the zone selector map in the Oceanbolt App or from the entities/zones endpoint.

    )

Returns:

.. csv-table::
    :header: "date","vessel_count","vessel_dwt"

    "2021-02-01","161","9384746"
    "2021-02-02","161","9385891"
    "2021-02-03","167","9707184"
    "2021-02-04","165","9590778"
    "2021-02-05","161","9367220"
    "2021-02-06","161","9353406"
    "2021-02-07","160","9312805"
    "2021-02-08","152","8829415"
    "2021-02-09","149","8637758"
    "2021-02-10","150","8698294"
    "2021-02-11","152","8811801"
    "2021-02-12","156","9084444"
    "2021-02-13","160","9320787"
    "2021-02-14","157","9155971"
    "2021-02-15","157","9180257"
    "2021-02-16","157","9144834"
    "2021-02-17","154","8964411"
    "2021-02-18","153","8904227"
    "2021-02-19","153","8904227"


Arguments
---------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageDataRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.tonnage_v3.types.GetTonnageZoneCountResponse
    :members:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesGroup
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageTimeseriesRow
    :members:
    :noindex:
