#python Frames

from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    # create frame
    frame = ttk.Frame(root)
    frame.pack()
    frame.config(height=200,width=200)
    root.mainloop()




if __name__ == '__main__':main()
