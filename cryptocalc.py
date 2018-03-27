#!/usr/bin/python
# Run as python3
# No dependencies ᕕ( ᐛ )ᕗ

print("How many coins do you have?")
amount = float(input())    # sets var amount to the user's input (in float form)

print("How much is one of your coins currently worth (in dollars)?")
worth1 = float(input())    # sets var worth1 to user's float input
original = worth1 * amount
print("Your total worth now is $%s." % original)

print("How much do you expect one coin to be worth (again, in dollars)?")
worth2 = float(input())    # sets var worth2 to a float input by the user
total = amount * worth2    # sets var total to change times amount

more = total - (worth1 * amount)
print("Your %s coins will be worth $%s." % (amount, total))
print("You'll have gained $%s in profit." % more)
