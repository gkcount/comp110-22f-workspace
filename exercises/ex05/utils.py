"""List utility funcitons exercise."""

__author__ = "730221956"

    
def only_evens(a: list[int]) -> list():
    """Print the even values in a list."""
    result: list[int] = list()
    for item in whole_list:
        if item % 2 == 0:
            result.append(item)
    return result


def sub(whole_list: list[int], start: int, end: int) -> list[int]:
    """List will return indices between the start and the end indices."""
    result: list[int] = list()
    if start < 0:
        start = 0
    if end > len(whole_list):
        end = len(whole_list)
    if start > end or end <= 0 or len(whole_list) == 1:
        return []
    while start < end:
        result.append(whole_list[start])
        start += 1
    return result

def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given the two different lists, the items of the first list will return then the items of the second list will return."""
    result: list[int] = list()
    for item in list_one:
        result.append(item)
    for item in list_two:
        result.append(item)
    return result
