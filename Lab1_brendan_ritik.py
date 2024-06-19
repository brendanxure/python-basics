##########################################################################
# Names:        Brendan Obilo
#               Ritik Sharma
# Reg No:       100952871
#               100952840
# Description:  This program is a program which would generate a random
#               strong password based on the users’ instructions.
#               The user can decide the number of characters in their
#               password along with the number of letters, digits, and
#               special characters in their custom password.
# Document Type:Group 10 Lab 1
# Date:         23/05/2024
##########################################################################
import random
import string

# Establish a Constant to keep the min password length
PASSWORD_MIN_LENGTH = 8

# Establish a Constant to hold the password min range
PASSWORD_MIN_RANGE = 0

# Establish a variable that hold the length entered by user
password_length = 0

# Establish variable to keep asking for password length
customize_password_length = True

# Establish a list to hold the new secure password
new_password = []

# Establish a list to hold requirements
requirements = ["letters", "digits", "special characters"]


# Display program banner or title
print("Random Password Generator\n")

# start the process of generating the password length
while customize_password_length:
    try:
        # To collect user input for password length and
        # validate input to be an integer
        user_length_input = int(input("Enter the length of the password: "))
        # To ensure user input is greater than the required min length
        if user_length_input >= PASSWORD_MIN_LENGTH:
            # Password length will store the user input
            password_length = user_length_input
            # Program will not ask for password length again
            customize_password_length = False
        else:
            # Tell user to put the required specification for the length
            print(f"Please enter a value of greater than or equal to 8 to"
                  f" create a secure password")
    except ValueError as ve:
        # Catch data type error and tells user what is expected to input
        print(f"Invalid input: Please enter a valid integer")


def collect_password_details():
    customize_password = True
    # Establish a variable that hold the unused length left
    unused_length = password_length
    requirements_index = 0
    while customize_password:
        try:
            # To collect user input to determine how many of each requirement is desired
            # and validate the input to be an integer
            user_input = int(input("Enter the number of " + str(requirements[requirements_index]) +
                                   " desired in the password: "))
            # To ensure the user input is within required range
            if PASSWORD_MIN_RANGE <= user_input <= unused_length:
                # To ensure that length of password is complete and not less than user desired
                if requirements[requirements_index] == requirements[2] and user_input != unused_length:
                    # Tell user to complete length for special character to complete password
                    print(f"The length of password must be {password_length} "
                          f"so the {requirements[requirements_index]} should be {unused_length}")
                else:
                    # Based on how many of each requirement the user desires
                    for element in range(user_input):
                        # Check if the program requirement is letters
                        if requirements[requirements_index] == requirements[0]:
                            # Randomly select letter(s) and add to list of new password
                            new_password.append(random.choice(string.ascii_letters))
                        # Check if the program requirement is digits
                        elif requirements[requirements_index] == requirements[1]:
                            # Randomly select digit(s) and add to list of new password
                            new_password.append(random.choice(string.digits))
                        # The program requirement is definitely special characters
                        else:
                            # Randomly select special character(s) and add to the
                            # list of new password
                            new_password.append(random.choice(string.punctuation))
                    # To update the unused password length
                    unused_length -= user_input
                    # To update requirement index
                    requirements_index += 1
                    # Check if the last requirement has been asked or no unused password length
                    if requirements_index == len(requirements) or unused_length == PASSWORD_MIN_RANGE:
                        # Program will not ask for more details again
                        customize_password = False
                        # returns true to approve that the password details has been generated
                        return not customize_password
            else:
                # Tell user to put the required amount from the range available
                print(f"The number of {requirements[requirements_index]} should be in the range of "
                      f"{PASSWORD_MIN_RANGE} and {unused_length}")
        except ValueError:
            # Catch data type error and tells user what is expected to input
            print(f"Invalid input: Please enter a valid integer")


# Call the function to collect password details and store response
# returned into a variable established
password_generate = collect_password_details()

# Check if password details has been generated
if password_generate:
    # Shuffle all the generated details twice
    random.shuffle(new_password)
    random.shuffle(new_password)
    # Collect the customized output
    secure_password = ""
    # Based on the details generated
    for characters in new_password:
        # Join the all together as a string
        secure_password += str(characters)
    # Print the custom password
    print(f"Your desired password is:\n{secure_password}")
