"""This program will help me better understand the list function."""

__author__ = "730221956"

def all(a: list[int], b: int ) -> bool:
    while a == b:
        return True
    else: 
        return False

def max(c: list[int]) -> int:
    """Finding the biggest item in a list of values."""
    if len(c) == 0:
        raise ValueError("max () arg is an empty List")
    i: int = 0
    biggest: int = 0
    #establish i so that the while loop can run
    while i < len(c):
        if biggest < c[i]:
            biggest = c[i]
        #return the largest value in a list
        #if the list is empty return value error
        i = i + 1
    return biggest

def is_equal(List_one: list[int], list_two: list[int]) -> bool:
    """finding if every element at every index is equal in both lists."""
    i: int = 0
    
    while i < len(List_one) and len(list_two):
        if List_one[i] != list_two[i]:
            return False
            
        i = i + 1
    return True

print(is_equal([1,0,1], [1,0,1]))
print(is_equal([1,0,1], [1,1,0]))