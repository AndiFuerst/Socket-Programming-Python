import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6789

# connect to the server on local computer
s.connect(('localhost', port))

message = 'GET /helloWorld.htm HTTP/1.1'  # need to somewhere state what file we wan

s.send(bytes(message, 'UTF-8'))
m = str(s.recv(1024), 'utf-8')
codeFinder = m.split()
if codeFinder[1] == "200":
    m = str(s.recv(1024), 'utf-8')
    codeFinder = m.split('/')
    if codeFinder[1] == "html":
        f = open("sample.htm", "w")
        while True:
            m = s.recv(1024)
            f.write(m.decode("utf-8"))
        print(f.read())
elif codeFinder[1] == "404":
    print("Error 404: File not found")
else:
    print("This is wrong")
# close the connection
s.close()