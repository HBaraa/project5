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
        self.interfacing = Interface_diplay()
        self.category_id = category_id
        self.product = self.interfacing.display_all_products(self.category_id)

    def interface(self):    
        if self.product is not []:    
            print("we found products of this category ********")    
            return "goto_products"
        else:
            print("There is no product for this category ///////////")
            return "goto_home"
        

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
                print("C'est le ", i, " ére", "category")
                print(name)   
            else:
                print("C'est le ", i, " éme", "category")
                print(name)    
            i += 1
        self.choice = input("choisi une catégory ")
        if self.choice:
            print(self.choice)
            return ProductsCommand(self.choice)
        else:
            return "quit"

class Products:
    name = "products"
    command = "goto_products"

    def __init__(self, products):    
        self.products = products  # on attend des produits ici !
        self.condition = True

    def display(self):
        print("Voilà les produits qui appartiennent à cette catégory...") 
        for item in self.products:
            print("c'est un produit")
            print(item)
        if self.products:
            self.condition = False
            return "quit"
        else:
            return "quit"


class Controller:
    def __init__(self):
        self.page = Home()
        self.categories = Categories()
        self.category_id = self.categories.choice
        #self.category_id = None
        self.productcommand = ProductsCommand(self.category_id)
        self.product = self.productcommand.product
        

    def run(self):
        running = True
        while running:
            command = self.page.display()  # on récupère un objet Command !
            if command == "goto_home":
                self.page = Home()
            elif command == "goto_categories":
                self.page = Categories()
                #self.category_id = self.categories.choice
            elif command == "goto_products":                
                self.productcommand.interface()
                self.page = Products(self.product)
                running = Products.condition
            elif command == "quit":
                self.page = QuitCommand()
                running = False


Controller().run()