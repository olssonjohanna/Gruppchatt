import threading

class Server_sender(threading.Thread):
    def __init__(self, list_of_client_sockets_):
        threading.Thread.__init__(self)
        self.list_of_client_sockets = list_of_client_sockets_


  #  def run(self):
  #          for client_socket in self.list_of_client_sockets:
   #             client_socket.send(str.encode())
