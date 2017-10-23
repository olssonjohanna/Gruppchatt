import tkinter as tk
import GUIFunctions
import tkinter.messagebox
class GuiClass:

    def __init__(self):
        self.root = tk.Tk()
        self.first_page()
        self.root.mainloop()

    def updateChat(self,text):
        self.windowText.config(state=tk.NORMAL)
        self.windowText.insert(tk.END,text+"\n")
        self.windowText.config(state=tk.DISABLED)
        self.windowText.see(tk.END)

    def retrieve_input(self):
        input = self.chatText.get('1.0', tk.END)
        self.chatText.delete('1.0', tk.END)
        self.updateChat(input)

    def chatWindow(self):
        root = tk.Tk()

        root.geometry('{}x{}'.format(600, 400))
        root.resizable(False, False)

        chatFrame = tk.Frame(height='250',bd = 1, width = '100',padx = 5)
        textFrame = tk.Frame(height='250',bd = 1,width='100',padx = 5)
        self.windowText = tk.Text(chatFrame,height='15',width='70')
        self.chatText = tk.Text(textFrame,height='5',width='60')
        sendBtn = tk.Button(textFrame,text='Send',height = '5',width=10,command = lambda: self.retrieve_input())

        scrollb = tk.Scrollbar(chatFrame, command=self.windowText.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.windowText['yscrollcommand'] = scrollb.set

        root.bind("<Return>", lambda x: self.retrieve_input())

        self.windowText.config(state=tk.DISABLED)

        self.windowText.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        chatFrame.grid_rowconfigure(0, weight=1)
        chatFrame.grid_columnconfigure(0, weight=1)
        chatFrame.pack(fill=tk.X, padx=5, pady=20)
        textFrame.pack(fill=tk.X, padx=5, pady=20)
        self.chatText.grid(row=0)
        sendBtn.grid(row=0,column=1)

        root.mainloop()

    def login_and_register(self):

        #SUBFUNC TO REGISTER NEW
        def sub_func_register(root, login):
            child = tk.Toplevel(root)

            welcome_register = tk.Label(child, text="REGISTER NEW USER")

            name = tk.Label(child, text="Name: ")
            name_entry = tk.Entry(child)

            email = tk.Label(child, text="Email: ")
            email_entry = tk.Entry(child)

            username = tk.Label(child, text="Username: ")
            username_entry = tk.Entry(child)

            password = tk.Label(child, text="Password: ")
            password_entry = tk.Entry(child)

            register_button = tk.Button(child, text="REGISTER", command= GUIFunctions.register(name_entry.get(), email_entry.get(), username_entry.get(), password_entry.get()))

            welcome_register.grid(row=0, column=0)
            name.grid(row=1, column=0)
            name_entry.grid(row=1, column=1)
            email.grid(row=2, column=0)
            email_entry.grid(row=2, column=1)
            username.grid(row=3, column=0)
            username_entry.grid(row=3, column=1)
            password.grid(row=4, column=0)
            password_entry.grid(row=4, column=1)
            register_button.grid(row=5, column=0)

        new_root = tk.Tk()

        try:
            self.root.destroy()

        except:
            pass


        print ("we are here")

        username = tk.Label(new_root, text="Username: ")
        username_entry = tk.Entry(new_root)

        password = tk.Label(new_root, text="Password: ")
        password_entry = tk.Entry(new_root)

        login_button = tk.Button(new_root, text="LOGIN", command=lambda: GUIFunctions.login(username_entry.get(),password_entry.get()))

        register_button = tk.Button(new_root, text="REGISTER NEW USER", command=lambda: sub_func_register(new_root))

        username.grid(row=0, column=0)
        username_entry.grid(row=0, column=1)
        password.grid(row=1, column=0)
        password_entry.grid(row=1, column=1)
        login_button.grid(row=2, column=0)
        register_button.grid(row=2, column=1)

        new_root.mainloop()

    def first_page(self):
        ip = tk.Label(self.root, text="IP: ")
        ip_entry = tk.Entry(self.root)

        port = tk.Label(self.root, text="Port: ")
        port_entry = tk.Entry(self.root)
        port_var = 0
        ip_var = ""

        def getValue(ip,port,entry1,entry2):
         try:
            ip_send = entry1.get()
            port_send = int(entry2.get())
            GUIFunctions.create_Connections(ip_send,port_send)
            self.login_and_register()
         except ValueError:
             tkinter.messagebox.showinfo("Error","Port should be a number")
             return False

        enter_button = tk.Button(self.root, text="ENTER", command = lambda: getValue(ip_var,port_var,ip_entry,port_entry))

        ip.grid(row=0, column=0)
        ip_entry.grid(row=0, column=1)
        port.grid(row=1, column=0)
        port_entry.grid(row=1, column=1)
        enter_button.grid(row=2, column=0)