


#function name: contains
#we will have two parameters needle: value we are searching for and haystack: list[str]
#return type: bool
def contains(needle:str, haystack:list[str]) -> bool:
#gameplan:
#1. start with the first index
  i: int = 0
    #2.loop through every index
  while i < len(haystack):
    #2.a test if every item at index equal to needle
    if haystack[i] == needle:
      #2.b True return True! we found it!
      return True
    i +=1
#Return false
  return False