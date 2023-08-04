from bank import value

def test_value_0():
    assert value("Hello") == 0
    assert value("hello there") == 0
    assert value("Hello, there") == 0
    assert value("hello123") == 0


def test_value_20():
    assert value("Hola") == 20
    assert value("Hola, buddy") == 20
    assert value("Happy birthday") == 20
    assert value("Happy birthday 2 u") == 20


def test_value_100():
    assert value("Yo") == 100
    assert value("Yo there") == 100
    assert value("Yo, There") == 100
    assert value("Yo there 123") == 100
