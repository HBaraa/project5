# -*- coding: utf-8 -*-
import json
import requests
from pprint import pprint
import mysql.connector
from mysql.connector import Error


from scoreconv import convert_score
from data_connexion import DATABASE_NAME, HOST, USER, PASSWORD
from bdd_connexion import connect_db


def get_products() -> list:
    datas = requests.get("https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=20&json=1.json", )
    if datas.status_code == 200:
        print('Success!')
    elif datas.status_code == 404:
        print('Not Found.')
    prods = datas.json()
    #pprint(prods)
    if prods:
        print("*********____DONE____*******")
    products = prods['products']
    print(type(products))
    #pprint(products)
    return products


def get_categories() -> list:
    categ_infos = []
    categories = []
    group={}
    info = requests.get("https://fr.openfoodfacts.org/categorie/produits-tripiers/categories.json", )
    if info.status_code == 200:
        print('YOU GOT IT!')
    elif info.status_code == 404:
        print('NOT FOUND.')
    categs = info.json()
    #pprint(categs)  #affichage du dictionnaire
    if categs:
        print("*********____WELL DONE____*******")
    categ_infos= categs['tags']
    #print(type(categ_infos))   #liste
    #pprint(categ_infos) #affichage clair d'une liste des dictionnaires
    n = len(categ_infos)
    for i in range (0, n-1):
        element = categ_infos[i]
        if element['name']:
            categories.append(element['name'])
    #print(categories)
    return categories



def clean_product(product: dict) -> dict:
    cleaned_product = {}
    wanted_keys = {
        "product_name": "name",
        "code": "code",
        "ingredients_text_fr": "details",
        "url": "url",
        "stores": "stores",
        "nutriscore_grade": "nutriscore",
    }
    for base_key, key in wanted_key.items():
        is_a_critical_key = not product.get(base_key) and key != "details"
        details_is_too_short = key == "details" and product[key] < 5

        if is_a_critical_key:
            return None
        if details_is_too_short:
            continue

        cleaned_product[key] = product[key]
    return cleaned_product


def insert_product(product):
    cleaned_product= clean_product(product)
    cleaned_product["nutri_score"]=convert_score(cleaned_product["nutri_score"])
    print(cleaned_product)
    insert_product_query =  'INSERT INTO product (name, code, description, url, store, nutriscore_id)  VALUES (%s, %s, %s, %s, %s, %s)'
    c.execute(insert_product_query, (cleaned_product["prod_name"], cleaned_product["prod_code"], cleaned_product["details"], cleaned_product["link"], cleaned_product["prod_store"],  cleaned_product["nutri_score"]))
    connexion.commit()

def insert_categories(category):
    insert_category_query= 'INSERT INTO category (name)  VALUES (%s)'
    c.execute(insert_category_query, (category, ))
    connexion.commit()

def main():
    products = get_products()
    for product in products:
        insert_product(product)
    c.execute('SELECT * FROM product')
    connexion.commit()
    print(c.fetchall())
    categories = get_categories()
    for category in categories:
        insert_categories(category)
    c.execute('SELECT * FROM category')
    connexion.commit()
    print(c.fetchall())


if __name__ == "__main__":
    connexion = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
    c = connexion.cursor(buffered=True)
    main()
