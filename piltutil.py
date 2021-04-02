"""General shared utilities for Piltdown."""
import piltdata


def to_monospace(string: str) -> str:
    """Monospace a string.

    Given a string of most of the ASCII character set, return a new
    analogous string composed of the Unicode "monospace" versions
    of the characters. These are really Asian font "full width" characters
    and will not play well with screen readers.
    """
    ret = ""
    for character in string:
        ret += piltdata.monospace[character]
    return ret
