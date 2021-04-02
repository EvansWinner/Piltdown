empty_block = "　"

monospace_chars = (
    empty_block
    + "０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ，．：；！？＂＇｀＾～＿＆＠＃％＋－＊＝＜＞（）［］｛｝￤／＼＄"
)
monospace_keys = " 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.:;!?\"'`^~_&@#%+-*=<>()[]{}|/\$"
monospace = dict(zip(monospace_keys, monospace_chars))


# When not supplied with a list of labels, we use these
latin_chars = "abcdefghijklmnopqrstuvwxyz"
greek_chars = "αβγδεζηθικλμνξοπρστυφχψω"
default_labels = (
    [x.upper() for x in latin_chars]
    + [x.upper() for x in greek_chars]
    + [x for x in latin_chars]
    + [x for x in greek_chars]
)


eight_eighths = "█"
eighths = {
    7: "▉",
    6: "▊",
    5: "▋",
    4: "▌",
    3: "▍",
    2: "▎",
    1: "▏",
}


tally_one = "𝍩"
tally_two = "𝍪"
tally_three = "𝍫"
tally_four = "𝍬"
tally_five = "ᚎ"

default3x5font = {
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
