# This is the client library generated by this plugin.
from google.api_core.gapic_v1.client_info import ClientInfo
from oceanbolt.com import tonnage_client_v3, portcalls_client_v3, drydock_client_v3, congestion_client_v3, tradeflows_client_v3, entities_client_v3, polygonmanagement_client_v3, \
    fleetmanagement_client_v3, distancecalculator_client_v3, custompolygon_client_v3, vessels_client_v3, vesselstates_client_v3
from google.auth import credentials, _helpers  # type: ignore
import os
import getpass
from pkg_resources import get_distribution


class ObCredentials(credentials.Credentials):
    @property
    def expired(self):
        """Returns `False`, OB credentials never expire."""
        return False

    @property
    def valid(self):
        """Returns `True`, OB credentials are always valid."""
        return True

    def refresh(self, request):
        """Raises :class:`ValueError``, anonymous credentials cannot be
        refreshed."""
        raise ValueError("OB credentials cannot be refreshed.")

    def apply(self, headers, token=None):
        """Sets the token in the header."""
        headers["authorization"] = "Bearer {}".format(
            _helpers.from_bytes(token or self.token)
        )

    def before_request(self, request, method, url, headers):
        """OB credentials applies headers to the request."""
        self.apply(headers)


def APIClientInteractive():
    return APIClient(getpass.getpass())


METRICS_METADATA_KEY = "x-goog-api-client"


class OBClientInfo(ClientInfo):
    def to_user_agent(self):
        return "oceanbolt-python-sdk/" + get_distribution("oceanbolt.sdk").version

    def to_grpc_metadata(self):
        """Returns the gRPC metadata for this client info."""
        return (METRICS_METADATA_KEY, self.to_user_agent())


class APIClient:

    def __init__(self, token=None, platform="dry"):
        api_key = os.getenv("OCEANBOLT_API_KEY")
        if api_key is None and token is None:
            raise KeyError(
                "You must either set the OCEANBOLT_API_KEY environment variable, or supply enter your Oceanbolt API key as a string argument."
                " You can create API keys at https://app.oceanbolt.com"
            )

        creds = ObCredentials()

        if token is not None:
            creds.token = token
        else:
            creds.token = api_key

        self.metadata = [('x-ob-platform', platform)]
        self.tonnageClient = tonnage_client_v3.TonnageServiceClient(credentials=creds, client_info=OBClientInfo())
        self.portCallsClient = portcalls_client_v3.PortCallServiceClient(credentials=creds, client_info=OBClientInfo())
        self.tradeFlowsClient = tradeflows_client_v3.TradeFlowServiceClient(credentials=creds, client_info=OBClientInfo())
        self.congestionClient = congestion_client_v3.CongestionServiceClient(credentials=creds, client_info=OBClientInfo())
        self.drydockClient = drydock_client_v3.DrydockServiceClient(credentials=creds, client_info=OBClientInfo())
        self.entitiesClient = entities_client_v3.EntityServiceClient(credentials=creds, client_info=OBClientInfo())
        self.polygonClient = polygonmanagement_client_v3.PolygonManagementServiceClient(credentials=creds,
                                                                              client_info=OBClientInfo())
        self.fleetClient = fleetmanagement_client_v3.FleetManagementServiceClient(credentials=creds, client_info=OBClientInfo())
        self.distanceClient = distancecalculator_client_v3.DistanceCalculatorServiceClient(credentials=creds,
                                                                                 client_info=OBClientInfo())
        self.customPolygonClient = custompolygon_client_v3.CustomPolygonServiceClient(credentials=creds,
                                                                            client_info=OBClientInfo())
        self.vesselsClient = vessels_client_v3.VesselServiceClient(credentials=creds, client_info=OBClientInfo())
        self.vesselStatesClient = vesselstates_client_v3.VesselStateServiceClient(credentials=creds, client_info=OBClientInfo())

    def _tonnage_client(self):
        return self.tonnageClient

    def _congestion_client(self):
        return self.congestionClient

    def _trade_flows_client(self):
        return self.tradeFlowsClient

    def _drydock_client(self):
        return self.drydockClient

    def _portcalls_client(self):
        return self.portCallsClient

    def _entities_client(self):
        return self.entitiesClient

    def _fleet_client(self):
        return self.fleetClient

    def _polygon_client(self):
        return self.polygonClient

    def _distance_client(self):
        return self.distanceClient

    def _custompolygon_client(self):
        return self.customPolygonClient

    def _vessels_client(self):
        return self.vesselsClient

    def _vessel_states_client(self):
        return self.vesselStatesClient
