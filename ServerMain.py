import socket
from ServerSend import Server_sender
from ServerRecieveAndHandler import Server_reciever_Handler
from GUIFunctions import register

class ServerMain:

    def registerAccount(name_entry,email_entry,username_entry,password_entry):
        register(name_entry,email_entry,username_entry,password_entry)

    def __init__(self):
        self.start()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_socket.bind(('127.0.0.1', 9999))

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