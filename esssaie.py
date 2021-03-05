# -*- coding: utf-8 -*-
import requests
import sqlite3
import unidecode
import pymysql
import mysql.connector

import openFOODfacts as opff

class OpenFood:

    def __init__(self):
        self.db = mysql.connector.connect(user='root', password='4405', host='localhost', database='openfoodfact')


    def found_products():
        '''get categories from the URL API'''
        r_prod = requests.get('https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1')
        data_json = r_prod.json()
        data_tags = data_json.get('tags')
        data_prod = [prod.get('name', 'None') for prod in data_tags]
        i = 2
        while i < 10:
            self.cursor = self.db.cursor()
            add_product = ("INSERT INTO product" "(name)" "VALUES('{}')".format(data_prod[i]))
            self.cursor.execute(add_product)
            self.db.commit()
            self.cursor.close()
            i=i+1



def main():
    OpenFood.found_products()
    
    
if __name__ == "__main__":
    main()

    