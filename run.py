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
        print("------------------------------------------")
        guess = input("Guess a letter: ")
        

        if guess in pick:
            index = 0
            for i in pick:
                if i == guess:
                    correct[index] = guess
                index += 1
            update_word()
        else:
            incorrect.append(guess)
            print("Incorrect:", incorrect)


guess_letter()
