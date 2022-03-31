import random

words = ['hangman', 'python']
pick = random.choice(words)

print("------------------------------------------")
print(f"The word is {len(pick)} letters long\n")

correct = ['_'] * len(pick)
incorrect = []

def update_word():
    """
    
    """
    for i in correct:
        print(i, end = " ")
    print()

update_word()

def guess_letter():
   while True:
        guess = input("Guess a letter: ")
        

        if guess in pick:
            correct.append(guess)
            print("Correct:", correct)
        else:
            incorrect.append(guess)
            print("Incorrect:", incorrect)


guess_letter()
