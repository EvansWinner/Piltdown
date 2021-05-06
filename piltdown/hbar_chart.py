"""Horizontal bar charts for Piltdown."""
import math
from typing import Dict, List
import piltdown.literals as lit
import piltdown.util as util


def hbar_line(
    length: float,
    eighths: Dict[int, str],
    eight_eighths: str,
) -> str:
    """Generate a single bar for a horizontal bar chart."""
    ret: str = ""
    rounded: float = round(length * 8) / 8 
    ret += eight_eighths * math.floor(rounded)
    ret += eighths[int((rounded - math.floor(rounded)) * 8)]
    return ret


def hbar(
    data: List[float],
    labels: List[str] = lit.DEFAULT_LABELS,
    max_line_len: int = 20,
    eighths: Dict[int, str] = lit.EIGHTHS,
    eight_eighths: str = lit.EIGHT_EIGHTHS,
    print_values: bool = True,
) -> str:
    """Generate a horizontal bar chart."""
    if len(data) > len(labels):
        raise ValueError("Not enough labels")
    # Left-pad labels so they're all the same length
    label_max: int = max(map(len, labels))
    for i, item in enumerate(labels):
        labels[i] = item.rjust(label_max)
    # Calculate scale factor for bars 
    max_data = max(data)
    max_bar_len: int = (
        max_line_len
        - max(list(map(len, map(str, data))))
        - max(list(map(len, labels)))
    )
    scale_factor: float = max_bar_len / max_data
    # Produce chart
    ret: str = ""
    for line, label in zip(data, labels):
        ret += util.fullwidth(label)
        ret += hbar_line(line * scale_factor, eighths, eight_eighths)
        if line == 0 and print_values:
            ret += " "
        if print_values:
            ret += str(line)
        ret += "\n"
    return ret

