from working import convert
import pytest

def test_convert():
    assert convert(r"9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert(r"9 AM to 5 PM") == "09:00 to 17:00"
    assert convert(r"12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert(r"12:00 PM to 12:00 AM") == "12:00 to 00:00"

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM 17:00 PM")
