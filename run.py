import random
from time import sleep
from hangman import HANGMAN



words = ['hangman', 'python']
pick = random.choice(words)
correct = ['_'] * len(pick)
incorrect = []


def delay():
    """
    Function calls a time delay on the program to slow gameplay a little.
    "." are printed out in a loop in range of 5.
    The function is used at the start ("let me think off a word!") and after
    the user has guessed a letter.
    """
    for i in range(5):
        print('.', end=' ')
        sleep(.5)
    print()


def begin():

    print("------------------------------------------")
    print("Let me think of a word!")
    delay()
    print(f"The word is {len(pick)} letters long\n")

    HANGMAN(len(incorrect))


def update_word():
    """
    Function prints out the correct letters and the underscores in the correct
    list.
    """
    for i in correct:
        print(i, end=" ")
    print()


def guess_letter():
    while True:
        print("------------------------------------------")

        attempt = input("Guess a letter: \n")
        print("Let me check your guess!")
        delay()
        guess = not_allowed(attempt)
        if guess in pick:
            index = 0
            for i in pick:
                if i == guess:
                    correct[index] = guess
                index += 1
            update_word()
        elif guess.isalpha():
            if guess not in incorrect:
                incorrect.append(guess)
                HANGMAN(len(incorrect))
            else:
                print("That letter has already been guessed!")
            print(f"Incorrect: {incorrect}")

        if len(incorrect) > 5:
            print("You've lost!")
            print(f"The word was {pick}!")
            break

        if "_" not in correct:
            print("You've won!")
            break


def not_allowed(attempt):
    """
    This function allows the user to only enter a valid value. (a-z and only 1
    letter). The invalid guess will not be added to the incorrect list as
    an attempt, instead will just pop up an error message and return the input
    field.
    """
    allowed_characters = "abcdefghijklmnopqrstuvwxyz"

    while (len(attempt) != 1 or attempt not in allowed_characters):
        print("Oops, that is not a valid guess. Try again!")
        attempt = input("Guess a letter: \n")
    return attempt


def play_again():
    play = input("Would you like to play again? y/n :\n")
    if play == "y":
        begin()
    else:
        print("Thank you for playing H's Hangman!")
        delay()


def main():
    begin()
    update_word()
    guess_letter()
    play_again()


main()
