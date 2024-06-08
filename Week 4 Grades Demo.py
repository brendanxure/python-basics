###################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  Week 4 Class review
# Date:         27/05/2024
####################################


def getstudentmarks():
    global counter

    while True:
        n = int(input("Enter a Number " + str(counter) + ": "))
        if n in range(0, 101):
            counter = counter + 1
            return n
        else:
            print("Please try again (Enter a value between 0 to 100)")


counter = 1

mark1 = getstudentmarks()
mark2 = getstudentmarks()
mark3 = getstudentmarks()

average_mark = int(mark1 + mark2 + mark3) / 3

if average_mark >= 75:
    print("First Division with distinction")
elif average_mark >= 60:
    print("First Division")
elif average_mark >= 50:
    print("Second Division")
elif average_mark >= 40:
    print("Third Division")
else:
    print("Fail")
