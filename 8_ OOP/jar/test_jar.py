from jar import Jar


def test_init():
    jar = Jar(23)
    assert jar.capacity == 23


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    assert str(jar) == ""
    jar.deposit(11)
    assert jar.size == 11


def test_withdraw():
    jar = Jar(12)
    assert str(jar) == ""
    jar.deposit(11)
    assert str(jar) == "🍪"*11

    jar.withdraw(7)
    assert jar.size == 4
