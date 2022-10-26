"""Demonstrations of dictionary capabilities."""


#declaring the type of a dictionary
schools: dict[str, int]

#initialize to an empty dictionary
schools = dict()

#set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["DUKE"] = 6717
schools["NCSU"] = 26150

#print a dictionary literal representation
print(schools)

#acess a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")
#when you use a string inside of a string, you must use the single quotations

#removing a key-value pair from a dicitonary
#by its key.
schools.pop("DUKE")

#test for the existence of a key
is_duke_present: bool = "DUKE" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

#demonstration of dictionary literals
schools = {} #same as dict()

#Alternatively, intialize key-value pairs
schools = {"UNC": 19400, "DUKE": 6717, "NCSU": 26150}

print(schools)
# print(schools["UNCC"])
#name error

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")


for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")