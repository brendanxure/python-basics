##################################################################
#  Program title:         Midterm Mark
#  Program Author:        Brendan Obilo
#  Date:                  05/03/2024
#
#  Description:           A program to calculate user midterm mark
#                         and display the user grade as a percentage
#                         and their percentage for each type of
#                         assessment.
##################################################################

# Constants and Variables
# PLANNING_APP_WEIGHT = 2
PLANNING_APP_WEIGHT = 2
# DECLARATION_WEIGHT = 1
DECLARATION_WEIGHT = 1
# WEEK_PRE_CLASS_WEIGHT = 3
WEEK_PRE_CLASS_WEIGHT = 3
# PERCENT = 100
PERCENT = 100
# WEEK_EXERCISE_WEIGHT = 3
WEEK_EXERCISE_WEIGHT = 3
# TEST_WEIGHT = 12
TEST_WEIGHT = 12
# MINIMUM_INPUT = 0
MINIMUM_INPUT = 0
# MAXIMUM_INPUT = 100
MAXIMUM_INPUT = 100
# FIRST_INDEX = 0
FIRST_INDEX = 0
# SECOND_INDEX = 1
SECOND_INDEX = 1
# pre_class_name = [“Planning an application”, “Declaration”, “Numeric and String”, “Selection”, “Iteration”]
pre_class_name = ["Planning an application", "Declaration", "Numeric and String", "Selection", "Iteration"]
# percent_planning_app = [ ]
percent_planning_app = []
# percent_declaration_quiz = [ ]
percent_declaration_quiz = []
# pre_class_weekly_percent_average = [ ]
pre_class_weekly_percent_average = []
# class_exercise_name = [“Planning an application”, “Numeric and String”, “Selection”, Iteration”]
class_exercise_name = ["Planning an application", "Numeric and String", "Selection", "Iteration"]
# percent_weekly_exercise = [ ]
percent_weekly_exercise = []
# percent_test = [ ]
percent_test = []
# ask_pre_class = true
ask_pre_class = True
# ask_exercise = true
ask_exercise = True
# ask_test = true
ask_test = True
# pre_class_name_index = 0
pre_class_name_index = 0
# exercise_name_index = 0
exercise_name_index = 0
# print(“Mid term Mark Calculator in Percent”)
print("********************************************\n"
      + "\tMid Term Mark Calculator in Percent\n"
      + "*********************************************")
# while ask_pre_class:
while ask_pre_class:
    # try:
    try:
        # print(“Please enter average percentage mark for
        #   	pre_class_name[pre_class_name_index] quiz”)
        user_input = float(input("\nPlease enter average percentage mark for "
                                  + pre_class_name[pre_class_name_index]
                                  + " pre-class quiz: "))
        # if MAXIMUM_INPUT >= user_input >= MINIMUM_INPUT:
        if MAXIMUM_INPUT >= user_input >= MINIMUM_INPUT:
            # if pre_class_name_index == FIRST_INDEX:
            if pre_class_name_index == FIRST_INDEX:
                # percent_planning_app.append(user_input)
                percent_planning_app.append(user_input)
            # elif pre_class_name_index == SECOND_INDEX:
            elif pre_class_name_index == SECOND_INDEX:
                # percent_declaration_quiz.append(user_input)
                percent_declaration_quiz.append(user_input)
            # else:
            else:
                # pre_class_weekly_percent_average.append(user_input)
                pre_class_weekly_percent_average.append(user_input)
            # pre_class_name_index += 1
            pre_class_name_index += 1
            # if pre_class_name_index > length(pre_class_name) -1:
            if pre_class_name_index > len(pre_class_name) -1:
                # ask_pre_class = false
                ask_pre_class = False
        # else:
        else:
            # print(“Please enter a number between MINIMUM_INPUT and
            #        MAXIMUM INPUT”)
            print("Please enter a number between " + str(MINIMUM_INPUT)
                   + " and " + str(MAXIMUM_INPUT))
    # except:
    except:
        # print(“Please enter a valid number”)
        print("Please enter a valid number")
# while ask_exercise:
while ask_exercise:
    # try:
    try:
        # print(“Please enter percentage mark for
        #        class_exercise_name[exercise_name_index] quiz”)
        user_input = float(input("\nPlease enter percentage mark for "
                                  + class_exercise_name[exercise_name_index]
                                  + " class exercise: "))
        # if MAXIMUM_INPUT >= user_input >= MINIMUM_INPUT:
        if MAXIMUM_INPUT >= user_input >= MINIMUM_INPUT:
            # percent_weekly_exercise.append(user_input)
            percent_weekly_exercise.append(user_input)
            # exercise_name_index += 1
            exercise_name_index += 1
            # if exercise_name_index > length(class_exercise_name) -1
            if exercise_name_index > len(class_exercise_name) -1:
                # ask_exercise = false
                ask_exercise = False
        # else:
        else:
            # print(“Please enter a number between MINIMUM_INPUT and
            #        MAXIMUM INPUT”)
            print("Please enter a number between " + str(MINIMUM_INPUT)
                   + " and " + str(MAXIMUM_INPUT))
    # except:
    except:
        # print(“Please enter a valid number”)
        print("Please enter a valid number")
# while ask_test:
while ask_test:
    # try:
    try:
        # print(“Please enter average percentage mark for your test”)
        user_input = float(input("\nPlease enter average percentage mark"
                                  + " for your test: "))
        # if MAXIMUM_INPUT >= user_input >= MINIMUM_INPUT:
        if MAXIMUM_INPUT >= user_input >= MINIMUM_INPUT:
            # percent_test.append(user_input)
            percent_test.append(user_input)
            # ask_test = false
            ask_test = False
        # else:
        else:
            # print(“Please enter a number between MINIMUM_INPUT
            # and MAXIMUM INPUT”)
            print("Please enter a number between " + str(MINIMUM_INPUT)
                   + " and " + str(MAXIMUM_INPUT))
    # except:
    except:
        # print(“Please enter a valid number”)
        print("Please enter a valid number")

# calculation
# total_weight = PLANNING_APP_WEIGHT + DECLARATION_WEIGHT
#               + WEEK_PRE_CLASS_WEIGHT
#               * length(pre_class_weekly_percent_average)
#               + WEEK_EXERCISE_WEIGHT * length(percent_weekly_exercise)
#               + TEST_WEIGHT
total_weight = float(PLANNING_APP_WEIGHT + DECLARATION_WEIGHT
                    + WEEK_PRE_CLASS_WEIGHT 
                    * len(pre_class_weekly_percent_average)
                    + WEEK_EXERCISE_WEIGHT * len(percent_weekly_exercise)
                    + TEST_WEIGHT)
# pre_class_weight = PLANNING_APP_WEIGHT + DECLARATION_WEIGHT
#                    + WEEK_PRE_CLASS_WEIGHT
#                    * length(pre_class_weekly_percent_average)
pre_class_weight = float(PLANNING_APP_WEIGHT + DECLARATION_WEIGHT
                    + WEEK_PRE_CLASS_WEIGHT
                    * len(pre_class_weekly_percent_average))
# exercise_weight = WEEK_EXERCISE_WEIGHT * length(percent_weekly_exercise)
exercise_weight = float(WEEK_EXERCISE_WEIGHT * len(percent_weekly_exercise))
# week_one_pre_class = (sum(percent_planning_app)
#                       * PLANNING_APP_WEIGHT/PERCENT)
#                       + (sum(percent_declaration_quiz) 
#                       * DECLARATION_WEIGHT/PERCENT)
week_one_pre_class = float(sum(percent_planning_app)
                        * PLANNING_APP_WEIGHT/PERCENT
                        + sum(percent_declaration_quiz)
                        * DECLARATION_WEIGHT/PERCENT)
# weekly_average_pre_class = (sum(pre_class_weekly_percent_average))
# 				            * WEEK_PRE_CLASS_WEIGHT/PERCENT
weekly_average_pre_class = float(sum(pre_class_weekly_percent_average)
                                * WEEK_PRE_CLASS_WEIGHT/PERCENT)
# pre_class_grade = week_one_pre_class + weekly_average_pre_class
pre_class_grade = week_one_pre_class + weekly_average_pre_class
# percent_pre_class = pre_class_grade * PERCENT / pre_class_weight
percent_pre_class = float(pre_class_grade * PERCENT/pre_class_weight)
# exercise_grade = (sum(percent_weekly_exercise)) * WEEK_EXERCISE_WEIGHT
# 				/PERCENT
exercise_grade = float(sum(percent_weekly_exercise)
                        * WEEK_EXERCISE_WEIGHT/PERCENT)
# percent_exercise = exercise_grade * PERCENT / exercise_weight
percent_exercise = float(exercise_grade * PERCENT /exercise_weight)
# test_grade = (sum(percent_test)) * TEST_WEIGHT/PERCENT
test_grade = float(sum(percent_test) * TEST_WEIGHT/PERCENT)
# percent_test_grade = test_grade * PERCENT / TEST_WEIGHT
percent_test_grade = float(test_grade * PERCENT / TEST_WEIGHT)
# percent_midterm_grade = (pre_class_grade + exercise_grade
#                          + test_grade) /total_weight * PERCENT
percent_midterm_grade = float((pre_class_grade + exercise_grade
                                + test_grade) /total_weight * PERCENT)
# print(“Your Mid Term Mark”)
print("\n********************************************\n"
      + "\tYour Mid Term Mark\n"
      + "*********************************************")
# print(“Pre-class Assessment is: ” 2dec_point(percent_pre_class))
print(f"\nPre-class Assessment is: {round(percent_pre_class, 2)} %")
# print(“Class exercise Assessment is: ” 2dec_point(percent_exercise))
print(f"Class exercise Assessment is: {round(percent_exercise, 2)} %")
# print(“Test grade Assessment is: ” 2dec_point(percent_test_grade))
print(f"Test grade Assessment is: {round(percent_test_grade, 2)} %")
# if percent_midterm_grade >= PERCENT:
if percent_midterm_grade >= PERCENT:
# print("MidTerm Grade is: PERCENT")
    print(f"Total MidTerm Grade is: {PERCENT} %")
else:
# print(“MidTerm Grade is:" 2dec_point(percent_midterm_grade))
    print(f"Total MidTerm Grade is: {round(percent_midterm_grade, 2)} %")
