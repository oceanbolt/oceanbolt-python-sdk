# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from oceanbolt.com.vessels_v3 import gapic_version as package_version

__version__ = package_version.__version__


from .services.vessel_service import VesselServiceClient
from .services.vessel_service import VesselServiceAsyncClient

from .types.service import DarkPeriodEvent
from .types.service import GetAisSummaryRequest
from .types.service import GetAisSummaryResponse
from .types.service import ListDarkPeriodEventsRequest
from .types.service import ListDarkPeriodEventsResponse
from .types.service import ListStoppageEventsRequest
from .types.service import ListStoppageEventsResponse
from .types.service import ListVesselsRequest
from .types.service import ListVesselsResponse
from .types.service import StoppageEvent
from .types.service import Vessel

__all__ = (
    'VesselServiceAsyncClient',
'DarkPeriodEvent',
'GetAisSummaryRequest',
'GetAisSummaryResponse',
'ListDarkPeriodEventsRequest',
'ListDarkPeriodEventsResponse',
'ListStoppageEventsRequest',
'ListStoppageEventsResponse',
'ListVesselsRequest',
'ListVesselsResponse',
'StoppageEvent',
'Vessel',
'VesselServiceClient',
)
