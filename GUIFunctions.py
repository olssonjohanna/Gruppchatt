import ClientMain
import GUIClassFile
from tkinter import messagebox
import tkinter as tk

def IP_and_port(get_ip, get_port):
    ClientMain.Client(get_ip, get_port)

def register(name_entry,email_entry,username_entry,password_entry, child,self):

    file = open("Users.txt", "a")

    file.write(name_entry+ "\n")
    file.write(email_entry+ "\n")
    file.write(username_entry+ "\n")
    file.write(password_entry+ "\n")
    file.write("\n")

    file.close()

    file = open("Users.txt", "r")
    list = [line.rstrip() for line in open('users.txt')]

    for i in range (len(list)):
        if i ==  email_entry:
            messagebox.showinfo("Error", "Email already exist, try to login")
            child.destroy()
            return

        else:
            messagebox.showinfo("Sucess", "You are now registred. Please login!")
            child.destroy()
            return

    for i in range (len(list)):
        if i == username_entry:
            messagebox.showinfo("Error", "Username already exist, pick a new one")
            username_entry.delete()
            return

        else:
            messagebox.showinfo("Sucess", "You are now registred. Please login!")
            child.destroy()
            return

    file.close()

def login(username_entry,password_entry,self, new_root,my_ip,my_port):
    from GUIClassFile import GuiClass
    from ServerFunc import ServerMain
    new_root.destroy()

    login_info = [line.rstrip() for line in open('users.txt')]
    found = False
    a = 0

    for i in range (len(login_info)):
        if a == 2:
            if login_info[i] == username_entry and login_info[i+1] == password_entry:
                print("1")
                serverObj = ServerMain()
                print("2")
                obj = ClientMain.Client(my_ip,my_port,self)
                print("3")
                obj.run()
                print("4")
                obj.chatWindow()
                print("5")
                serverObj.startRecv()
                print("6")
                obj.startRecv()
                print("7")
                found = True
        if a == 4:
            a = 0
        else:
            a = a+1

    if found == False:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error","Invalid username/password")
        GuiClass.login_and_register(self)

    def createChatWindow(socket):
        GUIClassFile.GuiClass.chatWindow(socket)


