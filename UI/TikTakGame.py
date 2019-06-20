#python tikTak toy game

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def btnClick(id):
    print("ID: {} ".format(id))


def main():

    root = Tk()
    root.title("Python Game : Player 1")

    #add button
    btn1 = ttk.Button(root,text='')
    btn1.grid(row=0,column=0,sticky='snew',ipadx='40',ipady='40')
    #call button click to refelect id: on click
    btn1.config(command=lambda :btnClick(1))










    root.mainloop()


if __name__ == '__main__':main()
