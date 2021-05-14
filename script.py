# -*- coding: utf-8 -*-
from mvc_modules.application import AppSql
from mvc_modules.view import Interface_diplay


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
    name = "categories"

    def __init__(self):
        self.disp = Interface_diplay()
        self.choice = None

    def display(self):
        print("Voici les categories...")
        lst = self.disp.display_all_categories()
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
            return "goto_products"
        else:
            return "quit"

        #choice = input("1: aller aux substitutes - 2: quitter ")
        #if choice == "1":
        #    return "goto_substitutes"
        #else:
        #    return "quit"

class Products:
    name = "products"

    def __init__(self):
        self.disp = Interface_diplay()
        self.categ = Categories()
        self.group = self.categ.choice

    def display(self):
        print("Voilà les produits qui appartiennent à cette catégory...")

        #self.ident = self.categ.choice1 
        print(self.group)
        if self.group:
            prods = self.disp.display_all_products(self.group)
            print(prods)
        else:
            return "quit"




class Controller:
    def __init__(self):
        self.page = Home()

    def run(self):
        running = True
        while running:
            command = self.page.display()
            if command == "goto_home":
                self.page = Home()
            elif command == "goto_categories":
                self.page = Categories()
            elif command == "goto_products":
                self.page = Products()
            #elif command == "goto_substitutes":
            #    self.page = Substitutes()
                #print("Pas encore implémenté ! :(")
            elif command == "quit":
                running = False
            


Controller().run()