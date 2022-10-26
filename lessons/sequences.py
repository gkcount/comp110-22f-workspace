"""Examples of the tuple and range sequences."""

#An example of a type without type aliasing
goat: tuple[str,int] = ("MJ", 23)

#tuples are sequences, so they are 0-indexed
print(goat[0])
print(goat[1])

#sequences have lengths
print(len(goat))

#sequences are iterable with for...in loops
#meaning you can loop over them with for...in
for item in goat:
    print(item)

#often used for 2d points and simple things that need to be defined within a program
# can "invent" a type with a type alias
Player = tuple[str, int] 

#creating variables of that type
unc_poy: Player = ["Bacot", 5]

# in a strange world where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)


#a range is another common sequence type
zero_to_nine: range = range(0, 10, 1)
#start = 0, stop = 10, increase by 1 (step)
# goes up to length-1 basically

print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

#we can have different steps for more control 
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)
# prints odd numbers

names: list[str] = [ "Kris", "alyssa", "michael", "lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")


print(odds_to_99)