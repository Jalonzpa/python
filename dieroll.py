#!/usr/bin/python
# run as python3
# no deps

from random import randint
choice = ""

print("How many dice do you want to roll?")
choice = int(input())    # sets the variable choice to an int based on the user's input

if choice == 1:
    print("You rolled this number: ")
else:
    print("You rolled these numbers: ")

for i in range(choice):    # iterates over the number of dice the user entered
    print(randint(1,6))    # prints a random number between one and six, however many times the user entered
