import random

words = ['hangman', 'python']
pick = random.choice(words)

def guess_letter():
    """
    
    """
    right = []
    wrong = []

    guess = input("Guess a letter: ")
    print(guess)

    if guess in pick:
        print("Yes")
    else:
        print("No")

guess_letter()
