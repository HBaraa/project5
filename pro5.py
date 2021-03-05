# -*- coding: utf-8 -*-
import json

def find_datas(products, codes, descriptions, links, stores, nutriscores, categories):
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

        
        return(products, codes, descriptions, links, nutriscores, categories)

def main_search():
    products = []
    codes = []
    descriptions = []
    links = []
    stores = []
    nutriscores = []
    categories = []
    #datas =[]
    find_datas(products, codes, descriptions, links, stores, nutriscores, categories)
    products = tuple(products)
    
    
    
if __name__ == "__main__":
    main_search()