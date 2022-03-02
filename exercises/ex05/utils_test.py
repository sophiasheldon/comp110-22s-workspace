"""Writing unit tests for the utility functions."""
__author__: str = "730330800"


from utils import only_evens, sub, concat

# unit testing for only_evens function


def test_only_evens_empty() -> None:
    n_list: list[int] = []
    assert only_evens(n_list) == []


def test_only_evens_single_item() -> None: 
    n_list: list[int] = [2, 5]
    assert only_evens(n_list) == [2]


def test_only_evens_many_items() -> None: 
    n_list: list[int] = [1, 2, 3, 4]
    assert only_evens(n_list) == [2, 4]


# unit testing for sub function 


def test_sub_empty() -> None:
    n_list: list[int] = []
    start: int = 0 
    end: int = 0
    assert sub(n_list, start, end) == []


def test_sub_single_item() -> None:
    n_list: list[int] = [0, 1]
    start: int = 0 
    end: int = 1
    assert sub(n_list, start, end) == [(n_list[0])]


def test_sub_many_items() -> None: 
    n_list: list[int] = [0, 1, 2, 3]
    start: int = 0 
    end: int = 3
    assert sub(n_list, start, end) == [(n_list[0]), (n_list[1]), (n_list[2])]


# unit testing for concat function 

def test_concat_empty() -> None: 
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_single_item() -> None: 
    list_one: list[int] = [1]
    list_two: list[int] = [2]
    assert concat(list_one, list_two) == [1, 2]


def test_concat_many_items() -> None: 
    list_one: list[int] = [1, 2]
    list_two: list[int] = [3, 4]
    assert concat(list_one, list_two) == [1, 2, 3, 4]