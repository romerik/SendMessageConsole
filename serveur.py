# coding: utf-8

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 1555))
socket.listen(5)
client, address = socket.accept()
print("{} connected".format( address ))
client.sendall(b"TAPER FIN POUR ARRETER LA DISCUSSION\nBONJOUR\n")
while True:
        response = client.recv(2048).decode("utf8")
        if response=="FIN\n":
                break
        print("Client--->{}".format(response))
        env=input("Server--->").encode("utf8")
        client.sendall(env)
print("Close")
client.close()
socket.close()