"""Finding a min value in a list."""

def min(c: list[int]) -> int:
    """locating the min in a list."""
    i: int = 0
    smallest: int = c[0]

    while i < len(c):
        if smallest > c[i]:
            smallest = c[i]

        i = i + 1
    return smallest

print(min([]))


