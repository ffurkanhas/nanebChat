import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listenPort = int(input("Please enter listening port: (furkan:12009,ozan:12010,benan,12011)"))
clientSocket.bind(('', listenPort))
while True:
    message, clientAddress = clientSocket.recvfrom(2048)
    receivedMessage = message.decode("utf-8")
    tempReceivedMessage = receivedMessage.split(',')
    print("From: <" + tempReceivedMessage[0] + ">" +" To: <you> " + "\nmessage: " + tempReceivedMessage[2])