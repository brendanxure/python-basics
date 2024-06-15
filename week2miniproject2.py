###################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  This mini project is based on
#               childhood counting game called Fizz Buzz
# Date:         14/05/2024
####################################

# Declare constants
FIVE = 5
THREE = 3
ZERO = 0

# To keep the game looping
for element in range(1000):
    try:
        # Ask user for input
        user_input = input('Please enter a number: ')
        # validate User input to ensure it is an integer
        user_input = int(user_input)
        # Check if the input meets the Fizz Buzz requirements
        if user_input % THREE == ZERO and user_input % FIVE == ZERO:
            print("Fizz Buzz")
        # Check if the input meets the Fizz requirement
        elif user_input % THREE == ZERO:
            print("Fizz")
        # Check if the input meets the Buzz requirements
        elif user_input % FIVE == ZERO:
            print("Buzz")
        # Print the user input if the above conditions aren't met
        else:
            print(f'{user_input}')
    # catch error if the user does not input required data type
    except error as error:
        print(f"Input is a not valid whole number")
