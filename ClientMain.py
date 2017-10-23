import socket
from ClientRecieve import Recieve_message
from ClientSend import Send_message

def create_Connections(my_ip, my_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((my_ip,my_port))

    thread_send = Recieve_message(client_socket)
    thread_send.start()

    thread_recv = Send_message(client_socket)
    thread_recv.start()

    #thread_send.join()

