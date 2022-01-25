"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730330800"

five_character: str = input("Enter a 5-character word: ")
check_word: int = len(five_character)
if check_word != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
check_letter: int = len(single_character)
if check_letter != 1: 
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_character)
count: int = 0
if five_character[0] == single_character: 
    print(single_character + " found at index 0")
    count = count + 1 
if five_character[1] == single_character:
    print(single_character + " found at index 1")
    count = count + 1
if five_character[2] == single_character:
    print(single_character + " found at index 2")
    count = count + 1 
if five_character[3] == single_character: 
    print(single_character + " found at index 3")
    count = count + 1
if five_character[4] == single_character: 
    print(single_character + " found at index 4")
    count = count + 1 
if count == 0: 
    print("No instances of " + single_character + " found in " + five_character)
else: 
    if count == 1:
        print((str(count)) + " instance of " + single_character + " found in " + five_character)
    else:
        print((str(count)) + " instances of " + single_character + " found in " + five_character)