#!/usr/bin/python
# Run as python3
# No dependencies ᕕ( ᐛ )ᕗ

print("How many coins do you have?")
amount = float(input())    # sets var amount to the user's input (in float form)

print("How much is one of your coins currently worth (in dollars)?")
worth1 = float(input())    # sets var worth1 to user's float input

print("How much do you expect one coin to be worth (again, in dollars)?")
worth2 = float(input())    # sets var worth2 to a float input by the user

change = worth2 / worth1    # sets var change to worth2 divided by worth1 (so you get another float)

print("The total change will be %s percent." % change)
total = change * amount    # sets var total to change times amount
print("Your %s coins will be worth $%s." % (amount, total))
