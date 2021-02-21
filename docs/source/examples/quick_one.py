from datetime import date, timedelta

from oceanbolt.sdk.client import APIClient
from oceanbolt.sdk.data.port_calls import PortCalls

base_client = APIClient("<your api access token>")

# Get capesize port calls in Port Hedland for last 7 days
port_calls = PortCalls(base_client).get(
    start_date=date.today() - timedelta(days=7),
    segment=["capesize"],
    unlocode=["AUPHE"],
)
