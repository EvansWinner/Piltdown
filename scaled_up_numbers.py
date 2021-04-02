from typing import Dict, List
import piltdata


def scaled_up_number(
    number: str,
    font: Dict[str, List[str]] = piltdata.default3x5font,
    leading_pad: int = 4,
) -> str:
    try:  # try to coerce to string to be nice
        number = str(number)
    except:
        print("Can't coerce input to string.")
    ret = ""
    for line in range(len(font["0"])):
        ret += (leading_pad - 1) * piltdata.empty_block
        for char in number:
            ret += piltdata.empty_block + font[char][line]
        ret += "\n"
    return ret
