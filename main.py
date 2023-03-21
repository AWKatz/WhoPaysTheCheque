# This is Day 4 of 100 for the Udemy Python Bootcamp

import random

names_string = input("Who are the attendees of the lunch? Separate names by comma. ")
names = names_string.split(",")

#debugging
#print(names)
#print(len(names))

attendees = len(names)

buyer = random.randint(0, attendees -1)

print(f"{names[buyer]} was selected to cover the cheque for lunch!")

