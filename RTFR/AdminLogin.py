import os
import sys
from tkinter import *
from subprocess import call
from PIL import Image, ImageTk

root = Tk()

root.title("HUMAN RESOURCE MANAGEMENT USING FACE RECOGNITION")

root.configure(bg="#D7CCC8")

root.focus_set()

num = 0;

def enter_the_value():
    uid = e1.get()

    #sid = uid[7:]

    #db = uid[0:6]


    password = e2.get()

    # to authenticate
    if (password == "12345" and uid=="Admin"):
        # storing the output in a wamp directory(here in windows)
        fh = open("c:/wamp/www/attendance/pyoutput/OP_0.txt", "w")

        fh.write(uid)

        fh.close()

        call(["python", "AdminHome.py"])

        root.destroy

if __name__ == "__main__":
    Label(root, text="ENTER CREDENTIALS", fg='white', bg='#424242', font=("helvetica", 40), width=23).grid(rowspan=2,
                        columnspan=3,sticky=E + W + N + S,padx=5, pady=5)

    Label(root, text="Enter ID: ", font=("helvetica ", 30), fg='#212121', bg="#D7CCC8").grid(row=2, sticky=E, column=0)

    Label(root, text="Enter password: ", font=("helvetica ", 30), fg='#212121', bg="#D7CCC8").grid(row=3, sticky=E,
                                                                                                   column=0)

    e1 = Entry(root)

    e2 = Entry(root)

    e1.grid(row=2, column=1, columnspan=2, sticky=W)

    e2.grid(row=3, column=1, columnspan=2, sticky=W)


    Button(root, text="CLEAR", font=("times new roman", 30), fg="white", bg="#3E2723", command=root.quit).grid(row=4,
                            column=0,pady=10,padx=10,sticky=E + W + N + S)

    Button(root, text="ENTER", font=("times new roman", 30), fg="white", bg="#3E2723", command=enter_the_value).grid(
        row=4, column=1, pady=10, padx=10, sticky=E + W + N + S)

    # Label(root, text="total number of faces detected are: ",fg="#212121",bg="#607D8B",font=(10)).grid(row=5,column=0,sticky=E)

    # Label( root, textvariable=var1,fg="#000000",font=(10)).grid(row=5,column=1)

    # Button(root,text="NEXT",width=5,height=3,command=run_command).grid(row=6,columnspan=2)

root.mainloop()
