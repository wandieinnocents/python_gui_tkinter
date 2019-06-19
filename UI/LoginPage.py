#creating login page with Tkinter

from tkinter import *
from tkinter import ttk

def main():

    root = Tk()
    #labelUsername
    labelUsername = ttk.Label(root,text="Username: ")
    labelUsername.grid(row=0,column=0)

    #entry/inputUsername
    inputUsername = ttk.Entry(root,width="100")
    inputUsername.grid(row=0,column=1)



    #labelPassword
    labelPassword = ttk.Label(root,text="Password")
    labelPassword.grid(row=1,column=0)

    # entry/inputPassword
    inputPassword = ttk.Entry(root, width="100")
    inputPassword.grid(row=1,column=1)

    #covert password to * characters
    inputPassword.config(show="*")

    # button login
    btnLogin= ttk.Button(root, text="Login")
    btnLogin.grid(row=2,column=1)

    #display credentials on button click

    def btnClick():
        print("Username: {} , Password: {}".format(inputUsername.get(),inputPassword.get()))

    #command login button to pick credentials from user !
    btnLogin.config(command=btnClick)

    root.mainloop()


if __name__ == '__main__':main()
