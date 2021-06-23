Oceanbolt Python SDK
********************

|GitHubStatusBadge|_ |NetlifyStatusBadge|_

.. |GitHubStatusBadge| image:: https://github.com/oceanbolt/oceanbolt-python-sdk/actions/workflows/python-ci.yml/badge.svg
.. _GitHubStatusBadge: https://github.com/oceanbolt/oceanbolt-python-sdk/actions



.. |NetlifyStatusBadge| image:: https://api.netlify.com/api/v1/badges/0c776868-ce00-4c64-a4e1-1817953d3169/deploy-status
.. _NetlifyStatusBadge: https://app.netlify.com/sites/oceanbolt-python-sdk/deploys


The Oceanbolt Python SDK provides access to Oceanbolt data. It is a python wrapper around the Oceanbolt Data API (REST).

It can be easily integrated existing tools such as jupyter notebooks, scripts, and applications.

Data is returned in the form of pandas.DataFrame, which allows for easy manipulation and further data processing.

The python SDK is available to all Oceanbolt API clients (API authentication token required in order to get access). API tokens can be generated in the Oceanbolt App (app.oceanbolt.com)

We suggest to read the :doc:`getting_started` page to get up and running quickly.


Project Status
______________

**IMPORTANT**: The oceanbolt-python-sdk is still undergoing development, and certain features may be changed/removed before the launch of version 1.0.0

Example
_______
Short example to illustrate the use of the **oceanbolt-python-sdk**:

.. literalinclude:: examples/quick_one.py
    :linenos:
    :language: python


API Reference
-------------
.. toctree::
   :maxdepth: 2
   :titlesonly:
   :caption: Home

   self
   getting_started

.. toctree::
    :maxdepth: 1
    :caption: Trade Flows

    tradeflows_v3/tradeflows
    tradeflows_v3/timeseries

.. toctree::
    :maxdepth: 1
    :caption: Tonnage Supply

    tonnage_v3/zone_count
    tonnage_v3/zone_changes
    tonnage_v3/chinese_waters
    tonnage_v3/fleet_speed
    tonnage_v3/fleet_growth
    tonnage_v3/fleet_status
    tonnage_v3/custom_polygon

.. toctree::
    :maxdepth: 1
    :caption: Congestion

    congestion_v3/congested_vessels
    congestion_v3/timeseries

.. toctree::
    :maxdepth: 1
    :caption: Drydock

    drydock_v3/current_stays
    drydock_v3/historical_stays
    drydock_v3/timeseries

.. toctree::
    :maxdepth: 1
    :caption: Port Calls/Port Data

    portcalls_v3/port_calls
    portcalls_v3/timeseries
    portcalls_v3/port_particulars


.. toctree::
    :maxdepth: 1
    :caption: Entities

    entities_v3/ports
    entities_v3/countries
    entities_v3/regions
    entities_v3/zones
    entities_v3/commodities
    entities_v3/segments
    entities_v3/search

.. toctree::
    :maxdepth: 1
    :caption: User Fleet

    fleet_v3/fleets

.. toctree::
    :maxdepth: 1
    :caption: Distance  Calculator

    distance_v3/distance

Indices and tables
------------------

* :ref:`genindex`
