"""more practice with if-else statements."""

SECRET: int = 3

print("I am thinking of a number between 1 and 10, what is it? ")
guess: int = int(input("What is your guess? "))
#guess will be an integer value
#input will have to be an integer value for the program to run

if guess == SECRET:
    print("Congratulations you guessed correct!")
else:
    print("The number you guessed is not correct!")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("you guessed too low!")

print("Game over!")

