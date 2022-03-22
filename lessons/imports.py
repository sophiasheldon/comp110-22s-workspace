"""Examples of importing Python."""

from lessons import helpers

# Alias a module / imported name as another name
from lessons import helpers as hp 

# import names defined globally in a module
from lessons.helpers import powerful


def main() -> None: 
    """Entry point of our program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))


if __name__ == "__main__":
    main()
