#!/usr/bin/python
# run as python3

from random import randint
choice = ""
choicelist = []

print("How many dice do you want to roll?")
choice = int(input())    # sets the variable choice to an int based on the user's input
choicelist = choice

if choice == 1:
    print("You rolled this number: ")
else:
    print("You rolled these numbers: ")

# todo: figure out how to expand the choice int into a list with all the numbers leading up to it
for i in choicelist:
    print(randint(1,6), "\n")
