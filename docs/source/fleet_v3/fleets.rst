================
Fleet Management
================



Introduction to Fleets
----------------------
The FleetManagement service provides an easy way for users to programmatically
interact with the Oceanbolt API and manage their fleet resources.

A Fleet is a user defined collection of vessels. Fleets can be used to a group vessels
of particular intererst (a users own fleet, or the fleet of a competitor for example).

Fleets are available in various parts of the Oceanbolt platform, facilitating for easy
monitoring and querying of the vessels in the fleet.

Fleets consists of Vessels, and Vessels can be added/removed from a Fleet using either
the API or the dashboard. Users can define custom metadata for the vessels when they add
the vessels. This enables combining Oceanbolt data with internal data on the vessel (such as current route,
operator name, current index, Vezon Imos platform link etc.).

Shared Fleets
-------------
By default Fleets are private to the user who created them. Fleets can however be shared with the rest of
the organization if fleet creator enables sharing the given Fleet.

Batch Methods
-------------

The API provides several "batch" methods, which make it easy to modify a fleet using
batch operations. This can for example facilite easy updating of an organizations's fleet
list in the Oceanbolt platform.

For example the FleetManagent SDK provides the following convenience functions to easily
update a fleet from the basis of a CSV sheet:

- :ref:`batch-add-vessels-csv`
- :ref:`replace-vessels-csv`


FleetManagement Client
----------------------
.. autoclass:: oceanbolt.sdk.fleet.FleetManagement
    :members:
    :noindex:

=======
Methods
=======

Create Fleet
------------
Create a user defined fleet

Example
#######
.. code-block:: python

    fleet = FleetManagement(base_client).create_fleet(
        fleet_name="my fleet"
    )

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.CreateFleetRequest
    :members:

Response
########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Fleet
    :members:
    :noindex:


List Fleets
-----------
Lists all user defined fleets

Example
#######
.. code-block:: python

    fleets = FleetManagement(base_client).list_fleets()

Arguments
#########
None

Response
########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Fleets
    :members:


Describe Fleet
--------------
Retrieves a user defined fleet

Example
#######
.. code-block:: python

    fleet = FleetManagement(base_client).describe_fleet(
        fleet_id="<fleet_id>"
    )

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.GetFleetRequest
    :members:

Response
########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Fleet
    :members:


Delete Fleet
------------
Deletes a user defined fleet

Example
#######
.. code-block:: python

    FleetManagement(base_client).delete_fleet(fleet_id="<fleet-id>")

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.DeleteFleetRequest
    :members:

Response
########
None

Rename Fleet
------------
Renames a user defined fleet

Example
#######
.. code-block:: python

    FleetManagement(base_client).rename_fleet(fleet_id="<fleet-id>",new_fleet_name="new name")

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.RenameFleetRequest
    :members:

Response
########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Fleet
    :members:
    :noindex:


Share Fleet
-----------
Shares a user defined fleet with other users in the same organization

Example
#######
.. code-block:: python

    FleetManagement(base_client).share_fleet(fleet_id="<fleet-id>")

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.ShareFleetRequest
    :members:

Response
########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Fleet
    :members:
    :noindex:

Unshare Fleet
-------------
Unshares a user defined fleet, so that it is no longer shared with other users in the same organization

Example
#######
.. code-block:: python

    FleetManagement(base_client).unshare_fleet(fleet_id="<fleet-id>")

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.ShareFleetRequest
    :members:
    :noindex:


Response
########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Fleet
    :members:
    :noindex:

Add Vessel
----------
Adds a vessel to a fleet. All metadata values must be strings.

Example
#######
.. code-block:: python

    vessel = FleetManagement(base_client).add_vessel(
        fleet_id="<fleet_id>",
        vessel={
            "imo":1234567,
            "metadata":{
                "key":"value"
            }
        }
    )

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.AddVesselRequest
    :members:

Response
########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.Vessel
    :members:

Delete Vessel
-------------
Deletes a vessel from a fleet

Example
#######
.. code-block:: python

    FleetManagement(base_client).delete_vessel(
        fleet_id="<fleet_id>",
        imo=1234567
    )

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.DeleteVesselRequest
    :members:

Response
########
None


Batch Add Vessels
-----------------
Batch adds new vessels from a fleet. All metadata values must be strings.

Example
#######
.. code-block:: python

    FleetManagement(base_client).batch_add_vessels(
        fleet_id="<fleet_id>",
        vessels=[
            {
            "imo":1234567,
            "metadata":{
                "key":"value"
            },
            {
            "imo":7654321,
            "metadata":{
                "key":"other_value"
            }
        ]
    )

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.BatchVesselsRequest
    :members:

Response
########
None

.. _batch-add-vessels-csv:

Batch Add Vessels From CSV
--------------------------
Batch adds new vessels from a fleet sourced from a CSV file. A maximum
of 1000 vessels can be added to a fleet.

The csv file must have a column named **'imo'**.

Example
#######

Example of csv file **my_fleet_list.csv**:

.. csv-table::
    :header:     imo,my_key,other_key,my_link

    1234567,"val","some value","https://mylink...."
    7654321,"another val","some other value","https://mylink...."


.. code-block:: python

    FleetManagement(base_client).batch_add_vessels_from_csv(
        fleet_id="<fleet_id>",
        path="path/my_fleet_list.csv"
    )

Arguments
#########
.. autoclass:: oceanbolt.sdk.fleet.FleetManagement.batch_add_vessels_from_csv()
    :members:

Response
########
None


Drop Vessels
------------
Removes all vessels from a fleet

Example
#######
.. code-block:: python

    FleetManagement(base_client).drop_vessels(
        fleet_id="<fleet_id>"
    )

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.DropVesselsRequest
    :members:

Response
########
None


Replace Vessels
---------------
Replaces the existing vessels in a Fleet with a batch
of new vessels. This is equivalent to first calling
DropVessels and then calling BatchAddVessels. A maximum
of 1000 vessels can be added to a fleet. All metadata values must be strings.

Example
#######
.. code-block:: python

    FleetManagement(base_client).replace_vessels(
        fleet_id="<fleet_id>",
        vessels=[
            {
            "imo":1234567,
            "metadata":{
                "key":"value"
            },
            {
            "imo":7654321,
            "metadata":{
                "key":"other_value"
            }
        ]
    )

Arguments
#########
.. autoclass:: oceanbolt.com.fleetmanagement_v3.types.BatchVesselsRequest
    :members:
    :noindex:

Response
########
None

.. _replace-vessels-csv:

Replace Vessels From CSV
------------------------
Replaces the existing vessels in a Fleet with a batch
of new vessels sourced from a CSV file. This is equivalent to first calling
DropVessels and then calling BatchAddVessels. A maximum
of 1000 vessels can be added to a fleet.

The csv file must have a column named **'imo'**.

Example
#######

Example of csv file **my_fleet_list.csv**:

.. csv-table::
    :header:     imo,my_key,other_key,my_link

    1234567,"val","some value","https://mylink...."
    7654321,"another val","some other value","https://mylink...."


.. code-block:: python

    FleetManagement(base_client).replace_vessels_from_csv(
        fleet_id="<fleet_id>",
        path="path/my_fleet_list.csv"
    )

Arguments
#########

.. autoclass:: oceanbolt.sdk.fleet.FleetManagement.replace_vessels_from_csv()
    :members:

Response
########
None
