from jar import Jar
import pytest

def test_init():
    jar = Jar(12)
    assert jar.capacity == 12


def test_str():
    jar = Jar(12)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(12)
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar(12)
    jar.deposit(5)
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(5)