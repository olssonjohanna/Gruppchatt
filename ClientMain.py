import socket
from ClientRecieve import Recieve_message
from ClientSend import Send_message
import tkinter.messagebox

def create_Connections(my_ip, my_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((my_ip,my_port))
    except:
        tkinter.messagebox.showinfo("Error","Wrong Ip or Port")

    thread_send = Recieve_message(client_socket)
    thread_send.start()

    thread_recv = Send_message(client_socket)
    thread_recv.start()

        #wait until sender will die
    #thread_send.join()

