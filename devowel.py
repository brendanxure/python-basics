# Author: Brendan Obilo
# Date:   26/03/2024
# Description:
# Removes the vowels from a piece of text in a tkinter GUI.
# As part of the Pre-Class Activity, you only have to modify
# a small part of this file!
# !!! Do not modify from here until specified. !!!

# Imports.
import tkinter as tk
from idlelib.tooltip import Hovertip

# Set up the window and a tkinter string variable.
window = tk.Tk()
text_content = tk.StringVar()


# This function SHOULD return a string with no vowels in it.
def remove_vowels(_event=None):
    input_string = text_content.get()
    # !!! Begin modifying the code !!!

    # This following line is a placeholder; it should be changed or removed.
    string_with_no_vowels = ""

    # Modify this part of the function to take "input_string"
    # and remove all vowels from it.
    # The resulting string value should be stored in string_with_no_vowels.
    vowels = "aeiou"
    for element in input_string:
        if element.lower() not in vowels:
            string_with_no_vowels += element

    # !!! No need to modify the rest of the file !!!
    text_content.set(string_with_no_vowels)
    print(string_with_no_vowels)
    return string_with_no_vowels


# Set up the two required tkinter widgets (with Hovertips).
text_field = tk.Entry(textvariable=text_content)
Hovertip(text_field, text="Enter text to remove vowels from.")
text_field.pack()
devoweler = tk.Button(text="Devowel", command=remove_vowels)
Hovertip(devoweler, text="Click to remove vowels.")
devoweler.pack()

# Set up a single hotkey for the Enter button.
window.bind("<Return>", remove_vowels)

window.mainloop()
