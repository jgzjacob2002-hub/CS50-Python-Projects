from numb3rs import validate



def test_correcto():
    assert validate(r"256.255.255.255") == False
    assert validate(r"255.255.255.255") == True
    assert validate(r"255.256.255.255") == False
    assert validate(r"255.255.256.255") == False
    assert validate(r"255.255.255.256") == False


def test_numero0():
    assert validate("256.255.255") == False
    assert validate("256.255") == False
    assert validate("256") == False
    assert validate("2.3.3.3") == True
    assert validate("89.65.45.55.54") == False
