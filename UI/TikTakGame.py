#python tikTak toy game

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def btnClick(id):
    print("ID: {} ".format(id))


def main():

    root = Tk()
    root.title("Python Game : Player 1")

    #add button 1
    btn1 = ttk.Button(root,text='')
    btn1.grid(row=0,column=0,sticky='snew',ipadx='40',ipady='40')
    #call button click to refelect id: on click
    btn1.config(command=lambda :btnClick(1))

    # add button 2
    btn2 = ttk.Button(root, text='')
    btn2.grid(row=0, column=1, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn2.config(command=lambda: btnClick(2))

    # add button 3
    btn3 = ttk.Button(root, text='')
    btn3.grid(row=0, column=2, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn3.config(command=lambda: btnClick(3))

    # add button 4
    btn4 = ttk.Button(root, text='')
    btn4.grid(row=1, column=0, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn4.config(command=lambda: btnClick(4))

    # add button 5
    btn5 = ttk.Button(root, text='')
    btn5.grid(row=1, column=1, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn5.config(command=lambda: btnClick(5))

    # add button 6
    btn6 = ttk.Button(root, text='')
    btn6.grid(row=1, column=2, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn6.config(command=lambda: btnClick(6))

    # add button 7
    btn7 = ttk.Button(root, text='')
    btn7.grid(row=2, column=0, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn7.config(command=lambda: btnClick(7))

    # add button 8
    btn8 = ttk.Button(root, text='')
    btn8.grid(row=2, column=1, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn8.config(command=lambda: btnClick(8))

    # add button 9
    btn9 = ttk.Button(root, text='')
    btn9.grid(row=2, column=2, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn9.config(command=lambda: btnClick(9))










    root.mainloop()


if __name__ == '__main__':main()