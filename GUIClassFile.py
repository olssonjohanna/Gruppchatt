import tkinter as tk

class GuiClass:

    def __init__(self):
        self.root = tk.Tk()
        self.first_page()
        self.root.mainloop()

    def chatWindow():
        root = tk.Tk()
        root.geometry('{}x{}'.format(600, 400))
        tk.Label(text="one").pack()
        windowFrame = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        windowFrame.pack(fill=tk.X, padx=5, pady=5)
        chatFrame = tk.Frame(height=10,bd = 1, width = 40,padx = 5)
        chatFrame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(text="two").pack()
        root.mainloop()

    def first_page(self):

        # REGISTER NEW SUBFUNC
        def sub_func_register(root):
            child = tk.Toplevel(root)

            name = tk.Label(child, text="Name: ")
            name_entry = tk.Entry(child)

            email = tk.Label(child, text="Email: ")
            email_entry = tk.Entry(child)

            username = tk.Label(child, text="Username: ")
            username_entry = tk.Entry(child)

            password = tk.Label(child, text="Password: ")
            password_entry = tk.Entry(child)

            register_button = tk.Button(self.root, text="REGISTER", command= self.first_page)

            name.grid()
            name_entry.grid()
            email.grid()
            email_entry.grid()
            username.grid()
            username_entry.grid()
            password.grid()
            password_entry.grid()
            login_button.grid()
            register_button.grid()

        username = tk.Label(self.root, text="Username: ")
        username_entry = tk.Entry(self.root)

        password = tk.Label(self.root, text="Password: ")
        password_entry = tk.Entry(self.root)

        login_button = tk.Button(self.root, text="LOGIN")   #denna ska trigga chattfönstret

        register_button = tk.Button(self.root, text="REGISTER NEW", command = lambda: sub_func_register(self.root))

        username.grid()
        username_entry.grid()
        password.grid()
        password_entry.grid()
        login_button.grid()
        register_button.grid()