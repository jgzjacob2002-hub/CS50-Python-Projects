from bank import value

def test_value():
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100

def test_H():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
