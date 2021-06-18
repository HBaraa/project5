# -*- coding: utf-8 -*-
from basic_datas.data_connexion import USER, PASSWORD, HOST, DATABASE_NAME
from models.db_creation.bdd_connexion import connect_db


class InsertIntoTables:
    def __init__(self):
        self.connexion = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
        self.cnx = self.connexion.cursor(buffered=True)

    def fill_tables(self, product, cleaned_product):
        if product.get("nutriscore_grade") in ["a", "b", "c", "d", "e"]:
            # print(cleaned_product)
            insert_product_query = (
                "INSERT IGNORE INTO product"
                " (name, code, description, url, store, nutriscore_id)"
                " VALUES (%s, %s, %s, %s, %s, %s)"
            )
            self.cnx.execute(
                insert_product_query,
                (
                    cleaned_product["prod_name"],
                    cleaned_product["prod_code"],
                    cleaned_product["details"],
                    cleaned_product["link"],
                    cleaned_product["prod_store"],
                    cleaned_product["nutri_score"],
                ),
            )
            self.connexion.commit()
        else:
            pass

    def insert_categories(self, category_name):
        insert_category_query = "INSERT IGNORE INTO category (name)" " VALUES (%s)"
        self.cnx.execute(insert_category_query, (category_name,))
        self.connexion.commit()

    def insert_category_product(self, category_id, product_id):
        query = (
            "INSERT IGNORE INTO category_product (category_id, product_id)"
            "  VALUES(%s, %s)"
        )
        self.cnx.execute(query, (category_id, product_id))
        self.connexion.commit()

    def get_product_id(self):
        query = "SELECT LAST_INSERT_ID() FROM product"
        self.cnx.execute(query)
        product_id = self.cnx.fetchone()[0]
        return product_id

    def get_category_id(self):
        second_query = "SELECT LAST_INSERT_ID() FROM category"
        self.cnx.execute(second_query)
        category_id = self.cnx.fetchone()[0]
        return category_id
