"""One shot wordle."""

__author__ = "730221956"



WORDLE: str = str("python")
Character_number: int = len(WORDLE)
Estimate: str = str (input ("What is your " + str(Character_number) + " letter guess?"))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(Estimate) != Character_number:
    Estimate = input(f"That was not (Number_of_characters) letters! Try again: ")
i: int = 0

outcome: str = str("")
while i < Character_number:
    if WORDLE[i] == Estimate[i]:
        outcome += GREEN_BOX
    else:
        check: int = 0
        inspecting: bool = True
        while check < Character_number and inspecting:
            if WORDLE[check] == Estimate[i]:
                outcome += YELLOW_BOX
                inspecting = False
            check += 1
        if inspecting:
            outcome += WHITE_BOX
    i += 1
print(outcome)
if Estimate == WORDLE:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")




