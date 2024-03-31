#######################################################
#  Program title:         GPA Grade
#  Program Author:        Brendan Obilo
#  Date:                  11/03/2024
#
#  Description:           Display the grade of a user using
#                         values entered by a user.
#########################################################

# Varaibles and constants
# MAXIMUM = 100
MAXIMUM = 100

# MINIMUM = 0
MINIMUM = 0

# gpa = [5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
gpa = [5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

# lower_limit = [90, 85, 80, 75, 70, 65, 60, 55, 50]
lower_limit = [90, 85, 80, 75, 70, 65, 60, 55, 50, 0]

# ask_grade = True
ask_grade = False


# def grade_to_gpa(grade: float):
def grade_to_gpa(grade: float):
    if MAXIMUM >= grade >= MINIMUM:
        # for element in lower_limit:
        for element in lower_limit:
            # if grade >= element:
            if grade >= element:
                # index = lower_limit.index(element)
                index = lower_limit.index(element)
                # print gpa[index]
                print(gpa[index])
                # exit function immediately
                return
    else:
        # print("Please enter a number between 0 and 100")
        print("Please enter a number between 0 and 100")


grade_to_gpa(75)
