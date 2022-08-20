#!/usr/bin/python3

import ftplib

host = "192.168.86.39"

ftp = ftplib.FTP()

ftp.connect(host, 21, -999)

print(ftp.getwelcome())

ftp.login('anonymous', '') # Guest log: Logeo como invitado

ftp.dir()

ftp.close()





