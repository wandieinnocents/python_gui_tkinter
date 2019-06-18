#button and entry or input

from tkinter import *
from tkinter import ttk




def main():
    #root of the layout
    root = Tk()

    # input
    entry = ttk.Entry(root, width=60)
    entry.pack()


    #writing button
    button = ttk.Button(root, text="click ass")
    button.pack()

    # buttonClickFunction
    def btnClicking():
        print(entry.get())
        #delete button entry after clicking
        entry.delete(0,3)

    button.config(command=btnClicking)

    #display the layout to user
    root.mainloop()


if __name__ == '__main__':main()
