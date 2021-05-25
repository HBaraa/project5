# -*- coding: utf-8 -*-
import string
import re
from pprint import pprint


from mvc_modules.insertion import InsertIntoTables
from basic_modules.get_datas import get_products, get_categories, clean_product

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
            self.categories = get_categories(product)
            for category_name in self.categories:
                self.inserttables.insert_categories(category_name)
                category_id = self.inserttables.get_category_id()
                self.inserttables.insert_category_product(
                    category_id, product_id
                    )
