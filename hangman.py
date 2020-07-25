# BE10105 Project

# Submitted by:
#	Akshay Raj PB
#	Gokul K
#	Reuben Thomas Peter
#	Teena Sabu

import random

NO_OF_ATTEMPTS = 5
WORDS = [
    "ALPHABET", "AEROPLANE", "IRREGARDLESS",
    "CALCULATOR", "ENCYCLOPEDIA", "DISINTERESTED"
]

def startGame(word, attempts, found):
    if attempts == 0:
        print("You Lost! The word is {0}".format(word))
        return

    if len(found) == len(word):
        print("You won! The word is {0}".format(word))
        return

    s = ""

    for i in range(len(word)):
        if i in found:
            k = word[i] + " "
        else:
            k = "_ "
        s += k

    print(s)
    print("Attempts left: {0}".format(attempts))
    y = input("Enter guess: ").upper()

    c = -1

    for i in range(len(word)):
        if word[i] == y:
            if i not in found:
                found.append(i)
            print("The letter found at {0}th position".format(i+1))
            c = 0

    if c == -1:
        attempts -= 1

    print("\n\n\n")
    startGame(word, attempts, found)

if __name__ == '__main__':
    print("HANGMAN Game")
    print("-"*8)

    x = int(len(WORDS) * random.random())
    word = WORDS[x].upper()
    found = []
    print("Length of the word is: {0}".format(len(word)))
    startGame(word, NO_OF_ATTEMPTS, found)
