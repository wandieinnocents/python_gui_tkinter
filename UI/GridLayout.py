
#python Grid Layouts

from tkinter import *
from tkinter import ttk


def main():

    #root of layout
    root = Tk()

    #add style
    style = ttk.Style()
    style.theme_use('classic')

    #adding labels to grid format
    ttk.Label(root,text="green",background="Green").grid(row=0,column=0,padx=5,pady=5,sticky='snew')
    ttk.Label(root,text="yellow",background="Yellow").grid(row=0,column=1,padx=5,pady=5,sticky='snew')
    ttk.Label(root, text="Blue", background="Blue").grid(row=0,column=2 ,rowspan=2,sticky='snew',padx=5,pady=5)
    ttk.Label(root, text="Orange", background="Orange").grid(row=1,column=0,columnspan=2,sticky='snew',padx=5,pady=5)

    root.rowconfigure(0,weight=2)
    root.rowconfigure(1,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=2)



    #wrap up of main loop - layout
    root.mainloop()






if __name__ == '__main__':main()
