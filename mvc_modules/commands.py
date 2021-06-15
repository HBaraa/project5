# -*- coding: utf-8 -*-
from models.db_creation.sql import AppSql
from models.data_maping import Interface_diplay


class HomeCommand:
    """Cette classe permet de mettre le nom de la commande à goto_home
    pour pouvoir appeler la calsse Home dans le controller"""
    name = "goto_home"


class CategoriesCommand:
    """Cette classe permet de mettre le nom de la commande à goto_categories
    pour pouvoir appeler la calsse Categories dans le controller"""
    name = "goto_categories"

    def __init__(self):
        self.filltables = AppSql()
        self.filltables.insert_datas()


class ProductsCommand:
    """Cette classe permet de mettre le nom de la commande à goto_products
    pour pouvoir appeler la calsse Products
    dans le controller et elle permet de récupérer les produits
    du catégorie choisit par l'utilisateur"""
    name = "goto_products"

    def __init__(self, category_id):
        self.category_id = category_id
        self.interfacing = Interface_diplay()
        self.products = self.interfacing.display_all_products(self.category_id)


class SubstitutesCommand:
    """Cette classe permet de mettre le nom de la commande à goto_substitutes
    pour pouvoir appeler la calsse Substitutes
    dans le controller et elle permet de faire la comparaison entre
    le produit choisit et les substituts
    et de sélectionner cellui qui a le nutriscore le plus petit"""
    name = "goto_substitutes"

    def __init__(self, product_id, substitutes):
        self.perfect_product = None
        self.substitutes_ids = substitutes
        self.product_id = product_id
        self.interfacing = Interface_diplay()
        self.nutriscore = self.interfacing.score(self.product_id)
        for item in self.substitutes_ids:
            score = self.interfacing.score(item)
            if (score < self.nutriscore) and (item != self.product_id):
                self.substituteid = item
            else:
                self.substituteid = self.product_id
                pass


class SaveSubstituteCommand:
    """Cette classe permet de mettre le nom de la commande à save_substitute
    pour pouvoir appeler la classe Savesubstitute
    dans le controller et elle sert à sauvegarder les susbstituts
    dans la table Favoris"""
    name = "save_substitute"

    def __init__(self, product_id, substitute_id):
        self.product_id = product_id
        self.substitute_id = substitute_id
        self.interface = Interface_diplay()
        self.interface.save_substitute(self.product_id, self.substitute_id)


class DisplayFavorisCommand:
    """Cette classe permet de mettre le nom de la commande à goto_favoris
    pour pouvoir appeler la classe DisplayFavoris
    dans le controller   """
    name = "goto_favoris"

    def __init__(self):
        self.interface = Interface_diplay()
        self.product_lst = self.interface.substituted_saved()
        print(self.product_lst)
        self.substitute_lst = self.interface.substitute_saved()
        print(self.substitute_lst)


class QuitCommand:
    """Cette classe permet de mettre le nom de la commande à quit
    pour pouvoir quitter le programme """
    name = "quit"
