##################################################################
#  Program title:         Midterm Mark
#  Program Author:        Brendan Obilo
#  Date:                  14/03/2024
#
#  Description:           A program to calculate user midterm mark
#                         and display the user grade as a percentage
#                         and their percentage for each type of
#                         assessment using functions.
##################################################################

# constants and variables
# PERCENT = 100
PERCENT = 100

# week = 4
week = 4

# test_week = 1
test_week = 1

# pre_class_grades = []
pre_class_grades = []

# exercise_grades = []
exercise_grades = []

# test_grade = []
test_grade = []

# pre_class_weight = 3
pre_class_weight = 3

# exercise_weight = 3
exercise_weight = 3

# test_weight = 12
test_weight = 12

# pre_class = "Pre-class quiz"
pre_class = "Pre-class quiz"

# exercise  = "exercise"
exercise  = "exercise"

# test = "test"
test = "test"

# assessment = ["Pre-class quiz", "exercise", "test"]
assessment = ["Pre-class quiz", "exercise", "test"]


# def calculate_scores(grades, grade_weight):
def calculate_scores(grades, grade_weight):
    # total_weight = length(pre_class_grades) * pre_class_weight
    #                + length(exercise_grades) * exercise_weight
    #                + length(test_grade) * test_weight
    total_weight = (len(pre_class_grades) * pre_class_weight
                    + len(exercise_grades) * exercise_weight
                    + len(test_grade) * test_weight)
    # grade_total = sum(grades) * grade_weight / PERCENT
    grade_total = sum(grades) * grade_weight / PERCENT
    # percent_grade_total = grade_total * PERCENT
    #                       / (length(grades) * grade_weight)
    percent_grade_total = grade_total * PERCENT / (len(grades) * grade_weight)
    # return percent_grade_total
    return percent_grade_total


# def get_scores(grade_type: string, grade_weeks: integer = week ):
def get_scores(grade_type: str, grade_weeks: int = week ):
    # for weeks in range(grade_weeks):
    for i in range(grade_weeks):
        # need_input = True
        need_input = True
        # while need_input:
        while need_input:
            # try:
            try:
                # user_input = float(input(Please enter average percentage
                #              mark for week str(i + 1) str(grade_type) :))
                user_input = float(input("\nPlease enter average percentage" 
                                         + " mark for week " + str(i + 1)
                                         + " " +  str(grade_type) + ": "))
                # is_valid = True
                is_valid = True
            # except:
            except:
                # is_valid = False
                is_valid = False

            # if is_valid:
            if is_valid:
                # if 0 <= user_input <=100:
                if 0 <= user_input <=100:
                    # if(grade_type == pre_class):
                    if(grade_type == pre_class):
                        # pre_class_grades.append(user_input)
                        pre_class_grades.append(user_input)
                    # elif(grade_type == exercise):
                    elif(grade_type == exercise):
                        # exercise_grades.append(user_input)
                        exercise_grades.append(user_input)
                    # else:
                    else:
                        # test_grade.append(user_input)
                        test_grade.append(user_input)
                    # need_input = False
                    need_input = False
                # else:
                else:
                    # print("Please enter a number between 0 and 100")
                    print("Please enter a number between 0 and 100")
            # else:
            else:
                # print("Entries must be numerical")
                print("Entries must be numerical")


# get_scores(pre_class)
get_scores(pre_class)
# get_scores(exercise)
get_scores(exercise)
# get_scores(test, test_week)
get_scores(test, test_week)
# percentage_preclass = calculate_scores(pre_class_grades, pre_class_weight)
percentage_preclass = calculate_scores(pre_class_grades, pre_class_weight)
# percentage_exercise = calculate_scores(exercise_grades, exercise_weight)
percentage_exercise = calculate_scores(exercise_grades, exercise_weight)
# percentage_test = calculate_scores(test_grade, test_weight)
percentage_test = calculate_scores(test_grade, test_weight)

# print(Your preclass is: {percentage_preclass}%
#       Your exercise is: {percentage_exercise}%
#       Your test is: {percentage_test})
print(f"Your {pre_class} is: {percentage_preclass:.2f}%\nYour {exercise} is: "
      f"{percentage_exercise:.2f}%\nYour {test} is: {percentage_test:.2f}%")
