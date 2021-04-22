"""Produce a column sparkline."""
import piltdown.literals as lit
from typing import List, TypeVar
import math

Tnum = TypeVar("Tnum", int, float)


def column_sparkline(data: List[Tnum], bottom: Tnum = 0) -> str:
    """Produce a column sparkline.

    Given a list of numbers, produce a column sparkline
    with columns shoehorned into the 9 possible values from
    empty to a full block. Paremeter `bottom` is the lowest
    value. That is, if `bottom` is 0 (default) and your range
    of your data is from 80 to 90, then all your bars will be
    mostly full. If your `bottom` is 80, then your bars will
    range across what is effectively a range of 10.
    """
    if min(data) >= bottom:
        data = list(map(lambda x: x - bottom, data))
    else:
        raise ValueError(
            "Bottom must be less than or equal to lowest data value"
        )
    scaler = 1 / (max(data) / 8)
    data = list(map(lambda x: math.ceil(x * scaler), data))
    ret = ""
    for i in data:
        ret += lit.V8THS[i]
    return ret
