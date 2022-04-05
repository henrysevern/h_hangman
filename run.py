import random
from time import sleep
from hangman import HANGMAN
words = ['hangman', 'python']
pick = random.choice(words)

print("------------------------------------------")


def delay():
    for i in range(5):
        print('.', end=' ')
        sleep(.5)
    print()


print("Let me think of a word!")
delay()
print(f"The word is {len(pick)} letters long\n")

correct = ['_'] * len(pick)
incorrect = []

HANGMAN(len(incorrect))


def update_word():
    """

    """
    for i in correct:
        print(i, end=" ")
    print()


update_word()


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

    allowed_characters = "abcdefghijklmnopqrstuvwxyz"

    while (len(attempt) != 1 or attempt not in allowed_characters):
        print("Oops, that is not a valid guess. Try again!")
        attempt = input("Guess a letter: \n")
    return attempt


guess_letter()
