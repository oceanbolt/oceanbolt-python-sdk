from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.fleet import FleetManagement
from datetime import datetime

__client__ = APIClient()


def test_create_fleet():
    now = datetime.now()

    current_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    fleet = FleetManagement(__client__).create_fleet(fleet_name="my_great_test_fleet" + current_time)
    assert fleet.fleet_id != ""
    assert fleet.fleet_name == "my_great_test_fleet" + current_time

    vessel = FleetManagement(__client__).add_vessel(fleet_id=fleet.fleet_id, vessel={"imo": 1234567, "metadata": {"key": "val"}})
    assert vessel.imo == 1234567
    assert vessel.metadata["key"] == "val"

    vessels = FleetManagement(__client__).list_vessels(fleet_id=fleet.fleet_id)
    assert len(vessels.vessels) == 1
    FleetManagement(__client__).delete_vessel(fleet_id=fleet.fleet_id, imo=1234567)

    fleets = FleetManagement(__client__).list_fleets()
    assert len(fleets.fleets) > 0

    FleetManagement(__client__).batch_add_vessels_from_csv(fleet.fleet_id, "tests/integration/test_fleet_data.csv")

    FleetManagement(__client__).replace_vessels_from_csv(fleet.fleet_id, "tests/integration/test_fleet_data.csv")

    FleetManagement(__client__).replace_vessels_from_csv(fleet.fleet_id, "tests/integration/test_fleet_data.csv")

    FleetManagement(__client__).delete_fleet(fleet_id=fleet.fleet_id)
