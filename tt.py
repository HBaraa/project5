# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
from pprint import pprint

req= urlopen("https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1.json")
#print(req.read())
data = json.loads(req.read())
print(type(data))
pprint([item for item in data['products']; if item == 'product_name_fr'])
#print(data['products'])(['product_name_fr'])