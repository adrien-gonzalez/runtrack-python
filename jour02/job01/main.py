class Personne:
    
    def __init__(self):
        self.nom = "gonzalez"
        self.prenom = "adrien"
        
    def SePresenter(self):
        print(self.nom+' '+self.prenom)
        
    def getNom(self):
        print(self.nom)
        
    def setNom(self, nom):
        self.nom = nom
    
    def getPrenom(self):
        print(self.prenom)
        
    def setPrenom(self, prenom):
        self.prenom = prenom
        
p1 = Personne()
p1.SePresenter()
p1.setNom('nouveau nom')
p1.getNom()
