"Practicing for exercise three."

def input_guess(number: int) -> str:     
    """The guess needs to be the correct length."""
    number: int
    word: str = ("")
    ("Enter a" + number + "character word: ")
    if number != word:
        print("That wasnt" + number + "chars! Try again: ")
    elif number == word:
        return(word)