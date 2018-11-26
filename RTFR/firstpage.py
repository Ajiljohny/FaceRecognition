#import module from tkinter for UI
from tkinter import *
from subprocess import call

import os

#creating instance of TK
root=Tk()

root.configure(background="#80D8FF")

#root.geometry("600x600")

def function1():
    call(["python", "Detection.py"])
    #os.system("python Recognition.py")
    
def function2():
    
    os.system("python facultylogin.py")

def function3():

    os.system("python c:/python27/face/command.py")

#stting title for the window
root.title("HUMAN RESOURCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="SELECT YOUR OPTION",font=("helvatica",40),fg="white",bg="#00BFA5",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating a button
Button(root,text="UPDATE DATABASE",font=("times new roman",30),bg="#3F51B5",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="FACULTY LOGIN",font=("times new roman",30),bg="#3F51B5",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="COMPARE",font=('times new roman',30),bg="#3F51B5",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
