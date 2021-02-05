import socket

buffer = 1024;

SRC = "192.168.1.188";




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRC, 8420))
msg = s.recv(buffer)
print(msg.decode("utf-8"))

