from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.distance import DistanceCalculator

__client__ = APIClient()


def test_distance():
    dist = DistanceCalculator(__client__).distance(
        locations=[
            {"imo": 9586801},
            {"port_id": 2143},
            {"unlocode": "HKHKG"},
            {"point": {"lat": 10, "lon": 30}}
        ]
    )

    assert dist > 1000


def test_duration():
    duration_hours = DistanceCalculator(__client__).duration(
        speed=12,
        locations=[
            {"imo": 9586801},
            {"port_id": 2143},
            {"unlocode": "HKHKG"},
            {"point": {"lat": 10, "lon": 30}}
        ]
    )

    assert duration_hours > 100


def test_shortest_path():
    df = DistanceCalculator(__client__).shortest_route(
        locations=[
            {"imo": 9586801},
            {"port_id": 2143},
            {"unlocode": "HKHKG"},
            {"point": {"lat": 10, "lon": 30}}
        ]
    )
    print(df)
    assert len(df) > 0
