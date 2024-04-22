##################################################################
#  Program title:         Leaderboard
#  Program Author:        Brendan Obilo
#  Date:                  19/04/2024
#
#  Description:           A function that accepts a score and
#                         a list of current top ten scores and will
#                         determine if the score should be added to
#                         the top ten score list. The current top ten
#                         scores list is sorted in descending order.
##################################################################

# import tkinter
from tkinter import *
# import hovertip
from idlelib.tooltip import Hovertip
# import sys
import sys

# Variables and Constants

# WINDOW_WIDTH = 500
WINDOW_WIDTH = 500
# WINDOW_HEIGHT = 300
WINDOW_HEIGHT = 300
# WINDOW_MIN_WIDTH = 500
WINDOW_MIN_WIDTH = 500
# WINDOW_MIN_HEIGHT = 300
WINDOW_MIN_HEIGHT = 300
# ZERO = 0
ZERO = 0
# score_list = [21,32,43,54,65,76,87,98,109,110,121]
score_list = [21,32,43,54,65,76,87,98,10,11,12]
# player_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
player_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# window = Tk()
window = Tk()

# window size
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width = WINDOW_MIN_WIDTH, height = WINDOW_MIN_HEIGHT)

# window title
window.title("Leader Board")


# def rank_players:
def rank_players (score: float, score_list: list = score_list):
    try:
        # sort the input list
        score_list.sort(reverse=True)
        # returnValue = False
        returnValue = 'False'
        # final_outcome = ''
        final_outcome = ''
        # if score > score_list[-1]:
        if score > score_list[-1]:
            # returnValue =  'True'
            score_list.append(score)
            score_list.sort(reverse=True)
            for element in score_list[:10]:
                final_outcome = final_outcome + player_list[score_list.index(element)] + '            ' + str(element) + '\n'
            returnValue = final_outcome
        else:
            for element in score_list[:10]:
                final_outcome = final_outcome + player_list[score_list.index(element)] + '            ' + str(element) + '\n'
            returnValue = final_outcome    
        print(returnValue)
        return returnValue
    except ValueError:
        #  print('Please a valid number')
        return 'Please enter valid input'
    

# def rank_players:
def rank_players (score: float, score_list: list = score_list):
    try:
        # sort the input list
        returnValue = False
        if score > score_list[-1]:
            returnValue = True
        return returnValue
    except ValueError:
        #  print('Please a valid number')
        return 'Please enter valid input'



# submit function
def submit(_event=None):
    try:
        returnValue = ''
        # input_player_name = string(entry_player_name.get())
        input_player_name = str(entry_player_name.get())
        # input_score = float(entry_score.get())
        input_score = float(entry_score.get())
        if input_player_name.strip() == '':
            returnValue =  'Please enter player name'
        elif input_score < 0: 
            returnValue = 'Please enter score greater than 0'
        else:
            returnValue = rank_players(input_score)
        return display_output.configure(text=returnValue)
    except ValueError:
        return display_output.configure(text='Please input a valid score')

# clear function
def clear(_event=None):
    # clear player name entry
    entry_player_name.delete(0, END)
    # clear display output
    display_output.configure(text = "")
    # set focus on player name entry
    entry_player_name.focus()
    # clear score 
    entry_score.delete(0, END)

# exit function
def exit(_event=None):
    sys.exit()


# Row 0 widgets.
# label for the player entry
label_player_name = Label(text='Player name:')
label_player_name.grid(row=0, column=0, sticky=E, padx=5, pady=5)
# entry for player name
entry_player_name = Entry()
entry_player_name.grid(row=0, column=1, padx=5, pady=5)
# hovertip for player name
hovertip = Hovertip(entry_player_name,
                    text='Enter Player name')

# Row 1 widgets.
# label for score
label_score = Label(text='Score:')
label_score.grid(row=1, column=0, sticky=E, padx=5, pady=5)
# entry for score
entry_score = Entry()
entry_score.grid(row=1, column=1, padx=5, pady=5)
# hovertip for Score
hovertip = Hovertip(entry_score,
                    text='Enter Score')

# Row 2 widgets.
# label for result
label_output = Label(text='Ranking:')
label_output.grid(row=2, column=0, sticky=NE, padx=5, pady=5)
# result display
display_output = Label(width=20, height=12, bd=2, relief=SUNKEN)
display_output.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky=W)
# hovertip for result display
hovertip = Hovertip(display_output, text='Displays Result')

# Row 3 widgets.
# submit Button
submit_button = Button(width=10, bg='deepskyblue', text='Submit',
                          command=submit)
submit_button.grid(row=3, column=0, padx=5, pady=5)
# clear button
clear_button = Button(width=10, bg='yellow', text='Clear', command=clear)
clear_button.grid(row=3, column=1, padx=5, pady=5)
# exit button
exit_button = Button(width=10, bg='red', text='Exit', command=exit)
exit_button.grid(row=3, column=2, padx=5, pady=5)
# Hovertip for submit button
hovertip = Hovertip(submit_button, text='Click to submit')
# Hovertip for reset button
hovertip = Hovertip(clear_button, text='Click to reset')
# Hovertip for close button
hovertip = Hovertip(exit_button, text='Click to exit')
# Add hotkey support.
# Enter key to Submit
window.bind('<Return>', submit)
# Escape key to reset
window.bind('<Escape>', clear)
# Alt + x key to exit
window.bind('<Alt-x>', exit)

clear()

# window.mainloop()
window.mainloop()
