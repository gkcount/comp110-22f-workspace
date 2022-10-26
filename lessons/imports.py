"""Examples of importing in python."""

from lessons import helpers
#importing lessons, lessons is the package name
#importing a module names helpers
#packages can be nested

#basic syntax: from package import module

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")
#refer to module name and them dot then function you want to import from that module


if __name__ == "__main__":
    main() 

#what is going on in this program

#stack
#lessons.imports
#Globals
#__name__|"__main__"
#helpers (fully evaluated before it is imported into the module)
#main- defined in imports.py on lines 7-9

#main frame created


#separate globals space for lessons.helpers
#lessons.helpers
#Globals
#__name__ | "lessons.helpers"
#THE_ANSWER | 42

#heap
#fn helpers.py 4-6
#fn imports.py 7-9