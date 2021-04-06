"""Horizontal bar charts for Piltdown."""
import math
from typing import Dict
import literals


def hbar_line(
    length: float,
    eighths: Dict[int, str] = literals.EIGHTHS,
    eight_eighths: str = literals.EIGHT_EIGHTHS,
    empty: str = literals.EMPTY_BLOCK,
) -> str:
    """Generate a horizontal bar chart."""
    ret: str = ""
    rounded: float = round(length * 8) / 8
    ret = eight_eighths * math.floor(rounded)
    ret += eighths[int((rounded - math.floor(rounded)) * 8)]
    return ret
