# Classes
## Classe Bibliotheque
class Bibliotheque:
    def __init__(self, nom, adresse, liste_livres):
        self.nom = nom 
        self.adresse = adresse
        self.liste_tous_livres = liste_livres
        self.liste_livres_disponibles = list(liste_livres)
    
    # fonction utilisée dans autres fonction de la classe pour afficher les deux listes
    def lister_livres(self, liste):
        for i, livre in enumerate(liste, start = 1):
            print(f"{i}. {livre['titre']} - {livre['auteur']} - {livre['isbn']}")
            
    def lister_tous_livres(self):
        print("\nListe de tous les livres :")
        self.lister_livres(self.liste_tous_livres)

        
    def lister_livres_disponibles(self):
        print("\nListe des livres disponibles :")
        self.lister_livres(self.liste_livres_disponibles)
        
        
    
    def lister_livres_empruntes(self, utilisateur):
        if not utilisateur.liste_emprunts:
            print("\nVous n'avez aucun livre emprunté.")
        else:
            print("\nListe des livres empruntés :")
            self.lister_livres(utilisateur.liste_emprunts)
            
    def retirer_livre(self, livre):
        if livre in self.liste_livres_disponibles:
            self.liste_livres_disponibles.remove(livre)
            
    def ajouter_livre(self, livre):
        # self.liste_tous_livres.append(livre)
        self.liste_livres_disponibles.append(livre)

## Classe Utilisateur
class Utilisateur:
    def __init__(self, nom, prenom, liste_emprunts):
        self.nom = nom
        self.prenom = prenom
        self.liste_emprunts = liste_emprunts
    
    def emprunter_livre(self, livre):
        self.liste_emprunts.append(livre)
        
    def retourner_livre(self, livre):
        if livre in self.liste_emprunts:
            self.liste_emprunts.remove(livre)
            
    def retourner_tous_les_livres(self):
        self.liste_emprunts = []