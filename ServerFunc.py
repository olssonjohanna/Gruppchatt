import socket
from ServerSend import Server_sender
from ServerRecieveAndHandler import Server_reciever_Handler
import GUIFunctions

Ip = '127.0.0.1'
port = 9999

class ServerMain:

    def registerAccount(name_entry,email_entry,username_entry,password_entry,self):
        GUIFunctions.register(name_entry,email_entry,username_entry,password_entry,self)

    def __init__(self):
        self.start()


    def start(self):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        global Ip

        global port
        self.server_socket.bind((Ip, int(port)))

        self.server_socket.listen()

        list_of_client_sockets = []

        sender = Server_sender(list_of_client_sockets)
        sender.start()

        while True:
            print("Waiting for connection...")
            client_socket, client_addr = self.server_socket.accept()

            list_of_client_sockets.append(client_socket)

            reciver = Server_reciever_Handler(client_socket,list_of_client_sockets,client_addr)
            reciver.start()