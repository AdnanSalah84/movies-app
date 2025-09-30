# Validates if input is an integer
# Rejects strings and empty inputs
def validate_int(question, validation):
    value = input(question)
    while True:
        try:
            int(value)
            return value
        except ValueError:
            value = input(validation)
# Validates if input is a string
# Rejects empty inputs and whitespace only inputs
def validate_string(question, validation):
    value = input(question)
    while True:
        if value.rstrip() == '':
            value = input(validation)
        else:
            return value
# Validates whether the input is either an integer or a string
# Rejects empty inputs and whitespace only inputs
def validate_input(question, validation):
    value = input("\n" + question)
    while True:
        try:
            int(value)
            return value
        except ValueError:
            if value.rstrip() == '':
                value = input(validation)
            else:
                return value
# Used when the user needs to confirm something
# Returns a boolean
# Only accepts many variations of yes and no
def validate_confirm(question):
    value = input("\n" + question).lower()
    while True:
        if value in ["y", "yes"]:
            return True
        elif value in ["n", "no", "confirm", "exit"]:
            return False
        else:
            value = input("Enter either 'y' or 'n': ").lower()
# Validates option user wants to select
# Accepts many variations of each option
def validate_choice():
    print(f"\nSelect one of the following:"
          f"\n1. Enter movies to the list"
          f"\n2. Remove movies from the list"
          f"\n3. Search for movies"
          f"\n4. List all movies")
    value = input("\nEnter your choice: ").lower()
    while True:
        if value in ["1", "one", "enter", "e", "ent"]:
            return 1
        elif value in ["2", "two", "remove", "delete", "r", "d", "rem", "del"]:
            return 2
        elif value in ["3", "three", "search", "se", "s"]:
            return 3
        elif value in ["4", "four", "list", "l", "ls"]:
            return 4
        else:
            value = input("Invalid option. Re-enter your choice: ")
 
 