#######################################################
#  Program title:         List Methods
#  Program Author:        Brendan Obilo
#  Date:                  29/02/2024
#
#  Description:           A program to use the different
#                         array methods in python
#########################################################

# list and its elements
capitals = ["Amsterdam", "Tokyo", "London", "Cape Town"]

# Print the full list.
print(capitals)
# Print the first item of the list.
print(capitals[0])
# Add “Paris” to the end of the list and print the updated list.
capitals.append("Paris")
print(capitals)
# Reverse the items of the list and subsequently print the updated list.
capitals.reverse()
print(capitals)
# Add “Cape Town” to the end of the list and print the updated list.
capitals.append("Cape Town")
print(capitals)
# Count the number of times “Cape Town” is in the list and print the result.
print(capitals.count("Cape Town"))
# Remove the first occurrence of “Cape Town” from the list.
capitals.remove("Cape Town")
print(capitals)
# Print the length (i.e. number of items) of the list.
print(len(capitals))
# Add the number 100 to the front of the list (i.e. index 0) & print the list.
capitals.insert(0, 100)
print(capitals)
# Update the value of the first item (i.e 100) to “Oshawa” & print the list.
capitals[0] = "Oshawa"
print(capitals)
