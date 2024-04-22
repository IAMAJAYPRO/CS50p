from fuel import convert, gauge
import pytest


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert "%" in gauge(50)


def test_convert():
    assert convert("3/5") == 60
    with pytest.raises(ValueError):
        convert("E/F")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

