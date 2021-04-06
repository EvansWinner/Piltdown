"""Piltdown tests."""
import hbar_chart
import win_loss_sparkline


def test_hbar_line():
    """Basic smoke test of hbar_line with single example."""
    assert hbar_chart.hbar_line(6.34) == "██████▍"


win_loss_sparkline_test_data1 = [2.3, -3, -0.1, 2, 0, 67]


def test_win_loss_sparkline():
    """Basic smoke test of win/loss sparkline."""
    assert (
        win_loss_sparkline.win_loss_sparkline(win_loss_sparkline_test_data1)
        == "▀▄▄▀－▀"
    )
