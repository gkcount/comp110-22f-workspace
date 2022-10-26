"""Practicing if-else statements."""

guess: str = int(input("What guess? "))
#in this example make sure that the function is forced into an integer so that you can get the correct equation
#without the int, the input would be asking for a string which would evaluate to false.

secret: int = 5

if guess == secret:
    print("Correct!")
else: 
    print("WRONG!")

print("Thank you for playing!!!")

#syntax for if-else:
#if then the condition:
#then block
#else
#else block
#every line in then block is indented one level