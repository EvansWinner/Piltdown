"""Horizontal bar charts for Piltdown."""
import math
from typing import Dict, List
import piltdown.literals as lit
import piltdown.util as util


def hbar_line(
    length: float,
    eighths: Dict[int, str],
    eight_eighths: str,
    empty: str,
) -> str:
    """Generate a single bar for a horizontal bar chart."""
    ret: str = ""
    rounded: float = round(length * 8) / 8 / 8
    ret += eight_eighths * math.floor(rounded)
    ret += eighths[int((rounded - math.floor(rounded)) * 8)]
    return ret


def hbar(
    data: List[float],
    lables: List[str] = lit.DEFAULT_LABELS,
    eighths: Dict[int, str] = lit.EIGHTHS,
    eight_eighths: str = lit.EIGHT_EIGHTHS,
    empty: str = lit.EMPTY_BLOCK,
) -> str:
    """Generate a horizontal bar chart."""
    if len(data) > len(lables):
        raise ValueError("Not enough lables")
    # Left-pad lables so they're all the same length
    lable_max: int = max(map(len, lables))
    for i,item in enumerate(lables):
        lables[i]=item.rjust(lable_max)
    # Produce chart
    ret: str = ""
    for line, lable in zip(data, lables):
        ret += util.fullwidth(lable) 
        ret += hbar_line(line, eighths, eight_eighths, empty) + str(line) + "\n"
    return ret


print(hbar([72, 93, 22, 54],["Cats","Monkeys","Dogs","Me"]))
