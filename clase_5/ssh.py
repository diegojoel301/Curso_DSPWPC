#!/usr/bin/python3

import paramiko

host = "192.168.86.39"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
	ssh.connect(host, username = 'msfadmin', password = 'msfadmin')

	while True:

		cmd = input(">")

		if cmd == "exit":
			break
		stdin, stdout, stderr = ssh.exec_command(cmd)

		if len(stderr.readlines()) != 0:
			print("Command error")
		else:
			for line in stdout.readlines():
				print(line.strip())
except:
	pass
ssh.close()

