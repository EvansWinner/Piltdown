"""Win/Loss sparkline for Piltdown."""

from typing import List
import piltdown.literals as lit


def win_loss_one(number: float) -> str:
    """Return appropriate win/loss character for a single scaler."""
    if number == 0:
        return lit.ZERO_CHAR
    if number < 0:
        return lit.LOSS_CHAR
    return lit.WIN_CHAR


def win_loss_sparkline(values: List[float]) -> str:
    """Produce a win/loss sparkline in Unicode given a list of values."""
    return "".join(list(map(win_loss_one, values)))
