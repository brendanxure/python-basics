##################################################################
#  Program title:         Square Numbers
#  Program Author:        Brendan Obilo
#  Date:                  01/03/2024
#
#  Description:           Creating Simple console application that will
#                         graphically display all the square numbers
#                         within a range provided by the user.
##################################################################

import math

# Declare variables and constant

# UPPER_LIMIT = 10000
UPPER_LIMIT = 10000

# LOWER_LIMIT = 1
LOWER_LIMIT = 1

# ONE = 1
ONE = 1

# ZERO = 0
ZERO = 0

# top_limit  = 0
top_limit  = 0

# bottom_limit = 0
bottom_limit = 0

# no_lower_bound = True
no_lower_bound = True

# no_upper_bound = True
no_upper_bound = True

# square_list = []
square_list = []

# Print(***********Input Header************)
print("********************************************\n"
      + "\tSQUARE NUMBER FINDER\n"
      + "*********************************************\n")
# while no_lower_bound:
while no_lower_bound:
    try:
        # Print(Please enter lower bound:)
        user_input = int(input("Please enter lower bound: "))
        # If UPPER_LIMIT > user_input > LOWER_LIMIT:
        if UPPER_LIMIT >= user_input >= LOWER_LIMIT:
            # bottom_limit = user_input
            bottom_limit = user_input
            # no_lower_bound = False
            no_lower_bound = False
            # while no_upper_bound:
            while no_upper_bound:
                try:
                    # Print(Please enter between bottom_limit and UPPER_LIMIT)
                    user_input = int(input("Please enter higher bound between"
                                       + " " + str(bottom_limit) + " and "
                                       + str(UPPER_LIMIT) + ": "))
                    # If UPPER_LIMIT > user_input > bottom_limit
                    if UPPER_LIMIT >= user_input >= bottom_limit:
                        # top_limit  = user_input
                        top_limit  = user_input
                        # no_upper_bound = False
                        no_upper_bound = False
                        # print(*************Output Header******************)
                        print("********************************************\n"
                            + "\tSquare numbers between " + str(bottom_limit)
                            + " and " + str(top_limit ) + "\n"
                            + "*********************************************")
                        # for num ranges between lower_bound & upper_bound + 1
                        for number in range(bottom_limit, top_limit  + ONE):
                            # if squarerroot(number) % ONE == ZERO:
                            if math.sqrt(number) % ONE == ZERO:
                                # add number to the list
                                square_list.append(number)
                                # square_root = squareroot(number)
                                square_root = int(math.sqrt(number))
                                # Print(number (square_root  squared))
                                print(f"{number} ({square_root} squared)")
                        # if no square numbers between the range provided
                        if len(square_list) == ZERO:
                            # Print no square numbers between btm and top
                            print("No Square numbers between "
                                    + str(bottom_limit) + " and "
                                    + str(top_limit))
                        input()
                    # else:
                    else:
                        # Print(Enter num btw enter botm_limit and UPER_LIMIT)
                        print("Invalid input: Please enter a number between "
                             + str(bottom_limit) + " and " + str(UPPER_LIMIT)
                             + '\n')
                except:
                    # Print(Invalid input: Please enter a whole number)
                    print("Invalid input: Please enter a whole number\n")
        # else:
        else:
            # Print(Invalid input: Please enter number between LOWER & UPPER)
            print("Invalid input: Please enter a number between "
                  + str(LOWER_LIMIT) + " and " + str(UPPER_LIMIT) + '\n')
    except ValueError:
        # Print(Invalid input: Please enter a whole number)
        print("Invalid input: Please enter a whole number\n")
