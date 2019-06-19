#creating readio buttons

from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    #add checkbox
    checkBox = ttk.Checkbutton(root,text="Male ?")
    checkBox.pack()

    root.mainloop()




if __name__ == '__main__':main()
