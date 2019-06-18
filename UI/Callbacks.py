from tkinter import *
from tkinter import ttk

def btnClick():
    print("Button is clicked")

def main():

    root = Tk()
    #add button
    button = ttk.Button(root,text="wandie, click me", command=btnClick).pack()
    button.pack()

    root.mainloop()


if __name__ == '__main__':main()
