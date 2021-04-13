"""General shared utilities for Piltdown."""
import literals


def to_monospace(string: str) -> str:
    """Monospace a string.

    Given a string of most of the ASCII character set, return a new
    analogous string composed of the Unicode "monospace" versions
    of the characters. These are really Asian font "full width" characters
    and will not play well with screen readers.
    """
    ret = ""
    for character in string:
        ret += literals.MONOSPACE[character]
    return ret


def bold(string: str) -> str:
    """Produce a fake bold string from Unicode math characters.

    Warning: Doesn't work with screen readers. Not really
    advised.
    """
    ret = ""
    for character in string:
        ret += literals.BOLD[character]
    return ret
