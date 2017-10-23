
#denna kan vi ta bort för detta är bara på terminal, eftersom vi har GUI func som skickar via knappen

import threading

class Send_message(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        while True:
            client_input = input("")
            self.client_socket.send(str.encode(client_input))