import socket
from ServerSend import Server_sender
from ServerRecieveAndHandler import Server_reciever_Handler

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('',9999))

server_socket.listen()

list_of_client_sockets = []

sender = Server_sender(list_of_client_sockets)
sender.start()
while True:
    print("Waiting for connection...")
    client_socket, client_addr = server_socket.accept()

    list_of_client_sockets.append(client_socket)

    reciver = Server_reciever_Handler(client_socket,list_of_client_sockets,client_addr)
    reciver.start()