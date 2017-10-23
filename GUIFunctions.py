from ClientMain import create_Connections

# kommer från ENTER knappen: denna ska skicka IP och port på clienten som connectar sen till login_and_register på GUIClassFile
def IP_and_port(get_ip, get_port):
    create_Connections(get_ip, get_port)

# kommer från REGISTER knappen: spara användaren på en fil sen till login på GUIClassFile
#def register():

# kommer från LOGIN knappen: kontrollera om det man skrivit finns på filen sen till chattfönstret
#def login():
