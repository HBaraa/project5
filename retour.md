Coucou Baraa, voici mes retours:

ORGANISATION DU CODE
- utiliser un dossier dans lequel mettre ses fichiers (à part main.py qui doit rester à la racine), comme nous l'avons vu au cours précédent.
- le code dans le fichier main doit être ailleurs. Il devrait être dans un fichier "insertion.py" par exemple.
- éviter de mélanger majuscules et minuscules dans le nom des fichiers (comme vu précedemment aussi ;) )


FONCTION GET_CATEGORIES
- la récupération des catégories se fait à partir d'un produit et non de l'url openfoodfact des catégories. Car nous voulons les catégories utilisées par les produits, et non toutes les catégories.
- On souhaite en effet éviter les catégories qui ne sont pas utilisées par nos produits par exemple.


FONCTION GET_PRODUCTS
- request.get possède un argument "params", qui permet de spécifier les paramètres de l'URL dans un dictionnaire. j'aimerai que tu te renseigne sur cette feature et l'incorpore au code (ton url sera plus lisible et courte).
- si le statut code est 404, il vaut mieux créer une erreur car sinon la suite du code va planter.
-

FONCTION CLEAN_PRODUCT
- attention tu peux très bien avoir des produits qui n'ont pas la clé souhaité, et tu auras alors une erreur KeyError affichée. Utiliser la méthode de dictionnaire "get" pour pallier à ça.
- ton code est très long et se répète. Une simple boucle sur une liste de clés souhaitées permet d'y pallier, comme tu pourras le constater.
- la fonction clean_product doit retourner None si une clé est pas bonne. Pas un produit avec des clé à None. Car un tel produit est inutilisable.
- tu pourras voir dans la fonction que j'ai englobé les conditions dans des variables pour créer une forme de documentation. On appel cela autodocumenter son code par le nommage.


FICHIER SCORE_CONVERTION
- la récupération de l'ID du score doit se faire dynamiquement via une requête GET. Ce n'est pas très sorcier et permet d'éviter des erreurs potentielles si une base de données n'a pas la même correspondance d'IDs.


ANNEXE
- attention à l'application de la PEP8 (les fonctions doivent être espacées de 2 lignes par exemple). Utiliser un formateur automatique pour éviter les petites erreurs de pep8. ;)
- j'ai vu que tu jouais avec pprint, c'est une bonne idée ;)
- de manière générale, éviter au maximum d'utiliser des abréviation qui ne facilitent pas la lecture du code. N'oublie pas qu'on lit bien plus qu'on n'écrit le code.
- tout code qui possède des répétitions est à réfléchir pour éviter ces répétitions :) tu gagneras en lisibilité et en maintenabilité (concept DRY, Don't Repet Yourself).



LA SUITE
- actuellement ton code ne lie pas les catégories aux produits.
- je te donne le processus qu'il te faut appliquer:

1. récupérer chaque produit depuis OFF (fait)
2. pour chaque produit récupéré:
    2.1 nettoyer le produit
    2.2 si le produit nettoyé est bon:
        2.2.1 récupérer l'ID du nutriscore du produit
        2.2.2 insérer le produit en base de données
        2.2.3 pour chaque catégorie du produit:
            2.2.3.1 insérer la catégorie si elle n'existe pas
            2.2.3.2 lier la catégorie au produit (insérer l'ID de la catégorie et du produit dans la table d'association category_product)

- tu peux ensuite commencer à créer ton projet *client* :)