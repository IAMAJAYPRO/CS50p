import pytest
from twttr import shorten



def test_vowel():
    assert shorten("hello") == "hll"

def test_upper():
    assert shorten("hEll") == "hll"
def test_lower():
    assert shorten("ello") == "ll"
def test_numeber():
    assert shorten("hello123") == "hll123"
def test_vowel():
    assert shorten("hello") == "hll"
def test_punctuation():
    assert shorten("hel,lo") == "hl,l"
    # Add more test cases as needed
