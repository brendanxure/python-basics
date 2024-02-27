#######################################################
#  Program title:         John Hotdogs
#  Program Author:        Brendan Obilo
#  Date:                  06/02/2024
#
#  Description:           Trying to calculate the percentage
#                         amount of hotdog sold 
#                         from inputs of the user
#########################################################

# Initialize Variables
# bulk_quantity = 1
bulk_quantity = 1
# each_quantity = 2
each_quantity = 2
# traditional = 1
traditional = 1
# veggie = 2
veggie = 2
# curry = 3
curry = 3
# calculate = 4
calculate = 4
# select_hotdog = true
select_hotdog = True
# amount_input = 0
amount_input = 0
# traditional_list =[]
traditional_list = []
# veggie_list = []
veggie_list = []
# curry_list = []
curry_list = []

while select_hotdog:
    try: 
        # Ask user to input which hotdog they sold
        bulk_input = int(input("Please enter " + str(traditional) 
                                + " for Tradtional Hotdogs\nPlease enter " + str(veggie)
                                + " for Veggie\nPlease enter " +
                                str(curry) + " for Curry\nPlease enter " + str(calculate) + " to calculate percentage\n "))
        # If bulk_input is equal traditional hotdogs
        if(bulk_input == traditional):
            # Ask user to input which traditional hotdog they sold
            amount_input = int(input(f"Please enter quantity for Traditional Hot Dogs: "))
            # Check if input is greater than or equal to 0
            if(amount_input >= 0):
                print(f"{amount_input}")
                # insert the number in the traditional list
                traditional_list.append(amount_input)
            else:
                # else print negatives are invalid
                print("Negatives are invalid")
            # check if input is equal veggie hotdogs
        elif(bulk_input == veggie):
            amount_input = int(input(f"Please enter quantity for Veggie Hot Dogs: "))
            # check if amount_input >= 0
            if(amount_input >= 0):
                print(f"{amount_input}")
                # insert the number in the veggie list
                veggie_list.append(amount_input)
            else:
                # print negatives are invalid
                print("Negatives are invalid")
        elif(bulk_input == curry):
            # input quantity for curry
            amount_input = int(input(f"Please enter quantity for Curry Hot Dogs: "))
            # if input quantity is greater than or equal to zero
            if(amount_input >= 0):
                print(f"{amount_input}")
                # insert the number in the curry list
                curry_list.append(amount_input)
            else:
                print("Negatives are invalid")
        elif(bulk_input == calculate):
            select_hotdog = False
            total_sum = int(sum(traditional_list) + sum(veggie_list) + sum(curry_list))
            if(total_sum > 0):
                percentage_traditional = (sum(traditional_list)/total_sum) * 100
                percentage_veggie = (sum(veggie_list)/total_sum) * 100
                percentage_curry = (sum(curry_list)/total_sum) * 100
                print("You sold\nTraditional:\t" + str("{:.2f}".format(percentage_traditional)) + " %\nVeggie:\t\t"
                        + str("{:.2f}".format(percentage_veggie)) + " %\nCurry:\t\t" + str("{:.2f}".format(percentage_curry)) + " %")
            else:
                print("Please input valid values before calculating")
        else:
            print("Please Enter a valid option")

    except:
        print("Please enter a valid integer")

