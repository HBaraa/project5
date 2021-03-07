# -*- coding: utf-8 -*-
import json
import requests
from pprint import pprint

def find_products():
    
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
    #print(products)
    for product in products:
       #pprint(product)
       print(product['product_name_fr'])
    #print(products['product_name_fr'])
    #product = prods['args']
    #print(type(prods['products']))
    

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
    find_products()
    