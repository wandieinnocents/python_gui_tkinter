#creating login page with Tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def main():

    root = Tk()
    root.title("Login Page")
    root.resizable(True,True)
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

        #message box to display data

        if(inputUsername.get() == "admin" and inputPassword.get() == "1234"):

             messagebox.showinfo(title="Login Page", message="Welcome to python man")

        else:
            messagebox.showinfo(title="Login prompt", message="Get outta here, u aint admin")



    #command login button to pick credentials from user !
    btnLogin.config(command=btnClick)

    root.mainloop()


if __name__ == '__main__':main()
