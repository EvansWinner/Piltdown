"""Unicode tally charts for Piltdown."""
from typing import Dict
import piltdata
import piltutil

ONEZIE_TWOZIES = {
    0: "",
    1: piltdata.TALLY_ONE,
    2: piltdata.TALLY_TWO,
    3: piltdata.TALLY_THREE,
    4: piltdata.TALLY_FOUR,
}


def tally(data: Dict[str, int]):
    """Produce a tally chart.

    Given a dict of "label":value pairs, produce a tally chart with Unicode
    chars.
    """
    ret: str = ""
    for label, value in data.items():
        if all(key in piltdata.MONOSPACE for key in label):
            label = piltutil.to_monospace(label)
        fives = value // 5
        ret += (
            label
            + piltutil.to_monospace(":")
            + ((piltdata.TALLY_FIVE + piltdata.EMPTY_BLOCK) * fives)
        )
        ret += ONEZIE_TWOZIES[value - fives * 5] + "\n"
    return ret
