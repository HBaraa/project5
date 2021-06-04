# -*- coding: utf-8 -*-
import os

from modules.application import AppSql
from modules.interfacing import Interface_diplay

from mvc_modules.commands import HomeCommand, CategoriesCommand, ProductsCommand, SubstitutesCommand, SaveSubstituteCommand, DisplayFavorisCommand, QuitCommand
from mvc_modules.views import Home, Categories, Products, Substitutes,SaveSubstitute, DisplayFavoris


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
