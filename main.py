"""
    So, if I remember correctly, everything in a tkinter window is displayed via a label.
    I do not remember exactly how, but I know in order to use functions that update they need to be passed to a label in a really stupid way.
    I think that I will have to review my previous alarm clock project to see if I can figure it out.

    What all am I looking to put on the window?
    I think that I want to create some type of to do list.
    I would then like to be able to add some type of function that would generate this as pdf report.
"""


import tkinter as tk
from tkinter import ttk

"""
    I have tried adding different coloration to the items and this did absolutely fuck all.
"""
darkBackground = "#1c1c1c"
darkText = "#ffffff"
darkWdiget = "#2d2d2d"

root = tk.Tk()
root.title("To Do List")

"""
    This will configure the window to have the values that I have defined above.
"""
root.configure(bg=darkBackground)

label = tk.Label(root, text = "Test Label bottom", font = ("Arial", 16))
label2 = tk.Label(root, text = "Test Label top", font = ("Arial", 16))

label2.pack(pady = 10)
label.pack(pady = 10)

"""
    So I threw in some arbitrary values to see if that would atleast get the program to run and it did. So this works for now.
    But, it does not center in the screen as intended.

    This is a window with predefined dimensions.
"""
root.geometry("600x500")

"""
    This in theory should center the window on the screen. Spoiler, it does not however, It does reposition the window once it has been created.
    So that's atleast a step up from it just appearing the in corner of the screen.
"""
root.eval('tk::PlaceWindow . center')

"""
    This is calling the mainloop function. This should compile everything used for 
the main loop.
"""
root.mainloop()