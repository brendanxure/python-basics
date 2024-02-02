#######################################################
#  Program title:         Age Checker
#  Program Author:        Brendan Obilo
#  Date:                  29/01/2024
#
#  Description:           Trying to check the age of user to know
#                         if it is valid for drinking, driving and voting.
#########################################################

# Declare variable
# age_to_drive = 16
age_to_drive = 16

# age_to_vote = 18
age_to_vote = 18

# age_to_drink = 19
age_to_drink = 19

# VALID_AGE = 0
VALID_AGE = 0

# collect user age
# print(“Please enter your age”)
user_age = int(input("Enter your age: "))
# user_age = user_input

# check if the input is valid
# if user_age < VALID_AGE :
# print(“Invalid age, Please put a proper age”)
if user_age < VALID_AGE:
    print("Invalid age, Please put a proper age")
# else:
else:
    driving_age = user_age >= age_to_drive
#   check the user eligibility to drive
#   driving_age = user_age >= VALID_AGE
# 	print(“Driving age in Ontario?: ” + driving_age)
    print("Driving age in Ontario?: " + str(driving_age))
#   check the user eligibility to vote
# 	voting_age = user_age >= VALID_AGE
    voting_age = user_age >= age_to_vote
# 	print(“Voting age in Ontario?: ” + voting_age)
    print("Voting age in Ontario?: " + str(voting_age))
# check the user eligibility to drink
# 	drinking_age = user_age >= VALID_AGE
    drinking_age = user_age >= age_to_drink
# 	print(“Alcohol purchasing age in Ontario?: ” + drinking_age)
    print("Alcohol purchasing age in Ontario: " + str(drinking_age))
