import json
from urllib.request import urlopen
from pprint import pprint

#req= urlopen("https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1.json")
#print(req.read())
#data = json.loads(req.read())
#print(type(data))
#pprint(data)
#print(data['page_count'])

prod_list = []
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
            prod_list.append(ligne[item])
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


    print(tuple(prod_list))
    print(tuple(codes))
    print(tuple(descriptions))
    print(tuple(links))
    print(tuple(stores))
    print(tuple(nutriscores))
    print(tuple(categories))

    #products=tuple(prod_list)
    
        