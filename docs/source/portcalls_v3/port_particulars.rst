Port Particulars Data
=====================
Retrieve port particulars data for a given port/terminal based on physical characteristics of the vessels that have actually visited the port/terminal.

Example questions that can be answered with this endpoint:

- *What is the maximum draught, loa and beam of the vessels that visited the Port of Narvik in the past 6 months?*

.. autoclass:: oceanbolt.sdk.data.port_calls.PortParticulars
    :members:

Example
-------
- *What is the maximum draught, loa and beam of the vessels that visited the Port of Narvik in the past 6 months?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.port_calls import PortParticulars
    from datetime import date,timedelta


    base_client = APIClient("<token>")
    df = PortParticulars(base_client).get_raw(
        unlocode="NONVK"
        start_date=date.today() - timedelta(days=180),
    )

Returns:

.. code-block:: json

    {
      "loa": {
        "min": 17309,
        "max": 211153,
        "percentile10": 17309,
        "percentile50": 82000,
        "percentile90": 205236,
        "percentile95": 207392.5,
        "mean": 117732.08571428571,
        "percentile99": 210950
      },
      "beam": {
        "min": 24,
        "max": 50,
        "percentile10": 24,
        "percentile50": 32.26,
        "percentile90": 49,
        "percentile95": 50,
        "mean": 38.199160000000028,
        "percentile99": 50
      },
      "maxDraught": {
        "min": 6.9,
        "max": 18.6,
        "percentile10": 8.42,
        "percentile50": 14.5,
        "percentile90": 18.37,
        "percentile95": 18.4,
        "mean": 14.919417473876365,
        "percentile99": 18.6
      },
      "reportedDraught": {
        "min": 6.6,
        "max": 18.7,
        "percentile10": 8.7,
        "percentile50": 14.4,
        "percentile90": 18.3,
        "percentile95": 18.45,
        "mean": 13.921904761904758,
        "percentile99": 18.55
      },
      "dwt": {
        "min": 17309,
        "max": 211153,
        "percentile10": 17309,
        "percentile50": 82000,
        "percentile90": 205236,
        "percentile95": 207392.5,
        "mean": 117732.08571428571,
        "percentile99": 210950
      },
      "numberOfPortCalls": 105
    }

Arguments
---------
.. autoclass:: oceanbolt.com.portcalls_v3.types.GetPortParticularsRequest
    :members:

Response
--------
.. autoclass:: oceanbolt.com.portcalls_v3.types.GetPortParticularsResponse
    :members:

.. autoclass:: oceanbolt.com.portcalls_v3.types.Statistic
    :members:
