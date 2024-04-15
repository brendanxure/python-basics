# Author: Brendan Obilo
# Date: March 28, 2023
# Description:
# This program uses a tkinter UI to help someone determine whether
# they should pass another car.

from tkinter import *
from idlelib.tooltip import Hovertip
import sys

# Variables and Constants

# WINDOW_WIDTH = 500
WINDOW_WIDTH = 500
# WINDOW_HEIGHT = 250
WINDOW_HEIGHT = 250
# WINDOW_MIN_WIDTH = 500
WINDOW_MIN_WIDTH = 500
# WINDOW_MIN_HEIGHT = 200
WINDOW_MIN_HEIGHT = 200
# MINUTES_PER_HOUR = 60
MINUTES_PER_HOUR = 60
# ZERO = 0
ZERO = 0

# window = Tk()
window = Tk()

# window size
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width = WINDOW_MIN_WIDTH, height = WINDOW_MIN_HEIGHT)

# window title
window.title("Speed Difference")

# calculate function
def calculate(_event=None):
    try:
        # Get the value from entry_speed_1 and treat it as a number.
        speed_one = float(entry_speed_1.get())
        # If entry is not numbers:
    except:
        # return error if entry_speed_1 is not a number
        return label_output.configure(text = "Error: Current driving" +
                                      " speed must be numeric.")
    
    try:
        # Get the value from entry_speed_2 and treat it as a number.
        speed_two = float(entry_speed_2.get())
        # If entry is not numbers:
    except:
        # return error if entry_speed_2 is not a number
        return label_output.configure(text = "Error: Desired driving" +
                                      " speed must be numeric.")

    try:
        # check if speed one and speed two is greater than zero
        if speed_one > ZERO and speed_two > ZERO:
            # low speed is minimum between the two
            low_speed = min((speed_one, speed_two))
            # High speed is maximum between the two
            high_speed = max((speed_one, speed_two))

            # speed_difference = high_speed - low_speed
            speed_difference = high_speed - low_speed

            # speed_difference_seconds = speed_difference / MINUTES_PER_HOUR
            speed_difference_seconds = speed_difference / MINUTES_PER_HOUR

            # print output
            label_output.configure(text = "Going from "
                                   + str(round(low_speed, 1)) + "km/h to "
                                   + str(round(high_speed, 1)) + \
                                    "km/h can gain you "
                                    + str(round(speed_difference_seconds, 2))
                                    + " kilometres per minute.")
        else:
            # print error for input number range
            return label_output.configure(text = "Error: speed entries" +
                                          " must be a positive number.")
    except:
        # print error for datatype error
        return label_output.configure(text = "Error: Please try again later.")

# reset function
def reset(_event=None):
    # clear entry speed 1
    entry_speed_1.delete(0, END)
    entry_speed_2.delete(0, END)
    label_output.configure(text = "")
    entry_speed_1.focus()

# exit function
def exit(_event=None):
    sys.exit()


# Now you need to set up the widgets!
# Note that if you use the exact names I did in the functions above,
# you won't need to modify those.
# If you use a different naming scheme, expect the functions to require
# some changes.


# Row 0 widgets.
label_speed_1 = Label(text='Current Driving Speed:')
label_speed_1.grid(row=0, column=0, sticky=E, padx=5, pady=5)
entry_speed_1 = Entry()
entry_speed_1.grid(row=0, column=1, padx=5, pady=5)
hovertip = Hovertip(entry_speed_1, text='Enter Current Driving Speed')

# Add widgets for all rows, based on your plan.
# Row 1 widgets.
label_speed_2 = Label(text='Desired Driving Speed:')
label_speed_2.grid(row=1, column=0, sticky=E, padx=5, pady=5)
entry_speed_2 = Entry()
entry_speed_2.grid(row=1, column=1, padx=5, pady=5)
hovertip = Hovertip(entry_speed_2, text='Enter Desired Driving Speed')

# Row 2 widgets.
label_output_prompt = Label(text='Speed Difference:')
label_output_prompt.grid(row=2, column=0, sticky=E, padx=5, pady=5)
label_output = Label(width=36, bd=2, relief=SUNKEN)
label_output.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
hovertip = Hovertip(label_output, text='Displays Speed Difference')

# Row 3 widgets.
# calculate Button
calculate_button = Button(width=10, bg='green', text='Calculate',
                          command=calculate)
calculate_button.grid(row=3, column=0, padx=5, pady=5)
# reset button
reset_button = Button(width=10, bg='yellow', text='Reset', command=reset)
reset_button.grid(row=3, column=1, padx=5, pady=5)
# close button
close_button = Button(width=10, bg='red', text='Close', command=exit)
close_button.grid(row=3, column=2, padx=5, pady=5)
# Hovertip for calculate button
hovertip = Hovertip(calculate_button, text='Click to calcuate')
# Hovertip for reset button
hovertip = Hovertip(reset_button, text='Click to reset')
# Hovertip for close button
hovertip = Hovertip(close_button, text='Click to exit')
# Add hotkey support.
# Enter key to calculate
window.bind('<Return>', calculate)
# Escape key to reset
window.bind('<Escape>', reset)
# Alt + x key to exit
window.bind('<Alt-x>', exit)

# window.mainloop()
window.mainloop()
