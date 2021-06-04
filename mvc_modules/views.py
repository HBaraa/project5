# -*- coding: utf-8 -*-
from mvc_modules.commands import HomeCommand, CategoriesCommand, QuitCommand
from mvc_modules.commands import ProductsCommand, SubstitutesCommand
from mvc_modules.commands import SaveSubstituteCommand, DisplayFavorisCommand
from models.application import AppSql
from models.interfacing import Interface_diplay


class Home:
    """Dans cette classe, l'utilisateur est demandé de choisir
    soit aller aux catégories ou quitter le programme"""
    def display(self):
        print("Bienvenue !")
        choice = input("1: aller aux categories - 2: quitter ")
        if choice == "1":
            return CategoriesCommand()
        else:
            return QuitCommand()


class Categories:
    """cette classe sert à afficher toutes les catégories et à demander
    aux utilisateurs de choisir une en entrant son identifiant
    et elle retourne un appel de la commande ProductsCommand"""
    def __init__(self):
        self.filltables = AppSql()
        self.interfacing = Interface_diplay()
        self.choice = None

    def display(self):
        self.filltables.insert_datas()
        print(" ***    Voici les categories ***  ")
        categories = self.interfacing.display_all_categories()
        for i, category in enumerate(categories, start=1):
            name = category[1]
            number = "première" if i == 1 else "ème"
            print("C'est le ", i, number, "category")
            print(name)
        self.choice = input("choisi une catégorie ")
        if self.choice:
            print(self.choice)
            return ProductsCommand(self.choice)
        else:
            return QuitCommand()


class Products:
    """Cette classe sert à afficher tous les produits qui appartiennent
    à la catégorie choisie et à demander à l'utilisateur de choisir un produit,
    aprés, elle permet d'afficher les détails de ce prosuit et elle retourne
    un appel de la commande SubstitutesCommand"""
    def __init__(self, products):
        self.categories = Categories()
        self.category_id = self.categories.choice
        self.productcommand = ProductsCommand(self.category_id)
        self.products = products  # on attend des produits ici !
        self.product_display = Interface_diplay()
        self.substitutes_id = []
        self.choice_product = None

    def display(self):
        print(
            "*** Voici les produits qui appartiennent à ",
            "cette catégorie  ****"
        )
        for j, product in enumerate(self.products, start=1):
            print("-" * 80)
            print("***Le produit ", j, " du catégorie choisie***")
            id = product[0]
            name = product[1]
            self.substitutes_id.append(id)
            print("l'identifiant =  ".center(35), id)
            print("le nom =  ".center(35), name)
        print("-" * 80)
        self.choice_product = input(
            "**Choisissez un produit et entrez son id **   "
            )
        self.product_display.display_details(self.choice_product)
        return SubstitutesCommand(self.choice_product, self.substitutes_id)


class Substitutes:
    """Cette classe sert à afficher le substitut du produit et retoune
    un appel de commande SaveSubstituteCommand"""
    def __init__(self, product, substitute):
        self.productdisplay = Interface_diplay()
        self.product_id = product
        self.substitute_id = substitute

    def display(self):
        print("-" * 80)
        print(
            "Ce produit appatient à la méme catégory choisie avec"
            " un nutriscore mieux que celui du produit choisit"
            )
        print(
            ">" * 60, "\n",
            ">" * 50, "\n",
            ">" * 40, "\n",
            ">" * 30, "\n",
            ">" * 20, "\n",
            ">" * 10, "\n"
        )
        self.productdisplay.display_details(self.substitute_id)
        self.save_choice = input(
            "1: sauvegader ce substitut parmis tes favoris  - 2: quitter "
            )
        if self.save_choice == "1":
            return SaveSubstituteCommand(self.product_id, self.substitute_id)
        else:
            return QuitCommand()


class SaveSubstitute:
    """Dans cette classe, l'utilisateur est demandé de choisir entre
    voir ses favoris, chercher le substitut d'un autre produit
    ou quitter l'application"""
    def __init__(self):
        self.interfacing = Interface_diplay()

    def display(self):
        print("Produit sauvegardé dans tes favoris")
        user_choice = input(
            "1- Voir vos favoris\n"
            "2- Chercher le substitut d'un autre produit\n"
            "3- Quitter l'application\n==========>>"
            )
        if user_choice == "1":
            return DisplayFavorisCommand()
        elif user_choice == "2":
            return HomeCommand()
        elif user_choice == "3":
            return QuitCommand()
        else:
            return HomeCommand()


class DisplayFavoris:
    """Cette classe sert à afficher les favoris sauvegerdés
    dans la table favorite"""
    def __init__(self):
        self.interfacing = Interface_diplay()

    def display(self):
        # self.interfacing.display_all_substitutes()
        self.interfacing.display_saved_favorites()
        print("fovoris displayed")
        return QuitCommand()
