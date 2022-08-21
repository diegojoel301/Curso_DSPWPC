#!/usr/bin/python3

import pickle

class Auto:
	def __init__(self, color, velocidad):
		self.color = color
		self.velocidad = velocidad
		self.numero_ruedas = 4

	def avanza(self, aceleracion):
		self.velocidad = self.velocidad + aceleracion

f = open("payload.dat", "rb")

auto = pickle.load(f)

print(auto.color)

f.close()