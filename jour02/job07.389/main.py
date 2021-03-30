class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def getNom(self):
        return self.nom
    
    def getPrenom(self):
        return self.prenom
    
class Client (Personne):

    collection = []
    
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        
    def inventaire(self):
        print(self.collection)
    
    
class Auteur (Personne):
    
    oeuvre = []
    
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        
    def listerOeuvre(self):
        return self.oeuvre
        
    def ecrireUnLivre(self, titreLivre):
        self.oeuvre.append(titreLivre)
        
        
class Livre (Auteur):
    
    titre = ''
    
    def __init__(self, titre, nom, prenom):
        super().__init__(nom, prenom)
        self.titre = titre
     
    def afficherTitre(self):
        print(self.titre)

class Bibliotheque (Auteur, Client):
    
    nom = ''
    catalogue = []
    
   
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        
    def acheterLivre(self, auteur, titre, quantite: int):
        if titre in auteur.oeuvre:
            self.catalogue.insert(1, {'titre': titre,'quantitée': quantite})
    
    def inventaire(self):
        print(self.catalogue)
        
    def louer(self, client, titreLivre):
        found = "false"
        for i in range(len(self.catalogue)):
            if self.catalogue[i]['titre'] == titreLivre:
                if self.catalogue[i]['quantitée'] > 0:
                    self.catalogue[i]['quantitée'] =  self.catalogue[i]['quantitée'] - 1
                else:
                    print('Stock épuisé !')
                
                found = "true"
           
        if found == "true":
            client.collection.append(titreLivre)        
            print(self.catalogue)
        else:
            print('livre introuvable !')

    def rendreLivres(self, client):
        
        print(client.collection)
        
        for i in range(len(client.collection)):
            if self.catalogue[i]['titre'] == client.collection[i]:
                self.catalogue[i]['quantitée'] =  self.catalogue[i]['quantitée'] + 1   
        print(self.catalogue)
        client.collection = []
        print(client.collection)
        
        
        
        
     
            
personne = Personne('adrien', 'gonzalez')
auteur = Auteur(personne.getPrenom(), personne.getNom())
client = Client(personne.getPrenom(), personne.getNom())      
auteur.ecrireUnLivre('livre1') 
auteur.ecrireUnLivre('livre2')   
  
bibli = Bibliotheque(personne.getPrenom(), personne.getNom())  
bibli.acheterLivre(auteur, 'livre1', int(1))
bibli.acheterLivre(auteur, 'livre2', int(5))

bibli.inventaire()
bibli.louer(client, 'livre1')
bibli.rendreLivres(client)

