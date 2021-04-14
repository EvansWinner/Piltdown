"""Global and shared variables for or potentially for any chart type."""
from typing import Dict, List

EMPTY_BLOCK: str = "　"

CHAR_KEYS: str = (
    " "
    + "0123456789"
    + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    + "abcdefghijklmnopqrstuvwxyz"
    + ",.:;!?\"'`^~_&@#%+-*=<>()[]{}|/\\$"
)

MONOSPACE_CHARS: str = (
    EMPTY_BLOCK
    + "０１２３４５６７８９"
    + "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    + "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    + "，．：；！？＂＇｀＾～＿＆＠＃％＋－＊＝＜＞（）［］｛｝￤／＼＄"
)

MONOSPACE: Dict[str, str] = dict(zip(CHAR_KEYS, MONOSPACE_CHARS))

BOLD_CHARS: str = ""

BOLD: Dict[str, str] = dict(zip(CHAR_KEYS, BOLD_CHARS))

# When not supplied with a list of labels, we use these
LATIN_CHARS: str = "abcdefghijklmnopqrstuvwxyz"
GREEK_CHARS: str = "αβγδεζηθικλμνξοπρστυφχψω"
DEFAULT_CHARS: str = (
    LATIN_CHARS.upper() + GREEK_CHARS.upper() + LATIN_CHARS + GREEK_CHARS
)
DEFAULT_LABELS: List[str] = list(DEFAULT_CHARS)

# Win/Loss Sparklines
LOSS_CHAR: str = "▄"
WIN_CHAR: str = "▀"
ZERO_CHAR: str = "－"

# Horizontal bar charts
EIGHT_EIGHTHS: str = "█"
EIGHTHS: Dict[int, str] = {
    7: "▉",
    6: "▊",
    5: "▋",
    4: "▌",
    3: "▍",
    2: "▎",
    1: "▏",
}


# Tally charts
TALLY_ONE: str = "𝍩"
TALLY_TWO: str = "𝍪"
TALLY_THREE: str = "𝍫"
TALLY_FOUR: str = "𝍬"
TALLY_FIVE: str = "ᚎ"

ONEZIE_TWOZIES: Dict[int, str] = {
    0: "",
    1: TALLY_ONE,
    2: TALLY_TWO,
    3: TALLY_THREE,
    4: TALLY_FOUR,
}

# Dot charts
HDOT_ONE: str = "⚫"
DOT_ONE: str = "＊"

# Scaled up numbers
DEFAULT3X5FONT: Dict[str, List[str]] = {
    "%": [
        "█░▞",
        "░▐░",
        "░▞░",
        "░▌░",
        "▞░█",
    ],
    "0": [
        "░█▙",
        "█░█",
        "█░█",
        "█░█",
        "▜█░",
    ],
    "1": [
        "░█░",
        "▞█░",
        "░█░",
        "░█░",
        "▗█▖",
    ],
    "2": [
        "▄▆▖",
        "▘░▛",
        "░▞░",
        "▐░░",
        "█▄▟",
    ],
    "3": [
        "▟▀▙",
        "░░█",
        "░█░",
        "░░█",
        "▜▄▛",
    ],
    "4": [
        "░░▟",
        "░▞█",
        "▟▄█",
        "░░█",
        "░░█",
    ],
    "5": [
        "▛▀▜",
        "▌░░",
        "█▀▙",
        "░░▐",
        "█▄▛",
    ],
    "6": [
        "▄▀▙",
        "█░░",
        "██▙",
        "█░█",
        "▜█▛",
    ],
    "7": [
        "▛▀█",
        "░░▛",
        "░▞░",
        "▐░░",
        "█░░",
    ],
    "8": [
        "▟█▙",
        "█░█",
        "███",
        "█░█",
        "▜█▛",
    ],
    "9": [
        "▟█▙",
        "█░█",
        "▜██",
        "░░█",
        "▗█▘",
    ],
    ",": [
        "░░░",
        "░░░",
        "░░░",
        "░░░",
        "░▜░",
    ],
    ".": [
        "░░░",
        "░░░",
        "░░░",
        "░░░",
        "░▖░",
    ],
}
