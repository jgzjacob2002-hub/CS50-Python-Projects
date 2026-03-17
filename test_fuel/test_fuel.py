import pytest

from fuel import convert, gauge


def test_porcentajes():
    assert convert("2/3") == 67
    assert convert("1/4") == 25

def test_fuel():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("dog/cat")
    with pytest.raises(ValueError):
        convert("6/5")
    with pytest.raises(ValueError):
        convert("-4/2")

