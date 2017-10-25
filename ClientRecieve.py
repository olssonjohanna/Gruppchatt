import threading
import GUIClassFile
import tkinter.messagebox

class Recieve_message (threading.Thread):

    def __init__(self,clientsocket,guiObj):
        threading.Thread.__init__(self)
        self.client_socket = clientsocket
        self.guiObj = guiObj
        #ta emot variable/objekt som kan trigga en funk för att visa på skärmen


    def run(self):
        from GUIClassFile import GuiClass
        while True:
          #  try:
                message = self.client_socket.recv(1024).decode()
                self.guiObj.updateChat(message)

           # except OSError:
               # self.client_socket.close()
               # tkinter.messagebox.showinfo("Error", "Try Again")
              #  return False
