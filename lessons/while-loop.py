"""An example of a while loop statement."""

Counter: int = 0
maximum: int = int(input( " Count up to, but not including what?"))
while Counter < maximum:
    Counter_squared: int = Counter ** 2
    print("The square of " + str(Counter) + " is " + str(Counter_squared))
    Counter = Counter + 2

print("Done!")