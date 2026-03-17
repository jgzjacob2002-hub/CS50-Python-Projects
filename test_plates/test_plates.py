from plates import is_valid

def test_correcto():
    assert is_valid("CS50") == True


def test_numero0():
    assert is_valid("CS05") == False
    assert is_valid(" CS50 ") == False


def test_al_final_letra():
    assert is_valid("CS50P") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("123456") == False


def test_puntos():
    assert is_valid("PI3.14") == False


def test_menos_2_letras():
    assert is_valid("H") == False
    assert is_valid("HS") == True


def test_muy_largo():
    assert is_valid("PARANGARICUTITIMICUARO") == False


def empieza_alfabeto():
    assert is_valid("???") == False

