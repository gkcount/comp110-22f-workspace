"""Tests for the sum function."""

# first thing we need to do is to import the function
from lessons.sum import sum

# first test function
# these are parameterless functions
# asserions- something that needs to be true based on how we expect this program to behave
def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum([]) == 0.0

def test_sum_single_item() -> None:
    xs: list[float] = 110.0
    assert sum([110.0])

def test_sum_many_items() -> None:
    xs: list[float]= [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0 


def test_sum_many_items_again() -> None:
    assert sum ([-1.0, 1.0, -2.0, 2.0]) == 0.0

def test_another_sum() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0

def test_another_sum_single_item() -> None:
    xs: list[float] == 110.0
    assert sum([110.0])