##################################################################
#  Program title:         Validation
#  Program Author:        Brendan Obilo
#  Date:                  11/03/2024
#
#  Description:           A program to to determine if a user input
#                         is a float or not using a function
##################################################################


# def is_float(user_input):
def is_float(user_input):
    # try
    try:
        # float(user_input)
        float(user_input)
        # return True
        return True
    # except ValueError
    except ValueError:
        # return False
        return False


print(is_float("kyle"))
