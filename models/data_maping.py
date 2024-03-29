﻿# -*- coding: utf-8 -*-
from models.db_creation.insertion import InsertIntoTables


class ModelMapping:
    """ This class is used to make the link between"""
    """ MVC modules and database"""
    def __init__(self):
        self.inserttables = InsertIntoTables()
        self.nutrition = None
        self.substitute_id = None

    def display_category(self, number):
        first_query = "SELECT category.name FROM category WHERE id=%s"
        self.inserttables.cnx.execute(first_query, (number, ))
        self.inserttables.cnx.fetchall()
        query = (
            "SELECT DISTINCT category_id, product_id FROM category_product"
            " LEFT JOIN product ON product.id = category_product.product_id"
            " WHERE category_product.category_id=%s"
        )
        self.inserttables.cnx.execute(query, (number, ))
        self.inserttables.cnx.fetchall()

    def display_all_categories(self):
        query = "SELECT * FROM category ORDER BY id LIMIT 50"
        self.inserttables.cnx.execute(query)
        categories = self.inserttables.cnx.fetchall()
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
        return prods

    def display_product(self, entry_number):
        query = "SELECT * FROM product WHERE id=%s"
        self.inserttables.cnx.execute(query, (entry_number, ))
        elements = self.inserttables.cnx.fetchall()
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
            "INSERT IGNORE INTO  favorite (substituted_id, substitute_id)"
            " VALUES(%s, %s)"
        )
        self.inserttables.cnx.execute(
            query_update_sub_id, (prod_number, sub_number)
            )
        self.inserttables.connexion.commit()

    def display_details(self, product_id):
        details_query = (
            "SELECT id, name, code, description, url,"
            " store, nutriscore_id FROM product"
            " WHERE product.id = %s "
        )
        self.inserttables.cnx.execute(details_query, (product_id, ))
        details = self.inserttables.cnx.fetchall()
        self.inserttables.connexion.commit()
        for detail in details:
            self.nutrition = detail[0]
            print(
                "-", "ID".center(40), ":", detail[0], "\n",
                "-", "Name".center(40), ":", detail[1], "\n",
                "-", "Code".center(40), ":", detail[2], "\n",
                "-", "Description".center(40), ":", detail[3], "\n",
                "-", "Link".center(40), ":", detail[4], "\n",
                "-", "Stores".center(40), ":", detail[5], "\n",
                "-", "Nutriscore".center(40), ":", detail[6], "\n"
            )
        return

    def score(self, product_id):
        details_query = (
            "SELECT name, code, description, url,"
            " store, nutriscore_id FROM product"
            " WHERE product.id = %s "
        )
        self.inserttables.cnx.execute(details_query, (product_id, ))
        details = self.inserttables.cnx.fetchall()
        self.inserttables.connexion.commit()
        for detail in details:
            grade = detail[5]
            return grade

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

    def insert_substitute(self, product_id, substitute_id):
        query = (
            "INSERT IGNORE INTO favorite (substituted_id, substitute_id)"
            " VALUES(%s, %s)"
        )
        self.inserttables.cnx.execute(query, (product_id, substitute_id))
        self.inserttables.connexion.commit()

    def substituted_saved(self):
        query = (
            "SELECT DISTINCT product.id FROM Product"
            " INNER JOIN favorite"
            " ON product.id = favorite.substituted_id"
        )
        self.inserttables.cnx.execute(query)
        products = self.inserttables.cnx.fetchall()
        return products

    def substitute_saved(self):
        query = (
            "SELECT DISTINCT product.id, product.name FROM Product"
            " INNER JOIN favorite"
            " ON product.id = favorite.substitute_id"
        )
        self.inserttables.cnx.execute(query)
        subsstitute_lst = self.inserttables.cnx.fetchall()
        return subsstitute_lst
