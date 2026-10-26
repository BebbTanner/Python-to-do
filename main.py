import tkinter as tk

root = tk.Tk()
root.title("To Do List")

label = tk.Label(root, text = "Test Label", font = ("Arial", 16))

label.pack(pady = 20)

"""
    These are two varibles that will get the window a preset width and height.
"""
windowWidth = 400
windowHeight = 300




"""
    This is calling the mainloop function. This should compile everything used for 
the main loop.
"""
root.mainloop()