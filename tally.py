import piltdata
import piltutil

onzie_twozies = {
    0: "",
    1: piltdata.tally_one,
    2: piltdata.tally_two,
    3: piltdata.tally_three,
    4: piltdata.tally_four,
}


def tally(data):
    ret = ""
    for label, value in data.items():
        if all(key in piltdata.monospace for key in label):
            label = piltutil.to_monospace(label)
        fives = value // 5
        ret += (
            label
            + piltutil.to_monospace(":")
            + ((piltdata.tally_five + piltdata.empty_block) * fives)
        )
        ret += onzie_twozies[value - fives * 5] + "\n"
    return ret


print(tally({"av": 24, " b": 13}))
