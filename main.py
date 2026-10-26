import tkinter as tk

root = tk.Tk()
root.title("To Do List")

label = tk.Label(root, text = "Test Label", font = ("Arial", 16))

label.pack(pady = 20)

"""
    So I threw in some arbitrary values to see if that would atleast get the program to run and it did. So this works for now.
    But, it does not center in the screen as intended.
"""
root.geometry("400x300")

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