import pytest
from um import count


def test_count():
    test_cases = [
        ("um", 1),
        ("um?", 1),

        ("Um, thanks, um...", 2)
    ]
    for case in test_cases:
        assert count(case[0]) == case[1]


def test_spaces():
    assert count(" um.. ,umm ") == 1



def test_diff_word():
    assert count(
        "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
