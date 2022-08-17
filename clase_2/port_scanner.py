#!/usr/bin/python3

import socket
import sys

# La cantidad de puertos totales son desde 0 a 65535

try:
	nombre_archivo = sys.argv[2]

	ip_server = sys.argv[1]
except:
	print("\t[+] python3 port_scanner.py <ip-victima> <nombre-archivo>")
	sys.exit()

file = open(nombre_archivo, "a")

salida = str()

for port in range(1, 65536):
	try:
		s = socket.socket()

		s.connect((ip_server, port))

		salida += str(port) + "\n"

		s.close()
	except:
		continue

file.write(salida)
file.close()
