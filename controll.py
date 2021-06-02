﻿# -*- coding: utf-8 -*-
import os

from modules.application import AppSql
from modules.interfacing import Interface_diplay



class HomeCommand:
    name = "goto_home"

class CategoriesCommand:
    name = "goto_categories"

class ProductsCommand:
    name = "goto_products"

    def __init__(self, category_id):
        self.category_id = category_id
        self.interfacing = Interface_diplay()
        self.products = self.interfacing.display_all_products(self.category_id)

class SubstitutesCommand:
    """ cette classe sert à insérer les substituts dans la table Favoris et les afficher aprés """
    name = "goto_substitutes"

    def __init__(self, product_id, substitutes):
        self.perfect_product = None
        self.substitutes_ids = substitutes
        self.product_id = product_id
        self.interfacing = Interface_diplay()
        self.nutriscore = self.interfacing.score(self.product_id)
        #print(self.nutriscore)
        for item in self.substitutes_ids:
            score = self.interfacing.score(item)
            if (item != self.product_id) and (score < self.nutriscore):
                self.substituteid = item
            else:
                self.substituteid = self.product_id
                pass
      


class SaveSubstituteCommand:
    name = "save_substitute"

    def __init__(self, product_id, substitute_id):
        self.product_id = product_id
        self.substitute_id = substitute_id
        self.interface = Interface_diplay()
        self.interface.save_substitute(self.product_id, self.substitute_id)
           
class DisplayFavorisCommand:
     name = "goto_favoris"
 
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

    def __init__(self, products):    
        self.categories = Categories()
        self.category_id = self.categories.choice
        self.productcommand = ProductsCommand(self.category_id)
        self.products = products  # on attend des produits ici !
        self.product_display = Interface_diplay()   
        self.substitutes_id = []
        self.choice_product = None

    def display(self):
        print("*** Voici les produits qui appartiennent à cette catégorie  **** ")    
        for j, product in enumerate(self.products, start=1):
            print("-" * 80)
            print("***Le produit ", j, " du catégorie choisie***")
            id = product[0]
            name = product[1]
            self.substitutes_id.append(id)
            print("l'identifiant =  ".center(35),id )
            print("le nom =  ".center(35), name)
        print("-" * 80)
        self.choice_product = input("**Choisissez un produit et entrez son id **   ")
        self.product_display.display_details(self.choice_product)
        return SubstitutesCommand(self.choice_product ,self.substitutes_id)


class Substitutes:
    
    def __init__(self, product, substitute):
        self.productdisplay = Interface_diplay()
        #self.categories = Categories()  
        #self.category_id = self.categories.choice
        self.product_id = product
        #self.product_id = self.products.choice_product
        self.substitute_id = substitute
       
    def display(self): 
        print("-" * 80)
        print("Ce produit appatient à la méme catégory choisie avec un nutriscore mieux que celui du produit choisit")
        print(">" * 60, "\n",
        ">" * 50, "\n",
        ">" * 40, "\n",
        ">" * 30, "\n",
        ">" * 20, "\n",
        ">" * 10, "\n")  
        self.productdisplay.display_details(self.substitute_id) 
        self.save_choice = input("1: sauvegader ce substitut parmis tes favoris  - 2: quitter ")
        if self.save_choice == "1":          
            return SaveSubstituteCommand(self.product_id, self.substitute_id) 
        else:
            return QuitCommand()


class SaveSubstitute:

    def __init__(self):
        self.interfacing = Interface_diplay()
      
    def display(self):
        print("Produit sauvegardé dans tes favoris")
        user_choice = input("1- Voir vos favoris tape\n2- Chercher le substitut d'un autre produit\n3- Quitter l'application\n==========>>")
        if user_choice == "1":
            return DisplayFavorisCommand()
        elif user_choice == "2":
            return HomeCommand()
        elif user_choice == "3":
            return QuitCommand()
        else:
            return HomeCommand()


class DisplayFavoris:
    def __init__(self):
        self.interfacing = Interface_diplay()

    def display(self):
        #self.interfacing.display_all_substitutes()
        self.interfacing.display_saved_favorites()
        print ("fovoris displayed")
        return QuitCommand()


class Controller:

    def __init__(self):
        self.page = Home()        
    
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    def run(self):
        running = True
        while running:
            command = self.page.display()  # on récupère un objet Command !
            if command.name == "goto_home":
                Controller.cls()
                self.page = Home()
            elif command.name == "goto_categories":
                Controller.cls()
                self.page = Categories()
            elif command.name == "goto_products":
                Controller.cls()
                self.page = Products(command.products)
            elif command.name == "goto_substitutes":
                self.page = Substitutes(command.product_id, command.substituteid)
            elif command.name == "save_substitute":
                Controller.cls()
                self.page = SaveSubstitute()
            elif command.name ==  "goto_favoris":
                self.page = DisplayFavoris()
            elif command.name== "quit":
                running = False

    
if __name__ == "__main__":
    Controller().run()
