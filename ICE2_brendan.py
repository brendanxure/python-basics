##########################################################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  This program is a program that will ask user to input sets of numbers
#               that are split by spaces and validate the user input to be an integer
#               and adds to a list, then produces the minimum number as the output.
# Type of Document: In class 2
# Date:         30/05/2024
##########################################################################

# A list that hold the required valid set of numbers from user
set_of_numbers = []


# A function that runs the entire program
def minimum_number():
    try:
        # ask user to input set of numbers
        user_input = input("Please enter the set of numbers: ")
        # To ensure the user input is not empty
        if user_input.strip() == "":
            # Display to the user that input is empty
            print("Input can not be empty")
        else:
            # Put the user input into a list of strings
            numbers = user_input.strip().split(" ")
            # check all the input in the list of strings and validate the data type
            for elements in numbers:
                # add the validated integer into a new list
                set_of_numbers.append(int(elements))
            # sort the new list of numbers in ascending order
            set_of_numbers.sort()
            # display the lowest number which is the first in the list
            print(set_of_numbers[0])
    except ValueError:
        # To catch error for data type and display to the user
        print("Please enter a valid integer")


# call the function
minimum_number()
