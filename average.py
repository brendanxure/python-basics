#######################################################
#  Program title:         Average
#  Program Author:        Brendan Obilo
#  Date:                  24/01/2024
#
#  Description:           Determining the average of two values
#                         entered by a user.
#########################################################

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