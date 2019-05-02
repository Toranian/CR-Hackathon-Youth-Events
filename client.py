import socket

hostname = "tbl-hackerspace-24-s"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 1234))

msg = s.recv(1024)

print(msg.decode("utf-8"))
