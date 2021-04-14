"""Bar charts for Piltdown."""
from typing import Dict
import piltdown.literals as lit


def max_bar_width(data: Dict[str, float], width: int) -> int:
    """Caluclate the maximum width of a bar based on the longest label."""
    return width - max(list(map(len, data.keys())))


def make_line(
    label: str, value: float, line_break: bool, key_labels: str
) -> str:
    """Make a single line of the bar chart."""
    return "This is just a stub."


def bar_chart(
    data: Dict[str, float],
    width: int,
    line_breaks: bool = False,
    key_labels: str = lit.DEFAULT_LABELS,
) -> str:
    """Create a bar chart.

    Return a bar plot given a dict of {"label":value} pairs and max line
    width.
    """
    ret: str = ""
    for line, value in data.items():
        ret += make_line(line, value, line_breaks, key_labels)
    return ret
