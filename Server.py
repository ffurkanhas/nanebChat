import socket

userList = {}
if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(("10.2.36.115", serverPort))
    print ("the server is ready at port: " + str(serverPort))
    userList["furkan"] = "12009"
    userList["ozan"] = "12010"
    userList["benan"] = "12011"
    while 1:
        message, clientAddress = serverSocket.recvfrom(1024)
        receivedMessage = message.decode("utf-8")
        tempMessageOptions = receivedMessage.split(',')
        fromUser = tempMessageOptions[0]
        to = tempMessageOptions[1]
        sendedMessage = tempMessageOptions[2]

        if fromUser not in userList:
            error = bytes("You are not registered","utf-8")
            serverSocket.sendto(error,clientAddress)
            print("You are not registered")

        elif to not in userList:
            error = bytes("Target user is not in user list","utf-8")
            serverSocket.sendto(error,clientAddress)
            print("Target user is not in user list")

        else:
            tempMessage = fromUser + "," + to + "," + sendedMessage
            messageSended = bytes(tempMessage,"utf-8")
            sent = bytes("Message sent", "utf-8")
            serverSocket.sendto(sent, clientAddress)
            serverSocket.sendto(messageSended,('',int(userList[to])))
            print(tempMessage)