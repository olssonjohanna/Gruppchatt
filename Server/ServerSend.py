import threading

class Server_sender(threading.Thread):
    def __init__(self, list_of_client_sockets_):
        threading.Thread.__init__(self)
        self.list_of_client_sockets = list_of_client_sockets_