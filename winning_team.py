##################################################################
#  Program title:         Winning team
#  Program Author:        Brendan Obilo
#  Date:                  19/04/2024
#
#  Description:           
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

# window = Tk()
window = Tk()

# window size
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width = WINDOW_MIN_WIDTH, height = WINDOW_MIN_HEIGHT)

# window title
window.title("Winning Team")


def winner_loser(team: str, homeScore: float, awayScore: float):
    try:
        returnValue = team.title()
        if team.lower() == 'away':
            if awayScore > homeScore:
                returnValue += '👑'
        elif team.lower() == 'home':
            if homeScore > awayScore:
                returnValue += '👑'
        else:
            returnValue = 'Please enter home or away'
        return returnValue
    except ValueError:
        return 'Error on data type'
    
# submit function
def submit(_event=None):
    try:
        returnValue = ''
        # input_team_side = string(entry_team_side.get())
        input_team_side = str(entry_team_side.get())
        # input_home_score = float(entry_home_score.get())
        input_home_score = float(entry_home_score.get())
        # input_away_score = float(entry_away_score.get())
        input_away_score = float(entry_away_score.get())
        # if input_team_side.strip() == '':
        if input_team_side.strip() == '':
            # returnValue =  'Please enter team side'
            returnValue =  'Please enter team side'
        # elif input_home_score < 0: 
        elif input_home_score < 0: 
            returnValue = 'Please enter home score greater than 0'
        elif input_away_score < 0: 
            returnValue = 'Please enter away score greater than 0'
        else:
            returnValue = winner_loser(input_team_side.strip(), input_home_score, input_away_score)
        return display_output.configure(text=returnValue)
    except ValueError:
        return display_output.configure(text='Please input a valid score')

# clear function
def clear(_event=None):
    # clear team side enry
    entry_team_side.delete(0, END)
    # clear display output
    display_output.configure(text = "")
    # set focus on team side entry
    entry_team_side.focus()
    # clear home score 
    entry_home_score.delete(0, END)
    # clear away score 
    entry_away_score.delete(0, END)

# exit function
def exit(_event=None):
    sys.exit()
    
# Row 0 widgets.
# label for the home or away
label_team_side = Label(text='Team side:')
label_team_side.grid(row=0, column=0, sticky=E, padx=5, pady=5)
# entry for team side
entry_team_side = Entry()
entry_team_side.grid(row=0, column=1, padx=5, pady=5)
# hovertip for team side
hovertip = Hovertip(entry_team_side,
                    text='Enter Home or Away')

# Row 1 widgets.
# label for home score
label_home_score= Label(text='Home Score:')
label_home_score.grid(row=1, column=0, sticky=E, padx=5, pady=5)
# entry for home score
entry_home_score = Entry()
entry_home_score.grid(row=1, column=1, padx=5, pady=5)
# hovertip for home score entry
hovertip = Hovertip(entry_home_score,
                    text='Enter score for home team')
# label for away score
label_away_score= Label(text='Away Score:')
label_away_score.grid(row=1, column=2, sticky=E, padx=5, pady=5)
# entry for away score
entry_away_score = Entry()
entry_away_score.grid(row=1, column=3, padx=5, pady=5)
# hovertip for away score entry
hovertip = Hovertip(entry_away_score,
                    text='Enter score for away team')

# Row 2 widgets.
# label for result
label_output = Label(text='Result:')
label_output.grid(row=2, column=0, sticky=NE, padx=5, pady=5)
# result display
display_output = Label(width=20, bd=2, relief=SUNKEN)
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
