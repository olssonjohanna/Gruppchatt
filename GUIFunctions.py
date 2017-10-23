from ClientMain import create_Connections

# kommer från ENTER knappen: denna ska skicka IP och port till clienten som connectar
def IP_and_port(get_ip, get_port):
    create_Connections(get_ip, get_port)

# kommer från REGISTER knappen: spara användaren på en fil sen till login på GUIClassFile
def register(name_entry,email_entry,username_entry,password_entry):

    file = open("users.txt", "w")

    file.write(name_entry+ "\n")
    file.write(email_entry+ "\n")
    file.write(username_entry+ "\n")
    file.write(password_entry+ "\n")
    file.write("\n")



    file.close()

    #om användare redan registrerad, om användarnamn redan finns

# kommer från LOGIN knappen: kontrollera om det man skrivit finns på filen sen till chattfönstret
def login(username_entry,password_entry):
    file = open("RegisterdUserLog.txt", "r")

    #if username_entry == file.read()

        #jämnföra user och pass med filen

#om det är OK - skicka till chattfönstret
