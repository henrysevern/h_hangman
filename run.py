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
            if guess not in incorrect:
                incorrect.append(guess)
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


guess_letter()
