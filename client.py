# coding: utf-8

import socket

hote = "localhost"
port = 1555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
socket.send(b"Salut serveur")
try:
    while True:
        donne=socket.recv(2048).decode("utf8")
        print("Server-->{}".format(donne))
        env=input("Client--->").encode("utf8")
        socket.sendall(env)
except:
    print("Close")
    socket.close()