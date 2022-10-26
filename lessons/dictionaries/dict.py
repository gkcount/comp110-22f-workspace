"""Demonstrations of dicitonary capabilities."""

# Decalring the type of dictionary
schools: dict[str, int]

#intialize to an empty dictionary (dictionaries constructing function)
schools = dict()

#set a key-value pairing in a dictionary
schools["UNC"] = 19400
# by printing this function you will get {'UNC': 19400}
schools["DUKE"] = 6717
schools["NCSU"] = 26150

#How to print a dictionary literal representation
print(schools)

# accessing a value by its key (how to perform a lookup)
print(schools["UNC"])
#you can also make it an f-string
print(f"UNC has {schools['UNC']} students.")
#The string value "UNC" is inside an f-string so it only needs single quotes

#remove a key-value pair from a dictionary
# by its key
schools.pop("DUKE")

#test for existence of a key in a given dictionary
is_duke_present: bool = "DUKE" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)