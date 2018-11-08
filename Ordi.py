# -*-coding:UTF-8 -*
"""Classe pour les ordinateurs
"""


class Ordi:
	"""Classe Ordinateur
	"""
	
	def __init__(self, numero):
		self.__numero = numero

	def __get_numero(self):
		return self.__numero
	numero = property(__get_numero)

		
		
		
		
		
