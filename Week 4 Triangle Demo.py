###################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  Week 4 Class review
# Date:         30/05/2024
####################################


counter = 1


def get_triangle_side():
    global counter
    ask_input = True
    while ask_input:
        try:
            n = int(input("Enter Side " + str(counter) + " of the triangle: "))
            if n in range(1, 101):
                counter = counter + 1
                ask_input = False
                return n
            else:
                print("Please try again (Enter a value between 1 to 100)")
        except ValueError:
            print("Please try again (Enter a value between 1 to 100)")


side_a = get_triangle_side()
side_b = get_triangle_side()
side_c = get_triangle_side()

side_a_square = pow(side_a, 2)
side_b_square = pow(side_b, 2)
side_c_square = pow(side_c, 2)

print(side_a_square)
print(side_b_square)
print(side_c_square)

if (side_a_square > side_b_square + side_c_square
    or side_b_square > side_c_square + side_a_square
        or side_c_square > side_a_square + side_b_square):
    print("Obtuse angled triangle")

if (side_a_square == side_b_square + side_c_square
    or side_b_square == side_c_square + side_a_square
        or side_c_square == side_a_square + side_b_square):
    print("Right angled triangle")

if (side_a_square < side_b_square + side_c_square
    and side_b_square < side_c_square + side_a_square
        and side_c_square < side_a_square + side_b_square):
    print("Acute angled triangle")
