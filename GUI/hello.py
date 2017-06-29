# IMPORT LIBRARIES
import tkinter
from tkinter import messagebox


# APPLICATION ELEMENTS
# **************************************************
top = tkinter.Tk()


# ACTION LISTENERS
# **************************************************
def helloCallBack():
    messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)


# LAYOUT GENERATION
# **************************************************
B.pack()
top.mainloop()