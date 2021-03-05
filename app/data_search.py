# -*- coding: utf-8 -*-

import json

# Dans le cadre du projet 5, il est demandé d'utiliser une bibliothèque qui s'appelle "requests", qui va directement requêter un site web pour récupérer les données JSON
# voici l'URL qui te permet d'accéder aux produits :
# https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1


def request_products() -> list:
    """Request the OpenFoodFact products.

    Returns the products as a list.
    """
    # 1. lancer une requête vers l'API
    # 2. traiter la réponse rapidement (récupérer en json, et juste récupérer la partie 'products')
    # 3. retourner la liste de produits de manière brute


def clean_product(product: dict) -> dict:
    """Clean a product.

    Clean the given product an return the cleaned version.
    """
    # tu vas créer un dictionnaire vide qui s'appel 'cleaned_product'
    # tu vas le remplir en fonction des champs du produit
    # si un champ du produit n'est pas valide, tu retourne None
    # sinon, tu retourne le produit

def insert_product(product):
    """Save the product in the database.

    NOTE: we don't save the categories for now.
    """
    # 1. connexion à la BDD
    # 2. récupérer l'id du nutriscore
    # 3. requête d'insertion de produit


def get_products():
    """Get the products from OFF and insert them in the database.

    NOTE: cette méthode va remplacer notre méthode 'find_data'
    """
    # appel la méthode pour requêter l'API
    products = request_products()

    # pour chaque produits trouvé
    for product in products:

        # cleaner le produit
        cleaned = clean_product(product)

        # continuer la boucle si le produit n'est pas valide
        if not cleaned:
            continue

        # sauvegarger le produit en base de données
        insert_product(cleaned)

        # récupérer aussi les catégories du produit

        # insérer les catégories si elles n'existent pas encore
        # lier les catégories aux produits
        # = une fonction d'insertion des catégories


""" EXEMPLE D'INSERTION DE PRODUITS SI LES PRODUITS SONT DES DICTIONNAIRES """
products = [...] # une liste de dictionnaires
for product in products:
    cursor.execute("INSERT INTO product (name, stores) VALUES (%s, %s)", (product["name"], product["stores"]))



def find_datas():
    products = []
    codes = []
    descriptions = []
    links = []
    stores = []
    nutriscores = []
    categories = []

    with open('APIoff.json') as file:
        data = json.load(file)

        products = data["products"]
        for product in products:
            if not product.get("product_name_fr"):
                continue

            # vérifier que le produit (qui est un dictionnaire possède les bonnes clés
            # et ensuite le sauvegarder

        for i in range(0, 10):
            ligne = row[i]
            # print (row[i])
            """ ici le produit est un dictionnaire """
            for item in ligne:
                if (item == "product_name_fr") :
                    products.append(ligne[item])
                    print(item, " : " ,ligne[item])
                    for code in ligne:
                        if (code == "code"):
                            codes.append(ligne[code])
                            print( code, " : ", ligne[code])
                    for description in ligne:
                        if (description == "ingredients_text_fr"):
                            descriptions.append(ligne[description])
                            print( description, " : ", ligne[description])
                    for url in ligne:
                        if (url == "url"):
                            links.append(ligne[url])
                            print( url, " : ", ligne[url])
                    for store in ligne:
                        if (store == "stores"):
                            stores.append(ligne[store])
                            print( store, " : ", ligne[store])
                    for score in ligne:
                        if (score == "nutriscore_grade"):
                            nutriscores.append(ligne[score])
                            print(score, " : " , ligne[score])
                    for cat in ligne:
                        if (cat == "categories_old"):
                            categories.append(ligne[cat])
                            print(cat, " : ", ligne[cat])
        return products, codes, descriptions, links, stores, nutriscores, categories

#def main_search():
 #   products = []
 #   codes = []
  #  descriptions = []
   # links = []
    #stores = []
    #nutriscores = []
    #categories = []
    #datas =[]
    #find_datas(products, codes, descriptions, links, stores, nutriscores, categories)
    #products = tuple(products)
    #return products, codes, descriptions, links, stores, nutriscores, categories



if __name__ == "__main__":
    find_datas()