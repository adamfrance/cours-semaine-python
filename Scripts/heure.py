# doctring ==> donne l'heure présente
# import datetime
# utiliser la fonction pour l'heure
# importer uniquement la fonction dans un script jupyter
# ajouter un test qui affiche l'heure 

"""Ce script donne l'heure actuelle du système
"""

# Import de la librairie datetime
import datetime

def heure_actuelle():
    time = datetime.datetime.now().time()
    return time

# Affiche l'heure (pour tests):
if __name__ == '__main__':
    print(heure_actuelle())