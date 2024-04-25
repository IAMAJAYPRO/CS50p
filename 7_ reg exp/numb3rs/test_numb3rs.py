import pytest
from numb3rs import validate


def test_length():
    assert not validate("123.123.234")
    assert not validate("123.123.123.123.123")
    assert validate("192.168.0.1")


def test_nums():
    assert not validate("123.123.256.1")
    assert not validate("123.-4.234.1")


