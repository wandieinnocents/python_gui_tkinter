#pythonGUI

from tkinter import *

#ttk works with layouts

from tkinter import ttk
import tkinter
import _tkinter


#clicking function


def btnClick():
    print("Button clicked")



def main():

    root = Tk()
    button = ttk.Button(root, text="click me")
    button.pack()

    #enable button click
    button.config(command=btnClick())

    #invoke button from click
    button.invoke()

    button.state(['!disabled'])
    # root of the gui

    root.mainloop()


if __name__ == '__main__':main()





