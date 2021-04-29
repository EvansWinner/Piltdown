"""Create a horizontal dot chart."""
from typing import List
import piltdown.literals as lit
import piltdown.util as util


def hdot_chart_line(datum: int) -> str:
    """Produce one line of a dot chart (without the label)."""
    return lit.HDOT_ONE * datum


def hdot_chart(data: List[int], labels: List[str] = lit.DEFAULT_LABELS) -> str:
    """Given a list of integers, plot a horizontal dot plot.

    Optional second argument is a list of labels. They will be
    converted to monospace, but in order for your table to line
    up you need to have the same number of characters in each,
    so space-pad the left end of your strings. Otherwise, take
    the defauly (A,B,C, etc.) and then write a key for your chart
    below the chart in your tweet.
    """
    if len(labels) < len(data):
        raise ValueError(("You don't have enough labels"))
    lines = []
    for label, datum in zip(labels, data):
        lines.append(util.fullwidth(label) + "|" + hdot_chart_line(datum))
    return "\n".join(lines)
