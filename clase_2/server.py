#!/usr/bin/python3

import socket

def connection():
	conn, addr = s.accept()
	print(addr)
	conn.send("Gracias por conectarte".encode())
	conn.close()

s = socket.socket()

port = 7676

ip_address = '127.0.0.1'

s.bind((ip_address, port))

max_clients = 5

s.listen(max_clients)

while True:
	connection()
	break
s.close()
