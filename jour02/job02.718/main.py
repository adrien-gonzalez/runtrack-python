class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def getNom(self):
        return self.nom
    
    def getPrenom(self):
        return self.prenom

class Auteur (Personne):
    
    oeuvre = []
    
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        
    def listerOeuvre(self):
        print(self.oeuvre)
        
    def ecrireUnLivre(self, titreLivre):
        self.oeuvre.append(titreLivre)
        
        
class Livre (Auteur):
    
    titre = ''
    
    def __init__(self, titre, nom, prenom):
        super().__init__(nom, prenom)
        self.titre = titre
     
    def afficherTitre(self):
        print(self.titre)
        
personne = Personne('adrien', 'gonzalez')
auteur = Auteur(personne.getPrenom(), personne.getNom())
auteur.ecrireUnLivre('test')
auteur.listerOeuvre()
livre = Livre('titre', personne.getPrenom(), personne.getNom())
livre.afficherTitre()
