"""General shared utilities for Piltdown."""
import piltdown.literals as lit


def fullwidth(string: str) -> str:
    """Sort of monospace a string.

    Given a string of most of the ASCII character set, return a new
    analogous string composed of the Unicode fullwidth versions
    of the characters. These are really Asian font "full width" characters
    and will not play well with screen readers. But they are a way
    to fake monospace that has some punctuation characters (unlike the
    mathematical monospace set (see function `monospace` but they
    have the disadvantage of being very wide, and not many will fit in
    a tweet.
    """
    ret = ""
    for character in string:
        ret += lit.FULLWIDTH[character]
    return ret


def bold(string: str) -> str:
    """Produce a fake bold string from Unicode math characters.

    Warning: Doesn't work with screen readers. Not really
    advised. Characters that are not in the set of Unicode mathematical
    bold will just be passed into the return string unchanged. For 
    punctuation and space characters, this doesn't seem to matter too
    much.
    """
    ret = ""
    for character in string:
        if character in lit.BOLD.keys():
            ret += lit.BOLD[character]
        else:
            raise ValueError("Character not present in Unicode mathematical bold")
    return ret


def monospace(string:str) -> str:
    """Produce a fake monospace string from Unicode math characters.

       Only Arabic digits and capital and miniscule Latin characters
       are covered, and anything else will ruin alignment in a tweet,
       so if you try to pass anything else in your string (including,
       for example, punctuation characters and spaces) you will get an
       error. Try the `fulwidth` function instead, which has more
       characters, but makes the result much wider.
    """
    ret = ""
    for character in string:
        if character in lit.MONOSPACE.keys():
            ret += lit.MONOSPACE[character]
        else:
            raise ValueError("Character not present in Unicode mathematical monospace")
    return ret

def cut_above() -> str:
    """Return a "cut before this line" line."""
    return "\n`--Cut before this line--'\n"


def cut_below() -> str:
    """Return a "cut after this line" line."""
    return "\n.--Cut after this line --.\n"


def with_cut_lines(string: str) -> str:
    """Wrap a string in cut lines."""
    return cut_below() + string + cut_above()


def with_char_count(string: str) -> str:
    """Return whatever string is passed.

    Unless that string is longer than 280 characters."""
    if len(string) <= 280:
        return string
    else:
        return "String too long to post on Twitter"


def bold(string: str) -> str:
    """Convert a string of alphanumerics to Unicode fake bold.

    String can include upper- or lower-case Latin or Greek
    characters and digits 0-9. Result uses mathemcatical
    bold characters from Unicode, so they won't be friendly
    to screen readers."""
    ret = ""
    for char in string:
        if char in lit.BOLD:
            ret += lit.BOLD[char]
        else:
            ret += char
    return ret
