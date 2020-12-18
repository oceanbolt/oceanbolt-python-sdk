# oceanbolt-python-sdk
A python wrapper around the Oceanbolt Data Api

## Endpoints

#### List endpoints:
| Method | URL   |      Description      |  R Function name |
|----------|----------|:-------------:|------:|
| GET | https://beta.api.oceanbolt.com/v2/entities/countries | returns list of countries | listCountries() |
| GET | https://beta.api.oceanbolt.com/v2/entities/zones | returns list of zones | listZones() |
| GET | https://beta.api.oceanbolt.com/v2/entities/segments | returns list of segments | listSegments() |
| GET | https://beta.api.oceanbolt.com/v2/entities/regions | returns list of regions | listRegions() |
| GET | https://beta.api.oceanbolt.com/v2/entities/commodities | returns list of commodities | listCommodities() |

#### Data endpoints:

| Method | Doc URL   |      Description      |  R Function name |
|----------|----------|:-------------:|------:|
| POST | https://openapi.oceanbolt.com/#operation/getTonnageZone | returns tonnage zone data | getTonnageZoneCount() |
| POST | https://openapi.oceanbolt.com/#tag/fleetspeed | returns fleet speed data | getFleetSpeed() |
| POST | https://openapi.oceanbolt.com/#operation/postTradeflowLadenLegs | returns individual trade flows | getTradeFlows()
| POST | https://openapi.oceanbolt.com/#operation/postTradeflowDailyTimeseries | returns trade flows timeseries | getTradeFlowsTimeseries()
| POST | https://openapi.oceanbolt.com/#operation/getCongestionLive | returns live congestion data | getCongestionLive()
| POST | https://openapi.oceanbolt.com/#operation/getCongestionTimeseries | returns congestion timeseries | getCongestionTimeseries()
| POST | https://openapi.oceanbolt.com/#operation/vesselsLiveStatus | returns list of vessels | getVesselStatus()
| POST | https://openapi.oceanbolt.com/#operation/vesselsPortCalls | returns list of port calls | getPortCalls()
