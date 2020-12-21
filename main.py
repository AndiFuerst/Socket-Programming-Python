import socket
from socket import *

import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('192.168.201.174', 6789))

serverSocket.listen(1)

while True:


    print('Ready to serve...')

    (connectionSocket, addr) = serverSocket.accept()

    try:

        message = connectionSocket.recv(1024)

        filename = message.split()[1]
        #filename = 'helloWorld.htm'

        f = open(filename[1:])

        outputdata = f.read()                     #Fill in end

        connectionSocket.send(bytes('HTTP/1.0 200 OK\n','UTF-8'))

        connectionSocket.send(bytes('Content-Type: text/html\n', 'UTF-8'))
        connectionSocket.send(bytes('\n', 'UTF-8'))

        # Send the content of the requested file to the client

        for i in range(0, len(outputdata)):

            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:

        # Send response message for file not found
        connectionSocket.send(bytes('\n HTTP/1.1 404 Not Found\n\n', 'UTF-8'))

    # Close client socket
    connectionSocket.close()

serverSocket.close()

sys.exit()  # Terminate the program after sending the corresponding data