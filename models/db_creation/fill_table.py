# -*- coding: utf-8 -*-
from basic_datas.data_connexion import DATABASE_NAME, HOST, USER, PASSWORD
from models.db_creation.bdd_connexion import connect_db
from basic_modules.get_datas import get_products, clean_product

connexion = connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
cnx = connexion.cursor(buffered=True)


def fill_tables(product, cleaned_product):
    if product.get("nutriscore_grade") in ["a", "b", "c", "d", "e"]:
        # print(cleaned_product)
        insert_product_query = (
            "INSERT IGNORE INTO product"
            " (name, code, description, url, store, nutriscore_id)"
            "  VALUES (%s, %s, %s, %s, %s, %s)"
        )
        cnx.execute(
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
        connexion.commit()
    else:
        pass


def insert_categories(category_name):
    insert_category_query = "INSERT IGNORE INTO category (name)  VALUES (%s)"
    cnx.execute(insert_category_query, (category_name,))
    connexion.commit()


def insert_category_product(category_id, product_id):
    query = (
        "INSERT IGNORE INTO category_product (category_id, product_id)"
        "  VALUES(%s, %s)"
    )
    cnx.execute(query, (category_id, product_id))
    connexion.commit()


def get_product_id():
    query = "SELECT LAST_INSERT_ID() FROM product"
    cnx.execute(query)
    product_id = cnx.fetchone()[0]
    # print(product_id)
    return product_id


def get_category_id():
    second_query = "SELECT LAST_INSERT_ID() FROM category"
    cnx.execute(second_query)
    category_id = cnx.fetchone()[0]
    # print(category_id)
    return category_id


def insert_datas():
    categories = []
    products = []
    products = get_products()
    for product in products:
        cleaned_product = clean_product(product)
        fill_tables(product, cleaned_product)
        product_id = get_product_id()
        categories = product["categories"]
        # print(categories)
        # print(type(categories))
        categories_names = categories.split(",")
        # print(list(categories_names))
        # n=len(categories_names)
        # print(n)
        for category_name in categories_names:
            insert_categories(category_name)
            category_id = get_category_id()
            insert_category_product(category_id, product_id)
