# -*- coding: utf8 -*-
import requests
import json
import pymysql

import mysql.connector

import openFOODfacts as opff



CATEGORIES_URL = 'https://world.openfoodfacts.org/categories.json'

        
class GetData():

    def __init__(self, database, PRODUCTS_URL):
        
        self.category_listed = []
    
    
    def get_categories():
        cursor = connexion.cursor()
        category_file = requests.get(CATEGORIES_URL).json()
        for categ in category_file:
            try:
                self.category_listed.append(opff.Category(categ["name"]))
                cursor.execute("INSERT INTO category (name)"\
                                "VALUES (%s)", (categ["name"]))
                connexion.commit()
                print("you have counsulted ", len(categ_listed), " categories")
            except connexion.OperationalError: 
                pass
            except connexion.DataError: 
                pass

    
class Categories():

    def __init__(self):
        self.categ_display = None
        self.categories = [] 

    def category_gotten():
        """displaying categories from the database"""
        cursor = connexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM category")
        self.categ_display = cursor.fetchall()
        cursor.close()       
        for element in self.categ_display:
            self.categories.append(opff.Category(element['name']))
        return self.categories
    
    def find_category(category):
        choice = ""
        while choice == "":
            choice = input('Enter the name of category thant you want to find : ')
            if choice != "":
                choice_effected = "%"+ choice + "%"      
            else:
                print("you hadn't choose the category")
        CURSOR.execute('USE openfoodfact;')
        CURSOR.execute("""SELECT id, name \
            FROM Category \
            WHERE name LIKE %s
            IMIT 50""", (choice_effected,))
        categories = CURSOR.fetchall() 
    
    def findt_products_for_category(category):
        cursor = connexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT * FROM product WHERE category LIKE %s """, (category))
        result = cursor.fetchall()
        products_list = []
        for element in result:
            products_list.append(opff.Product(element['name'], element['code'], element['nutriscore_id'], element("description"), element['store'], element['url']))
        return products_list

    


class Products():

    def __init__(self):
        self.prod_display = None
        self.choice_user = ""
       

    def product_gotten(products):
        """displaying products from the database"""
        cursor = connexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM product")
        self.prod_display = cursor.fetchall()
        cursor.close()
        for element in self.prod_display:
            products.append(opff.Product(element['name'], element['code'], element['nutriscore_id'], element("description"), element['store'], element['url']))
        return products
           
    def find_product(products):
        selection = ""
        while selection == "":
            selection = input('Enter the name of product thant you want to find : ')
            if selection != "":
                choice_selected = "%"+ selection + "%"      
            else:
                print("you hadn't choose the category")
        CURSOR.execute('USE openfoodfact;')
        CURSOR.execute("""SELECT id, name, code, nutriscore_id, description \
            FROM product \
            WHERE name, code, nutriscore_id, description LIKE %s, %s, %s, %s
            IMIT 50""", (choice_selected,))
        products = CURSOR.fetchall() 
    
    #def display_product(product):

    #    while True:
    #        print("\n\t__product_informations__\n"\
     #       "name : {} \n"
      #      "Nutrition id : {} \n"
       #     "description : {} \n"
        #    "store : {} \n"           
         #   "URL : {} \n".format(product.name, product.nutriscore_id, product.description, product.store, product.url)
#
 #           self.choice_user = input("type: 0 - Return to the products list  1 - look for a product more healthy | 2 - save your choice | 3 - delete a product ")
  #          if self.choice_user == '0':
   #             break
#
#            if self.choice_user == '1':
#                substitutes_browser(product)

#            if self.choice_user == '2':
 #               save_user_product(product)
#
 #           if self.choice_user == '3':
  #              drop_user_product(product) 
    
