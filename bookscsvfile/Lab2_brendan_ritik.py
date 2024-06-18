##########################################################################
# Names:        Brendan Obilo
#               Ritik Sharma
# Reg No:       100952871
#               100952840
# Description:  This program is a program that can store and retrieve
#               information of a user's reading list
# Type of Document: Lab 2 Group 10
# Date:         06/06/2024
##########################################################################

# Declare constants and Variables
# To establish a constant that holds value for add book option in the list of menu
ADD_BOOK_OPTION = 1
# To establish a constant that holds a value for list book option in the list of menu
LIST_BOOKS_OPTION = 2
# To establish a constant that holds a value for search book option in the list of menu
SEARCH_BOOK_OPTION = 3
# To establish a constant that holds a value for the quit application option in the list of menu
QUIT_APPLICATION_OPTION = 4
# A constants that holds the value of the index of book title in my list of options
BOOK_TITLE_INDEX = 0
# To establish a constant that holds the minimum value for year
MINIMUM_YEAR = 1
# To establish a constant that hold this year
THIS_YEAR = 2024
# To establish a list that holds few words that should not be capitalized when appending to the csv file
DONT_CAPITALIZE = ["and", "to", "or", "for", "of", "a", "in", "the", "is", "on", "with", "but", "at"]
# To establish a variable to hold the comma string not to be stored in the csv
COMMA = ","
# To establish a list that holds the detailed options for adding a book
options = ["Book title", "Author of the book", "Year of publication"]
# To establish a variable that holds the title of the book the user inputs
user_title = ""
# To establish a variable that holds the author of the book the user inputs
user_author = ""
# To establish a variable and initialize to holds the year of publication the user inputs
user_book_year = 0
# To establish a variable that holds a boolean value that determine if the program should continue running
select_options = True


# A function that accepts the title year and author of a book, formats and adds them to the books.csv
def add_book(title, author, year):
    # To establish a variable that holds the list of formatted title of the book
    title_to_format = [title.split()[0]]
    # To format the words in the title starting from the second word since the first word is already capitalize
    for words in title.split()[1:]:
        # To check if the words capitalize is part of the list of words not be capitalized
        if words.strip().lower() in DONT_CAPITALIZE:
            # To format the word properly by swapping with the one in the array
            new_word_format = DONT_CAPITALIZE[DONT_CAPITALIZE.index(words.strip().lower())]
            # To add the word to the list of formatted titles
            title_to_format.append(new_word_format)
        else:
            # To add the word that is not in the Don't capitalize list to the formatted title list
            title_to_format.append(words.strip())
    # To establish a variable that holds the title as a string
    formatted_title = ""
    # To remove the formatted title from the list and make it a string
    for each_word in title_to_format:
        formatted_title += each_word + " "
    # To establish a variable that holds the author as a string
    formatted_author = ""
    # To make the author entered by the user a list to remove unwanted space if any and convert back to a string
    for each_name in author.split():
        formatted_author += each_name + " "
    # To append the formatted inputs by user into the book.csv file
    with open("books.csv", "a") as write_book:
        write_book.write(f"\n{formatted_title.strip()}, {formatted_author.strip()}, {year}")
        print(f""""{formatted_title.strip()}" by {formatted_author.strip()} has been successfully added""")


# A function that displays the list of books in the books.csv file
def list_books():
    # To establish a list that holds the list of books from the books.csv file
    book_store = []
    # To retrieve all the data stored in the books.csv file
    with open("books.csv", "r") as book_list:
        book_data = book_list.readlines()
    # To take each book in the books.csv file and to the book_store list
    for each_book in book_data:
        title, author, year = each_book.strip().split(",")
        book_dictionary = {"title": title, "author": author, "year": year}
        book_store.append(book_dictionary)
    # To return the list of books in the csv file
    return book_store


# A function that search for books by title input
def search_book(title):
    # To call the function that list the books
    book_search_list = list_books()
    # To establish a list that hold the matching book from the search
    matching_book_list = []
    # To establish a variable that holds the title and removes whitespaces between words
    formatted_title = ""
    # No book in the book list
    if not book_search_list:
        print("The book list is empty")
    # The book list is filled with books
    else:
        # To split the title entered by the user, remove the whitespaces between words
        for input_title in title.split():
            # To format the title without whitespaces between the words
            formatted_title += input_title + " "
        # To scan through each book title in the book list
        for book_search in book_search_list:
            # To match the formatted user title input with the title of the book search
            if formatted_title.strip().lower() in book_search["title"].lower():
                # To add matching inputs to a new list
                matching_book_list.append(book_search)
        # There is a matching title with the user input
        if matching_book_list:
            # Display the list of matching titles to user
            for search_result in matching_book_list:
                print(f"\nTitle: {search_result["title"]},"
                      f" Author: {search_result["author"]}, Year: {search_result["year"]}")
        # No matching title with user input
        else:
            # Display to user that the book is not the list
            print("The book not in the list")


# The user ran the program or has not quit the program
while select_options:
    # The list of options the user should choose from
    print("\nWelcome to our book club\n1. Add book\n2. List of all books\n"
          "3. Search for a particular book\n4. Quit the application")
    try:
        # Accept user option input and validate
        option_selected = int(input("Please enter number of one option : "))
        # To know if user choose the add book option
        if option_selected == ADD_BOOK_OPTION:
            # An index that updates the after each correct book details is collected
            # This index reads the details from the list called option to know which input to ask the user
            option_index = 0
            # To ensure the option index has not exceeded the required inputs
            while option_index < len(options):
                try:
                    # To ensure the input required is the publication year which is the last element of the option list
                    if option_index == len(options) - 1:
                        # To collect the publication year and validate
                        user_book_input = int(input(options[option_index] + ": "))
                        # Check if the year of publication is a with expected range
                        if MINIMUM_YEAR <= user_book_input <= THIS_YEAR:
                            # Collect the input and update the index of option
                            user_book_year = user_book_input
                            option_index += 1
                        # The user input for year of publication is in the expected range of year
                        else:
                            print(f"{options[option_index]} cannot be less than 1 or greater than {THIS_YEAR}")
                    # The required input is between title and author
                    else:
                        # Ask the user for the required input based on the current option index
                        user_book_input = input(options[option_index] + ": ").strip().title()
                        # To remove comma from the input not to break the code
                        if COMMA in user_book_input:
                            user_book_input = user_book_input.replace(",", "")
                        # To ensure the user input is not empty value
                        if user_book_input == "":
                            # Tell the user the input can not be empty
                            print(f"{options[option_index]} cannot enter empty value")
                        # The user enter a valid input
                        else:
                            # Check if the required input was for the book title
                            if option_index == BOOK_TITLE_INDEX:
                                # collect the user input and store as the title of the book
                                user_title = user_book_input
                            # The required input is the author of the book
                            else:
                                # The user author is collected and stored in the appropriate variable
                                user_author = user_book_input
                            # update the option index for next detail
                            option_index += 1
                # Catch all data type error for add book option
                except ValueError:
                    print("Please enter a valid value")
            add_book(user_title, user_author, user_book_year)
        # To know if user choose the list books option
        elif option_selected == LIST_BOOKS_OPTION:
            # Call the list book option and store in the variable list of books
            list_of_books = list_books()
            # check if there is no book in the list of books
            if not list_of_books:
                # Tell user that the book list is empty
                print("Book list is empty")
            # The book list has books stored in it
            else:
                # Display all books in the list to the user
                for element in list_of_books:
                    print(f"\nTitle: {element["title"]},"
                          f" Author: {element["author"]}, Year: {element["year"]}")
        # To know if user choose the search book option
        elif option_selected == SEARCH_BOOK_OPTION:
            # A variable to ensure the search book option does not exit, till the appropriate input is collected
            book_title_search = True
            while book_title_search:
                # Ask the user to input the title of the book
                user_search = input("Book title: ").strip().title()
                # To ensure the user didn't enter an empty value
                if user_search == "":
                    # Tell user to enter appropriate input
                    print("Input cannot be empty")
                # The user entered an appropriate input
                else:
                    # Search for the book based on user input
                    search_book(user_search)
                    # Exit search book option
                    book_title_search = False
        # If the option selected by the user is to exit the application
        elif option_selected == QUIT_APPLICATION_OPTION:
            # Exit the application
            select_options = False
        # The user did not select any option between the range of values
        else:
            # Tell the user to choose between the range of option displayed
            print("Please enter between number 1 to 4 to select option")
    # Catch all data type error when choosing options for the program
    except ValueError:
        # Tell user to input appropriate data type of integer
        print("Please enter valid number")
