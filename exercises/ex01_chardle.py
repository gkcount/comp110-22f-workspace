"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730221956"

term: str = str(input("Enter a 5-character word: "))
if len(term) > 5 or len(term) < 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = str(input("Enter a single character: "))
if len(letter) > 1 or len(letter) < 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + term)

number = int = 0
if term[0] == letter:
    print(letter + " found at index 0")
    number = number + 1
if term[1] == letter:
    print(letter + " found at index 1")
    number = number + 1
if term[2] == letter:
    print(letter + " found at index 2")
    number = number + 1
if term[3] == letter:
    print(letter + " found at index 3")
    number = number + 1
if term[4] == letter:
    print(letter + " found at index 4")
    number = number + 1
if number == 0:
    print("No instances of " + letter + " found in " + term)
if number == 1:
    print(str(number) + " intance of " + letter + " found in " + term)
if number > 1:
    print(str(number) + " intances of " + letter + " found in " + term)