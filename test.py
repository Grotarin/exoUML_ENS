# -*- coding: utf-8 -*

class Etablissement:
	def __init__(self, nom):
		self.nom = None
		
class Etage:
	def __init__(Etablissement, self):
        Etablissement.__init__(self)
		self.numero_etage = 0
		self.surface = 0.0
		self.affectation_principale = None	
		
class Salle:
	def __init__(Etage, self):
        Etage.__init__(self)
		self.destination = None
		self.numero = 0
		self.liste_materiel = []
        
class Ordinateur:
	def __init__(Salle, self):
        Salle.__init__(self)
		self.numero = 0
		self.microprocesseur = None
		self.memoire_vive = 0
		self.capacite_disque = 0.0
		self.date_achat = 01/01/1970
      
      def branchement(Salle):
         self.salle = salle.numero
		
class Carte_reseau :
	def __init__(Ordinateur, self):
		self.type_carte = None
		self.adresse_ip = None
		self.adresse_mac = None
        
""""        
		
class Videoproj:
	def __init__(Salle, self):
		self.ID = 0
		self.modele = None
		self.luminosite = 0
		self.duree_de_vie = 0
		
class Table :
	def __init__(Salle, self):
		self.ID = 0
		self.largeur = 0
		self.longueur = 0
		#Salle.numero
		Salle.liste_materiel = self.ID

salle1 = Salle("cours", 101)
print Salle.liste_materiel		
table1=Table(13234, 120, 50)
print table1.ID
print Salle.liste_materiel
		
class Chaise:
	def __init__(self, ID, type_chaise):
		self.ID = 0
		self.type = None


""""
print "voilà la fin !"
