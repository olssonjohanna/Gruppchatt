import socket
from ClientRecieve import Recieve_message
import tkinter.messagebox
class Client:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self,my_ip,my_port):
        try:
            self.client_socket.connect((my_ip, my_port))
        except:
            tkinter.messagebox.showinfo("Error", "Wrong Ip or Port")

        thread_recv = Recieve_message(self.client_socket)
        thread_recv.start()


    def chatWindow(self):
        import GUIClassFile

        obj = GUIClassFile.GuiClass()
        obj.chatWindow(self.client_socket)



