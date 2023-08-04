from working import convert
import pytest

def test_1Digit():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_2Digit():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_Error():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        assert convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        assert convert("9 to 5")
    with pytest.raises(ValueError):
        assert convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        assert convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        assert convert("12:60 AM to 5 PM")
    with pytest.raises(ValueError):
        assert convert("17:00 to 9 PM")
    with pytest.raises(ValueError):
        assert convert("11 am to 9 pm")