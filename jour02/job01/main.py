class Personne:
    
    nom = ''
    prenom = ''
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
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
        
p1 = Personne('gonzalez', 'adrien')
p1.SePresenter()
p1.setNom('nouveau nom')
p1.getNom()
