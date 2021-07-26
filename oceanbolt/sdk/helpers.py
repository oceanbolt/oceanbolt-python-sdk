from datetime import date
import enum
from typing import Any, Dict, Optional
import pandas as pd
from google.protobuf.wrappers_pb2 import DoubleValue


def filter_nones_from_dict(query_parameters: Dict[str, Optional[Any]]) -> Dict[str, Any]:
    return {k: v for k, v in query_parameters.items() if v}


def process_enum_parameter(
    parameter: Optional[enum.Enum], to_lower_case: bool = True
) -> Optional[str]:
    return (
        (str(parameter.value.lower()) if to_lower_case else str(parameter.value))
        if parameter
        else None
    )


def pb_timeseries_to_pandas(data):
    if len(data) == 0:
        return pd.DataFrame()

    first_group = data[0]

    if len(first_group.rows) == 0:
        return pd.DataFrame()

    first_row = first_group.rows[0]

    dict_list = []
    for g in data:
        for r in g.rows:
            d = {}
            if g.group != "" and g.group != "default":
                d["group"] = g.group
            for attr in first_row._meta.fields:
                d[attr] = getattr(r, attr)
            dict_list.append(d)

    df = pd.DataFrame(dict_list)
    df = df.convert_dtypes()

    return df


def validate(kwargs):
    for key, value in kwargs.items():
        if isinstance(value, date):
            kwargs[key] = value.isoformat()
    return filter_nones_from_dict(kwargs)


def wrapPoints(kwargs):
    for key, value in kwargs.items():
        if key == "locations":
            for index, item in enumerate(value):
                for key, value in item.items():
                    if key == "point":
                        kwargs["locations"][index]["point"]["lon"] = DoubleValue(value=value["lon"])
                        kwargs["locations"][index]["point"]["lat"] = DoubleValue(value=value["lat"])

    return filter_nones_from_dict(kwargs)


def pb_list_to_pandas(data):

    if len(data) == 0:
        return pd.DataFrame()

    first = data[0]

    df = pd.DataFrame([[getattr(i, attr) for attr in first._meta.fields] for i in data], columns=first._meta.fields)
    df = df.convert_dtypes()
    return df
