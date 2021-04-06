"""Global and shared variables for or potentially for any chart type."""
EMPTY_BLOCK = "　"

MONOSPACE_CHARS = (
    EMPTY_BLOCK
    + "０１２３４５６７８９"
    + "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    + "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    + "，．：；！？＂＇｀＾～＿＆＠＃％＋－＊＝＜＞（）［］｛｝￤／＼＄"
)
MONOSPACE_KEYS = (
    " "
    + "0123456789"
    + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    + "abcdefghijklmnopqrstuvwxyz"
    + ",.:;!?\"'`^~_&@#%+-*=<>()[]{}|/\\$"
)
MONOSPACE = dict(zip(MONOSPACE_KEYS, MONOSPACE_CHARS))


# When not supplied with a list of labels, we use these
LATIN_CHARS = "abcdefghijklmnopqrstuvwxyz"
GREEK_CHARS = "αβγδεζηθικλμνξοπρστυφχψω"
DEFAULT_LABELS = (
    LATIN_CHARS + GREEK_CHARS + LATIN_CHARS.upper() + GREEK_CHARS.upper()
)


# Win/Loss Sparklines
LOSS_CHAR = "▄"
WIN_CHAR = "▀"
ZERO_CHAR = "－"


EIGHT_EIGHTHS = "█"
EIGHTHS = {
    7: "▉",
    6: "▊",
    5: "▋",
    4: "▌",
    3: "▍",
    2: "▎",
    1: "▏",
}


TALLY_ONE = "𝍩"
TALLY_TWO = "𝍪"
TALLY_THREE = "𝍫"
TALLY_FOUR = "𝍬"
TALLY_FIVE = "ᚎ"

ONEZIE_TWOZIES = {
    0: "",
    1: TALLY_ONE,
    2: TALLY_TWO,
    3: TALLY_THREE,
    4: TALLY_FOUR,
}

DEFAULT3X5FONT = {
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
