# -*- coding: utf8 -*-

class Category():
    def __init__(self, name):
        self.name = name
        

class Product():
    def __init__(self, nutriscore_id, name, code, description, url, store):
        self.nutiscore_id = nutriscore_id
        self.name = name
        self.code = code
        self.description = description
        self.url = url
        self.store = store


class Category_product():
    def __init__(self, catgory_id, product_id):
        self.category_id = category_id
        self.product_id = product_id


class Nutriscore():
    def __init__(self, score):
        self.score = score



class Favorite():
    def __init__(self, product_id, substitute_id):
        self.product_id = product_id
        self.substitute_id = substitute_id
