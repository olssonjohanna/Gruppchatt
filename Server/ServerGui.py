import tkinter as tk
import threading
import Server.ServerSend


class ServerGui():

    def __init__(self):
        pass

    def start(self):
        self.chatWindow()

    def sendMessage(self, message):
        pass

    def updateChat(self, text):
        self.windowText.config(state=tk.NORMAL)
        self.windowText.insert(tk.END, text + "\n")
        self.windowText.config(state=tk.DISABLED)
        self.windowText.see(tk.END)

    def chatWindow(self):
        root = tk.Tk()
        root.title("Server")
        root.geometry('{}x{}'.format(600, 400))
        root.resizable(False, False)

        chatFrame = tk.Frame(height='250', bd=1, width='100', padx=5)
        textFrame = tk.Frame(height='250', bd=1, width='100', padx=5)
        self.windowText = tk.Text(chatFrame, height='15', width='70')
        self.chatText = tk.Text(textFrame, height='5', width='60')
        sendBtn = tk.Button(textFrame, text='Send', height='5', width=10,
                            command=lambda: self.retrieve_input())

        scrollb = tk.Scrollbar(chatFrame, command=self.windowText.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.windowText['yscrollcommand'] = scrollb.set

        root.bind("<Return>", lambda x: self.retrieve_input())

        self.windowText.config(state=tk.DISABLED)

        self.windowText.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        chatFrame.grid_rowconfigure(0, weight=1)
        chatFrame.grid_columnconfigure(0, weight=1)
        chatFrame.grid(padx=5, pady=20)
        textFrame.grid(padx=5, pady=20)
        self.chatText.grid(row=0)
        sendBtn.grid(row=0, column=1)

        root.mainloop()

    def updateChat(self, text):
        self.windowText.config(state=tk.NORMAL)
        self.windowText.insert(tk.END, text + "\n")
        self.windowText.config(state=tk.DISABLED)
        self.windowText.see(tk.END)

    def retrieve_input(self):
        input = self.chatText.get('1.0', tk.END)
        self.chatText.delete('1.0', tk.END)
        self.sendMessage(input)