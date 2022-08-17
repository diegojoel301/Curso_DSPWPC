#!/usr/bin/python3

class Auto:
	def __init__(self, color, aceleracion):
		self.color = color # Encapsulacion tipo: public
		self.__kilometraje = 0 # Encapsulacion tipo: private
		self.aceleracion = aceleracion # Encapsulacion tipo: public
		self.velocidad = 0 # Encapsulacion tipo: public
	def acelera(self, vel):
		self.velocidad = vel + self.aceleracion
	def frena(self):
		v = self.velocidad - self.aceleracion
		if v < 0:
			v = 0
		self.velocidad = v
	def get_kilometraje(self):
		return self.__kilometraje

autito = Auto("Rojo", 100) # instanciamos la clase Auto en el objecto autito
print(autito.color)
print(autito.get_kilometraje())

vector = list() # vector vacio

vector = [1, 2, 3, 4, 5, 6, 7 ,8]

persona = dict() # diccionario vacio

persona = {"Nombre": "Pepe",
		"Edad": 19,
		"Genero": 'M',
		"DNI": 6253536267263} # diccionario con datos
print(persona["Edad"]) # diccionario
print(vector[2]) # vector
