#######################################################
#  Program title:         Password Validator
#  Program Author:        Brendan Obilo
#  Date:                  01/02/2024
#
#  Description:           create a script to convert from the universal
#                         percentage grading scale to a fairly arbitrary
#                         version of a common letter grade scale
#                         (A, B, C, D, E and F)
#########################################################

# Declare variables
# max_num = 100
max_num = 100
# min_num = 0
min_num = 0
# A = 80
grade_a = 80
# B = 70
grade_b = 70
# C = 60
grade_c = 60
# D = 50
grade_d = 50

# collect user input
score = input("Please input grade: ")
print(score.isdecimal())
# if input is not digit and not between the range of 0 - 100
if ((score.isdigit() or score.isdecimal()) and
   (max_num >= float(score) >= min_num)):
    # if score >= grade_a
    if float(score) >= grade_a:
        # print("Your letter grade is A.")
        print("Your letter grade is A.")
    # if score >= grade_b
    elif float(score) >= grade_b:
        # print("Your letter grade is B.")
        print("Your letter grade is B.")
    # if score >= grade_c
    elif float(score) >= grade_c:
        # print("Your letter grade is C.")
        print("Your letter grade is C.")
    # if score >= grade_d
    elif float(score) >= grade_d:
        # print("Your letter grade is D.")
        print("Your letter grade is D.")
    # else
    else:
        # print("Your letter grade is F.")
        print("Your letter grade is F.")
else:
    print("Please input a digit between 0 and 100.")
