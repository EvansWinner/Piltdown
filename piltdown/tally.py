"""Unicode tally charts for Piltdown."""
from typing import Dict
import literals
import util


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
        ret += literals.ONEZIE_TWOZIES[value - fives * 5] + "\n"
    return ret


print(tally({"a": 65, "g": 33}))
