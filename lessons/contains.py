"""Example of writing a function to search a list."""

# Define a function named contains 
# Parameters: 
#   1. needle - the str we're searching for 
#   2. haystack - the list of str values we're searching through 


def main() -> None: 
    guess: str = input("What is the code word? ")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club...")
    else: 
        print("Go back to Davis.")


def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle is found in haystack."""
    for item in haystack: 
        if item == needle: 
            return True
# After all items checked, that means needle not found, return False
    return False
# Returns True if needle is found in haystack


print(__name__)

if __name__ == "__main__":
    main()