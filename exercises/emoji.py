

def contains_char(search: str, char: str) -> bool:
    """Searching indices for matching character."""
    assert len(char) == 1
    check_word: int = len(search)
    counter: int = 0 
    while counter < check_word:
        if search[counter] == char:
            return True
        else:
            counter = counter + 1 
    return False


def emojified(guess: str, secret: str) -> str:
    """Codifing for yellow or white box emoji."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    counter: int = 0
    check_word: int = len(guess)
    emoji_result: str = ""
    while counter < check_word:
        if guess[counter] == secret[counter]:
            emoji_result = emoji_result + GREEN_BOX
        else:
            if contains_char(secret, guess[counter]) is True:
                emoji_result = emoji_result + YELLOW_BOX
            else: 
                emoji_result = emoji_result + WHITE_BOX
        counter = counter + 1
    return emoji_result