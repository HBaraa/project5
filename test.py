import json
from urllib.request import urlopen
from pprint import pprint

#req= urlopen("https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1.json")
#print(req.read())
#data = json.loads(req.read())
#print(type(data))
#pprint(data)
#print(data['page_count'])

#with open('APIoff.json', 'w') as f:
  #  json.dump(data, f, indent=2)


with open('APIoff.json') as f:
    data_raw = json.load(f)
    row = data_raw["products"]
    for i in range(0, 10):
      ligne = row[i]
        #print (row[i])
      for item in ligne:
        if (item == "product_name_fr") :
          print( item, " = " ,ligne[item])
      for code in ligne:
        if (code == "code"):
          print( code, " = ", ligne[code])
      for description in ligne:
        if (description == "ingredients_text_fr"):
          print( description, " = ", ligne[description])
      for url in ligne:
        if (url == "url"):
          print( url, " = ", ligne[url])
      for store in ligne:
        if (store == "stores"):
          print( store, " = ", ligne[store])
      for score in ligne:
        if (score == "nutriscore_grade"):
          print(score, " = " , ligne[score])
        
