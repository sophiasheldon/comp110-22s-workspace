"""EX06: Dictionary Functions - Building Dictionaries."""
__author__: str = "730330800"

# Invert Dictionary Function


def invert(data: dict[str, str]) -> dict[str, str]: 
    """Given a dictionary of string key-value pairs, returns the corresponding inverse dictionary."""
    inverse_data: dict[str, str] = dict()
    for key in data:
        if data[key] in inverse_data: 
            raise KeyError("Multiples of the same key encountered when inverted.")
        else: 
            inverse_data[data[key]] = key
    return inverse_data


# Favorite Colors Dictionary Function 


def favorite_color(data: dict[str, str]) -> str:
    """Returns the color that appears in the given data most frequently."""
    new_data: dict[str, str] = {}
    freq_color: str = ""
    max_count: int = 0
    count: int = 0
    for key in data: 
        count = 0 
        color = data[key] 
        if color in new_data:
            count += 1
        else:
            count = 1
        for data[key] in new_data:
            max_count = 0 
            freq_color = ""
            if count > max_count: 
                max_count = count 
                freq_color = data[key]
    return freq_color


# Count Dictionary Function 


def count(data: list[str]) -> dict[str, int]:
    """Returns a dictionary of the counts of each of the items in the input list."""
    new_data: dict[str, int] = dict()
    for item in data: 
        if item in new_data: 
            new_data[item] += 1 
        else: 
            new_data[item] = 1 
    return new_data