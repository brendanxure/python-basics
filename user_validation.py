#######################################################
#  Program title:         User Validator
#  Program Author:        Brendan Obilo amd Samer Moussa
#  Date:                  01/02/2024
#
#  Description:           create a user validation 
#                         using a series of "if" statements that 
#                         check the details of the user input
#                         and ensure the inputs are valid.
#########################################################

# Declare variables

# Upper_year_limit = 9
upper_yr_limit = 9
# Lower_year_limit = 0
lower_yr_limit = 0

try:
    # print(“Please input your name: ”)
    name = input("Please input your name: ")
    # if user_input == empty
    if name.strip() == "":
        # print(“Name not valid”)
        print("Name not valid")
    else:
        # print(“Please input your program: ”)
        program_study = input("Please input your program: ")
        # if user_input == empty
        if program_study.strip() == "":
            # print(“Program not valid”)
            print("Program not valid")
        else:
            # print(“Please input years to completion: ”)
            yrs_completion = int(input("Please input years to completion: "))
            # if Lower_year_limit > user_input or user_input >= Upper_year_limit
            if lower_yr_limit > yrs_completion or yrs_completion >= upper_yr_limit:
                # print(“DC year not valid”)
                print("DC year not valid")
            else:
                # print(“Name: ” + name)
                print("Name:\t\t\t" + str(name))
                # print(“Program of study: ” + program)
                print("Program of study:\t" + str(program_study))
                # print("Year(s) to completion: “ + years_completion)
                print("Year(s) to completion:\t" + str(yrs_completion))
# Incase of any other type error in the try block
except:
    # print(“Error! input is invalid”)
    print("Error! Input is invalid")




