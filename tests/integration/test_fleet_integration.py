from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.fleet import FleetManagement

__client__ = APIClient()

def test_create_fleet():
    fleet = FleetManagement(__client__).create_fleet(fleet_name="my_test_fleet")
    assert fleet.fleet_id != ""
    assert fleet.fleet_name == "my_test_fleet"

    FleetManagement(__client__).delete_fleet(fleet_id=fleet.fleet_id)

