"""This program will help me better understand the list function."""

__author__ = "730221956"

def all(a: list[int], b: int ) -> bool:
    """Is the integer True or False?"""
    i: int = 0 
    while a != b:
        return False
    else: 
        return True
    i = i + 1

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


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Finding if every element at every index is equal in both lists."""
    i: int = [0]
   
    while i < len(list_one) and len(list_two):
        if list_one[i] != list_two[i]:
            return False    
        return True
        i = i + 1

