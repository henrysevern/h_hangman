import random

words = ['hangman', 'python']
pick = random.choice(words)

def guess_letter():
    """
    
    """
    correct = []
    incorrect = []

    while True:
        guess = input("Guess a letter: ")
        

        if guess in pick:
            correct.append(guess)
            print("Correct:", correct)
        else:
            incorrect.append(guess)
            print("Incorrect:", incorrect)

guess_letter()
