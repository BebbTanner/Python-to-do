
import tkinter as tk

root = tk.Tk()
root.title("To Do List")

label = tk.Label(root, text = "Test Label", font = ("Arial", 16))

label.pack(pady = 20)

"""
    This is calling the mainloop function. This should compile everything used for 
the main loop.
"""
root.mainloop()