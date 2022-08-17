#!/usr/bin/python3

from pwn import *

conexion = remote("192.168.86.33", 21)
print(conexion.recvline())
