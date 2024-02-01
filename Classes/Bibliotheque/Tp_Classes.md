## Exercice : Gestion d'une bibliothèque

### Trois classes :

- Bibliothèque : représente une bibliothèque.
- Utilisateur : représente un utilisateur de la bibliothèque.
- Livre : représente un livre de la bibliothèque.

Les classes devront interagir de la manière suivante :

- La bibliothèque doit contenir une liste de livres.
- L'utilisateur doit pouvoir emprunter des livres de la bibliothèque.
- L'utilisateur doit pouvoir retourner les livres empruntés.

En plus de ces interactions, les classes devront contenir les propriétés et méthodes suivantes :

#### Classe Bibliothèque

Propriétés
- nom : le nom de la bibliothèque
- adresse : l'adresse de la bibliothèque
- liste_livres : une liste de livres
Méthodes
- ajouter_livre() : permet d'ajouter un livre à la bibliothèque
- retirer_livre() : permet de retirer un livre de la bibliothèque
- lister_livres() : permet de lister tous les livres de la bibliothèque

#### Classe Utilisateur

Propriétés
- nom : le nom de l'utilisateur
- prénom : le prénom de l'utilisateur
- liste_emprunts : une liste de livres empruntés
Méthodes
- emprunter_livre() : permet à l'utilisateur d'emprunter un livre
- retourner_livre() : permet à l'utilisateur de retourner un livre

#### Classe Livre

Propriétés
- titre : le titre du livre
- auteur : l'auteur du livre
- isbn : l'identifiant du livre
Méthodes
- get_titre() : retourne le titre du livre
- get_auteur() : retourne l'auteur du livre
- get_isbn() : retourne l'identifiant du livre

Énoncé

L'exercice consiste à créer un programme qui permet à un utilisateur d'emprunter des livres d'une bibliothèque.

Le programme doit commencer par créer une bibliothèque et un utilisateur.

Ensuite, le programme doit permettre à l'utilisateur d'emprunter des livres de la bibliothèque. Pour cela, le programme doit demander à l'utilisateur le titre du livre qu'il souhaite emprunter. Si le livre est disponible, le programme doit l'ajouter à la liste des emprunts de l'utilisateur.

Le programme doit également permettre à l'utilisateur de retourner des livres empruntés. Pour cela, le programme doit demander à l'utilisateur le titre du livre qu'il souhaite retourner. Si le livre est dans la liste des emprunts de l'utilisateur, le programme doit le retirer de cette liste.

Enfin, le programme doit afficher la liste des livres empruntés par l'utilisateur.

Exemple de code

```python
# Créer une bibliothèque
bibliothèque = Bibliothèque("Bibliothèque municipale de Wattrelos", "12 rue de la République")

# Créer un utilisateur
utilisateur = Utilisateur("Jean", "Paul", [])

# Emprunter un livre
titre_livre = input("Quel livre souhaitez-vous emprunter ? ")
bibliothèque.emprunter_livre(utilisateur, titre_livre)

# Retourner un livre
titre_livre = input("Quel livre souhaitez-vous retourner ? ")
bibliothèque.retourner_livre(utilisateur, titre_livre)

# Afficher la liste des emprunts
print("Liste des emprunts :")
for livre in utilisateur.liste_emprunts:
    print(livre)
```

## Data

livres = [
    {
        "titre": "La Terre",
        "auteur": "David Attenborough",
        "genre": "Géographie",
        "description": "Documentaire sur la planète Terre",
        "isbn": "978-2-07-033384-4",
    },
    {
        "titre": "Le Monde",
        "auteur": "Yann Arthus-Bertrand",
        "genre": "Géographie",
        "description": "Documentaire aérien sur le monde",
        "isbn": "978-2-85621-222-9",
    },
    {
        "titre": "Le Guide du Routard",
        "auteur": "Le Routard",
        "genre": "Géographie",
        "description": "Guides de voyage",
        "isbn": "978-2-07-033385-1",
    },
    {
        "titre": "Larousse des Voyages",
        "auteur": "Larousse",
        "genre": "Géographie",
        "description": "Dictionnaire encyclopédique sur les voyages",
        "isbn": "978-2-07-033386-8",
    },
    {
        "titre": "National Geographic",
        "auteur": "National Geographic",
        "genre": "Géographie",
        "description": "Revue sur les sujets géographiques",
        "isbn": "978-2-07-033387-5",
    },
    {
        "titre": "L'Histoire du monde",
        "auteur": "Jean-Pierre Rioux",
        "genre": "Histoire",
        "description": "Ouvrage de référence sur l'histoire de l'humanité",
        "isbn": "978-2-07-033388-2",
    },
    {
        "titre": "Les Grandes Civilisations",
        "auteur": "Pierre Grimal",
        "genre": "Histoire",
        "description": "Ouvrage sur les principales civilisations de l'Antiquité",
        "isbn": "978-2-07-033389-9",
    },
    {
        "titre": "Larousse de l'Histoire",
        "auteur": "Larousse",
        "genre": "Histoire",
        "description": "Dictionnaire encyclopédique sur l'histoire",
        "isbn": "978-2-07-033390-5",
    },
    {
        "titre": "National Geographic History",
        "auteur": "National Geographic",
        "genre": "Histoire",
        "description": "Revue sur les sujets historiques",
        "isbn": "978-2-07-033391-2",
    },
]
