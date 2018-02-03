import socket

serverName = input("Please enter host name:")
serverPort = int(input("Please enter port number:"))
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    userName = input("Please enter your user name: ")
    toName = input("To: ")
    message = input("Message: ")
    sendedMessage = userName + "," + toName + "," + message
    sendedMessage = bytes(sendedMessage,"utf-8")
    clientSocket.sendto(sendedMessage,(serverName,serverPort))
    message, clientAddress = clientSocket.recvfrom(1024)
    receivedMessage = message.decode("utf-8")
    print("****" + receivedMessage)
