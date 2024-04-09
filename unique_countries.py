#########################################################
#  Program title:         Unique Countries
#  Program Author:        Brendan Obilo
#  Date:                  29/02/2024
#
#  Description:           A program that makes a list
#                         of countries without repeating
#                         each countries twice from a list
#                         multiple countries entered by user.
############################################################

# list and its elements
countries = [
                "United States",
                "Brazil",
                "Germany",
                "Spain",
                "The Netherlands",
                "United States",
                "United States",
                "Australia",
                "Japan",
                "Egypt",
                "South-Africa",
                "South-Korea",
                "China",
                "Japan",
                "Mexico",
                "Germany",
                "Sweden",
                "The Netherlands",
                "Canada"
]

# unique_countries = []
unique_countries = []

# for elements in countries
for element in countries:
    # if each country exist more than once
    if element not in unique_countries:
        # Add country to unique_countries
        unique_countries.append(element)
# print unique countries
print(unique_countries)
