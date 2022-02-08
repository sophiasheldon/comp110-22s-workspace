"""EX03 - Structured Wordle!"""
__author__ = "730330800"

# declare function contains_char


def contains_char(search: str, char: str) -> bool:
    """Searching indices for matching character."""
    assert len(char) == 1
    check_word: int = len(search)
    counter: int = 0
    # matching character check
    while counter < check_word:
        if search[counter] == char:
            return True
        else:
            counter = counter + 1 
    return False


# declare function emojified 


def emojified(guess: str, secret: str) -> str:
    """Codifing for yellow or white box emoji."""
    assert len(guess) == len(secret)
    # set emoji box variables
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    counter: int = 0
    check_word: int = len(guess)
    emoji_result: str = ""
    count_correct: int = 0
    while counter < check_word:
        # green box check
        if guess[counter] == secret[counter]:
            emoji_result = emoji_result + GREEN_BOX
            count_correct = count_correct + 1
        else:
            # yellow box check
            if contains_char(secret, guess[counter]) is True:
                emoji_result = emoji_result + YELLOW_BOX
            else: 
                # white box check
                emoji_result = emoji_result + WHITE_BOX
        counter = counter + 1
    return emoji_result

# declare function input_guess


def input_guess(ex_len: int) -> str: 
    """Ensuring the expected length of the guess."""
    word_guess: str = input("Enter a " + str(ex_len) + " character word: ")
    # word length check
    while int(len(word_guess)) != ex_len: 
        word_guess: str = input("That was not " + str(ex_len) + " letters! Try again: ")
    return word_guess

# declare function main


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    # define secret word
    secret_word: str = "codes"
    turn_counter: int = 1
    len_secret: int = len(secret_word)
    while turn_counter <= 6:
        # print current turn number
        print("=== Turn " + str(turn_counter) + "/6 ===")
        # win test check
        win_test: str = input_guess(len_secret)
        print(emojified(win_test, secret_word))
        if win_test == secret_word:
            # user has won 
            print("You won in " + str(turn_counter) + "/6 turns!")
            exit()
        else: 
            turn_counter = turn_counter + 1
    # user has lost 
    print("X/6 - Sorry, try again tomorrow!")

    if __name__ == "__main__":
        main()