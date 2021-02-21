Segments
========
Retrieve list of vessel segments

.. autoclass:: oceanbolt.sdk.data.entities.Segments
    :members:

Example
-------
.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.entities import Segments

    base_client = APIClient("<token>")
    df = Segments(base_client).get()



Arguments
---------

None

Response
--------
.. autoclass:: oceanbolt.com.entities_v3.types.ListSegmentsResponse
    :members:

.. autoclass:: oceanbolt.com.entities_v3.types.Segment
    :members:
