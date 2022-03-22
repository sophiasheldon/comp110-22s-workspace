def sub(n_list: list[int], start: int, end: int) -> list[int]:
    """Returns subset of given list, between the specified start index and end index minus one.""" 
    subset: list[int] = list()
    for n in n_list: 
        if n_list[start] < len(n_list):
            subset.append(n)
        subset.pop(len(n_list) - 1)
    return subset 