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


def display_category(number):
    first_query = "SELECT category.name FROM category WHERE id=%s"
    cnx.execute(first_query, (number,))
    print((cnx.fetchall()))
    query = (
        "SELECT DISTINCT category_id, product_id FROM category_product"
        " INNER JOIN product ON product.id = category_product.product_id"
        " WHERE category_product.category_id=%s"
    )
    cnx.execute(query, (number,))
    print((cnx.fetchall()))


def display_all_categories():
    query = "SELECT * FROM category ORDER BY id"
    cnx.execute(query)
    print((cnx.fetchall()))


def display_all_products(category_id):
    query = (
        "SELECT DISTINCT product.id, product.name FROM product"
        " INNER JOIN category_product"
        " ON product.id = category_product.product_id"
        " WHERE category_product.category_id=%s"
    )
    cnx.execute(query, (category_id,))
    print((cnx.fetchall()))


def display_product(entry_number):
    query = "SELECT * FROM product WHERE id=%s"
    cnx.execute(query, (entry_number,))
    print((cnx.fetchall()))


def get_sustitute_id(prod_id, categ_id):
    substitute_id = ""
    nutriscore_query = "SELECT nutriscore_id FROM product WHERE id=%s"
    cnx.execute(nutriscore_query, (prod_id,))
    score_id = cnx.fetchone()[0]
    connexion.commit()
    query = (
        "SELECT product.id FROM product"
        " INNER JOIN category_product"
        " ON product.id = category_product.product_id"
        " INNER JOIN category"
        " ON category_product.category_id = category.id"
        " WHERE category.id = %s  AND (product.nutriscore_id <= %s)"
    )
    cnx.execute(query, (categ_id, score_id))
    substitute_id = cnx.fetchone()[0]
    connexion.commit()
    return substitute_id


def get_substitute(substituted_id):
    query = (
        "SELECT favorite.substitute_id FROM favorite"
        " WHERE favorite.substituted_id = %s"
    )
    cnx.execute(query, (substituted_id,))
    substitute_id = cnx.fetchone()[0]
    connexion.commit()
    return substitute_id


def save_substitute(prod_number, sub_number):
    query_update_sub_id = (
        "INSERT INTO  favorite(substituted_id, substitute_id)" " VALUES(%s, %s)"
    )
    cnx.execute(query_update_sub_id, (prod_number, sub_number))
    connexion.commit()


def display_saved_favorites():
    query_favorite = (
        "SELECT product.id, product.name FROM product"
        " INNER JOIN favorite"
        " ON product.id = favorite.substituted_id"
    )
    cnx.execute(query_favorite)
    print((cnx.fetchall()))


def display_substitute(sub_id):
    query = "SELECT * FROM product" " WHERE product.id = %s"
    cnx.execute(query, (sub_id,))
    print((cnx.fetchall()))


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

    #    cnx.execute('SELECT * FROM product')
    # print(c.fetchall())
    #    cnx.execute('SELECT * FROM category ORDER BY id')
    # print(c.fetchall())
    #   cnx.execute('SELECT DISTINCT * FROM category_product ')
    # print(c.fetchall())
    #    query_test = 'SELECT product.name, category.name
    # FROM category_product INNER JOIN category
    # ON category.id = category_product.category_id
    # INNER JOIN product ON product.id = category_product.product_id'
    #    cnx.execute(query_test)
    # print(c.fetchall())
