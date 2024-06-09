###################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  Week 4 Class review
# Date:         27/05/2024
####################################


def getnumbers():
    global counter
    while True:
        n = int(input("Enter a Number " + str(counter) + ": "))
        if n in range(1, 301):
            counter = counter + 1
            return n
        else:
            print("Please try again (Enter a value between 1 to 300)")


counter = 1
x_value = getnumbers()
y_value = getnumbers()
z_value = getnumbers()

if x_value > y_value:
    if x_value > z_value:
        print("The largest of the three numbers is: ", x_value)
    else:
        print("The largest of the three numbers is: ", z_value)
else:
    if y_value > z_value:
        print("The largest of the three numbers is: ", y_value)
    else:
        print("The largest of the three numbers is: ", z_value)

