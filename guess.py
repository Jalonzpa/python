#!/usr/bin/python
# run as python3
# no dependencies

from random import randint
number = randint(0, 50)    # sets the variable number to a random number between 0 and 50

print("Guess the number between 1 and 50!")

while True:
    guess = int(input())    # sets the variable guess to an integer from the user's input

    if guess > 50: # if guess is higher than 50
        print("It's between 1 and 50. Too high!")
    if guess == number:    # if the user's guess equals the random number
        print("Right on!")
        break    # breaks out of the while loop and exits the program
    elif guess < number:    # if guess is lower than the random number
        print("It is higher than %s." % guess)
    elif guess > number:    # if the guess is higher than the random number
        print("It's lower than %s." % guess)
