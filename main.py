import requests
import pymysql
import json
import mysql.connector

from connexion import HOST, USER, PASSWORD, NUMBER_PRODUCT

DATA_FILE = 'OpenFoodFacts.sql'
PRODUCTS_URL ='https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1'

try:
    """  Connection to the database """
    connexion = pymysql.connect(host='localhost',
                                user=USER,
                                password=PASSWORD,
                                db='openfoodfactS',
                                charset='utf8mb4', )
    
except pymysql.InternalError:
    print("No database detected, creating a new one...")
    connexion = pymysql.connect(host='localhost',
                                user=USER,
                                password=PASSWORD,
                                charset='utf8mb4', )


    cursor = connexion.cursor()
    db_sql_file(cursor, "openfoodfacts.sql")
    new_data = 1


def product_gotten():
    page = 1 
    cursor = connexion.cursor(pymysql.cursors.DictCursor)
    for page in range(1, 100): 
        prod_file = prod_file.get('https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tagtype_1=countries&tag_contains_1=france&page_size=10&json=1'.format(page)).json()  
        for prod in prod_file['product']:
            try:
                prod_information = (prod["name"], prod["score"], prod["code"], prod["description"], prod["url"])
                prod_listed.append(cl.Product(prod["name"], prod["code"], prod["description"], prod["url"]))        
                cursor.execute("INSERT INTO product" "(name, code, description, url)"\
                "VALUES (%s, %s, %s, %s)", prod_information)
                cursor.execute("INSERT INTO nutriscore" "(score)"\
                "VALUES (%s)", prod_information)
                connexion.commit()
                print(len(prod_listed), " product")
            except KeyError: #Don't take lignes without 'product_name'
                pass
            except connexion.OperationalError: #Don't take the products with encoding error
                pass
            except connexion.DataError: #Pass when product name is too long
                pass

def category_gotten():
    cursor = connexion.cursor()
    categ_file = categ_file.get('https://fr.openfoodfacts.org/categories.json').json()
    for categ in categ_file['tags']:
        if categ['product'] > 1000:
            try:
                categ_listed.append(cl.Category(categ["name"]))
                cursor.execute("INSERT INTO category (name)"\
                                "VALUES (%s)", (categ["name"]))
                connexion.commit()
                print(len(categ_listed), " category")
            except connexion.OperationalError: #Don't take the products with encoding error
                pass
            except connexion.DataError: #Pass when product name is too long
                pass

def get_products_from_db():
    """Get a list of products from the database"""
    cursor = connexion.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM product")
    result = cursor.fetchall()
    cursor.close()

    db_product = []
    for element in result:
        db_product.append(cl.Product(element["name"], element["code"], element["description"], element["url"]))
    return db_product

def get_categories_from_db():
    """Get a list of categories from the database"""
    cursor = connexion.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM category")
    result = cursor.fetchall()
    cursor.close()

    db_category = []
    for element in result:
        db_category.append(cl.Category(element['name']))
    return db_category

def categories_browser():
    global prod_listed
    global categ_listed

    page_min = 0
    page_max = 10
    while True:
        print("\nSélectionnez une catégorie:")
        if len(categ_listed)-page_max < 10 <= page_max:
            page_max += len(categ_listed)-page_max
            if page_max < 10:
                page_min = 0
            else:
                page_min = page_max-10
        if page_min < 0:
            page_min = 0
            page_max = 10

        for i in range(page_min, page_max):
            print("{} - {}".format(i+1, categ_listed[i].name))

        uinput = input("\nEntrez: Numéro pour selectionner la catégorie "
                       "| > page suivante | < page précédente "
                       "| 0 - revenir au menu principal\n")

        if uinput == '0':
            break
        if uinput == '>':
            page_max += 10
            page_min += 10
        if uinput == '<' and page_min > 0:
            page_max -= 10
            page_min -= 10
        if uinput.isdigit():
            category_product_browser(int(uinput)-1, category_listed[int(uinput)-1].tag)

def category_product_browser(c_id, category_name):
    global categ_listed
    global prod_listed

    category_products = select_products_from_category(category_name)
    page_min = 0
    page_max = 10
    while True:
        if len(category_products)-page_max < 10 <= page_max:
            page_max += len(category_products)-page_max
            if page_max < 10:
                page_min = 0
            else:
                page_min = page_max-10
        if page_min < 0:
            page_min = 0
            page_max = 10

        if len(category_products)==0:
        	print("\nIl n'y a pas de produits dans cette catégorie")
        	break


        print("\nAffichage des produits de la catégorie {}".format(categories_list[c_id].name,))
        for i in range(page_min, page_max):
            print("{} - {}".format(i+1, category_products[i].name))

        uinput = input("\nEntrez: Numéro pour selectionner un produit "
                       "| > page suivante | < page précédente "
                       "| 0 - revenir aux catégories\n")

        if uinput == '0':
            break
        if uinput == '>':
            page_max += 10
            page_min += 10
        if uinput == '<' and page_min > 0:
            page_max -= 10
            page_min -= 10
        if uinput.isdigit():
            if 0 < int(uinput) <= len(category_products):
                print_product(category_products[int(uinput)-1])

