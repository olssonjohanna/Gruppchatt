import threading
import tkinter as tk
import tkinter.messagebox

class Recieve_message (threading.Thread):

    def __init__(self,clientsocket,guiObj):
        threading.Thread.__init__(self)
        self.client_socket = clientsocket
        self.guiObj = guiObj

    def run(self):
        while True:
            print ("we are waiting for message")
         # try:
            message = self.client_socket.recv(1024).decode()
            print (message)
            self.guiObj.updateChat(message)


          #except OSError:
          #      self.client_socket.close()
          #      tk.messagebox.showinfo("Error", "Try Again")
          #      return
