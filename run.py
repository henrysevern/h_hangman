import random
import os
import sys
from colorama import Fore
from colorama import Style
from time import sleep
from hangman import HANGMAN
from word_bank import animals_text
from word_bank import words, animals


def landing():
    """
    Function for the landing with a welcome message and a catergory choice.
    """
    print("Welcome to H's Hangman!")
    delay()
    print("Please choose a catergory! a - animals w - words")


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


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def begin():
    """
    Function is called after a catergory has been chosen, prints "let me think
    of a word!" withe the delay function and then give the user a hint on how
    long the word is
    """

    print("------------------------------------------")
    print("Let me think of a word!")
    delay()
    clear()
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
    """
    Function calls the guess input, checks wether the guess is correct,
    incorrect or not valid. Also the loop is broken based on wether the
    game is won or lost.
    """
    while True:

        print("------------------------------------------")

        attempt = input("Guess a letter: \n")
        # User input

        print("Let me check your guess!")
        delay()
        guess = not_allowed(attempt)
        # Delay funtion called on user guess checks if guess is valid entry

        if guess in pick:
            index = 0
            for i in pick:
                if i == guess:
                    correct[index] = guess
                index += 1
                clear()
            print(Fore.GREEN + f"{attempt} was correct!" + Style.RESET_ALL)
            update_word()
            HANGMAN(len(incorrect))
            print(f"Incorrect: {incorrect}")
        elif guess.isalpha():
            if guess not in incorrect:
                clear()
                print(Fore.RED + f"{attempt} was incorrect!" + Style.RESET_ALL)
                update_word()
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
    # String of only accepted characters.

    while (len(attempt) != 1 or attempt not in allowed_characters):
        print("Oops, that is not a valid guess. Try again!")
        attempt = input("Guess a letter: \n")
    return attempt
    # Only allows the user to enter accepted characters and only 1 character
    # at once


def play_again():
    """
    Function is called at the end of the game to give the user a play again or
    not choice.
    """
    play = input("Would you like to play again? y/n :\n")
    if play == "y":
        python = sys.executable
        os.execl(python, python, * sys.argv)
        # Restarts the program
    elif play == "n":
        print("Thank you for playing H's Hangman!")
        delay()
        quit()
        # Exits the program
    else:
        print("That is not a valid choice")
        play = input("Would you like to play again? y/n :\n")
        play
        # Brings the user back to the input if invalid choice is entered.


def main():
    """
    Main function calling all other functions.
    """
    begin()
    update_word()
    guess_letter()
    play_again()


landing()

# words = ['hangman', 'python']
# animals = ['dolphin', 'buzzard', 'elephant']

choose = input()

while True:
    if choose == "w":
        print("You chose words!")
        pick = random.choice(words)
        correct = ['_'] * len(pick)
        incorrect = []
        main()
    elif choose == "a":
        print("You chose animals!")
        animals_text()
        pick = random.choice(animals)
        correct = ['_'] * len(pick)
        incorrect = []
        main()
    else:
        print("That is not a valid choice! Please choose again.")
        choose = input()
        choose

main()
