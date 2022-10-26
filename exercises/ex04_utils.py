"""This program will help me better understand the list function."""

__author__ = "730221956"


def all(a: list[int], b: int) -> bool:
    """Is the integer True or False?"""
    i: int = 0
    
    while i < len(a):
        if a[i] != b:
            return False
        if len(a) == 0:
            return False
        i += 1
    return True
       

def max(c: list[int]) -> int:
    """Finding the biggest item in a list of values."""
    if len(c) == 0:
        raise ValueError("max () arg is an empty List")
    
    i: int = 0
    biggest: int = c[0]

    while i < len(c):
        if biggest < c[i]:
            biggest = c[i]
        i = i + 1
    return biggest


def is_equal(d: list[int], e: list[int]) -> bool:
    """Finding if every element at every index is equal in both lists."""
    i: int = [0]

    while i < len(d):
        if d[i] != e[i]:
            return False
            if len(d) == 0 and len(e) != 0:
                return False
            if len(e) > len(d):
                return False
            if len(d) > len(e):
                return False
        i = i + 1
    return True

print(is_equal([1, 0, 1], [1, 0, 1]))
