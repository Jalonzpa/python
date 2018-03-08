#!/usr/local/bin/python3
from random import randint
choice = ""

print("Would you like to roll a six sided die or a twelve sided die? Or more than one die?\n\n1. Six sided die\n2. Twelve sided die\n3. Two six sided dice\n4. Two twelve sided dice\n")
choice = int(input())

if choice == 1:
    print("You rolled a %s!") % randint(1,6)
elif choice == 2:
    print("You rolled a %s!") % randint(1,12)
elif choice == 3:
    print("You rolled a %s and a %s!") % (randint(1,6), randint(1,6))
elif choice == 4:
    print("You rolled a %s and a %s!") % (randint(1,12), randint(1,12))
else:
    print("That is not a correct number. Try again.")
