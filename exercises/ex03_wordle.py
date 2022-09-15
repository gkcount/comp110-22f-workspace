"""Creating a structured wordle."""

__author__ = "730221956"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, letter: str) -> bool:
    """Determines whether a character is found within the first string."""
    assert len(letter) == 1
    i: int = 0
    while i < len(word): 
        if letter == word[i]:
            return True
        i+=1
    return False
    

def emojified(guess: str, secret: str) -> str:
    """Assigns emoji's to string guesses."""
    assert len(guess) == len(secret)
    a: int = 0 
    result: str = ""
    while a < len(secret):
        if guess[a] == secret[a]:
            result += GREEN_BOX
        elif contains_char(secret,guess[a]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        a += 1
    return str(result)

def input_guess(number: int) -> str:  
    """Matches the character count to the number inputted."""   
    guess: str = (input(f"Enter a {number} character word: "))
    while len(guess) != number:
        guess = input(f"That wasn't {number} chars! Try again: ")
    assert len(guess) == number
    return guess

def main() -> None:
    """This is where the program enters."""
    SECRET: str = "codes"
    win: bool = False
    turn: int = 1
    while turn <= 6 and not win:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(SECRET))
        print(emojified(guess, SECRET))
        if guess == SECRET:
            print(f"You won in {turn}/6 turns!")
            win = True
        turn += 1
    if not win:
        print("x/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()