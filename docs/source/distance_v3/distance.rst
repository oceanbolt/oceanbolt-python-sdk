===================
Distance Calculator
===================



Introduction to the Distance Calculator
---------------------------------------
The DistanceCalculator service provides an easy way for users to calculate distances and shortest route between
ports and vessels.

More examples can be found in the following juypyter notebook:
`Calculating Distances <https://github.com/oceanbolt/oceanbolt-python-sdk/blob/master/docs/examples/12_calculating_distances.ipynb>`_

DistanceCalculator Client
-------------------------
.. autoclass:: oceanbolt.sdk.distance.DistanceCalculator
    :members:
    :noindex:


Calculating the shortest distance
---------------------------------

Example
#######
.. code-block:: python

    #Distance between ports
    distance = DistanceCalculator(base_client).distance(
        locations=[
            {"unlocode": "USHOU"},
            {"unlocode": "HKHKG"},
        ]
    )

    #Distance between a vessel's current location and a port
    distance = DistanceCalculator(base_client).distance(
        locations=[
            {"imo": 9586801},
            {"unlocode": "HKHKG"},
        ]
    )

    #Distance calculation with a waypoint
    distance = DistanceCalculator(APIClient()).distance(
        locations=[
            {"unlocode":"AUPHE"},
            {"unlocode":"HKHKG"},
            {"unlocode":"USHOU"}
        ]
    )

    #Distance between a raw coordinates
    distance = DistanceCalculator(base_client).distance(
        locations=[
            {"point": {"lon":-75.522015,"lat":10.298378}},
            {"point": {"lon":-95.127000,"lat":29.727500}},
        ]
    )




Arguments
#########
.. autoclass:: oceanbolt.com.distancecalculator_v3.types.DistanceRequest
    :members:

Response
########
.. autoclass:: oceanbolt.com.distancecalculator_v3.types.DistanceResponse
    :members:
    :noindex:


Batch Calculations
------------------
The distance calculator also supports batch calculations. The primary usage differences from non-batch calculations are
in the client's method name, prefixed with "batch\_", and in the request object, where each request to be calculated is
an element of a ``requests`` array.

Batch methods include:

- batch_distance()
- batch_duration()
- batch_shortest_route()
- batch_get_raw()

Example
#######

.. code-block:: python
    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.distance import DistanceCalculator
    from oceanbolt.sdk.data.entities import Search
    base_client = APIClient("<TOKEN>")
    
    distances = DistanceCalculator(base_client).batch_distance(
        requests=[
            {
                "locations": [
                    {"unlocode": "AUPHE"},
                    {"unlocode": "HKHKG"},
                    {"unlocode": "USHOU"}
                ]
            },
            {
                "locations": [
                    {"point": {"lon":-75.522015,"lat":10.298378}},
                    {"point": {"lon":-95.127000,"lat":29.727500}}
                ]
            }
        ]
    )
