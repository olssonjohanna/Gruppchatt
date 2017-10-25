import threading


class Server_reciever_Handler(threading.Thread):
    def __init__(self, client_socket_, list_of_client_sockets_, client_addr_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.list_of_client_socktes = list_of_client_sockets_
        self.client_addr = client_addr_


    def run(self):
        print("startat meddelande tagare")
        while True:

            #try:
                self.message = self.client_socket.recv(1024).decode()

                self.var = str (self.client_addr)+" " + self.message
                print(self.message)

    def sendToAllSockets(self):
        from GUIClassFile import GuiClass
        obj = GuiClass()

        obj.updateChat(self.message)
        for sock in self.list_of_client_socktes:
            sock.send(str.encode(self.var))

            #except:
            #    self.client_socket.close()
             #   self.list_of_client_socktes.remove(self.client_socket)
              #  print(str(self.client_addr)+" Disconnected")
               # return