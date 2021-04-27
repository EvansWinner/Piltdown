"""Global and shared variables for or potentially for any chart type."""
from typing import Dict, List

EMPTY_BLOCK: str = "　"

LATIN_CHARS: str = "abcdefghijklmnopqrstuvwxyz"
GREEK_CHARS: str = "αβγδεζηθικλμνξοπρστυφχψω"
DIGITS = "0123456789"

# When not supplied with a list of labels, we use these
DEFAULT_CHARS: str = (
    LATIN_CHARS.upper() + GREEK_CHARS.upper() + LATIN_CHARS + GREEK_CHARS
)

DEFAULT_LABELS: List[str] = list(DEFAULT_CHARS)

FULLWIDTH_KEYS: str = (
    " "
    + DIGITS
    + LATIN_CHARS.upper()
    + LATIN_CHARS
    + ",.:;!?\"'`^~_&@#%+-*=<>()[]{}|/\\$"
)

FULLWIDTH_CHARS: str = (
    EMPTY_BLOCK
    + "０１２３４５６７８９"
    + "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    + "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    + "，．：；！？＂＇｀＾～＿＆＠＃％＋－＊＝＜＞（）［］｛｝￤／＼＄"
)

FULLWIDTH: Dict[str, str] = dict(zip(FULLWIDTH_KEYS, FULLWIDTH_CHARS))

MONOSPACE_CHARS: str = (
    "\n"
    + " "
    + "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
    + "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
    + "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
)

MONOSPACE_KEYS: str = (
    "\n" 
    + " " # This is not a normal space character!
    + LATIN_CHARS.upper()
    + LATIN_CHARS
    + DIGITS
)

MONOSPACE: Dict[str, str] = dict(zip(MONOSPACE_KEYS, MONOSPACE_CHARS))

BOLD_KEYS: str = LATIN_CHARS.upper() + LATIN_CHARS + GREEK_CHARS.upper() + GREEK_CHARS + DIGITS

BOLD_CHARS: str = (
    "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙"
    + "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳"
    + "𝚨𝚩𝚪𝚫𝚬𝚭𝚮𝚯𝚰𝚱𝚲𝚳𝚴𝚵𝚶𝚷𝚸𝚺𝚻𝚼𝚽𝚾𝚿𝛀"
    + "𝛂𝛃𝛄𝛅𝛆𝛇𝛈𝛉𝛊𝛋𝛌𝛍𝛎𝛏𝛐𝛑𝛒𝛓𝛔𝛕𝛖𝛗𝛘𝛙𝛚"
    + "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟬"
)

BOLD: Dict[str, str] = dict(zip(BOLD_KEYS, BOLD_CHARS))


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
    0: "",
}

# Waffle charts
WAFFLES = "▩▥▦▤▧▨▣"


# Column sparklines
V8THS = {
    0: EMPTY_BLOCK,
    1: "▁",
    2: "▂",
    3: "▃",
    4: "▄",
    5: "▅",
    6: "▆",
    7: "▇",
    8: "█",
}

# Xs and checks
X = "✗"
CHECK = "✓"


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
