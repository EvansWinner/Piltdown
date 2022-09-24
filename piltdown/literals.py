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
    + "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
    + "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
    + "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
)

MONOSPACE_KEYS: str = (
    "\n" 
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
    + "𝛂𝛃𝛄𝛅𝛆𝛇𝛈𝛉𝛊𝛋𝛌𝛍𝛎𝛏𝛐𝛑𝛒𝛔𝛕𝛖𝛗𝛘𝛙𝛚"
    + "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟬"
)

BOLD: Dict[str, str] = dict(zip(BOLD_KEYS, BOLD_CHARS))


# Win/Loss Sparklines
LOSS_CHAR: str = "▄"
WIN_CHAR: str = "▀"
ZERO_CHAR: str = "－"

# Horizontal bar charts
EIGHT_EIGHTHS: str = "█"
ZERO_EIGHTHS: str = "⠀" # Not a regular space char
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
BLOCK_RED    = "🟥"
BLOCK_BLUE   = "🟦"
BLOCK_ORANGE = "🟧"
BLOCK_YELLOW = "🟨"
BLOCK_GREEN  = "🟩"
BLOCK_PURPLE = "🟪"
BLOCK_BROWN  = "🟫"
BLOCK_BLACK  = "⬛"
BLOCK_WHITE  = "⬜"

# Dot matrix plots
CIRCLE_RED    = "🔴"
CIRCLE_BLUE   = "🔵"
CIRCLE_ORANGE = "🟠"
CIRCLE_YELLOW = "🟡"
CIRCLE_GREEN  = "🟢"
CIRCLE_PURPLE = "🟣"
CIRCLE_BROWN  = "🟤"
CIRCLE_BLACK  = "⚫"
CIRCLE_WHITE  = "⚪"

WAFFLES_GRAYSCALE = "▩▥▦▤▧▨▣"
WAFFLES_COLOR = BLOCK_RED + BLOCK_BLUE + BLOCK_YELLOW + BLOCK_PURPLE +\
    BLOCK_BROWN + BLOCK_GREEN + BLOCK_ORANGE + BLOCK_BLACK + BLOCK_WHITE
DOTMATRIX = CIRCLE_RED + CIRCLE_BLUE + CIRCLE_ORANGE + CIRCLE_YELLOW +\
    CIRCLE_GREEN + CIRCLE_PURPLE + CIRCLE_BROWN + CIRCLE_BLACK + CIRCLE_WHITE

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

# Misc unicode things
SPACE_FULLWIDTH = "　"
SMILEY = "☺"
FROWNIE = "☹"
STAR = "★"
HARVEY_BALL_THREE_QUARTER = "◕"
HARVEY_BALL_EMPTY = "⭘"
HARVEY_BALL_FULL = "⬤"
HARVEY_BALL_ONE_QUARTER = "◔"
HARVEY_BALL_TOP_HALF = "◓"
HARVEY_BALL_BOTTOM_HALF = "◒"
HARVEY_BALL_RIGHT_HALF = "◑"
HARVEY_BALL_LEFT_HALF = "◐"
CHECKMARK = "✓"
POINTING_FINGER_RIGHT = "☞"
BOX_FILLED = "◼"
BOX = "◻"
PIE_UPPER_LEFT = "◷"
PIE_LOWER_LEFT = "◶"
PIE_LOWER_RIGHT = "◵"
PIE_UPPER_RIGHT = "◴"
CIRCLE_LARGE = "◯"
BULLET_POINT_OPEN = "◦"
BULLET_POINT_CLOSED = "•"


