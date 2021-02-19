from datetime import date
import enum
import logging
from typing import Any, Dict, Optional
import pandas as pd

def filter_nones_from_dict(query_parameters: Dict[str, Optional[Any]]) -> Dict[str, Any]:
    """
    This function takes a list of parameters as a dict, and returns a dict containing only non null parameters

    Examples:
        >>> filter_nones_from_dict({"key1": None, "key2": "some value"})
        {"key2": "some value"}

    Args:
        query_parameters (dict): query parameters in the form of a dict with `None` values

    Returns:
        dict: a dict with None values filtered

    """
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

    firstGroup = data[0]
    rows = firstGroup.rows
    firstRow = firstGroup.rows[0]

    l = []
    for g in data:
        for r in rows:
            d = {}
            if g.group != "" and g.group != "default":
                d["group"] = g.group
            for attr in firstRow._meta.fields:
                d[attr] = getattr(r,attr)

            l.append(d)

    df = pd.DataFrame(l)
    df.convert_dtypes()

    return df

def validate(kwargs):
    for key,value in kwargs.items():
        if isinstance(value,date):
            kwargs[key] = value.isoformat()
    return filter_nones_from_dict(kwargs)

def pb_list_to_pandas(data):

    if len(data) == 0:
        return pd.DataFrame()

    first = data[0]
    members = [attr for attr in dir(first._pb) if attr.islower() and not attr.startswith("_")]

    # print(first._meta.fields)

    df = pd.DataFrame([[getattr(i, k) for k in members] for i in data], columns=members)
    return df

