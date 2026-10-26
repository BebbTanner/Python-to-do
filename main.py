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

"""
    I have tried adding different coloration to the items and this did absolutely fuck all.
"""
cyberBlack = "#000000"
cyberRed = "#c5003c"
cyberMaroon = "#880425"
cyberYellow = "#FFD300"
cyberBlue = "#00aeff"



"""
    This is a function that will allow users to add items to the list.
"""
def addItem():
    newItem = Entry.get()

    if newItem:
        Listbox.insert(tk.END, newItem)
        Entry.delete(0, tk.END)

root = tk.Tk()
root.title("To Do List")
root.geometry("900x500")
root.eval('tk::PlaceWindow . center')
root.configure(bg=cyberBlack)

Entry = tk.Entry(root)
Entry.pack(pady = 10, padx = 10, fill=tk.X)

addButton = tk.Button(root, text = "Add item", command = addItem)
addButton.pack(pady = 10, padx = 10, fill=tk.X)



root.mainloop()