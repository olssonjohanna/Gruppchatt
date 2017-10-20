import threading
#import socket

class Recieve_message (threading.Thread):

    def __init__(self,clientsocket):
        threading.Thread.__init__(self)
        self.client_socket = clientsocket

    def run(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            print(message)
