﻿# -*- coding: utf-8 -*-
import string
import re
import mysql.connector
from mysql.connector import Error


from mvc_modules.insertion import InsertIntoTables


class Interface_diplay:
    def __init__(self):
        self.inserttables = InsertIntoTables()
        self.nutrition_= None
        self.substitute_id = None
        
    def display_category(self, number):
        first_query = "SELECT category.name FROM category WHERE id=%s"
        self.inserttables.cnx.execute(first_query, (number, ))
        print((self.inserttables.cnx.fetchall()))
        query = (
            "SELECT DISTINCT category_id, product_id FROM category_product"
            " LEFT JOIN product ON product.id = category_product.product_id"
            " WHERE category_product.category_id=%s"
        )
        self.inserttables.cnx.execute(query, (number, ))
        print((self.inserttables.cnx.fetchall()))

    def display_all_categories(self):
        query = "SELECT * FROM category ORDER BY id"
        self.inserttables.cnx.execute(query)
        categories = self.inserttables.cnx.fetchall()
        print(categories)
        return categories

    def display_all_products(self, category_id):
        query = (
            "SELECT DISTINCT product.id, product.name FROM product"
            " INNER JOIN category_product"
            " ON product.id = category_product.product_id"
            " WHERE category_product.category_id=%s"
        )
        self.inserttables.cnx.execute(query, (category_id, ))
        prods = self.inserttables.cnx.fetchall()
        print(prods)
        return prods

    def display_product(self, entry_number):
        query = "SELECT * FROM product WHERE id=%s"
        self.inserttables.cnx.execute(query, (entry_number, ))
        elements = self.inserttables.cnx.fetchall()
        #for element in elements:
        print(elements)
        return elements


    def get_sustitute_id(self, prod_id, categ_id):
        substitute_id = ""
        nutriscore_query = "SELECT nutriscore_id FROM product WHERE id=%s"
        self.inserttables.cnx.execute(nutriscore_query, (prod_id,))
        score_id = self.inserttables.cnx.fetchone()[0]
        self.inserttables.connexion.commit()
        query = (
            "SELECT product.id FROM product"
            " INNER JOIN category_product"
            " ON product.id = category_product.product_id"
            " INNER JOIN category"
            " ON category_product.category_id = category.id"
            " WHERE category.id = %s  AND (product.nutriscore_id <= %s)"
        )
        self.inserttables.cnx.execute(query, (categ_id, score_id))
        substitute_id = self.inserttables.cnx.fetchone()[0]
        self.inserttables.connexion.commit()
        return(substitute_id)

    def get_substitute(self, substituted_id):
        query = (
            "SELECT favorite.substitute_id FROM favorite"
            " WHERE favorite.substituted_id = %s"
        )
        self.inserttables.cnx.execute(query, (substituted_id, ))
        substitute_id = self.inserttables.cnx.fetchone()[0]
        self.inserttables.connexion.commit()
        return substitute_id

    def save_substitute(self, prod_number, sub_number):
        query_update_sub_id = (
            "INSERT IGNORE INTO  favorite (substituted_id, substitute_id)"
            " VALUES(%s, %s)"
        )
        self.inserttables.cnx.execute(
            query_update_sub_id, (prod_number, sub_number)
            )
        self.inserttables.connexion.commit()

    def display_saved_favorites(self):
        query_favorite = (
            "SELECT product.id, product.name FROM product"
            " INNER JOIN favorite ON product.id = favorite.substituted_id"
        )
        self.inserttables.cnx.execute(query_favorite)
        print("Your favorite products saved are :  ")
        print((self.inserttables.cnx.fetchall()))

    def display_substitute(self, sub_id):
        query = (
            "SELECT * FROM product"
            " WHERE product.id = %s"
        )
        self.inserttables.cnx.execute(query, (sub_id, ))
        print((self.inserttables.cnx.fetchall()))

    def display_all_substitutes(self):
        query = (
            "SELECT * FROM favorite"
        )
        self.inserttables.cnx.execute(query)
        subs = self.inserttables.cnx.fetchall()
        return subs

    def display_details(self, product_id):
        details_query = (
            "SELECT name, code, description, url, store, nutriscore_id FROM product"
            " WHERE product.id = %s "
        )
        self.inserttables.cnx.execute(details_query, (product_id, ))
        details = self.inserttables.cnx.fetchall()
        self.inserttables.connexion.commit()
        #print(details)
        for detail in details:
            self.nutrition_grade = detail[5]
            print(" -  Nom :   ", detail[0], "\n",
            "-  Code  :   ", detail[1], "\n",
            "-  Ingrédients  :   ", detail[2], "\n",
            "-  Url  :   ", detail[3], "\n",
            "-  Magasins  :   ", detail[4], "\n",
            "-  Nutriscore  :   ", detail[5], "\n"
            )
        
    def substitute_product(self, category_id):
        query = (
            "SELECT product.id FROM product"
            " INNER JOIN category_product"
            " ON category_product.product_id = product.id "
            " WHERE category_product.category_id = %s"
        )
        self.inserttables.cnx.execute(query, (category_id, ))
        substitute_id = self.inserttables.cnx.fetchall()
        return substitute_id
        