# import module from tkinter for UI
from tkinter import *
from subprocess import call
# creating instance of TK
root = Tk()
root.configure(background="#80C58F")
#root.geometry("600x500")

def function1():
    call(["python", "Enter.py"])
def function2():
    call(["python", "Exit.py"])

# stting title for the window
root.title("HUMAN RESOURCE MANAGEMENT USING FACE RECOGNITION")

# creating a text label
Label(root, text="Authentication Required", font=("helvatica", 40), fg="white", bg="#00BFA5", height=2).grid(row=0,rowspan=2,
                                                        columnspan=2,sticky=N + E + W + S,padx=5, pady=5)
# creating a button
Button(root, text="ENTER", font=("times new roman", 30), bg="#3F5105", fg='white', command=function1).grid(
    row=2, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

# creating second button
Button(root, text="EXIT", font=("times new roman", 30), bg="#3F5105", fg='white', command=function2).grid(
    row=3, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

root.mainloop()
