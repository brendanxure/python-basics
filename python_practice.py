########################################################################
# Name:         Brendan Obilo
# Date:         Jan 12th, 2024
# Program:      Practice Python
# Description:  Learning most basics of python
#
# 
#
#######################################################################

years_to_experience = 3

print("Name: \t\t\tBrendan Obilo") 
print("Program: \t\tPython")
print("Years to complete: \t" + str(years_to_experience))
print(type([1, 2, 3, 5]))
print(type({"Name:", "Brendan"}))

# Initialization of variables
slices_of_pizza = 50
each_programmer_eats = 3
addition = 0
subraction = 0
multiplication = 0
division = 0.0
pizza_remainder = 0

# Addition
addition = 120 + 43

# Subraction
subraction = 9382 - 450

# Multiplication
multiplication = 999 * 999

# Division
division = 120 / 40

# Modulo
pizza_remainder = slices_of_pizza % each_programmer_eats

# output
print(addition)
print(subraction)
print(multiplication)
print(division)
print(pizza_remainder)

# Initialize variables
first_number = 0.0
second_number = 0.0
average_number = 0.0

# Declaration of constant
AVERAGE = 2

# Request user to enter first number
first_number = float(input("Enter your first number "))

# Request user to enter second number
second_number = float(input("Enter your second number "))

# Get the average of the two numbers
average_number = float((first_number + second_number)/AVERAGE)

# Print the required outcome
print(average_number)