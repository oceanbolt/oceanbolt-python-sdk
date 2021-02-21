List Trade Flows
================
Retrieve list of trade flows between countries, regions, for various commodity groups, for various vessels, or various ports.

Example questions that can be answered with this endpoint:

- *Which vessels loaded coal in Richards Bay in 2020?*
- *Which vessels discharged Australian coal into China in the past 30 days?*
- *Which vessels are currently loading fertilizers from the Arabian Gulf?*

.. autoclass:: oceanbolt.sdk.data.trade_flows.TradeFlows
    :members:

Example
-------
*Which vessels discharged Australian coal into China in the past 30 days?*

.. code-block:: python

    from oceanbolt.sdk.client import APIClient
    from oceanbolt.sdk.data.trade_flows import TradeFlowTimeseries
    from datetime import date, timedelta

    base_client = APIClient("<token>")
    df = TradeFlowTimeseries(base_client).get(
        load_country_code=['AU'],
        discharge_country_code=['CN'],
        commodity_group=['coal'],
        start_date=date.today() - timedelta(days=7),
        flow_direction="import", #Specified to filter and group on import date
    )

Returns:

.. csv-table::
    :header: voyage_id,flow_id,imo,vessel_name,segment,sub_segment,dwt,commodity,commodity_value,commodity_group,volume,load_port_id,load_port_name,load_port_unlocode,load_berth_id,load_berth_name,load_country_code,load_country,load_region,load_port_arrived_at,load_port_berthed_at,load_port_unberthed_at,load_port_departed_at,load_port_days_total,load_port_days_berthed,load_port_days_waiting,discharge_port_id,discharge_port_name,discharge_port_unlocode,discharge_berth_id,discharge_berth_name,discharge_country_code,discharge_country,discharge_region,discharge_port_arrived_at,discharge_port_berthed_at,discharge_port_unberthed_at,discharge_port_departed_at,discharge_port_days_total,discharge_port_days_berthed,discharge_port_days_waiting,days_steaming,days_total_duration,distance_calculated,distance_actual,eta,destination,status,parceling

    a3ba0ef87f61242681c7c70a37960127,534a71d70e8f775b3f0a620957e1838f,9611747,CS SALUBRITY,Capesize,Large Capesize (180-250k),180300.0,Coking Coal,coking_coal,Coal,44100.0,104,Hay Point,AUHPT,2893,Hay Point BHP Billiton Mitsubishi Alliance Coal Berths,AU,Australia,EAUSSIE,2020-12-10T11:47:15Z,2020-12-19T05:43:08Z,,2020-12-21T09:32:28Z,10.906,2.159,8.747,454,Taicang,CNTAC,5875,Taicang Iron Ore Berth,CN,China,FAREAST,2021-02-19T01:59:11Z,2021-02-19T01:59:11Z,,2021-02-20T11:21:49Z,1.39,1.39,0.0,59.685,71.982,3722.93,10829.0869359729,,CNCFD AUPHE,Complete,True
    afc185111ba16621aefb58b2ddff0111,561759de6538530ff53746f5187c7095,9591571,BULK INDONESIA,Panamax,Post-Panamax (90-110k),95712.0,Thermal Coal,thermal_coal,Coal,46800.0,122,Newcastle,AUNTL,3362,Newcastle NCIG Kooragang Coal Terminal Berths #8 to 10,AU,Australia,EAUSSIE,2020-12-01T20:30:49Z,2020-12-18T02:55:04Z,,2020-12-19T07:15:12Z,17.447,1.18,16.266,405,Lanshan,CNLSN,9778,Lanshan Multibulk Berth 4,CN,China,FAREAST,2021-02-14T08:57:04Z,2021-02-14T13:16:30Z,,2021-02-18T03:46:55Z,3.784,3.604,0.18,57.07,78.302,4657.7,12901.4480851075,2021-01-04T04:00:00Z,SINGAPORE,Complete,True
    c59c682f03c1b04d66e8f192b4738c01,1c5372651561f01161d89e5d4759a48f,9259161,HC PROGRESS,Panamax,Post-Panamax (90-110k),91879.0,Coal (unclassified),coal_unclassified,Coal,27800.0,104,Hay Point,AUHPT,2892,Hay Point DBCT Management Coal Berths,AU,Australia,EAUSSIE,2020-11-21T23:03:57Z,2020-11-25T11:00:36Z,,2020-11-26T11:34:28Z,4.521,1.023,3.497,413,Xinsha,CNMCI,9123,Xinsha Coal Berth 1,CN,China,FAREAST,2021-02-11T08:20:54Z,2021-02-14T08:58:54Z,,2021-02-16T10:56:43Z,5.108,2.081,3.026,76.865,86.494,3469.46,7314.21327295022,2020-12-09T19:30:00Z,KAOHSIUNG,Complete,True
    6e3493a6934b3a5d2c330a5269de6738,94a31ee3849059f35bbc5cfa858c618a,9469649,PING MAY,Capesize,Capesize (140-180k),178043.0,Coking Coal,coking_coal,Coal,86300.0,99,Gladstone,AUGLT,2851,Gladstone RG/Tanna Coal Berth,AU,Australia,EAUSSIE,2020-06-05T02:59:41Z,2020-06-11T14:55:57Z,,2020-06-13T19:58:42Z,8.707,2.21,6.497,395,Jingtang,CNJTG,2073,Jingtang Ores Berth 2,CN,China,FAREAST,2020-06-29T18:55:07Z,2021-02-16T04:27:45Z,,2021-02-20T00:35:12Z,235.236,3.838,231.397,15.955,259.899,4285.72,4391.5983731839,2020-06-30T14:00:00Z,CN TAS,Complete,True
    6e3493a6934b3a5d2c330a5269de6738,3ace89f90616a2b3a59a8aa353c3b5af,9469649,PING MAY,Capesize,Capesize (140-180k),178043.0,Coking Coal,coking_coal,Coal,86300.0,104,Hay Point,AUHPT,2892,Hay Point DBCT Management Coal Berths,AU,Australia,EAUSSIE,2020-05-28T05:59:52Z,2020-06-03T10:44:59Z,,2020-06-04T10:59:45Z,7.208,1.01,6.197,395,Jingtang,CNJTG,2073,Jingtang Ores Berth 2,CN,China,FAREAST,2020-06-29T18:55:07Z,2021-02-16T04:27:45Z,,2021-02-20T00:35:12Z,235.236,3.838,231.397,25.33,267.774,4142.27,4632.39126379947,2020-06-05T04:30:00Z,GLT AUS,Complete,True
    a98932063b7964d92d3a060fd2089dcf,a3d77733ed47db58433591655876d5bb,9774264,NAVIOS CORAL,Panamax,Kamsarmax (80-90k),84904.0,Coking Coal,coking_coal,Coal,83200.0,104,Hay Point,AUHPT,2893,Hay Point BHP Billiton Mitsubishi Alliance Coal Berths,AU,Australia,EAUSSIE,2020-05-25T01:46:48Z,2020-06-05T11:55:21Z,,2020-06-06T15:59:53Z,12.592,1.169,11.422,395,Jingtang,CNJTG,2073,Jingtang Ores Berth 2,CN,China,FAREAST,2020-06-20T19:55:15Z,2021-02-13T13:48:35Z,,2021-02-16T05:57:31Z,240.418,2.672,237.745,14.163,267.174,4142.27,4102.23079895485,2020-06-21T12:00:00Z,JINGTANG CHINA,Complete,False


Arguments
---------
.. autoclass:: oceanbolt.com.tradeflows_v3.types.TradeFlowDataRequest
    :members:
    :noindex:

Response
--------
.. autoclass:: oceanbolt.com.tradeflows_v3.types.GetTradeFlowsResponse
    :members:

.. autoclass:: oceanbolt.com.tradeflows_v3.types.TradeFlow
    :members:

