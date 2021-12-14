Chinese Waters
===================
Track how many Chinese flagged vessels that are currently trading in cabotage in coastal waters
vs how many Chinese flagged vessels are currently trading in international waters.

Example questions that can be answered with this endpoint:

- *How many Chinese flagged Panamax vessels are currently trading outside of China?*
- *Whats the percentage of the Chinese flagged fleet that is currently trading internationally and how has this changed over time?*


.. autoclass:: oceanbolt.sdk.data.tonnage.ChineseWatersTimeseries
    :members:

Example
-------
*How many ballast ultramax or supramax vessels are currently in the Indian Ocean?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.tonnage import ChineseWatersTimeseries
    from datetime import date


    base_client = APIClient("<token>")
    df = ChineseWatersTimeseries(base_client).get(
        sub_segment=['ultramax','supramax'],
        group_by="segment",
    )

Returns:

.. csv-table::
    :header: group,date,inside_chinese_waters_count,inside_chinese_waters_dwt,outside_chinese_waters_count,outside_chinese_waters_dwt

    Supramax,2017-01-01,126,6690636.0,65,3411383.0
    Supramax,2017-01-02,129,6841846.0,62,3260173.0
    Supramax,2017-01-03,125,6621076.0,66,3480943.0
    Supramax,2017-01-04,125,6621076.0,66,3480943.0
    Supramax,2017-01-05,125,6630355.0,66,3471664.0
    Supramax,2017-01-06,125,6630153.0,66,3471866.0
    Supramax,2017-01-07,126,6690125.0,65,3411894.0
    Supramax,2017-01-08,125,6628425.0,66,3473594.0
    Supramax,2017-01-09,125,6619114.0,66,3482905.0



Arguments
---------
.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageChineseWatersRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.tonnage_v3.types.TonnageChineseWatersResponse
    :members:

.. autoclass:: oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesGroup
    :members:
    :noindex:

.. autoclass:: oceanbolt.com.tonnage_v3.types.ChineseWatersTimeseriesRow
    :members:
    :noindex:
