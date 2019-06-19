#python Frames

from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    # create frame
    frame = ttk.Frame(root)
    frame.pack()
    frame.config(height=200,width=200)

    #adding buttons to a frame
    ttk.Button(frame,text="Button 1").grid(row=0,column=0)
    ttk.Button(frame, text="Button 2").grid(row=0, column=2)
    ttk.Button(frame, text="Button 3").grid(row=0, column=3)

    #frame 2
    frame2 = ttk.Frame(root)
    frame2.pack()
    frame2.config(height=300,width=300)

    #add buttons to frame 2
    ttk.Button(frame2,text="Button X").grid(row=0,column=0)
    ttk.Button(frame2,text="Button Y").grid(row=0,column=1)
    ttk.Button(frame2, text="Button Z").grid(row=0, column=2)
    
    #label frame
    ttk.LabelFrame(height=200,width=200,text="Third text frame").pack()
    root.mainloop()




if __name__ == '__main__':main()
