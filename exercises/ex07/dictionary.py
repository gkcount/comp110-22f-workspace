"""Dictionary utils exercise."""

__author__ = "730221956"


def invert(backwards: dict[str, str]) -> dict[str, str]:
    """The keys become the values and the values become the keys."""
    result: dict[str, str] = {} 
    for key in backwards:
        if backwards[key] in result:
            raise KeyError("You cannot have multiple identical keys")
        result[backwards[key]] = key
    return result
    

def favorite_color(my_favorite_color: dict[str, str]) -> str:
    """Gives the color that appears most frequently."""
    frequent: str = ""
    i: int = 0
    a: dict[str, str] = {}
    for item in my_favorite_color:
        if my_favorite_color[item] in a:
            a[my_favorite_color[item]] += 1
        else:
            a[my_favorite_color[item]] = 1
    for color in my_favorite_color:
        if my_favorite_color[color] > i:
            i = my_favorite_color[color]
            frequent = color
    return frequent


def count(a_list: list[str]) -> (dict[str, int]):
    """Records the number of times each value is found in a list."""
    new_dictionary: dict[str, int] = {}
    i: int = 0
    while i < len(a_list):
        if a_list[i] in new_dictionary:
            new_dictionary[a_list[i]] += 1
        else:
            new_dictionary[a_list[i]] = 1
        i += 1
    return new_dictionary