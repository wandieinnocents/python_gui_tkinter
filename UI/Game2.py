#python tikTak toy game
from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#Global Variables
ActivePlayer = 1
player1 = [] #what player one selected
player2 = [] #what player two selected

def btnClick(id):

    #import global variables
    global ActivePlayer
    global player1
    global player2
    #alternate player symbols on p
    if(ActivePlayer == 1):
        SetLayout(id,"X")
        player1.append(id)
        root.title("Tic Tac palyer 2:")
        ActivePlayer =2
        print("Player 1: {}".format(player1))
    elif(ActivePlayer == 2):
        SetLayout(id, "O")
        player2.append(id)
        root.title("Tic Tac palyer 1:")
        ActivePlayer = 1
        print("Player 1: {}".format(player1))



# layout function
def SetLayout(id,PlayerSymbol):

    if(id==1):
        btn1.config(text=PlayerSymbol)
        btn1.state(['disabled'])
    elif id==2:
        btn2.config(text=PlayerSymbol)
        btn2.state(['disabled'])
    elif id==3:
        btn3.config(text=PlayerSymbol)
        btn3.state(['disabled'])
    elif id==4:
        btn4.config(text=PlayerSymbol)
        btn4.state(['disabled'])
    elif id==5:
        btn5.config(text=PlayerSymbol)
        btn5.state(['disabled'])
    elif id==6:
        btn6.config(text=PlayerSymbol)
        btn6.state(['disabled'])
    elif id==7:
        btn7.config(text=PlayerSymbol)
        btn7.state(['disabled'])
    elif id==8:
        btn8.config(text=PlayerSymbol)
        btn8.state(['disabled'])
    elif id==9:
        btn9.config(text=PlayerSymbol)
        btn9.state(['disabled'])




    print("ID: {} ".format(id))



def main():

    root = Tk()
    root.title("Python Game : Player 1")

    #add button 1
    global btn1
    btn1 = ttk.Button(root,text='')
    btn1.grid(row=0,column=0,sticky='snew',ipadx='40',ipady='40')
    #call button click to refelect id: on click
    btn1.config(command=lambda :btnClick(1))

    # add button 2
    global btn2
    btn2 = ttk.Button(root, text='')
    btn2.grid(row=0, column=1, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn2.config(command=lambda: btnClick(2))

    # add button 3
    global btn3
    btn3 = ttk.Button(root, text='')
    btn3.grid(row=0, column=2, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn3.config(command=lambda: btnClick(3))

    # add button 4
    global btn4
    btn4 = ttk.Button(root, text='')
    btn4.grid(row=1, column=0, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn4.config(command=lambda: btnClick(4))

    # add button 5
    global btn5
    btn5 = ttk.Button(root, text='')
    btn5.grid(row=1, column=1, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn5.config(command=lambda: btnClick(5))

    # add button 6
    global btn6
    btn6 = ttk.Button(root, text='')
    btn6.grid(row=1, column=2, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn6.config(command=lambda: btnClick(6))

    # add button 7
    global btn7
    btn7 = ttk.Button(root, text='')
    btn7.grid(row=2, column=0, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn7.config(command=lambda: btnClick(7))

    # add button 8
    global btn8
    btn8 = ttk.Button(root, text='')
    btn8.grid(row=2, column=1, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn8.config(command=lambda: btnClick(8))

    # add button 9
    global btn9
    btn9 = ttk.Button(root, text='')
    btn9.grid(row=2, column=2, sticky='snew', ipadx='40', ipady='40')
    # call button click to refelect id: on click
    btn9.config(command=lambda: btnClick(9))










    root.mainloop()


if __name__ == '__main__':main()
