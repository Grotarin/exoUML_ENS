# -*-coding:UTF-8 -*
"""Classes pour les salles
"""

	

class Salle:
	"""Classe Salle
	"""
	
	def __init__(self):
		self.__ordis = []

	def get_ordis(self):
		return self.__ordis
		
	def find_ordi(self, num_ordi):
		for ordi in self.__ordis:
			if ordi.numero == num_ordi:
				return ordi
		return None
		
	def add_ordi(self, ordi):
		self.__ordis.append(ordi)
		
	def remove_velo(self, num_ordi):
		for ordi in self.__ordi:
			if ordi.numero == num_ordi:
				self.__ordis.remove(ordi)
				return True
		return False
		
	def empty_ordis(self):
		self.__ordis.clear()


		
		
		
		
		
		
		
		
		
		
