from classes import Bibliotheque, Utilisateur
from datas import livres
        
bibliotheque = Bibliotheque("Bibliothèque municipale de Wattrelos", "12 rue de la République", livres)
utilisateur = Utilisateur("Jean", "Paul", [])


## Script - IHM - Appelle et coordonne l'action des classes

while True:
    print("1. Emprunter un livre")
    print("2. Retourner un livre")
    print("3. Afficher la liste des emprunts")
    print("4. Quitter")
    
    choix = input("\nChoisissez une option (1/2/3/4):  ")
    
    if choix == "1":
        bibliotheque.lister_livres_disponibles()
        print("\n")
        try:
            choix_livre = int(input("Choisissez le numéro du livre que vous souhaitez emprunter (0 pour annuler): "))
        except ValueError:
            print("\nVeuillez entrer un numéro valide")
            choix_livre = int(input("Choisissez le numéro du livre que vous souhaitez emprunter (0 pour annuler): "))
        
        if choix_livre == 0:
            continue
        
        if 1 <= choix_livre <= len(bibliotheque.liste_livres_disponibles):
            livre_emprunt = bibliotheque.liste_livres_disponibles[choix_livre - 1]
            bibliotheque.retirer_livre(livre_emprunt)
            utilisateur.emprunter_livre(livre_emprunt)
            print(f"\n{livre_emprunt['titre']} a été emprunté avec succès.")
            bibliotheque.lister_livres_empruntes(utilisateur)
        else:
            print("Numéro de livre invalide.")
            
    elif choix == "2":
        bibliotheque.lister_livres_empruntes(utilisateur)
        print("1. Retourner un seul livre")
        print("2. Retourner tous les livres")
        sous_choix = input("Choisissez une option (1/2): ")
        
        if sous_choix == "1":
            isbn_livre_retour = input("Entrez l'ISBN du livre que vous souhaitez retourner: ")
            livre_retour = next((livre for livre in utilisateur.liste_emprunts if livre['isbn'] == isbn_livre_retour), None)
            if livre_retour:
                utilisateur.retourner_livre(livre_retour)
                bibliotheque.ajouter_livre(livre_retour)
                print(f"{livre_retour['titre']} a été retourné avec succès.")
                bibliotheque.lister_livres_empruntes(utilisateur)
            else:
                print("Le livre n'est pas dans votre liste d'emprunts.")
                
        elif sous_choix == "2":
            utilisateur.retourner_tous_les_livres()
            print("Tous les livres ont été retournés avec succès.\n")
            
    elif choix == "3":
        bibliotheque.lister_livres_empruntes(utilisateur)
        print("\n"*2)
        
    elif choix == "4":
        print("Au revoir!")
        break
    
    else:
        print("Choix invalide. Veuillez choisir une option valide.")
            
        
        
            