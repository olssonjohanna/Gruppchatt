from Client import ClientMainFuncs, GUIClassFile
import tkinter as tk
import tkinter.messagebox

def IP_and_port():
    ClientMainFuncs.Client()

def register(name_entry,email_entry,username_entry,password_entry, child):

    file = open("users.txt", "a")

    file.write(name_entry+ "\n")
    file.write(email_entry+ "\n")
    file.write(username_entry+ "\n")
    file.write(password_entry+ "\n")
    file.write("\n")

    file.close()

    file = open("users.txt", "r")
    list = [line.rstrip() for line in open('users.txt')]

    for i in range (len(list)):
        if i ==  email_entry:
            tk.messagebox.showinfo("Error", "Email already exist, try to login")
            child.destroy()
            return

        else:
            tk.messagebox.showinfo("Sucess", "You are now registred. Please login!")
            child.destroy()
            return

    for i in range (len(list)):
        if i == username_entry:
            tk.messagebox.showinfo("Error", "Username already exist, pick a new one")
            username_entry.delete()
            return

        else:
            tk.messagebox.showinfo("Sucess", "You are now registred. Please login!")
            child.destroy()
            return

    file.close()

def login(username_entry,password_entry,self,new_root,my_ip,my_port):
    new_root.destroy()

    login_info = [line.rstrip() for line in open('users.txt')]
    found = False
    a = 0

    for i in range (len(login_info)):
        if a == 2:
            if login_info[i] == username_entry and login_info[i+1] == password_entry:
                obj = ClientMainFuncs.Client(my_ip, my_port, self)
                obj.run()
                obj.chatWindow()
                obj.startRecv()
                found = True
        if a == 4:
            a = 0
        else:
            a = a+1

    if found == False:
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showerror("Error","Invalid username/password")
        GUIClassFile.GuiClass.login_and_register(self)

def createChatWindow(socket):
    GUIClassFile.GuiClass.chatWindow(socket)


