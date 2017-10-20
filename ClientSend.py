import threading
#import socket

class Send_message(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        while True:
            client_input = input("input:")
            self.client_socket.send(str.encode(client_input))