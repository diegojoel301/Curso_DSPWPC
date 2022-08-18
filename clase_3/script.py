#!/usr/bin/python3

import nmap

nmScan = nmap.PortScanner() # Instanciamos de nmap la clase PortScanner() que nos servira
                            # Para hacer escaneos con nmap

# nmScan.scan(<direccion ip>, <puertos>, <parametros>)
# Formas de declarar puertos:
# Primera: 21, 22, 23, 25, .....
# Segunda: 21-443
# Parametros: por ejemplo -sT -sS --script mago.nse

ip_address = "192.168.86.31"

# para un escaneo total usar:
# ip_address = "192.168.86.0/24"

#puertos = "21-500"

puertos = "445"

#puertos = "1-65535"

#parametros = "-sU --open" para escaneo upd

parametros = "--script smb-vuln-ms17-010.nse"

escaneo = nmScan.scan(ip_address, puertos, parametros) # este es un diccionario de todo el escaneo

#print(escaneo['scan']['192.168.86.33']['tcp'][22]["state"])

puertos = escaneo['scan'][ip_address]["tcp"][445]

print(escaneo["scan"][ip_address]["hostscript"])

# -sC: este parametro ejecuta scripts vulnrables posibles
# -sV: este parametro se encarga de devolver la version del servicio del determinado puerto
"""
puertos_abiertos = list()

for port in puertos.keys():
	if puertos[port]["state"] == "open": # verificamos si el estado del puerto esta en open
		escaneo_puerto = nmScan.scan(ip_address, str(port), "-sCV") # Hacemos una enumeracion de cada puerto abierto
		escaneo_de_puerto = escaneo_puerto["scan"][ip_address]["tcp"][port]
		print(escaneo_de_puerto["product"])
		if "script" in escaneo_de_puerto.keys():
			print(escaneo_de_puerto["script"])

		puertos_abiertos.append(port)
"""
# Como alternativa pueden poner de inicio en los parametros --open pero por cuestiones de practica
# en programacion usamos el for que se vee anteriormente

