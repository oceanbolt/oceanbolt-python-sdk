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
            {imo: 9586801},
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



Arguments
#########
.. autoclass:: oceanbolt.com.distancecalculator_v3.types.DistanceRequest
    :members:

Response
########
.. autoclass:: oceanbolt.com.distancecalculator_v3.types.DistanceResponse
    :members:
    :noindex: