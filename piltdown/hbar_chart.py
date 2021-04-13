"""Horizontal bar charts for Piltdown."""
import math
from typing import Dict
import piltdown.literals as lit


def hbar_line(
    length: float,
    eighths: Dict[int, str] = lit.EIGHTHS,
    eight_eighths: str = lit.EIGHT_EIGHTHS,
    empty: str = lit.EMPTY_BLOCK,
) -> str:
    """Generate a horizontal bar chart."""
    ret: str = ""
    rounded: float = round(length * 8) / 8
    ret = eight_eighths * math.floor(rounded)
    ret += eighths[int((rounded - math.floor(rounded)) * 8)]
    return ret
