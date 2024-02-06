#######################################################
#  Program title:         Rubber ducks amount
#  Program Author:        Brendan Obilo and Ruth Niyomugabo
#  Date:                  25/01/2024
#
#  Description:           Calculating the amount rubber ducks
#                         would be required to cover a reservoir
#                         almost completely by inputing the
#                         length and width of the reservoir and
#                         the diamter of the rubber ducks 
#########################################################

# import math library
import math

# Initialize variables

# length_of_reservoir = 0.0
length_of_reservoir = 0.0

# width_of_reservoir = 0.0
width_of_reservoir = 0.0

# diameter_of_duck = 0.0
diameter_of_duck = 0.0

# total_rubber_ducks = 0
total_rubber_ducks = 0

# Declare constant
# MINIMUM_DIAMETER = 0
MINIMUM_DIAMETER = 0

# collect data from user

# print(Please enter the length of reservoir in cm)
# length_of_reservoir = user_input()
length_of_reservoir = float(input("Enter the length of reservoir in cm "))

# print(Please enter the width of reservoir in cm)
# width_of_reservoir = user_input()
width_of_reservoir = float(input("Enter the width of reservoir in cm "))

# print(Please enter the diameter of reservoir in cm)
# diameter_of_duck = user_input()
diameter_of_duck = float(input("Enter the diameter of reservoir in cm "))

# if user inputs diameter of 0
if diameter_of_duck <= MINIMUM_DIAMETER:
    print("Diameter should be greater than 0")
else:
# calculate the total number of rubber ducks
# total_rubber_ducks = [length_of_reservoir/diameter_of_duck] 
#                     * [length_of_reservoir/diameter_of_duck]
    total_rubber_ducks = (math.floor(length_of_reservoir/diameter_of_duck)
                        * math.floor(width_of_reservoir/diameter_of_duck))

# output
# print(The number of rubber ducks required is + total_rubber_ducks)
    print("The number of rubber ducks required is " + str(total_rubber_ducks))
