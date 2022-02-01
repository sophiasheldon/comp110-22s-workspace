"""EX02 - One Shot Wordle - Loops!"""
__author__ = "730330800"

secret_word: str = "python"
check_word: int = 6
word_guess: str = input("What is your 6-letter guess? ")
# set emoji box variables
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_index: int = 0 
emoji_result: str = ""
# word length check 
while int(len(word_guess)) != check_word:
    word_guess: str = input("That was not 6 letters! Try again: ")
# green box check
while word_index < check_word:
    any_yellow: bool = False
    if word_guess[word_index] == secret_word[word_index]: 
        emoji_result = emoji_result + GREEN_BOX
    else:
        # yellow box check 
        alt_index: int = 0 
        while any_yellow is not True and alt_index < check_word:
            if word_guess[word_index] == secret_word[alt_index]:
                any_yellow = True 
            else:
                alt_index = alt_index + 1 
        if any_yellow is True:
            emoji_result = emoji_result + YELLOW_BOX
        else: 
            # white box check
            emoji_result = emoji_result + WHITE_BOX
    word_index = word_index + 1 
print(emoji_result)
# secret word test
if word_guess != secret_word: 
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")