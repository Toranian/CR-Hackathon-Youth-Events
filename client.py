import socket

hostname = "Hackathon5"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))

msg = s.recv(1024)

print(msg.decode("utf-8"))
