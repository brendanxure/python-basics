##################################################################
#  Program title:         Temperature Conversion
#  Program Author:        Brendan Obilo
#  Date:                  06/04/2024
#
#  Description:           Creating Graphic User Interface that will
#                         accept a temperature as either 
#                         Celsius or Fahrenheit and convert that 
#                         temperature to the other scale.
##################################################################

# import tkinter
from tkinter import *
# import hovertip
from idlelib.tooltip import Hovertip
# import sys
import sys
# import math
import math

# Variables and Constants

# WINDOW_WIDTH = 500
WINDOW_WIDTH = 500
# WINDOW_HEIGHT = 250
WINDOW_HEIGHT = 250
# WINDOW_MIN_WIDTH = 500
WINDOW_MIN_WIDTH = 500
# WINDOW_MIN_HEIGHT = 200
WINDOW_MIN_HEIGHT = 200
# CONVERSION_CONSTANT_1 = 1.8
CONVERSION_CONSTANT_1 = 1.8
# CONVERSION_CONSTANT_2 = 32
CONVERSION_CONSTANT_2 = 32
# CELSIUS = 'Celsius'
CELSIUS = 'Celsius'
# FAHRENHEIT = 'Fahrenheit'
FAHRENHEIT = 'Fahrenheit'

# window = Tk()
window = Tk()

# window size
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width = WINDOW_MIN_WIDTH, height = WINDOW_MIN_HEIGHT)

# window title
window.title("Temperature Conversion")

# a varaible to store the selected radio option 
selected_radio = StringVar()
# select default radio option to radio_celsius
selected_radio.set(CELSIUS)


# convert function
def convert(_event=None):
    # try:
    try:
        # user_input()
        user_input = float(entry_temperature.get())
        # if the selected ratio is celsius
        if(selected_radio.get() == FAHRENHEIT):
            # calculate desired output
            desired_output = (user_input * CONVERSION_CONSTANT_1)\
                        + CONVERSION_CONSTANT_2
            # display the desired output
            label_output.configure(text=str(user_input) +' degrees Celsius'
                                   +' converts to '
                                   + str(math.floor(desired_output * 100)/100)
                                   + ' degrees Fahrenheit.')
        # else:
        else:
            # calculate desired output
            desired_output = (user_input - CONVERSION_CONSTANT_2)\
                             / CONVERSION_CONSTANT_1
            # display the desired output
            label_output.configure(text=str(user_input) +' degrees Fahrenheit'
                                   +' converts to '
                                   + str(math.floor(desired_output * 100)/100)
                                   + ' degrees Celsius.')
    # except ValueError:
    except ValueError:
        # display the desired output
        label_output.configure(text="ERROR: Please enter a numeric"
                                + " temperature to convert.")

# clear function
def clear(_event=None):
    # clear temperature entry
    entry_temperature.delete(0, END)
    # clear display output
    label_output.configure(text = "")
    # set focus on temperature entry
    entry_temperature.focus()
    # set default radio option to celsius
    selected_radio.set(CELSIUS)

# exit function
def exit(_event=None):
    sys.exit()

# Row 0 widgets.
# label for the temperature entry
label_temperature = Label(text='Temperature:')
label_temperature.grid(row=0, column=0, sticky=E, padx=5, pady=5)
# entry for temperature
entry_temperature = Entry()
entry_temperature.grid(row=0, column=1, padx=5, pady=5)
# hovertip for temperature
hovertip = Hovertip(entry_temperature,
                    text='Enter Temperature in Celsius or Fahrenheit')

# Row 1 widgets.
# label for unit option
label_covert_option = Label(text='Convert to:')
label_covert_option.grid(row=1, column=0, sticky=E, padx=5, pady=5)
# radio button for celsius
radio_celsius = Radiobutton(text='Celsius',
                            value=CELSIUS, variable=selected_radio)
radio_celsius.grid(row=1, column=1, padx=5, pady=5, sticky=W)
# radio button for fahrenheit
radio_fahrenheit = Radiobutton(text='Fahrenheit',
                                value=FAHRENHEIT, variable=selected_radio)
radio_fahrenheit.grid(row=1, column=2, padx=5, pady=5)
# hovertip for celsius
hovertip = Hovertip(radio_celsius,
                    text='Select to convert from Fahrenheit to Celsius')
# hovertip for fahrenheit
hovertip = Hovertip(radio_fahrenheit,
                    text='Select to convert from Celsius to Fahrenheit')

# Row 2 widgets.
# label for result
label_output_prompt = Label(text='Result:')
label_output_prompt.grid(row=2, column=0, sticky=E, padx=5, pady=5)
# result display
label_output = Label(width=45, bd=2, relief=SUNKEN)
label_output.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
# hovertip for result display
hovertip = Hovertip(label_output, text='Displays Conversion Result')

# Row 3 widgets.
# convert Button
convert_button = Button(width=10, bg='deepskyblue', text='Convert',
                          command=convert)
convert_button.grid(row=3, column=0, padx=5, pady=5)
# clear button
clear_button = Button(width=10, bg='yellow', text='Clear', command=clear)
clear_button.grid(row=3, column=1, padx=5, pady=5)
# exit button
exit_button = Button(width=10, bg='red', text='Exit', command=exit)
exit_button.grid(row=3, column=2, padx=5, pady=5)
# Hovertip for calculate button
hovertip = Hovertip(convert_button, text='Click to convert')
# Hovertip for reset button
hovertip = Hovertip(clear_button, text='Click to reset')
# Hovertip for close button
hovertip = Hovertip(exit_button, text='Click to exit')
# Add hotkey support.
# Enter key to calculate
window.bind('<Return>', convert)
# Escape key to reset
window.bind('<Escape>', clear)
# Alt + x key to exit
window.bind('<Alt-x>', exit)

clear()

# window.mainloop()
window.mainloop()
