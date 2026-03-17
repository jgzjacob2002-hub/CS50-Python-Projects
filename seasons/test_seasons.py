from seasons import cumpleanos
import pytest



def test_cumpleanos():
    with pytest.raises(SystemExit):
        cumpleanos("Invalid date")

def cumpleanos_hoyyy_cambia_dia():
    assert cumpleanos("2002-09-08") == "Twelve million, seventy-one thousand, five hundred twenty minutes"

