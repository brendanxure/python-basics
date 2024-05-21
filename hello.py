#######################################################
#  Program title:         hello
#  Program Author:        Brendan Obilo
#  Date:                  23/01/2024
#
#  Description:           A simple script called hello.py,
#                         which should ask the user to input their name
#                         and then print the exact string Hello name
#                         to the screen.
#########################################################

# initializing variables
name = input("Please write your name: ")
person = 'brendan'

# outcome
print("Hello " + str(name) + "!")
print("Hello I am"  + str(person) + "!")

for duplicate in range(9):
    print("1" * duplicate)