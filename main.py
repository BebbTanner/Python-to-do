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
    These are two preset functions that will detect the width and the height of the user's screen.
"""
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

"""
    In theory, this should center the window on the user's screen.
"""
centerX = int(screenWidth/2 - windowWidth/2)
centerY = int(screenHeight/2 - windowHeight/2)

"""
    This is calling the mainloop function. This should compile everything used for 
the main loop.
"""
root.mainloop()