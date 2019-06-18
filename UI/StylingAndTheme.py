#styling and theming in tkinter

from tkinter import *
from tkinter import ttk




def main():
    root = Tk()
    button = ttk.Button(root,text="Button 1")
    button.pack()

    btn2 = ttk.Button(root,text="Button 2")
    btn2.pack()

    btn3 = ttk.Button(root,text="Button3")
    btn3.pack()

    #addding styles and theming
    style = ttk.Style()
    style.theme_use('classic')

    #color all the buttons,
    #buttons use class TButton
    style.configure('TButton',background='blue')







    root.mainloop()




if __name__ == '__main__':main()
