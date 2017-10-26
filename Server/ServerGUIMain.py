from Server.ServerGui import ServerGui

from Server.ServerFunc import ServerMain


serverGui = ServerGui()
serverGui.start()
server = ServerMain(serverGui)
server.start()

