#!/usr/bin/python3

import shodan
import nmap

def verifica_ftp(ip, port):
	nm = nmap.PortScanner()
	nm.scan(ip, port, "--script ftp-anon.nse")
	return nm[ip]['tcp'][int(port)]['script']['ftp-anon']

def verifica_ms_017_10(ip, port):
	nm = nmap.PortScanner()
	nm.scan(ip, port, "--script smb-vuln-ms17-010.nse")

	try:
		print("[+] IP:", ip_address, ":", nm[ip]['hostscript'][0]['output'])
	except:
		pass


def ftp_anonymous_spray(resultados):
	for result in resultados['matches']:
		ip_address = result['ip_str']
		print("[+] IP:", ip_address, ":", verifica_ftp(ip_address, "21"))


API_KEY = "PONTUKEYNOSVEMOSENELEXAMEN"

try:
	#resultados = api.search("port:'21 Anonymous user logged in'")
	resultados = api.search("os:'Windows 7' port:445") # Sabiendo que ms17-010 solo esta disponible por lo general en windows XP y 7
except:
	print("[+] Hubo un error con tu API KEY")

print(resultados['total'])

for result in resultados['matches']:
	ip_address = result['ip_str']
	verifica_ms_017_10(ip_address, "445")


