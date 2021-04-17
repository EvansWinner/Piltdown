"""General shared utilities for Piltdown."""
import piltdown.literals as lit


def to_monospace(string: str) -> str:
    """Monospace a string.

    Given a string of most of the ASCII character set, return a new
    analogous string composed of the Unicode "monospace" versions
    of the characters. These are really Asian font "full width" characters
    and will not play well with screen readers.
    """
    ret = ""
    for character in string:
        ret += lit.MONOSPACE[character]
    return ret


def bold(string: str) -> str:
    """Produce a fake bold string from Unicode math characters.

    Warning: Doesn't work with screen readers. Not really
    advised.
    """
    ret = ""
    for character in string:
        ret += lit.BOLD[character]
    return ret


def cut_above() -> str:
    """Return a "cut before this line" line."""
    return "\n`--Cut before this line--'\n"


def cut_below() -> str:
    """Return a "cut after this line" line."""
    return "\n.--Cut after this line --.\n" 


def with_cut_lines(string:str)->str:
    """Wrap a string in cut lines."""
    return cut_below() + string + cut_above()


def with_char_count(string:str)->str:
    """Return whatever string is passed.
   
       Unless that string is longer than 280 characters."""
    if len(string) <= 280:
        return string
    else:
        return "String too long to post on Twitter"
