import socket
from objects import *

header_length = 10;

hostname = socket.gethostbyname(socket.gethostname())

port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hostname, port))
#s.bind(("184.66.168.85", port))

s.listen(5)
print(socket.gethostname())

while True:
    clientsocket, address = s.accept()

    print("connection from {address} has been done with {clientsocket}")
    clientsocket.send(bytes("welcome to server", "utf-8"))
