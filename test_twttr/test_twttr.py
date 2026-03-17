from twttr import shorten

def test_shorten():
    assert shorten("murcielago") == "mrclg"
    assert shorten("MURCIELAGO") == "MRCLG"
    assert shorten("node123456789") == "nd123456789"
    assert shorten("modulo.lio") == "mdl.l"



