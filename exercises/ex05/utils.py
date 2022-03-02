"""Building utility functions."""
__author__: str = "730330800"

# defining only_evens function


def only_evens(n_list: list[int]) -> list[int]:
    """Returns a list of integers, containing only the even integers of the input parameter."""
    evens: list[int] = list()
    for n in n_list: 
        if n % 2 == 0: 
            evens.append(n)
        n += 1
    return evens


# defining sub function


def sub(n_list: list[int], start: int, end: int) -> list[int]:
    """Returns subset of given list, between the specified start index and end index minus one.""" 
    subset: list[int] = list()
    for n in n_list: 
        if n_list[start] < len(n_list):
            subset.append(n)
        subset.pop(len(n_list) - 1)
    return subset 


# defining concat function 

def concat(list_one: list[int], list_two: list[int]) -> list[int]: 
    """Generates new list containing elements of first list followed by second."""
    list_both: list[int] = list()
    for n in list_one: 
        list_both.append(n)
    for n in list_two: 
        list_both.append(n)
    return list_both