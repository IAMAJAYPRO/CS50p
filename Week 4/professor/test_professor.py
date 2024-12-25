import pytest
from unittest.mock import patch
from professor import main, get_level, generate_integer


@pytest.mark.parametrize("level, expected_range", [(1, (0, 9)), (2, (10, 99)), (3, (100, 999))])
def test_generate_integer(level, expected_range):
    generated_number = generate_integer(level)
    assert expected_range[0] <= generated_number <= expected_range[1]


def test_get_level(monkeypatch):
    user_inputs = ["-1", "0", "4", "foo", "2"]
    expected_output = [2]

    def mock_input(prompt):
        nonlocal user_inputs
        return user_inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    for expected in expected_output:
        assert get_level() == expected


# Add more test cases as needed
