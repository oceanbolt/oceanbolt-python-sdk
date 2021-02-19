Ports
=====================
Retrieve list of ports

.. autoclass:: oceanbolt.sdk.data.entities.Ports
    :members:

Example
-------
.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.entities import Ports

    base_client = APIClient("<token>")
    df = Ports(base_client).get()



Arguments
---------

None

Response
--------
.. autoclass:: oceanbolt.com.entities_v3.types.ListPortsResponse
    :members:

.. autoclass:: oceanbolt.com.entities_v3.types.Port
    :members:

