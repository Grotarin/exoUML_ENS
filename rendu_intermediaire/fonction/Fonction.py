#Ordinateur
	def __init__(self):
		self.__ordinateurs = []
	def get_ordinateurs(self):
		return self.__ordinateurs
		
	def find_ordinateur(self, numero_ordinateur):
		for ordinateur in self.__ordinateurs:
			if ordinateur.numero == numero_ordinateur:
				return ordinateur
		return None
		
	def add_ordinateur(self, ordinateur):
		self.__ordinateurs.append(ordinateur)
		
	def remove_ordinateur(self, numero_ordinateur):
		for ordinateur in self.__ordinateur:
			if ordinateur.numero == numero_ordinateur:
				self.__ordinateurs.remove(ordinateur)
				return True
		return False
		
	def empty_ordinateurs(self):
		self.__ordinateurs.clear()
