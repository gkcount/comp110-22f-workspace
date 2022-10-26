"""Testing utils functions. """

__author__ = "730221956"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_no_items() -> None:
    """Tests the only_evens function with no inputs and return should be empty"""
    odds: list[int] = list([])
    assert only_evens(odds) == []
    

def test_only_evens_one_item() -> None:
    """Tests the only_evens function if return should be one item."""
