"""Dictionary related utility functions."""

__author__ = "730221956"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}  
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(not_mutated: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new dictionary with N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in not_mutated:
        a_list: list[str] = not_mutated[column]
        end_result: list[str] = []
        i: int = 0
        if N > len(not_mutated):
            return not_mutated
        while i < N:
            end_result.append(a_list[i])
            i += 1
        result[column] = end_result
    return result


def select(origin: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Creates a new column-based table with a set number of columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = origin[column]
    return result


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Create a new column-based table by combining two column-based tables."""
    result: dict[str, list[str]] = {}
    for column in one:
        result[column] = one[column]
    for column in two:
        if column in result:
            result[column] += two[column]
        else:
            result[column] == two[column]
    return result


def count(list_one: list[str]) -> dict[str, int]:
    """Each key is a value in a given list, and each value is the number of times the value appeared into the input list."""
    result: dict[str, int] = {}
    for item in list_one:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result