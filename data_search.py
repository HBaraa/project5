# -*- coding: utf-8 -*-
import json
import requests
from pprint import pprint
import mysql.connector
from mysql.connector import Error


from scoreconv import convert_score
from data_connexion import DATABASE_NAME, HOST, USER, PASSWORD
from bdd_connexion import connect_db


def request_products() -> list:
    
    datas = requests.get("https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1.json", )
    if datas.status_code == 200:
        print('Success!')
    elif datas.status_code == 404:
        print('Not Found.')
    prods = datas.json()
    if prods:
        print("*********____DONE____*******")
    products = prods['products']
    print(type(products))
    #pprint(products)
    
       #pprint(product)
    #   print(product['product_name_fr'])
    #print(products['product_name_fr'])
    #product = prods['args']
    #print(type(prods['products']))
    return products

def clean_product(product: dict) -> dict:
    cleaned_product = {}
    if product["product_name_fr"]:
        print("product is valid")
        cleaned_product["prod_name"] = product["product_name_fr"]     
    else:
        cleaned_product["prod_name"]= None
        print("this product isn't valid")
        pass
    if product["code"]:
        print("code is valid")
        cleaned_product["prod_code"] = product["code"]
    else:
        cleaned_product["prod_code"]= None
        print("this code isn't valid")    
        pass
    if (type(product["ingredients_text_fr"])==str and len(product["ingredients_text_fr"]) >= 5 ):
        print("description is valid")
        cleaned_product["details"] = product["ingredients_text_fr"]     
    else:
        cleaned_product["details"]= None
        print("this description isn't valid")
        pass
    if product["url"]:
        print("link is valid")
        cleaned_product["link"] = product["url"]     
    else:
        cleaned_product["link"]= None
        print("this link isn't valid")
        pass
    if product["stores"]:
        print("store is valid")
        cleaned_product["prod_store"] = product["stores"]     
    else:
        cleaned_product["prod_store"]= None
        print("this store isn't valid")
        pass
    if product["nutriscore_grade"]:
        print("nutriscore is valid")
        cleaned_product["nutri_score"] = product["nutriscore_grade"]     
    else:
        cleaned_product["nutri_score"]= None
        print("this nutriscore isn't valid")
        pass   
    
    return cleaned_product
    
#def insert_product(product):

    

def find_datas():
    products = []
    codes = []
    descriptions = []
    links = []
    stores = []
    nutriscores = []
    categories = []
    with open('APIoff.json') as f:
        data_raw = json.load(f)
        row = data_raw["products"]
        for i in range(0, 10):
            ligne = row[i]
             #print (row[i])
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
    #find_datas()
    connexion = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
    c = connexion.cursor()
    products = request_products()
    for product in products:
        cleaned_product= clean_product(product)
        cleaned_product["nutri_score"]=convert_score(cleaned_product["nutri_score"])
        print(cleaned_product)
        insert_query =  'INSERT INTO product (nutriscore_id, name, code, description, url, store)  VALUES (%s, %s, %s, %s, %s, %s)'
        c.execute(insert_query, (cleaned_product["nutri_score"], cleaned_product["prod_name"], cleaned_product["prod_code"], cleaned_product["details"], cleaned_product["link"], cleaned_product["prod_store"]))
        connexion.commit()
        #(%s, %s, %s, %s, %s, %s)

    c.execute("""SELECT * FROM product""")
    print(c.fetchall())
        
    