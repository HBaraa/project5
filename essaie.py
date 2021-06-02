# -*- coding: utf-8 -*-
import os

from mvc_modules.application import AppSql
from mvc_modules.interfacing import Interface_diplay


class Controller:
    def __init__(self):
        self.running = False
        self.page = HomePage()

    def run(self):
        self.running = True
        while self.running:
            self.cls()
            command = self.page.display()
            command.execute(controller=self)


    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")


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
                pass


class QuitCommand:
    name = "quit"


class HomePage:
    
    def display(self):
        print("Bienvenue !")

        choice = input("1: aller aux categories - 2: quitter ")
        if choice == "1":
            return CategoriesCommand()
        else:
            return QuitCommand()


class CategoryPage:
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


class ProductPage:

    def __init__(self, products):    
        self.categories = CategoryPage()
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

class SubstitutesPage:
    
    def __init__(self, substitutes):
        self.productdisplay = Interface_diplay()
        self.categories = CategoryPage()  
        self.category_id = self.categories.choice
        self.products = ProductPage(self.category_id)
        self.product_id = self.products.choice_product
        self.substitutes_id = substitutes
       
    def display(self): 
        print("-" * 80)
        print("Ce produit appatient à la méme catégory choisie avec un nutriscore mieux que celui du produit choisit")
        print(">" * 60, "\n",
        ">" * 50, "\n",
        ">" * 40, "\n",
        ">" * 30, "\n",
        ">" * 20, "\n",
        ">" * 10, "\n")  
        self.productdisplay.display_details(self.substitutes_id) 
        self.save_choice = input("1: sauvegader ce substitut parmis tes favoris  - 2: quitter ")
        if self.save_choice == "1":          
            return SaveSubstitueCommand(self.product_id, self.substitutes_id) 
        else:
            return QuitCommand()

class SaveSubstitueCommand:
    name = "save_substitute"

    def __init__(self, product_id, substitute_id):
        self.product_id = product_id
        self.substitute_id = substitute_id
        self.interface = Interface_diplay()
        
    def execute(self, controller):
        self.interface.save_substitute(self.product_id, self.substitute_id)
        self.controller.page = HomePage()


if __name__ == "__main__":
    Controller().run()