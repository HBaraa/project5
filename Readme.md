# Parcours OpenClassrooms: Projet5 "Utilisez les données publiques de l'OpenFoodFacts"

## Mission

La startup Pur Beurre travaille connait bien les habitudes alimentaires françaises. Leur restaurant, Ratatouille, remporte un succès croissant et attire toujours plus de visiteurs sur la butte de Montmartre.
L'équipe a remarqué que leurs utilisateurs voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer. Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ? Leur idée est donc de créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

## Cahier des charges

### Description du parcours utilisateur:

L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :
1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.
L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :
Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

### Fonctionnalitées:

Recherche d'aliments dans la base Open Food Facts.
L'utilisateur interagit avec le programme dans le terminal, mais si vous souhaitez développer une interface graphique vous pouvez,
Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question,
La recherche doit s'effectuer sur une base MySql.

### Contraintes:

-Le code sera écrit en anglais: variables, noms de fonctions, commentaires, documentation..
- Projet versionné et publié sur Github.

## Création de la base des données en SQL: dans le fichier "openfoodfact.sql"

Création de la base de données "openfoodfact" et la sélection de cette base: la création des tables "product", "category", "category_product", "Favorite" et "nutriscore".
Création des clées étrangéres et des contraintes d'unicité.

## Le remplissage de la base des données à partir de l'API d'openfoodfacts en utilisant les requétes API aprés l'importation de la bibliothéque "requests":
cette tache a été effectée dans le fichier "commands.py" du package "mvc_modules". Dans ce fichier, on a fait l'appel des fonctions de la classe "AppSQL" du package "sql.py" avec la fonction " insert_datas" dans laquelle on a instancié la classe "InsertIntoTables" du package "insertion.py" et on a utilisé ses méthodes; "Fill_tables", "insert_categories", "insert_category_product", 
"get_product_id" et "get_category_id".

## L'interaction avec la base des données: 
cette tache a été effectuée dans le fichier "commands.py" du dossier "mvc_modules", en appelant les fonctions du module "data_maping.py" du dossier "models" pour l'insertion et la récupération des données.
Et on aussi une interraction avec la base des données dans le fichier "views" du dossier "mvc_modules", pour pouvoir afficher des données de la base.

## L'installation:
Vous n'avez pas besoin d'installer tous les packages externes nécessaires au projet. J'ai mis en place un fichier requirements.txt qui est un fichier répertoriant les packages nécessaires que j'ai utilisé dans mon environnement virtuel.
Afin de pouvoir utiliser ses packages, il suffit de créer un environnement virtuel , l'activer et d'installer des dépendances du programme en tapant dans le terminal de git bash:
$ py -3.9 -m venv .venv
$ source .venv/Scripts/activate
$ pip install -r requirements.txt

## L'usage:
Pour lancer le programme, vous avez besoin de:
	- avoir une connexion internet pour pouvoir remplir la base des données à partir de l'url de l'API d'OpenFoodFacts
	- cloner le projet sur votre machine locale
	- créer un environnement virtuel
	- installer les indépendances du programme
	- taper $ py -3.9 main.py
