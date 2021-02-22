from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.data import Ports, Countries, Commodities, Segments, Regions, Zones
from oceanbolt.sdk.data import TradeFlows, TradeFlowTimeseries
from oceanbolt.sdk.data import PortCalls, PortCallTimeseries
from oceanbolt.sdk.data import TonnageZoneTimeseries, FleetSpeedTimeseries, ChineseWatersTimeseries
from oceanbolt.sdk.data import CongestionVessels, CongestionTimeseries

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


# Data endpoints

def test_congestion_vessels():
    df = CongestionVessels(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_congestion_timeseries():
    df = CongestionTimeseries(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_port_calls():
    df = PortCalls(__client__).get(country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_port_call_timeseries():
    df = PortCallTimeseries(__client__).get(frequency="monthly", country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_tonnage_count():
    df = TonnageZoneTimeseries(__client__).get(segment=["handysize"], start_date="2021-01-01")
    assert len(df) > 0


def test_fleet_speed():
    df = FleetSpeedTimeseries(__client__).get(segment=["handysize"], start_date="2021-01-01")
    assert len(df) > 0


def test_chinese_waters():
    df = ChineseWatersTimeseries(__client__).get(segment=["handysize"], start_date="2021-01-01")
    assert len(df) > 0


def test_trade_flows():
    df = TradeFlows(__client__).get(load_country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0


def test_trade_flow_timeseries():
    df = TradeFlowTimeseries(__client__).get(frequency="monthly", load_country_code=["cn"], start_date="2021-01-01")
    assert len(df) > 0
