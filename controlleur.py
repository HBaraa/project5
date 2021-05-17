# -*- coding: utf-8 -*-
from mvc_modules.application import AppSql
from mvc_modules.view import Interface_diplay


class HomeCommand:
  command = "goto_home"


class CategoriesCommand:
  command = "goto_categories"


class ProductsCommand:
    command = "goto_products"

    def __init__(self, category_id):
        self.diplay = Interface_diplay()
        self.products = self.diplay.display_all_products(category_id)

    def found_products(self):
        return Products(self.products)


class QuitCommand:
  command = "quit"


class Home:
    name = "home"

    def display(self):
        print("Bienvenue !")

        choice = input("1: aller aux categories - 2: quitter ")
        if choice == "1":
            return "goto_categories"
        else:
            return "quit"


class Categories:

    def __init__(self):
        self.interfacing = Interface_diplay()
        self.choice = None

    def display(self):
        print("Voici les categories...")
        lst = self.interfacing.display_all_categories()
        i = 1
        for item in lst:
            name = item[1]
            if i == 1:
                print("C'est le ", i, " er", "category")
                print(name)   
            else:
                print("C'est le ", i, " éme", "category")
                print(name)    
            i += 1
        self.choice = input("choisi une catégory ")
        if self.choice:
            print(self.choice)
            return Products(self.choice)
        else:
            return QuitCommand()


class Products:
    name = "products"

    def __init__(self, products):    
        self.product = products  # on attend des produits ici !

    def display(self):
        print("Voilà les produits qui appartiennent à cette catégory...") 
        for item in self.product:
            print("c'est un produit")
            print(item)
        if self.product:
            print("doing well")
            return  QuitCommand()
        else:
            print("no product")
            return  QuitCommand()


class Controller:
    def __init__(self):
        self.page = Home()

    def run(self):
        running = True
        while running:
            command = self.page.display()  # on récupère un objet Command !
            if command == "goto_home":
                self.page = Home()
            elif command == "goto_categories":
                self.page = Categories()
            elif command == "goto_products":
                self.page = Products(command.products)
            elif command == "quit":
                running = False


Controller().run()