from typing import List
import piltdown.literals as lit
import piltdown.util as util


def dot_chart(data: List[int], labels: List[str] = lit.DEFAULT_LABELS) -> str:
    """Given a list of values, plot a vertical dot chart.

    Second argument is a list of labels. Labels should be
    a single alphanumeric character, as they can only occupy
    one character space to line up with the chart columns. Add
    a key ad lib under your chart if you want one.
    """
    lines = []
    for label, number in zip(labels, data):
        maximum_length = max(data) + 1
        line = util.fullwidth(label)
        line += lit.DOT_ONE * number
        line += lit.EMPTY_BLOCK * (maximum_length - len(line))
        lines.append(line)
    lines = list(map(list, zip(*lines[::-1][::-1])))
    lines = lines[::-1]
    ret = "\n"
    for line in lines:
        ret += "".join(line) + "\n"
    return ret
