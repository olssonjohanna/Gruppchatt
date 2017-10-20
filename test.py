import tkinter as tk
import tkinter.messagebox

#USER & REGISTER FIRST PAGE
def first_page():

    # REGISTER NEW SUBFUNC
    def sub_func_register():
        child = tkinter.Toplevel(self.root)

        name = tk.Label(child, text="Name: ")
        name_entry = tk.Entry(child)

        email = tk.Label(child, text="Email: ")
        email_entry = tk.Entry(child)

        username = tk.Label(child, text="Username: ")
        username_entry = tk.Entry(child)

        password = tk.Label(child, text="Password: ")
        password_entry = tk.Entry(child)

        register_button = tk.Button(self.root, text="REGISTER", command= first_page)

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

    login_button = tk.Button(self.root, text="LOGIN", command = XX)   #denna ska trigga chattfönstret

    register_button = tk.Button(self.root, text="REGISTER NEW", command = sub_func_register)

    username.grid()
    username_entry.grid()
    password.grid()
    password_entry.grid()
    login_button.grid()
    register_button.grid()



