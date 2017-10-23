from GUIClassFile import GuiClass
from ClientMain import create_Connections

# kommer från ENTER knappen: denna ska skicka IP och port till clienten som connectar
def IP_and_port(get_ip, get_port):
    create_Connections(get_ip, get_port)

# kommer från REGISTER knappen: spara användaren på en fil sen till login på GUIClassFile
def register():
    file = open("users.txt", "r")

# kommer från LOGIN knappen: kontrollera om det man skrivit finns på filen sen till chattfönstret
def login():
    file = open("users.txt", "r")

