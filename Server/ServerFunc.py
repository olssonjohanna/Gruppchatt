import socket

from Client import GUIFunctions
from Server.ServerRecieveAndHandler import Server_reciever_Handler
import tkinter as tk
import threading
import tkinter.messagebox

Ip = ''

class ServerMain(threading.Thread):

    def registerAccount(name_entry,email_entry,username_entry,password_entry,self):
        GUIFunctions.register(name_entry, email_entry, username_entry, password_entry, self)

    def __init__(self,guiObj,port):
        threading.Thread.__init__(self)
        self.guiObj = guiObj
        self.port = port
        self.statement = 0

    def getStatement(self):
        return self.statement

    def run(self):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global Ip
        try:
            self.server_socket.bind((Ip, int(self.port)))
            self.statement = 1
            self.server_socket.listen()
            list_of_client_sockets = []


            while True:
                print("Waiting for connection...")
                client_socket, client_addr = self.server_socket.accept()
                self.guiObj.getClientSocket(client_socket, list_of_client_sockets)
                list_of_client_sockets.append(client_socket)

                self.reciver = Server_reciever_Handler(client_socket, list_of_client_sockets, client_addr, self.guiObj)
                self.reciver.start()
        except:
            tk.messagebox.showerror("Port error", "Port is already in use. Try a different port.")
