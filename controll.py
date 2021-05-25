# -*- coding: utf-8 -*-
import os

from mvc_modules.application import AppSql
from mvc_modules.interfacing import Interface_diplay

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class HomeCommand:
    name = "goto_home"

class CategoriesCommand:
    name = "goto_categories"

class ProductsCommand:
    name = "goto_products"

    def __init__(self, category_id):
        self.interfacing = Interface_diplay()
        self.category_id = category_id
        self.products = self.interfacing.display_all_products(self.category_id)  
             

class QuitCommand:
    name = "quit"

class Home:
    
    def display(self):
        print("Bienvenue !")

        choice = input("1: aller aux categories - 2: quitter ")
        if choice == "1":
            return CategoriesCommand()
        else:
            return QuitCommand()


class Categories:
    
    def __init__(self):
        self.interfacing = Interface_diplay()
        self.choice = None

    def display(self):
        print("Voici les categories...")
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

    def __init__(self, products):    
        self.categories = Categories()
        self.category_id = self.categories.choice
        self.productcommand = ProductsCommand(self.category_id)
        #self.products = self.productcommand.products
        self.products = products  # on attend des produits ici !
        self.product_display = Interface_diplay()
        
    
       
    def display(self):
        cls()
        print("Voilà les produits qui appartiennent à cette catégorie...")    
        for j, product in enumerate(self.products, start=1):
            print(" ******* Le procuit ", j, " du catégorie choisie ****** ")
            id = product[0]
            name = product[1]
            print("l'identifiant =  ",id )
            print("le nom =  ", name)
        choice_product = input("choisit un product et entrer son id  ")
        cls()
        self.product_display.display_details(choice_product)
        #substitute_id = self.product_display.get_sustitute_id(self.choice_product, self.category_id)
        #self.product_display.display_substitute(substitute_id)
        substitute_id = int(self.product_display.get_sustitute_id(choice_product, self.category_id))
        substitute = self.product_display.display_substitute(substitute_id)
        for item in substitute:
            print(item)
        return HomeCommand()


class Controller:
    def __init__(self):
        self.page = Home()

    def run(self):
        running = True
        while running:
            command = self.page.display()  # on récupère un objet Command !
            if command.name == "goto_home":
                self.page = Home()
            elif command.name == "goto_categories":
                self.page = Categories()
            elif command.name == "goto_products":
                self.page = Products(command.products)
            elif command.name== "quit":
                running = False

Controller().run()
