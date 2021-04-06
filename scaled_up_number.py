"""Generate a large version of a number in a pseudo-monocode font."""
from typing import Dict, List
import literals


def scaled_up_number(
    number: str,
    font: Dict[str, List[str]] = literals.DEFAULT3X5FONT,
    leading_pad: int = 4,
) -> str:
    """Given a number as a string, produce a larger version of the number.

    Produce string as Unicode "ASCII" art.
    """
    try:  # try to coerce to string to be nice
        number = str(number)
    except ValueError:
        print("Can't coerce input to string.")
    ret: str = ""
    for line in range(len(font["0"])):
        ret += (leading_pad - 1) * literals.EMPTY_BLOCK
        for char in number:
            ret += literals.EMPTY_BLOCK + font[char][line]
        ret += "\n"
    return ret
