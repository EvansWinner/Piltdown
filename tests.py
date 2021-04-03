"""Piltdown tests."""
from bar_chart import bar_chart
from hbar_chart import hbar_line


def test_hbar_line():
    """Test hbar_line with single example."""
    assert hbar_line(6.34) == "██████▍"


bar_chart({"a": 1, "b": 2}, 10)
