"""Some examples of loving function definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        # Do what i need to do
        counter = counter + 1
        love_note += love(to) + "\n"
    return love_note
        