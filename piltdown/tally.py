"""Unicode tally charts for Piltdown."""
from typing import Dict
import piltdown.literals as lit
import piltdown.util as util


def tally(data: Dict[str, int]):
    """Produce a tally chart.

    Given a dict of "label":value pairs, produce a tally chart with Unicode
    chars.
    """
    ret: str = ""
    for label, value in data.items():
        if all(key in lit.FULLWIDTH for key in label):
            label = util.fullwidth(label)
        fives = value // 5
        ret += (
            label
            + util.fullwidth("|")
            + ((lit.TALLY_FIVE + lit.EMPTY_BLOCK) * fives)
        )
        ret += lit.ONEZIE_TWOZIES[value - fives * 5] + "\n"
    return ret
