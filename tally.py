"""Unicode tally charts for Piltdown."""
from typing import Dict
import literals
import util

ONEZIE_TWOZIES = {
    0: "",
    1: literals.TALLY_ONE,
    2: literals.TALLY_TWO,
    3: literals.TALLY_THREE,
    4: literals.TALLY_FOUR,
}


def tally(data: Dict[str, int]):
    """Produce a tally chart.

    Given a dict of "label":value pairs, produce a tally chart with Unicode
    chars.
    """
    ret: str = ""
    for label, value in data.items():
        if all(key in literals.MONOSPACE for key in label):
            label = util.to_monospace(label)
        fives = value // 5
        ret += (
            label
            + util.to_monospace(":")
            + ((literals.TALLY_FIVE + literals.EMPTY_BLOCK) * fives)
        )
        ret += ONEZIE_TWOZIES[value - fives * 5] + "\n"
    return ret
