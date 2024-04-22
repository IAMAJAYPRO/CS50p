from plates import is_valid


def test_():
    assert is_valid("CS50")


def test_length():
    assert is_valid("C2") is False
    assert is_valid("CS22345") is False


def test_without_num():
    assert is_valid("CSSP")

def test_numberpos():
    assert is_valid("CS23D") is False

def test_zero():
    assert is_valid("CS02") is False

def test_punctuation():
    assert is_valid("CS,1") is False

