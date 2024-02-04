#######################################################
#  Program title:         Password Validator
#  Program Author:        Brendan Obilo
#  Date:                  01/02/2024
#
#  Description:           create a very basic password validator
#                         using a series of "if" statements that
#                         check the details of a string.
#########################################################

# Declare variables
special_characters = ["$", "@", "!"]

# Collect user password
# Print(“please input password”)
password = input("Please fill in password: ")
# If user_input has only alphabets
if password.isalpha():
    # Print(“Your password: ” + user_input)
    print("Your password: " + str(password))
    # Print(“The password must contain at least one non-alpha character.”)
    print("The password must contain at least one non-alpha character.")
# Else if input is all digits
elif password.isdigit():
    # Print(“Your password: ” + user_input)
    print("Your password: " + str(password))
    # Print(“The password must contain at least one non-digit character.”)
    print("The password must contain at least one non-digit character.")
# Else if input has no special characters
elif not(special_characters[0] in password or
         special_characters[1] in password or
         special_characters[2] in password):
    # Print(“Your password: ” + user_input)
    print("Your password: " + str(password))
    # Print(“The password must contain at least
    # one of the following special characters: $, @ or !.”)
    print("The password must contain at least\
    one of the following special characters: $, @ or !.")
# Else if input has no upper case or lower case
elif password.islower() or password.isupper():
    # Print(“Your password: ” + user_input)
    print("Your password: " + str(password))
    # Print(“The password must have both uppercase and lowercase letters.”)
    print("The password must have both uppercase and lowercase letters.")
# Else
else:
    # Print(“Your password: ” + user_input)
    print("Your password: " + str(password))
    # Print(“The password is valid!”)
    print("The password is valid!")
