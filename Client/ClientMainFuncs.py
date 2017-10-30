import socket
from Client.ClientRecieve import Recieve_message
import tkinter.messagebox

class Client:

    def __init__(self,my_ip,my_port,guiObj):
        self.ip = my_ip
        self.port = my_port
        self.guiObj = guiObj
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            self.client_socket.connect((self.ip, self.port))
        except:
            self.client_socket.close()
            tkinter.messagebox.showerror("Error", "Try Again")
            return False

    def startRecv(self):
        thread_recv = Recieve_message(self.client_socket,self.guiObj)
        thread_recv.start()

    def chatWindow(self):
        self.guiObj.chatWindow(self.client_socket)



