barFull = ""
bar7_8th = ""
bar6_8th = ""
bar5_8th = ""
bar4_8th = ""
bar3_8th = ""
bar2_8th = ""
bar1_8th = ""
barSpace = ""  # Unicode full char width spacing char

# When not supplied with a list of labels, we use these
lat = "abcdefghijklmnopqrstuvwxyz"
grk = "αβγδεζηθικλμνξοπρστυφχψω"
defaultLabels = (
    [x.upper() for x in lat]
    + [x.upper() for x in grk]
    + [x for x in lat]
    + [x for x in grk]
)
