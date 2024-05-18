##########################################################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  This program is a program that ask the to input user how many
#               movies they want to add to a list of the movies. Then allows
#               the user to input the movie name and budget. It calculates the
#               average budget for all movies in the list and determines the
#               movies above the average budget and display them, how many
#               they are, and the average budgets of all movies.
# Type of Document: In class 1
# Date:         16/05/2024
##########################################################################

# Establish a variable to store the total budget
total_budget = 0.0

# The list of movies and budget stored in a variable  named movies
movies = [
        ("Eternal Sunshine of the Spotless Mind", 20000000),
        ("Memento", 9000000),
        ("Requiem for a Dream", 4500000),
        ("Pirates of the Caribbean: On Stranger Tides", 379000000),
        ("Avengers: Age of Ultron", 365000000),
        ("Avengers: Endgame", 356000000),
        ("Incredibles 2", 200000000)
]

# Create an empty list to store the movies and budget above average budget
higher_budget_movies = []

# A prompt to enter the number of movie the user wants to add
user_movies_option = int(input("Enter how many new movies you wish to add: "))
# Based on how many movies the user wants to add collect inputs
for option in range(user_movies_option):
    # Ask user to input new movie name
    movie_name = input("Enter new movie name: ")
    # Ask user to input new movie budget
    movie_budget = float(input("Enter new movie budget: "))
    # Put the movie name and budget in a tuple
    new_movie = (movie_name, movie_budget)
    # Add the tuple in the list of movies
    movies.append(new_movie)

# Based on each movie in the list of movies
for element in movies:
    # Sum all the budgets in the list
    total_budget += element[1]

# Calculate the average budget
average_budget = total_budget / len(movies)

#  Print out every movie that has a budget higher than the average
print(f"\nThe average budget of the movies is: {round(average_budget)}")
# Based on each movie in the list of movies
for element in movies:
    # If any movie has a budget is greater than the average budget
    if element[1] > average_budget:
        # Add the movie and the budget to a new list created
        higher_budget_movies.append(element)
        # Determine the difference between the budget and the average budget
        budget_difference = element[1] - average_budget
        # Print the movie name, budget and the difference with average
        print(f"{element[0]} cost $ {round(element[1])} : "
              f"${round(budget_difference)} over average.")

# Print the number movies spent more than the average budget
print(f"There were {len(higher_budget_movies)} movies with over average"
      f" budgets.")
