"""
    So, if I remember correctly, everything in a tkinter window is displayed via a label.
    I do not remember exactly how, but I know in order to use functions that update they need to be passed to a label in a really stupid way.
    I think that I will have to review my previous alarm clock project to see if I can figure it out.

    What all am I looking to put on the window?
    I think that I want to create some type of to do list.
    I would then like to be able to add some type of function that would generate this as pdf report.
"""


import tkinter as tk
from tkinter import Entry, Listbox, ttk

cyberBlack = "#000000"
cyberRed = "#c5003c"
cyberMaroon = "#880425"
cyberYellow = "#FFD700"
cyberBlue = "#00aeff"

def display_text():
    # 1. Retrieve the text string from the Entry widget
    user_input = entry.get()
    
    # 2. Update the Label widget with the user's string
    output_label.config(text=f"You typed: {user_input}")

root = tk.Tk()
root.title("User Input Example")
root.geometry("400x200")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Display Text", command=display_text, bg = cyberMaroon, fg = cyberBlue, activebackground = cyberYellow, activeforeground = cyberBlue) 
submit_button.pack(pady=5)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=20)

root.title("To Do List")
root.geometry("900x500")
root.eval('tk::PlaceWindow . center')
root.configure(bg=cyberBlack)

root.mainloop()