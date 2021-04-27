"""Formatted (aligned) tables for Piltdown."""
from typing import List
import piltdown.literals as lit
import piltdown.util as util


def table(data: List[List[str]]) -> str:
    """Given a list of lists of strings produce a table.

    Each list will turn into a row. The nth item in each
    list will together form the nth column. Strings,
    including the first row, which you can use as column
    headers, will be converted to Unicode's "monospace"
    text, which will not work well with screen readers.

    The width of each column will be the maximum width
    of any entry of in that column.
    """
    # Let's be nice and convert any numbers to strings
    data = [list(map(str, row)) for row in data]
    # Get maximum length for each column
    lengths = [list(map(len, row)) for row in zip(*reversed(data))]
    maxes = list(map(max, lengths))
    maxes[-1] = maxes[-1] - 1  # No extra border padding for last column
    # Add spaces to pad cells
    for i, item in enumerate(data):
        for j, jtem in enumerate(data[i]):
            data[i][j] = jtem + (maxes[j] - len(jtem) + 1) * " "
    # Convert to monospace
    mono = [list(map(util.fullwidth, row)) for row in data]
    # Convert to a single string with newlines
    ret = ""
    for i in mono:
        ret += "".join(i) + "\n"
    return ret
