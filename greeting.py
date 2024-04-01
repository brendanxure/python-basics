#######################################################
#  Program title:         Greeting
#  Program Author:        Brendan Obilo
#  Date:                  26/03/2024
#
#  Description:           Created a user interface using tkinter
#                         where the button is clicked and hello is displayed
#########################################################


# from tkinter import *
from tkinter import *

# window = Tk()
window = Tk()

# set properties for windows
window.geometry("350x250")
window.minsize(width=250, height=150)
window.title('Greeting')


# output to display function
def display_hello(_event=None):
    # prints the out "Hello!"
    label_user_display.configure(text='Hello!')


# row 0 widgets
label_user_display = Label(text='Should I say something')
label_user_display.pack()

# row 1 widgets
button_user_submit = Button(text='Say Hello!', padx=2, pady=2,
                            command=display_hello)
button_user_submit.pack()
# window.mainloop()
window.mainloop()
