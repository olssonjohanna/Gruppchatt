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

        register_button = tk.Button(child, text="REGISTER", command=first_page)

        name.grid(row=0, column=0)
        name_entry.grid(row=0, column=1)
        email.grid(row=1, column=0)
        email_entry.grid(row=1, column=1)
        username.grid(row=2, column=0)
        username_entry.grid(row=2, column=1)
        password.grid(row=3, column=0)
        password_entry.grid(row=3, column=1)
        register_button.grid(row=4, column=0)

    def login_and_register():
        new_root = tkinter.Tk()

        username = tk.Label(new_root, text="Username: ")
        username_entry = tk.Entry(new_root)

        password = tk.Label(new_root, text="Password: ")
        password_entry = tk.Entry(new_root)

        login_button = tk.Button(new_root, text="LOGIN", command=XX)  # denna ska trigga chattfönstret

        register_button = tk.Button(new_root, text="REGISTER NEW", command=sub_func_register)

        username.grid(row=0, column=0)
        username_entry.grid(row=0, column=1)
        password.grid(row=1, column=0)
        password_entry.grid(row=1, column=1)
        login_button.grid(row=2, column=0)
        register_button.grid(row=3, column=0)

    #IP AND PORT
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







