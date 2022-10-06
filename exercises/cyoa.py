"""An adventure program."""

__author__ = "730221956"

points: int 
player: str
import random


def main() -> None:
    """Calls main at the end of the program."""
    global player
    global points
    greet()
    quiz_type = int(input("To determine which quiz you are going to take, enter either the number 1, 2, or 3: "))
    if quiz_type == 1:
        personality_quiz_one()
    if quiz_type == 2:
        personality_quiz_two()
    if quiz_type == 3:
        print("Your experience is ended, Goodbye for now!")
        exit()


def greet() -> None:
    """Welcome the participant to the quiz."""
    global player
    print("Welcome to the quiz!")
    print("This quiz will tell you which emoji best represents you!")
    player = str(input("What is your name?"))
    print(f"{player} let's figure out which emoji you are.")


def personality_quiz_one() -> None:
    """Asking the player for additional input."""
    global player
    global points
    print(f"Welcome {player}!")
    print(f"{player}, what is your favorite color")
    color = str(input("What is your favorite color?"))
    points = 0

    if len(color) >= 6:
        print("Wow, that is a really interesting color!")
        points += 4
    if len(color) == 0:
        print("That is not a color, Try again.")
        points += 0
    if len(color) > 0 and len(color) < 6:
        print(f"This is a solid color {player}")
        points += 2
    
    
    print("Respond 1 for True and 2 for False to the next three questions.")
    print(input("You are a morning person."))
    trueorfalse = input()
    if trueorfalse == 1:
        points += 1
    if trueorfalse == 2:
        points += 2
   
    print(input("(2/3: True or False) You love to drink water."))
    true_or_false = input()
    if true_or_false == 1: 
        points += 2
    if true_or_false == 2:
        points += 1

    print(input("(3/3: True or False) You like to clean. "))
    t_or_f = input()
    if t_or_f == 1: 
        points += 2
    if t_or_f == 2: 
        points += 1
    
    points_calculator()


def personality_quiz_two() -> None:
    """The second adventure option."""
    global points
    print(f"Welcome to Personality quiz two {player}!")
    print(input("What is your favorite season?"))
    season: str(input("What is your favorite season?"))
    if len(season) == 6:
        print("Great choice!")
        points += 6
    if len(season) == 4:
        print("The fall is a lovely time.")
        points += 4   
    print(f"Okay, {player}, now for the real questions.")

    print("For this next section, you will input 1 for True or 2 for False.")
    
    print(input("I drink coffee everyday."))
    answer = input()
    if answer == 1:
        print("Caffeine addict!")
        points += 1
    if answer == 2:
        print("incredible!")
        points += 1
    
    print(input("(True or False) I prefer sweet over savory."))
    if answer == 1:
        print("True!")
        points += 2
    if answer == 2:
        print("Interesting!")
        points += 1
    
    print(input("(True or False) Chipotle is better than moes"))
    if answer == 1:
        print("This is the correct answer!")
        points += 3
    if answer == 2
        print("This opinion is respectable.")
        points += 1
    
    print(input("Hulu is better than Netflix."))
    if answer == 1:
        print("Hot take!")
        points += 0
    if answer == 2:
        print("Correct-ish!")

    points_calculator()


def points_calculator(points: int) -> int:
    """After interacting with the player for the last time, the final score will be calculated."""
    print(f"This is the final question {player}!")
    number = input(int("Pick a number between 1-100: "))
    

    if __name__ == "__main__":
        main()

#game loop call main again at then end of the