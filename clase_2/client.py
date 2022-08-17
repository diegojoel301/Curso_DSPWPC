#!/usr/bin/python3

import socket

s = socket.socket()

port_server = 7676

ip_server = "127.0.0.1"

s.connect((ip_server, port_server))

print(s.recv(1024).decode())

s.close()
