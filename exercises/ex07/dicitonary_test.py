"""This is where tests will occur for the dictionary assignment."""

import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_key_error() -> None:
    """An invalid input dictionary."""
    with pytest.raises(KeyError):
        test_input = {"what": "the", "what": "the"}
        invert(test_input)

def test_invert_use_1() -> None:
    """A test that shows the ideal function of invert."""
    test_input: dict[str, str] = {"1": "2", "3": "4", "5": "6"}
    expected_output: dict[str, str] = {"2": "1", "4": "3", "6": "5"}
    assert invert(test_input) == expected_output


def test_invert_use_2() -> None:
    """Another example of the ideal function of invert."""
    assert invert ({"your": "mom"}) == {"mom": "your"}


def test_favorite_color_1() -> None:
    """The color with the highest frequency will be the output."""
    a: dict[str, str] = {"Jeff": "purple", "Josie": "purple", "Steph": "blue"}
    assert favorite_color(a) == "purple"
    

def test_favorite_color_2() -> None:
    """An incorrect funcitoning of favorite color."""
    a: dict[str, str] = {"Grace": "pink", "Emma": "pink", "Cory": "purple", "Greer": "purple"}
    assert favorite_color(a) == "pink"


def test_favorite_color_3() -> None:
    """This test works with an empty dictionary."""
    a: dict[str, str] = {}
    assert favorite_color(a) == ""


def test_count_use() -> None:
    """Test with "w" as the most frequent."""
    a: list[str] = ["z", "y", "w", "w"]
    result_expected: dict[str,int] = {"z": 1, "y": 1, "w": 2}
    assert count(a) == result_expected


def test_count_use_1() -> None:
    """Test that uses the same item and repeats it."""
    a: list[str] = ["yep", "yep", "yep"]
    result_expected: dict[str, int] = {"yep": 3}
    assert count(a) == result_expected


def test_count_use_2() -> None:
    """Test with an empty list."""
    assert not count ([])
