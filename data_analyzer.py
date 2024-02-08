#######################################################
#  Program title:         Data Analyzer
#  Program Author:        Brendan Obilo
#  Date:                  06/02/2024
#
#  Description:           Trying to check the age of user to know
#                         if it is valid for drinking, driving and voting.
#########################################################

# Declare variables
numbers = []
is_continuing = True
maximum_number = 0
minimum_number = 0

while is_continuing:
    try:
        # users input
        user_input = input("Please input number ")
        # if user input is a number
        if(user_input.isnumeric()):
            # if true then add the number to the list of numbers
            numbers.append(int(user_input))
        else:
            # if input is not a number
            is_continuing = False
            # get max number
            maximum_number = max(numbers)
            # get min number
            minimum_number = min(numbers)
            # print maximum number
            print('Maximum: ' + str(maximum_number))
            # print minimum number
            print('Minimum: ' + str(minimum_number))
    except ValueError:
        print('No integer')
