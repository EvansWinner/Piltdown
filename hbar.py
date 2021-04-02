import math
import piltdata


def mkbar(
    len,
    eighths=piltdata.eighths,
    eight_eighths=piltdata.eight_eighths,
    empty=piltdata.empty_block,
):
    ret = ""
    rounded = round(len * 8) / 8
    ret = eight_eighths * math.floor(rounded)
    ret += eighths[(rounded - math.floor(rounded)) * 8]
    return ret


print(mkbar(6.34))
print(mkbar(3.45))
print(mkbar(7.93))
