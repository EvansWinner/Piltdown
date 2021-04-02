"""Bar charts for Piltdown."""
from typing import Dict, List
import piltdata
import piltutil


def max_bar_width(data: Dict[str, float], width: int) -> int:
    """Caluclate the maximum width of a bar based on the longest label."""
    return width - max(list(map(len, data.keys())))


def make_line(label: str, value: float, line_break: bool, key_labels) -> str:
    """Pass."""
    pass


def bar(
    data: Dict[str, float],
    width: int,
    line_breaks: bool = False,
    key_labels: List[str] = piltdata.default_labels,
) -> str:
    """Return a bar plot given a dict d of {"label":value} pairs and max line width, w."""
    ret: str = ""
    for line, value in data.items():
        ret += make_line(line, value, line_breaks, key_labels)
    return ret
