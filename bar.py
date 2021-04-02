from typing import Dict, List
import piltdata
import piltutil


def max_bar_width(d: Dict[str, float], w: int) -> int:
    return w - max(list(map(len, d.keys())))


# def make_line(lab:str,v:float,lineBreak:bool,keyLabels)->str:


def bar(
    d: Dict[str, float],
    w: int,
    line_breaks: bool = False,
    key_labels: List[str] = piltdata.default_labels,
) -> str:
    """Return a bar plot given a dict d of {"Label":value} pairs and max line width, w."""
    ret = ""
    for l, v in d.items():
        ret += make_line(l, v, line_breaks, key_labels)
    return ret
