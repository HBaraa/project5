import mysql.connector
from openfoodfacts import Openfoodfacts
from config import HOST, USER, PASSWORD, DATABASE

class Database:
    """Connect to database"""
    def __init__(self, host, user, password, name_database):
        self.cnx = mysql.connector.connect(host=host,
                                           user=user,
                                           password=password,
                                           database=name_database)
        self.cursor = self.cnx.cursor(buffered=True)

class Table:

    def __init__(self, database):
        self.database = database

    def create_table(self):
        self.database.cursor.execute(self.__class__.SQL_QUERY_CREATE_TABLE)

class PurchaseStores(Table):
    """Create Purchase_stores and insert stores in it"""

    SQL_QUERY_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS Purchase_stores (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        store_name VARCHAR(255) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB"""
    SQL_QUERY_INSERT_INTO = """INSERT IGNORE INTO Purchase_stores
        (store_name)
        VALUES (%(store_name)s)"""

    def insert_into_table(self, products):
        stores = []
        for product in products:
            if product['stores'] != 0:
                stores.append(product['stores'])

        stores = list(dict.fromkeys(stores))
        for store in stores:
            store_to_add = {'store_name': store}
            self.database.cursor.execute(PurchaseStores.SQL_QUERY_INSERT_INTO,
                                         store_to_add)
        self.database.cnx.commit()

class Categories(Table):
    """Create Categories and insert categories in it"""

    SQL_QUERY_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS Categories(
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        category_name VARCHAR(255) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB"""
    SQL_QUERY_INSERT_INTO = """INSERT IGNORE INTO Categories
        (category_name)
        VALUES(%(category_name)s)"""
    SQL_QUERY_SELECT_CATEGORIES = """SELECT category_name FROM
                                    Categories"""

    def insert_into_table(self, products):
        categories_list = []
        for product in products:
            categories_list.append(product['categories'])

        categories_list = list(dict.fromkeys(categories_list))
        for category in categories_list:
            if category:
                category_to_add = {'category_name': category}
                self.database.cursor.execute(Categories.SQL_QUERY_INSERT_INTO,
                                             category_to_add)
        self.database.cnx.commit()

    def return_categories(self):
        self.database.cursor.execute(Categories.SQL_QUERY_SELECT_CATEGORIES)
        categories = []
        for category in self.database.cursor:
            cat_to_add = category[0]
            categories.append(cat_to_add)

        return categories

class Products(Table):
    def insert_into_table(self, products):
        for product in products:
            product_attributes = {
                'product_name': product['product_name'],
                'nutriscore': product['nutriscore'],
                'link': product['link'],
                'details': product['details']
            }
            self.database.cursor.execute(Products.SQL_QUERY_INSERT_INTO,
                                         product_attributes)
            self.database.cnx.commit()

    def return_prod_cat(self):
        self.database.cursor.execute(Products.SQL_QUERY_SELECT_PROD_CAT)
        prod_cat = []
        for item in self.database.cursor:
            prod_cat_to_add = item[0], item[1]
            prod_cat.append(prod_cat_to_add)

        return prod_cat

    def return_details(self, product_name):
        self.database.cursor.execute(Products.SQL_QUERY_SELECT_DETAILS,
                                     product_name)
        details = []
        for detail in self.database.cursor:
            details.append(detail)

        return details
    def return_replace(self, prod_to_replace):
        replacement = []
        self.database.cursor.execute(Products.SQL_QUERY_REPLACE,
                                     prod_to_replace)
        for replace in self.database.cursor:
            replacement.append(replace)

        return replacement

class Favorites(Table):
    def insert_into_table(self, product_names):
        self.database.cursor.execute(Favorites.SQL_QUERY_INSERT_INTO,
                                     product_names)
        self.database.cnx.commit()

    def return_fav_names(self):
        self.database.cursor.execute(Favorites.SQL_QUERY_SELECT_FAV_NAMES)
        favs_names = []
        for fav_name in self.database.cursor:
            favs_names.append(fav_name)

        return favs_names
    
class ProductCategories(Table):
    def insert_into_table(self, products):
        prod_cat = []
        for product in products:
            prod_cat_to_add = (product['product_name'], product['categories'])
            prod_cat.append(prod_cat_to_add)

        for item in prod_cat:
            self.database.cursor.execute(ProductCategories.
                                         SQL_QUERY_INSERT_INTO, item)
        self.database.cnx.commit()

        return prod_cat

class Init():

    def __init__(self):
        self.db = Database(HOST, USER, PASSWORD, DATABASE)
        self.categories = Categories(self.db)
        self.products = Products(self.db)
        self.product_categories = ProductCategories(self.db)
        self.favorites = Favorites(self.db)
        self.product_dict = None

    def sync_products(self):
        datas = Openfoodfacts()
        self.product_dict = datas.create_dict()

    def create_tables(self):
        self.categories.create_table()
        self.products.create_table()
        self.product_categories.create_table()
        self.favorites.create_table()

    def insert_datas(self):
        self.categories.insert_into_table(self.product_dict)
        self.products.insert_into_table(self.product_dict)
        self.product_categories.insert_into_table(self.product_dict)
