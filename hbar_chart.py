"""Horizontal bar charts for Piltdown."""
import math
from typing import Dict
import piltdata


def hbar_line(
    length: float,
    eighths: Dict[int, str] = piltdata.EIGHTHS,
    eight_eighths: str = piltdata.EIGHT_EIGHTHS,
    empty: str = piltdata.EMPTY_BLOCK,
) -> str:
    """Generate a horizontal bar chart."""
    ret: str = ""
    rounded: float = round(length * 8) / 8
    ret = eight_eighths * math.floor(rounded)
    ret += eighths[int((rounded - math.floor(rounded)) * 8)]
    return ret


print(hbar_line(6.34))
print(hbar_line(3.45))
print(hbar_line(7.93))
