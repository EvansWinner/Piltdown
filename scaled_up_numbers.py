from typing import Dict, List
import piltdata

emptyBlock = "　"


def scaled_up_number(
    number: str,
    font: Dict[str, List[str]] = piltdata.default3x5font,
    leadingPad: int = 4,
) -> str:
    try:  # try to coerce to string to be nice
        number = str(number)
    except:
        print("Can't coerce input to string.")
    ret = ""
    for line in range(len(font["0"])):
        ret += (leadingPad - 1) * piltdata.emptyBlock
        for char in number:
            ret += piltdata.emptyBlock + font[char][line]
        ret += "\n"
    return ret
