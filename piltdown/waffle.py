"""Waffle charts for Piltdown."""
from typing import List
import math
import piltdown.literals as lit


def waffle(
    data: List[int],
    categories: List[str],
    glyphs: str = lit.WAFFLES,
    layout: List[int] = [0, 0],
    ltor: bool = True,
) -> str:
    """Produce a waffle chart.

    Charts that use 9 or fewer categories (strongly recommended)
    can use the default set of glyphs. Otherwise pass a string of
    single Unicode characters and they will be used in order.
    Categories should be a list of strings for the key. Layout is
    a tuple of two integers: preffered (width,height). Zero mean
    calculate based on the other value. Two zeros (the default)
    means try to get as close to a square as possible. ltor
    (default True) means fill in glyphs staeting top-left and going
    left to right,then down rows. False means start at the same
    place but fill down to the bottom abd then by column.
    """
    if len(data) != len(categories): raise ValueError("Data/categories length mismatch")
    if len(data) > len(glyphs):
        raise ValueError("Not enough glyphs")
    if layout == [0, 0]:
        layout[0] = int(round(math.sqrt(sum(data))))
        layout[1] = layout[0]
    if (
        layout[0] * layout[1] >= sum(data) + layout[0] + layout[1]
        or layout[0] * layout[1] <= sum(data) - layout[0] - layout[1]
    ):
        raise ValueError("Layout not consistent with data length")
    # Get glyphs as a bare string.
    chars = ""
    for i, value in enumerate(data):
        for j in range(value):
            chars += glyphs[i]
    # Convert to a list of lists, with each sublist corresponding to
    # a line of output
    listed = [
        list(chars)[i * layout[0] : (i + 1) * layout[0]]
        for i in range((len(list(chars)) + layout[0] - 1) // layout[0])
    ]
    # Reverse every other line, as that is how the glyphs fill into
    # the block, switching direction every row.
    for i in range(0, len(listed), 2):
        listed[i].reverse()
    # Rotate the block if the user asked for that.
    if ltor == False:
        listed = list(map(list, zip(*reversed(listed))))
    # Convert back to a string with a newline at the end of each
    # sublist
    for i in listed:i.append("\n")
    ret = ""
    for i in listed:
        for j in i:
            ret+=j
    # Add key underneath
    key="\n"
    for i, cat in enumerate(categories):
        key+=glyphs[i] + " = " + cat
        if i !=len(categories)-1:key+="; "
    key+="\n"
    ret+=key
    return ret


print(waffle([2, 3, 5, 7, 9, 11], ["A", "B", "C", "D", "E", "F"],ltor=False))
