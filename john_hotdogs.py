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
# loop_valid = true
loop_valid = True
# bulk_quantity = 1
bulk_quantity = "1"
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

while loop_valid:
    try: 
        user_input = int(input("For Bulk input enter" + str(bulk_quantity) 
                                + "\nFor each input enter" + str(each_quantity)
                                + "\nPlease enter input here: "))
        print(str("Yes"))
        if(user_input == int(bulk_quantity)):
            while select_hotdog:
                bulk_input = int(input("Please enter" + traditional 
                                       + "for Tradtional Hotdogs\nPlease enter" + veggie + "for Veggie\n Please enter" + curry + "for Curry"))
                if(bulk_input == traditional):
                    amount_input = int(input(f"Please enter quantity for Traditional Hot Dogs: "))
                    if(amount_input >= 0):
                        print(f"{amount_input}")
                        traditional_list.append(amount_input)
                    else:
                        print("Negatives are invalid")
                elif(bulk_input == veggie):
                    amount_input = int(input(f"Please enter quantity for Veggie Hot Dogs: "))
                    if(amount_input >= 0):
                        print(f"{amount_input}")
                        veggie_list.append(amount_input)
                    else:
                        print("Negatives are invalid")
                elif(bulk_input == calculate):
                    loop_valid = False
                    print(max(traditional_list))
                    print(max(veggie_list))
                else:
                    print("")
        else:
            print("")
    except:
        print("Please enter a valid integer")

