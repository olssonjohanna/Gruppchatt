import socket
import tkinter.messagebox
from Client.ClientRecieve import Recieve_message

class Client:

    def __init__(self,my_ip,my_port,guiObj):
        self.ip = my_ip
        self.port = my_port
        self.guiObj = guiObj
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        print("nu connectas den")
        try:
            print(self.client_socket)
            self.client_socket.connect((self.ip, self.port))
        except:
            tkinter.messagebox.showinfo("Error", "Wrong Ip or Port")

    def startRecv(self):
        thread_recv = Recieve_message(self.client_socket,self.guiObj)
        thread_recv.start()


    def chatWindow(self):
        from Client import GUIClassFile

        obj = GUIClassFile.GuiClass()
        obj.chatWindow(self.client_socket)



