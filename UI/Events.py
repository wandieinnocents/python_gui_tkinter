from tkinter import *
from tkinter import ttk

def keyPress(event):
    print("type: {}".format(event.type))

def main():

    root = Tk()


    #show when user preses ctr+c

    root.bind("<Control-c>",keyPress)

    root.mainloop()


if __name__ == '__main__':main()
