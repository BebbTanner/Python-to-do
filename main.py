"""
    So, if I remember correctly, everything in a tkinter window is displayed via a label.
    I do not remember exactly how, but I know in order to use functions that update they need to be passed to a label in a really stupid way.
    I think that I will have to review my previous alarm clock project to see if I can figure it out.

    What all am I looking to put on the window?
    I think that I want to create some type of to do list.
    I would then like to be able to add some type of function that would generate this as pdf report.

    Lore updadate:
    I have no idea where the fuck I am going with this. 
    I am literally just throwing shit at the wall and hoping that something sticks on gah frfr.
"""


import tkinter as tk
from tkinter import *
from tkinter import messagebox

cyberBlack = "#000000"
cyberRed = "#c5003c"
cyberMaroon = "#880425"
cyberYellow = "#FFD700"
cyberBlue = "#00aeff"

def generate_listbox_with_input():

    def display_text():
        # 1. Retrieve the text string from the Entry widget
        user_input = entry.get()
        
        # 2. Update the Label widget with the user's string
        output_label.config(text=f"You typed: {user_input}", bg = cyberMaroon, fg = cyberBlue)

    # This is defining the winow that will allow me to place objects within that window that I have labeled root.
    root = tk.Tk()

    # Here are my widgets that I have defined, but I removed the packing for now. So if I want to display these again I will need to repack them into my root window.
    entry = tk.Entry(root, width=30)
    submit_button = tk.Button(root, text="Display Text", command=display_text, bg = cyberMaroon, fg = cyberBlue, activebackground = cyberYellow, activeforeground = cyberBlue) 
    output_label = tk.Label(root, text="", font=("Arial", 12))

    # Here is the sizing of the window and other configurations. 
    root.title("To Do List")
    root.geometry("900x500")
    root.eval('tk::PlaceWindow . center')
    root.configure(bg=cyberBlack)
    
    # Frame for input controls
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    
    tk.Label(input_frame, text="Add Item:").pack(side=tk.LEFT)
    entry = tk.Entry(input_frame, width=20)
    entry.pack(side=tk.LEFT, padx=5)
    
    # Create listbox with scrollbar
    listbox_frame = tk.Frame(root)
    listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    scrollbar = tk.Scrollbar(listbox_frame)
    listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Functions to add and remove items
    def add_item():
        item = entry.get().strip()
        if item:
            listbox.insert(tk.END, item)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an item!")
    
    def remove_item():
        try:
            selected_index = listbox.curselection()[0]
            listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to remove!")
    
    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)
    
    tk.Button(button_frame, text="Add", command=add_item).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Remove", command=remove_item).pack(side=tk.LEFT, padx=5)
    tk.Button(input_frame, text="Add", command=add_item).pack(side=tk.LEFT, padx=5)
    
    # Bind Enter key to add function
    entry.bind('<Return>', lambda event: add_item())

    root.mainloop()

# I still have no got damned idea as to what the fuck this does.
if __name__ == "__main__":
    generate_listbox_with_input()