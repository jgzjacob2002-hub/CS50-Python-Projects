from jar import Jar
import pytest

def test_init():
    jar= Jar(4)
    assert jar.capacity == 4
    jar = Jar(6)
    assert jar.capacity == 6


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(4)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(6)



def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(6)
