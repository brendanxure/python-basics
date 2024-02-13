#######################################################
#  Program title:         Multiplication square
#  Program Author:        Brendan Obilo
#  Date:                  06/02/2024
#
#  Description:           A code that will give you a
#                         multipliaction table ranging
#                         from 1 to any integer the user
#                         inputs that is greater than 0.
#########################################################

# Initialize Variables and Constants
# valid_input = true
valid_input = True
# lower_limit
lower_limit = 0
# Plus_one
plus_one = 1
# start_loop
start_loop = 1

try:
    # while loop
    while valid_input:
        # input("Input a positive whole number: ")
        user_input = int(input("Input a positive whole number: "))
        # if(user_input > lower_limit):
        if(user_input > lower_limit):
            # for range(start_loop, user_input + plus_one):
            for outer_counter in range(start_loop, user_input + plus_one):
                # for range(start_loop, user_input + plus_one):
                for inner_counter in range(start_loop, user_input + plus_one):
                    # valid_input = False
                    valid_input = False
                    # print(str(outer_counter * inner_counter), end="\t")
                    print(str(outer_counter * inner_counter), end="\t")
                print("\n")
        else:
            print("Please try again")
except ValueError:
    print("Please try again")


sum = 0

for counter in range(12, 8):
    sum += counter

print(str(sum))