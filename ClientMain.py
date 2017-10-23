import socket
import os
from ClientRecieve import Recieve_message
from ClientSend import Send_message

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',9999))

thread_send = Recieve_message(client_socket)
thread_send.start()

thread_recv = Send_message(client_socket)
thread_recv.start()

#wait until sender will die

thread_send.join()
os._exit(0)

#client_socket.close()
