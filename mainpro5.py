# -*- coding: utf-8 -*-

# imports de la stdlib
# ici on en a pas

# imports des libs tierces
import requests
from mysql.connector import Error

# ici, les imports personnels de notre app
from data_search import find_datas
from connect_opff import connect_db
import openFOODfacts as opff
from scoreTOid import convert_score
from data_connexion import DATABASE_NAME, HOST, USER, PASSWORD


def insert_values_category(categories):
    """Method that inserts predefined categories into the category table"""
    # Inserting our first values into table1
    try:
        sql_category_formula = """INSERT INTO Category(name) VALUES (%s)"""
        cursor.executemany(sql_category_formula, categories)
        return True
    except :
        print("""Erreur dans l'insertion des données dans la table category""")
        return False


def fill_products():
    products = []
    codes = []
    descriptions = []
    links = []
    stores = []
    nutriscores = []
    categories = []
    products, codes, descriptions, links, stores, nutriscores, categories = find_datas()
    print(products)

    conn = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
    if conn:
        print("done")
    else:
        print("don't yet")
    c = conn.cursor()
    #c.execute('SELECT * FROM nutriscore')
    #print(c.fetchall())
    #c.execute("""INSERT INTO product(nutriscore_id, name, code, description, url, store)
       #       (%s, %s, %s, %s, %s, %s);""" , (score_id, products, codes, descriptions, links, stores))
    #conn.commit()
    #c.execute("SELECT * FROM product")
    #print(c.fetchall())

    score_id = convert_score(nutriscores)
    print(score_id)
    for product in products:
        c.execute("""INSERT INTO product(name)
          VALUES(%s);""", (product.name,))
        conn.commit()

    #c.execute("SELECT * FROM product")
    #conn.commit()
    #print(c.fetchall())
    #data = (score_id, products, codes, descriptions, links, stores)
    #c.execute(insert_prod, data)
    #c.execute("SELECT * FROM product")

    #sql_category_formula = """INSERT INTO Category(name)
     #                                       VALUES (%s)"""
    #data = (categories)
    #c.execute(sql_category_formula, data, )
    #select_stmt = "SELECT * FROM category"
    #c.execute(select_stmt)
    #print(c.fetchall())


if __name__ == "__main__":
    fill_products()

