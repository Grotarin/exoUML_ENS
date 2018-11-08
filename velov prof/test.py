# -*-coding:UTF-8 -*

"""	
	Stations de velos
	Programme de test
	
"""
import *
from velov.Velo import *
from velov.Station import *

class Tests:

	def __init__(self):
		Tests.tests()

	def tests():
		# instanciation des vélos
		print("Velos-----------------------------------------------------")
		velo1 = Velo(8)
		velo2 = Velo(5)
		velo3 = Velo(19)
		print(velo1.numero)

		# instanciation des stations
		print("Stations-----------------------------------------------------")
		station1 = Station()
		station1.add_velo(velo1)
		station1.add_velo(velo2)
		station1.add_velo(velo3)
		velo4 = station1.find_velo(5)
		velo5 = station1.find_velo(19)
		print(velo2.numero)
		print(station1.get_velos())
		for velo in station1.get_velos():
			print(velo.numero)
			


		
		
Tests()









