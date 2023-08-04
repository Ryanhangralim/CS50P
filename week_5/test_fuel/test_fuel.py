from fuel import convert, gauge
import pytest


def test_value_error():
    with pytest.raises(ValueError):
        assert convert("3/2")
        assert convert("4/2")
        assert convert("Cat/Dog")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("-3/0")
        assert convert("-4/0")


def test_convert():
    assert convert("1/2") == 50


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
