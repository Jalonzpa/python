#!/usr/bin/python
from random import randint
number = randint(0, 50)

print("Guess the number between 1 and 50!")

while True:
    guess = int(input())

    if guess > 50:
        print("It's between 1 and 50. Too high!")
    if guess == number:
        print("Right on!")
        break
    elif guess < number:
        print("It is higher than %s." % guess)
    elif guess > number:
        print("It's lower than %s." % guess)
