import socket
from socket import *
from _thread import *
import threading
import sys

def threaded(c):
    print("Threaded Method")
    try:

        message = c.recv(1024)
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()  # Fill in end

        c.send(bytes('HTTP/1.0 200 OK\n', 'UTF-8'))

        c.send(bytes('Content-Type: text/html\n', 'UTF-8'))
        c.send(bytes('\n', 'UTF-8'))

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            c.send(outputdata[i].encode())

        c.send("\r\n".encode())

        c.close()

    except IOError:
        # Send response message for file not found
        c.send(bytes('\nHTTP/1.1 404 Not Found\n\n', 'UTF-8'))
        c.close()


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', 6789))

    serverSocket.listen(10)

    while True:
        print('Ready to serve...')

        (connectionSocket, addr) = serverSocket.accept()
        start_new_thread(threaded, (connectionSocket,))

    serverSocket.close()


if __name__ == '__main__':
    main()

sys.exit()  # Terminate the program after sending the corresponding data