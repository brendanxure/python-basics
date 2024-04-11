#######################################################
#  Program title:         zombie cups
#  Program Author:        Brendan Obilo
#  Date:                  24/02/2024
#
#  Description:           Trying to calculate the amount
#                         amount of coffee in grams 
#                         from inputs of the user
#########################################################

import math

# Initialize Variables and Constant

# TABLESPOON
TABLESPOON = 6
# GRAM_QUANTITY
GRAM_QUANTITY = 15
# extra_large_coffee = 1
extra_large_cups = 1
# large_cups = 2
large_cups = 2
# medium_cups = 3
medium_cups = 3
# small_cups = 4
small_cups = 4
# calculate = 5
calculate = 5
# select_cup = true
select_cup = True
# amount_input = 0
amount_input = 0
# extra_large_list =[]
extra_large_list = []
# large_list = []
large_list = []
# medium_list = []
medium_list = []
# small_list = []
small_list = []

while select_cup:
    try:
        # user select the type of cup
        user_input = int(input("Please enter " + str(extra_large_cups) 
                                + " for extra large\nPlease enter " + str(large_cups)
                                + " for large\nPlease enter " +
                                str(medium_cups) + " for medium\nPlease enter " + str(small_cups)
                                + " for small\nPlease enter " + str(calculate) + " to calculate percentage\n "))
        # if it is extra large cups
        if(user_input == extra_large_cups):
            # quantity needed
            amount_input = int(input(f"Please enter quantity for Extra large cups: "))
            # qunatity equals to 0
            if(amount_input >= 0):
                print(f"{amount_input}")
                extra_large_list.append(amount_input)
            else:
                print("Negatives are invalid")
        # if it is large cups
        elif(user_input == large_cups):
            amount_input = int(input(f"Please enter quantity for Large cups: "))
            if(amount_input >= 0):
                print(f"{amount_input}")
                large_list.append(amount_input)
            else:
                # Negatives are invalid
                print("Negatives are invalid")
                # if it is large cups
        elif(user_input == medium_cups):
            amount_input = int(input(f"Please enter quantity for medium cups: "))
            # amount_input >= 0
            if(amount_input >= 0):
                print(f"{amount_input}")
                # add to medium list
                medium_list.append(amount_input)
            else:
                # Negatives are invalid
                print("Negatives are invalid")
        elif(user_input == small_cups):
            amount_input = int(input(f"Please enter quantity for small cups: "))
            # amount_input >= 0
            if(amount_input >= 0):
                print(f"{amount_input}")
                small_list.append(amount_input)
            else:
                # Negatives are invalid
                print("Negatives are invalid")
        elif(user_input == calculate):
            # end the loop
            select_cup = False
            # Total amount of pots of coffee = math.ceil((Extra large/4) + (Large/6) + (Medium/8) + (Small/10))
            total_pots_of_coffee = math.ceil(sum(extra_large_list)/4 + sum(large_list)/6 + sum(medium_list)/8 + sum(small_list)/10)
            if(total_pots_of_coffee > 0):
                # Total amount of Tablespoons = Total amount of pots of coffee * 6
                table_tablespoons = total_pots_of_coffee * TABLESPOON
                # Total amount of coffee grounds(g) = Total amount of Tablespoons * 15
                total_coffe_grounds = table_tablespoons * GRAM_QUANTITY
                print("Total anmount of coffee in gram is " + str(total_coffe_grounds))
            else:
                # if total pots of coffee is not greater of zero
                print("Please input valid values before calculating")
    except ValueError:
        print("Please enter a valid integer")