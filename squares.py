#######################################################
#  Program title:         Squares
#  Program Author:        Brendan Obilo
#  Date:                  29/02/2024
#
#  Description:           A program that makes the list
#                         into a list of square numbers,
#                         none of which will exceed 100.
#########################################################

# creating a list
squares = []

# counting from 1- 10
for element in range(1, 10):
    # square of each elements not exceeding 100
    squares.append(element ** 2)
# print list of squares
print(squares)
