#tickt reservation

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()

#fullname label
ttk.Label(root, text="Full Name:").grid(row=0,column=0)

#entry
inputFullname = ttk.Entry(root,width=30, font = ('Arial',10))
inputFullname.grid(row=0,column=1,columnspan=2)

#gender label
SpanGender = StringVar()
SpanGender.set("Male")
ttk.Radiobutton(root,text="Male",variable=SpanGender,value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender,value="Female").grid(row=2,column=1)

ttk.Label(root, text="Gender").grid(row=1,column=0)

#comments label

TextComments = Text(root,width=30,height=40,font = ('Arial',10))
ttk.Label(root, text="Comment:").grid(row=2,column=0)

#button
ttk.Button(root,text="Submit").grid(row=3,column=3)



root.mainloop()