"""Practicing the input function."""

user_name: str = input("What is your name? ")
#in this variable we are identifying the 'user_name' variable as a string type and assigning it to the input function ("What is your name? ")
#This allows us to replace the input function ("What is your name? ") with the variable 'user_name'.
#how to ask the user for input with the input function
print("Hello, " + user_name + ", good morning!")
#the input is the first thing that is going to be evaluated in this function because it is an unknown
#remember to leave space where the input is being put in, so there is accurate spacing in the terminal

print("What is up " + user_name)

great: str = input("How are you doing today? ")

#this prints the result for the str great, does not need to be included
print(great)

#uses the variable great and inputs it into the str
print(" I am so glad you are " + great + "! I am the same!")

bootycheeks: str = input("What is your favorite color? ")
#a new variable bootycheeks is definced

print("WOW, I love " + bootycheeks + " too!")

#user_name would be in the globals frame with a value that is inputted
#output would be "Hello, Grace, good morning"

#great would be in the globals frame with the string that is inputted
#output would be "I am so glad you are great! I am the same!"

#bootycheeks would be in the globals frame with the string that is inputted
#output: "WOW, I love purple too!""