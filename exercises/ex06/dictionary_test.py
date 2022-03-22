"""EX06: Dictionary Functions - Writing Unit Tests for Dictionaries."""
__author__: str = "730330800"

from dictionary import invert, favorite_color, count

# unit testing for invert dictionary function


def test_invert_empty() -> None:
    """Unit test for invert dictionary function: return empty dictionary."""
    data_input: dict[str, str] = dict()
    assert invert(data_input) == {}


def test_invert_single() -> None: 
    """Unit test for invert dictionary function: return inverted list with only one key-value pairing."""
    data_input: dict[str, str] = {"apple": "cat"}
    assert invert(data_input) == {"cat": "apple"}


def test_invert_multiple() -> None: 
    """Unit test for invert dictionary function: return inverted list with multiple key-value pairings."""
    data_input: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(data_input) == {'z': 'a', 'y': 'b', 'x': 'c'}

# unit testing for favorite_color dictionary function


def test_favorite_color_empty() -> None: 
    """Unit test for favorite_color dictionary function: return empty string."""
    data_input: dict[str, str] = dict()
    assert favorite_color(data_input) == ""


def test_favorite_color_single() -> None: 
    """Unit test for favorite_color dictionary function: return the most frequent color."""
    data_input: dict[str, str] = {"sophia": "blue", "sabrina": "pink", "gianna": "blue"}
    assert favorite_color(data_input) == "blue"


def test_favorite_color_multiple() -> None: 
    """Unit test for favorite_color dictionary function: returns the most frequent color that appeared first in the list."""
    data_input: dict[str, str] = {"sophia": "blue", "sabrina": "pink", "gianna": "blue", "megan": "green", "willow": "pink"}
    assert favorite_color(data_input) == "blue"

# unit testing for count 


def test_count_empty() -> None: 
    """Unit test for count dictionary function: returns an empty dictionary."""
    data_input: list[str] = list()
    assert count(data_input) == {}


def test_count_single() -> None: 
    """Unit test for count dictionary function: returns a single item dict."""
    data_input: list[str] = ["1", "1"]
    assert count(data_input) == {"1": 2}


def test_count_multiple() -> None: 
    """Unit test for count dictionary function: returns multiple item dict."""
    data_input: list[str] = ["1", "1", "2", "2", "2"]
    assert count(data_input) == {"1": 2, "2": 3}