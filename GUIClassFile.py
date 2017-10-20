import tkinter as tk

class GuiClass:

    def __init__(self):
        self.root = tk.Tk()
        self.first_page()
        self.root.mainloop()

    def chatWindow(self, new_root):
        root = tk.Tk()
        new_root.destroy()

        root.geometry('{}x{}'.format(600, 400))
        tk.Label(text="one").pack()
        windowFrame = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        windowFrame.pack(fill=tk.X, padx=5, pady=5)
        chatFrame = tk.Frame(height=10,bd = 1, width = 40,padx = 5)
        chatFrame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(text="two").pack()
        root.mainloop()

    def first_page(self):

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

            register_button = tk.Button(child, text="REGISTER", command= login)

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

        #SECOND WINDOW: LOGIN AND REGISTER
        def login_and_register():
            new_root = tk.Tk()
            #self.root.destroy() TEST TRY EXCEPT HÄR ?!

            username = tk.Label(new_root, text="Username: ")
            username_entry = tk.Entry(new_root)

            password = tk.Label(new_root, text="Password: ")
            password_entry = tk.Entry(new_root)

            login_button = tk.Button(new_root, text="LOGIN", command= lambda: self.chatWindow(new_root))

            register_button = tk.Button(new_root, text="REGISTER NEW USER", command= lambda: sub_func_register(new_root, login_and_register))

            username.grid(row=0, column=0)
            username_entry.grid(row=0, column=1)
            password.grid(row=1, column=0)
            password_entry.grid(row=1, column=1)
            login_button.grid(row=2, column=0)
            register_button.grid(row=2, column=1)

        #FIRST PAGE: IP AND PORT
        ip = tk.Label(self.root, text="IP: ")
        ip_entry = tk.Entry(self.root)

        port = tk.Label(self.root, text="Port: ")
        port_entry = tk.Entry(self.root)

        enter_button = tk.Button(self.root, text="ENTER", command= login_and_register)

        ip.grid(row=0, column=0)
        ip_entry.grid(row=0, column=1)
        port.grid(row=1, column=0)
        port_entry.grid(row=1, column=1)
        enter_button.grid(row=2, column=0)