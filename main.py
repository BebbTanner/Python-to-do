"""
    So, if I remember correctly, everything in a tkinter window is displayed via a label.
    I do not remember exactly how, but I know in order to use functions that update they need to be passed to a label in a really stupid way.
    I think that I will have to review my previous alarm clock project to see if I can figure it out.

    What all am I looking to put on the window?
    I think that I want to create some type of to do list.
    I would then like to be able to add some type of function that would generate this as pdf report.
"""


import tkinter as tk
from tkinter import *

cyberBlack = "#000000"
cyberRed = "#c5003c"
cyberMaroon = "#880425"
cyberYellow = "#FFD700"
cyberBlue = "#00aeff"

def display_text():
    # 1. Retrieve the text string from the Entry widget
    user_input = entry.get()
    
    # 2. Update the Label widget with the user's string
    output_label.config(text=f"You typed: {user_input}", bg = cyberMaroon, fg = cyberBlue)

# This is defining the winow that will allow me to place objects within that window that I have labeled root.
root = tk.Tk()

# Here are my widgets that I have defined for the window. I will add more to this documentation later.
listbox = Listbox(root, height = 10, width = 15, bg = "grey",activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
entry = tk.Entry(root, width=30)
submit_button = tk.Button(root, text="Display Text", command=display_text, bg = cyberMaroon, fg = cyberBlue, activebackground = cyberYellow, activeforeground = cyberBlue) 
output_label = tk.Label(root, text="", font=("Arial", 12))
label = Label(root, text = " FOOD ITEMS") 

# These are the items that are hardcoded in the listbox. Eventually, I will be adding some type of loop to allow the user to add items.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# Here is all of the widgets that are being packed into the window. these will be displayed in the order that they are packed in.
entry.pack(pady=10)
submit_button.pack(pady=5)
output_label.pack(pady=20)
label.pack()
listbox.pack()

# Here is the sizing of the window and other configurations. 
root.title("To Do List")
root.geometry("900x500")
root.eval('tk::PlaceWindow . center')
root.configure(bg=cyberBlack)

# This will run the main loop of the window and display it. This will always be at the bottom of the main file.
root.mainloop()