import threading

class Recieve_message (threading.Thread):

    def __init__(self,clientsocket):
        threading.Thread.__init__(self)
        self.client_socket = clientsocket+
        #ta emot variable/objekt som kan trigga en funk för att visa på skärmen

    def run(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            print(message) #här ska vi kalla på funktionen
