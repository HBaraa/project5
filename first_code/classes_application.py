# -*- coding: utf-8 -*-
import string
import re
import mysql.connector
from mysql.connector import Error
from pprint import pprint


from basic_datas.data_connexion import DATABASE_NAME, HOST, USER, PASSWORD
from basic_modules.bdd_connexion import connect_db
from basic_modules.get_datas import get_products, get_categories, clean_product
from basic_modules.scoreconv import convert_score

connexion = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
cnx = connexion.cursor(buffered=True)


class InsertIntoTables:
    def __init__(self):
        self.connexion = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
        self.cnx = self.connexion.cursor(buffered=True)

    def fill_tables(self, product, cleaned_product):
        if product.get("nutriscore_grade") in ["a", "b", "c", "d", "e"]:
            grade = product.get("nutriscore_grade")
            nutri_grade = convert_score(grade)
            # print(cleaned_product)
            insert_product_query = (
                'INSERT IGNORE INTO product'
                ' (name, code, description, url, store, nutriscore_id)'
                ' VALUES (%s, %s, %s, %s, %s, %s)'
            )
            self.cnx.execute(
                insert_product_query,
                (
                    cleaned_product["prod_name"],
                    cleaned_product["prod_code"],
                    cleaned_product["details"],
                    cleaned_product["link"],
                    cleaned_product["prod_store"],
                    cleaned_product["nutri_score"]
                )
                )
            self.connexion.commit()
        else:
            pass

    def insert_categories(self, category_name):
        insert_category_query = (
            "INSERT IGNORE INTO category  (name)"
            "  VALUES (%s)"
        )
        self.cnx.execute(insert_category_query, (category_name, ))
        self.connexion.commit()

    def insert_category_product(self, category_id, product_id):
        query = (
            'INSERT IGNORE INTO category_product (category_id, product_id)'
            '  VALUES(%s, %s)'
        )
        self.cnx.execute(query, (category_id, product_id))
        self.connexion.commit()

    def get_product_id(self):
        query = 'SELECT LAST_INSERT_ID() FROM product'
        self.cnx.execute(query)
        product_id = self.cnx.fetchone()[0]
        return product_id

    def get_category_id(self):
        second_query = 'SELECT LAST_INSERT_ID() FROM category'
        self.cnx.execute(second_query)
        category_id = self.cnx.fetchone()[0]
        return category_id


class AppSql:
    def __init__(self):
        self.inserttables = InsertIntoTables()
        self.products = []
        self.categories = []

    def insert_datas(self):
        self.products = get_products()
        for product in self.products:
            cleaned_product = clean_product(product)
            self.inserttables.fill_tables(product, cleaned_product)
            product_id = self.inserttables.get_product_id()
            if type(product["categories"]) == str:
                self.categories = product.get("categories")
                # print(categories)
                # print(type(categories))
                categories_names = self.categories.split(',')
                # print(list(categories_names))
                # n=len(categories_names)
                # print(n)
                for category_name in categories_names:
                    self.inserttables.insert_categories(category_name)
                    category_id = self.inserttables.get_category_id()
                    self.inserttables.insert_category_product(
                        category_id, product_id
                        )


class Interface_diplay:
    def __init__(self):
        self.inserttables = InsertIntoTables()

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
        print((self.inserttables.cnx.fetchall()))

    def display_all_products(self, category_id):
        query = (
            "SELECT  product.id, product.name FROM product"
            " INNER JOIN category_product"
            " ON product.id = category_product.product_id"
            " WHERE category_product.category_id=%s"
        )
        self.inserttables.cnx.execute(query, (category_id, ))
        print((self.inserttables.cnx.fetchall()))

    def display_product(self, entry_number):
        query = "SELECT * FROM product WHERE id=%s"
        self.inserttables.cnx.execute(query, (entry_number, ))
        print((self.inserttables.cnx.fetchall()))

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
        return substitute_id

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
            "INSERT INTO  favorite (substituted_id, substitute_id)"
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
