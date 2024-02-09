#######################################################
#  Program title:         Lap Times
#  Program Author:        Brendan Obilo
#  Date:                  06/02/2024
#
#  Description:           Trying to calculate and displaying
#                         the best and worst lap with the
#                         miniutes and second input from
#                         the user.
#########################################################

# Initialize Variables and Constants
# time = []
time = []
# valid_input
valid_input = 1
# count = 1
count = 1
# TIME_CONVERSION = 60
TIME_CONVERSION = 60

try:
    # using for loop to get number of time to request input
    for inputs in range(1, 4):
        # Tell user to input minutes
        minutes = input("Enter the minutes for lap "
                        + str(count) + " : ")
        # Tell user to input seconds
        seconds = input("Enter the seconds for lap "
                        + str(count) + " : ")
        # if user inputs nothing
        if(minutes.strip() == "" and seconds.strip() == ""):
            # print(You must a input a value)
            print("You must input a value")
        elif(int(minutes) <= valid_input and int(seconds) <= valid_input):
            # print(Value must not be less than 1)
            print("Value must not be less than 1")
        else:
            # calculate the time for each lap
            total_time = (int(minutes) * TIME_CONVERSION) + int(seconds)
            # Add the value to the list of time
            time.append(total_time)
            count += 1
    # Get maximum time
    maximum_time = max(time)
    # Get minimum time
    minimum_time = min(time)
    # print output
    print("Best lap: " + str(minimum_time))
    print("Worst lap: " + str(maximum_time))
# Incase of any wrong input
except ValueError:
    # print("Please input an integer")
    print("Please input an integer")
