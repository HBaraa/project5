# -*- coding: utf-8 -*-
from models.db_creation.sql import AppSql
from models.data_maping import ModelMapping


class HomeCommand:
    """This class allows you to set the name of the command to goto_home
     to be able to call the calss Home in the controller"""
    name = "goto_home"


class CategoriesCommand:
    """This class allows you to set the name of the command to goto_categories
     to be able to call the calss Categories in the controller"""
    name = "goto_categories"

    def __init__(self):
        self.filltables = AppSql()
        self.filltables.insert_datas()


class ProductsCommand:
    """This class allows you to set the name of the command to goto_products
     to be able to call the calss Products
     in the controller and it allows you to retrieve the products
     of the category chosen by the user"""
    name = "goto_products"

    def __init__(self, category_id):
        self.category_id = category_id
        self.interfacing = ModelMapping()
        self.products = self.interfacing.display_all_products(self.category_id)


class SubstitutesCommand:
    """This class allows you to set the name of the command to goto_substitutes
     to be able to call the calss Substitutes
     in the controller and it allows to make the comparison between
     the chosen product and substitutes
     and select the one with the smallest nutriscore"""
    name = "goto_substitutes"

    def __init__(self, product_id, substitutes):
        self.perfect_product = None
        self.substitutes_ids = substitutes
        self.product_id = product_id
        self.interfacing = ModelMapping()
        self.nutriscore = self.interfacing.score(self.product_id)
        for item in self.substitutes_ids:
            score = self.interfacing.score(item)
            if (score < self.nutriscore) and (item != self.product_id):
                self.substituteid = item
            else:
                self.substituteid = self.product_id
                pass


class SaveSubstituteCommand:
    """This class allows you to set the name of the command to save_substitute
     to be able to call the class Savesubstitute
     in the controller and it is used to save the substitutes
     in the Favorites table"""
    name = "save_substitute"

    def __init__(self, product_id, substitute_id):
        self.product_id = product_id
        self.substitute_id = substitute_id
        self.interface = ModelMapping()
        self.interface.save_substitute(self.product_id, self.substitute_id)


class DisplayFavorisCommand:
    """This class allows you to set the name of the command to goto_favoris
     to be able to call the class DisplayFavoris
     in the controller"""
    name = "goto_favoris"

    def __init__(self):
        self.interface = ModelMapping()
        self.product_lst = self.interface.substituted_saved()
        # print(self.product_lst)
        self.substitute_lst = self.interface.substitute_saved()
        # print(self.substitute_lst)


class QuitCommand:
    """This class allows you to put the name of the command to quit
     to be able to exit the program"""
    name = "quit"
