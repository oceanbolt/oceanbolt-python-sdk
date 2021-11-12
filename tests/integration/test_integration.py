from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.data import Ports, Countries, Commodities, Segments, Regions, Zones, Search
from oceanbolt.sdk.data import TradeFlows, TradeFlowTimeseries
from oceanbolt.sdk.data import PortCalls, PortCallTimeseries, PortParticulars
from oceanbolt.sdk.data import TonnageZoneTimeseries, FleetSpeedTimeseries, ChineseWatersTimeseries, FleetStatusTimeseries, FleetGrowthTimeseries, ZoneChangesTimeseries
from oceanbolt.sdk.data import CongestionVessels, CongestionTimeseries
from oceanbolt.sdk.data import DryDockTimeseries, DryDockCurrentVessels, DryDockHistoricalStays
from oceanbolt.sdk.data import Vessels

__client__ = APIClient()


# Entities endpoints

def test_ports():
    df = Ports(__client__).get()
    assert len(df) > 0


def test_zones():
    df = Zones(__client__).get()
    assert len(df) > 0


def test_commodities():
    df = Commodities(__client__).get()
    assert len(df) > 0


def test_countries():
    df = Countries(__client__).get()
    assert len(df) > 0


def test_segments():
    df = Segments(__client__).get()
    assert len(df) > 0


def test_regions():
    df = Regions(__client__).get()
    assert len(df) > 0


def test_search_polygons():
    df = Search(__client__).search_polygons("tokyo")
    assert len(df) > 0


def test_search_vessels():
    df = Search(__client__).search_vessels("tenacity")
    assert len(df) > 0


# Data endpoints
def test_congestion_vessels():
    df = CongestionVessels(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_congestion_timeseries():
    df = CongestionTimeseries(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_drydock_historical_stays():
    df = DryDockHistoricalStays(__client__).get(port_id=[403], start_date="2021-01-01")
    assert len(df) > 0


def test_drydock_live_vessels():
    df = DryDockCurrentVessels(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_drydock_timeseries():
    df = DryDockTimeseries(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_port_calls():
    df = PortCalls(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_port_call_timeseries():
    df = PortCallTimeseries(__client__).get(frequency="monthly", country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_port_particulars():
    df = PortParticulars(__client__).get_raw(unlocode="NONVK")
    assert df.number_of_port_calls > 0


def test_tonnage_count():
    df = TonnageZoneTimeseries(__client__).get(segment=["handysize"], start_date="2021-01-01")
    assert len(df) > 0


def test_tonnage_count_empty():
    df = TonnageZoneTimeseries(__client__).get(sub_segment=["babycape"], zone_id=[22], port_status=["in_port"], laden_status=["laden"], start_date="2021-07-25", end_date="2021-07-26")
    assert len(df) == 0


def test_fleet_speed():
    df = FleetSpeedTimeseries(__client__).get(segment=["handysize"], start_date="2021-01-01")
    assert len(df) > 0


def test_fleet_status():
    df = FleetStatusTimeseries(__client__).get(segment=["handysize"])
    assert len(df) > 0


def test_fleet_growth():
    df = FleetGrowthTimeseries(__client__).get(segment=["handysize"])
    assert len(df) > 0


def test_zone_changes():
    df = ZoneChangesTimeseries(__client__).get(segment=["handysize"], start_date="2021-01-01")
    assert len(df) > 0


def test_chinese_waters():
    df = ChineseWatersTimeseries(__client__).get(segment=["handysize"], start_date="2021-01-01")
    assert len(df) > 0


# def test_custom_polygon():
#     df = CustomPolygonTimeseries(__client__).get(
#         geojson="{\"type\":\"Polygon\",\"coordinates\":[[[45.50537109374999,31.93351676190369],[50.4931640625,16.846605106396304],[61.083984375,20.138470312451155],[66.9287109375,27.819644755099446],[61.94091796875,31.89621446335144],[45.50537109374999,31.93351676190369]]]}",
#         start_date="2015-01-01",
#         end_date="2021-03-01",
#         sub_segment=["ultramax"]
#
#     )
#     assert len(df) > 0


def test_trade_flows():
    df = TradeFlows(__client__).get(load_country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_trade_flow_timeseries():
    df = TradeFlowTimeseries(__client__).get(frequency="monthly", load_country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


# Vessels Service
def test_vessels():
    df = Vessels(__client__).get(segment=["supramax"])
    assert len(df) > 0


def test_stoppage_events():
    df = Vessels(__client__).get(imo=[9583706])
    assert len(df) > 0
