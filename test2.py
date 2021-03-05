import json
from urllib.request import urlopen
from pprint import pprint

#req= urlopen("https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1.json")
#print(req.read())
#data = json.loads(req.read())
#print(type(data))
#pprint(data)
#print(data['page_count'])

class SearchData:
    
    def __init__(self, products, codes, descriptions, links, stores, nutriscores, categories):
        self.products = products
        self.codes = codes
        self.descriptions = descriptions
        self.links = links
        self.stores = stores
        self.nutriscores = nutriscores
        self.categories = categories
        self.data = []

    def fin_datas(self):
        with open('APIoff.json') as f:
            data_raw = json.load(f)
            row = data_raw["products"]
            for i in range(0, 10):
                ligne = row[i]
                #print (row[i])
                for item in ligne:
                    if (item == "product_name_fr") : 
                        self.products.append(ligne[item])
                        print(item, " : " ,ligne[item])
        return self.products
        