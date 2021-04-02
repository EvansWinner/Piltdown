import piltdata


def to_monospace(string):
    ret = ""
    for character in string:
        ret += piltdata.monospace[character]
    return ret
