# -*- coding: utf-8 -*-
import requests
import sqlite3
import pymysql
import pymysql.cursors
import mysql.connector
from mysql.connector import Error




from data_search import find_datas
from data_connexion import DATABASE_NAME, HOST, USER, PASSWORD
import openFOODfacts as opff
from scoreTOid import convert_score

#def fill_Procudcts():

def connect_db(USER, PASSWORD, HOST, DATABASE_NAME):
    connection = None
    try:
        connexion = mysql.connector.connect(user=USER,
                                    password=PASSWORD,
                                    host=HOST,
                                    database=DATABASE_NAME)
        cursor = connexion.cursor
        print (" ****** connected to database ****** ")
    except Error as e:
        print(f"The error '{e}' occurred")
        pass
    
    return connexion

def fill_Procudcts():
    products = []
    codes = []
    descriptions = []
    links = []
    stores = []
    nutriscores = []
    categories = []    
    products, codes, descriptions, links, stores, nutriscores, categories = find_datas()
    print(products)
    #connexion = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
    #if (connexion.cursor()):
    #    print("yes")
    #else:
    #    print("not")
    
    #query = """USE openfoodfact"""
    #cursor = connexion.cursor
    #try:
    #    cursor.execute(query)
    #    connexion.commit()
    #    print("Query executed successfully")
    #except Error as e:
    #    print(f"The error '{e}' occurred")
    conn = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
    sqlite3.connect('openfoodfact')
    if conn:
        print("done")
    else:
        print("don't yet")
    c = conn.cursor()
    c.execute('SELECT * FROM nutriscore')
    print(c.fetchall())
    score_id = convert_score(nutriscores)
    print(score_id)
    
    

    #add_product = ("INSERT INTO product" "(nutriscore_id, name, code, description, link, store)" "VALUES('%s, %s, %s, %s, %s, %s')".format(scores_id, products,  descriptions, links, stores))
    #c.execute(add_product)
    #db.commit()
    #c.execute('SELECT name FROM product')
    #print(c.fetchall())
    #conn.commit()
    #conn.close()
    #query = """USE openfoodfact"""
    #cursor.execute(query)
    #connection.commit()
    #cursor.close()
      
    #products, codes, descriptions, links, stores, nutriscores, categories = find_datas()
    #print(products, codes)
    #ligne =[]
    #for i in range(5):
    #    for k in range(9):
    #        ligne[i][k].append(scores_id[k])
    #        ligne[i][k].append(products[k])
    #        ligne[i][k].append(codes[k])
    #        ligne[i][k].append(descriptions[k])
    #        ligne[i][k].append(links[k])
    #        ligne[i][k].append(stores[k])
    #    print(ligne[i])
            



if __name__ == "__main__":
    fill_Procudcts()
