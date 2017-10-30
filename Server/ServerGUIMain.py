from Server.ServerGui import ServerGui
import tkinter as tk
from tkinter import messagebox
from Server.ServerFunc import ServerMain
import time

root = tk.Tk()
root.title("Server")

port = tk.Label(root, text="Port: ")
port_entry = tk.Entry(root)

def getValue(entry1):
    try:
        port_send = int(entry1.get())

        serverGui = ServerGui()
        server = ServerMain(serverGui, port_send)
        server.start()
        time.sleep(0.5)
        var = server.getStatement()
        if var == 1:
            root.destroy()
            serverGui.start()

    except ValueError:
        tk.messagebox.showinfo("Error", "Port should be a number")
        port_entry.delete(0, tk.END)
        return False

enter_button = tk.Button(root, text="ENTER", command = lambda: getValue(port_entry))
root.bind("<Return>",lambda x: getValue(port_entry))
port.grid(row=1, column=0)
port_entry.grid(row=1, column=1)
enter_button.grid(row=2, column=1)
root.mainloop()
