#######################################################
#  Program title:         Guessing Game
#  Program Author:        Brendan Obilo
#  Date:                  06/02/2024
#
#  Description:           Trying to calculate the percentage
#                         amount of hotdog sold 
#                         from inputs of the user
#########################################################


# Declare constants and constant
# MAX_NUM = 80
max_num = 100
# MIN_NUM = 20
min_num = 0
# mid_limit = 50
mid_limit = 50
# counter = 0
counter = 0
# answer = 33
answer = 33

# getting_close = true
getting_close = True

# keep_guessing = True
keep_guessing = True

# while keep_guessing:
while keep_guessing:
    try:
        counter += 1
        user_input = int(input("Guess a number between " + str(min_num) + " and " + str(max_num) + " : "))
        if min_num < user_input or user_input < max_num:
            if user_input == answer:
                print("You have got the answer after " + str(counter) + " tries!")
                keep_guessing = False
            elif user_input < answer:
                min_num = user_input
                print("The number I have is bigger than " + str(user_input))
            else:
                max_num = user_input
                print("The number I have is smaller than " + str(user_input))
        else:
            print("Sorry, input must be between " + str(min_num) + " and " + str(max_num) + ", inclusively!")
    except ValueError: 
        print("Sorry, input must be a number")
    