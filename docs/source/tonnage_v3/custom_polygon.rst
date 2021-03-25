Custom Polygon Counts
=====================
The CustomPolygon service provides users access to a highly flexible tonnage supply count engine. The service allows
users to provide custom polygons (in GeoJSON format), and get current + historical counts of how many vessels within a
given segment/laden status was inside the defined polygon.

Example questions that can be answered with this endpoint:

- *How many Panamax vessels are currently laden in this specific part of AG?*
- *How many Capesize vessels have historically been in ballast the Indian Ocean and how does this compare to current numbers?*


.. autoclass:: oceanbolt.sdk.data.tonnage.CustomPolygonTimeseries
    :members:

Example
-------
- *How many Panamax vessels are currently laden in this specific part of AG?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.tonnage import CustomPolygonTimeseries
    from datetime import date


    base_client = APIClient("<token>")
    df = CustomPolygonTimeseries(base_client).get(
        geom_polygon="{\"type\":\"Polygon\",\"coordinates\":[[[45.50537109374999,31.93351676190369],[50.4931640625,16.846605106396304],[61.083984375,20.138470312451155],[66.9287109375,27.819644755099446],[61.94091796875,31.89621446335144],[45.50537109374999,31.93351676190369]]]}"
        sub_segment=['ultramax','supramax'],
        start_date=date(2021,2,1)
        end_date=date(2021,3,1)

    )

Returns:

.. csv-table::
    :header: "date","value"

    "2021-02-01","161"
    "2021-02-02","161"
    "2021-02-03","167"
    "2021-02-04","165"
    "2021-02-05","161"
    "2021-02-06","161"
    "2021-02-07","160"
    "2021-02-08","152"
    "2021-02-09","149"
    "2021-02-10","150"
    "2021-02-11","152"
    "2021-02-12","156"
    "2021-02-13","160"
    "2021-02-14","157"
    "2021-02-15","157"
    "2021-02-16","157"
    "2021-02-17","154"
    "2021-02-18","153"
    "2021-02-19","153"


Arguments
---------
.. autoclass:: oceanbolt.com.custompolygon_v3.types.CustomPolygonRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.custompolygon_v3.types.CustomPolygonResponse
    :members:

.. autoclass:: oceanbolt.com.custompolygon_v3.types.TimeseriesGroup
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.custompolygon_v3.types.TimeseriesRow
    :members:
    :noindex:
