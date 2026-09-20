import socket
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    data, clientAdress = serverSocket.recvfrom(2048)
    message = data.decode("UTF-8")
    print("Message from client: ", message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode("UTF-8"), clientAdress)