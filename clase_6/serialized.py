#!/usr/bin/python3

import pickle

class Auto:
	def __init__(self, color, velocidad):
		self.color = color
		self.velocidad = velocidad
		self.numero_ruedas = 4

	def avanza(self, aceleracion):
		self.velocidad = self.velocidad + aceleracion

f = open("file.dat", "wb")

cadillac = Auto("Rojo", 123)

print("El color del cadillac es:", cadillac.color)

pickle.dump(cadillac, f)

f.close()