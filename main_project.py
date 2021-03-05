# -*- coding: utf8 -*-
import requests
import pymysql
import mysql.connector

import openFOODfacts as opff
from data_connexion import DATABASE_NAME, HOST, USER, PASSWORD
from classes import GetData, Categories, Products


def import_sql_file(cursor, sql_file):
        """ function to import the sql file and create the db """
        statement = ""
        for line in open(sql_file):
            if not line.strip().endswith(';'): 
                statement = statement + line
            else:   
                #statement = statement + line
                #cursor.execute(statement)
                statement = ""

def get_products(connexion, PRODUCTS_URL):
        cursor = connexion.cursor(pymysql.cursors.DictCursor)
        for page in range(1, 100): 
            prod_file = requests.get(PRODUCTS_URL.format(page)).json()  
            for prod in prod_file['products']:
                try:
                    product_information = (prod["name"], prod["code"], prod["description"], prod["url"], prod["store"])
                    product_listed.append(opff.Product(prod["name"], prod["code"], prod["description"], prod["url"], prod["store"]))        
                    cursor.execute("INSERT INTO product" "(name, code, description, url, store)"\
                    "VALUES (%s, %s, %s, %s)", product_information)
                    cursor.execute("INSERT INTO nutriscore" "(score)"
                    "VALUES (%s)", product_information)
                    connexion.commit()
                    cursor.execute("SELECT nutriscore.id AS score_id"\
                    "FROM nutriscore"\
                    "INNER JOIN product"\
                    "ON product.score = nutriscore.score")
                    connexion.commit()
                    cursor.execute("INSERT INTO Category_product(product_id)"\
                    "SELECT id"\
                    "FROM product")
                    connexion.commit()
                    print("you have counsulted ", len(product_listed), "products")
                except KeyError: #Don't take lignes without 'product_name'
                    pass
                except connexion.OperationalError: #Don't take the products with encoding error
                    pass
                except connexion.DataError: #Pass when product name is too long
                    pass
        
def main():
    PRODUCTS_URL = 'https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1'
    database = DATABASE_NAME
    product_information = ()
    product_listed = ()
    try:
            """  Connection to the database """
            connexion = mysql.connector.connect(user=USER,
                                        password=PASSWORD,
                                        host= HOST,
                                        database=DATABASE_NAME,)
            cursor = connexion.cursor
    except pymysql.InternalError:
            print("No database founded, we have to create a one ")
            connexion = mysql.connector.connect(user=USER, 
                                        password=PASSWORD,
                                        host= HOST,)
                    
            cursor = connexion.cursor()
            cursor.execute(" DROP database IF EXISTS openfoodfact")
            sql = "CREATE database openfoodfact"
            cursor.execute(sql) 
    project_file = sql_file(cursor,"openfoodfact.sql")
    new_data = 1
    import_sql_file(cursor, project__file)
    get_products(connexion, PRODUCTS_URL)


if __name__ == "__main__":
    main()
