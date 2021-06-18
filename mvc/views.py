# -*- coding: utf-8 -*-
from mvc.commands import HomeCommand, CategoriesCommand, QuitCommand
from mvc.commands import ProductsCommand, SubstitutesCommand
from mvc.commands import SaveSubstituteCommand, DisplayFavorisCommand
from models.data_maping import ModelMapping


class Home:
    """In this class, the user is asked to choose
     either go to categories or exit the program"""
    def display(self):
        print("Welcome !")
        choice = input("1: Go to catégories  - 2: Quit ")
        if choice == "1":
            return CategoriesCommand()
        else:
            return QuitCommand()


class Categories:
    """this class is used to display all categories and to request
     users to choose by entering its ID
     and it returns a call of the ProductsCommand command"""
    def __init__(self):
        self.interfacing = ModelMapping()
        self.choice = None

    def display(self):
        print(" ***   Here are the categories   ***  ")
        categories = self.interfacing.display_all_categories()
        for i, category in enumerate(categories, start=1):
            name = category[1]
            # number = "première" if i == 1 else "ème"
            print(i, "  :  ")
            print(name)
        self.choice = input("choose a category ")
        if self.choice:
            print(self.choice)
            return ProductsCommand(self.choice)
        else:
            return QuitCommand()


class Products:
    """This class is used to display all products that belong
     to the chosen category and to ask the user to choose a product,
     afterwards, it allows to display the details of this prosuit and it
     returns a call to the SubstitutesCommand"""
    def __init__(self, products):
        self.categories = Categories()
        self.category_id = self.categories.choice
        self.productcommand = ProductsCommand(self.category_id)
        self.products = products  # on attend des produits ici !
        self.product_display = ModelMapping()
        self.substitutes_id = []
        self.choice_product = None
        self.substitutes = None

    def display(self):
        print(
            "*** Here are the products that belong to ",
            "this category  ****"
        )
        for j, product in enumerate(self.products, start=1):
            print("-" * 80)
            print("***The product ", j, "of the chosen category***")
            id = product[0]
            name = product[1]
            self.substitutes_id.append(id)
            print("The id =  ".center(35), id)
            print("The name =  ".center(35), name)
        print("-" * 80)
        self.choice_product = input(
            "**Choose a product and enter its id **   "
            )
        self.product_display.display_details(self.choice_product)
        self.substitutes = self.product_display.substitute_product(
            self.category_id
            )
        return SubstitutesCommand(self.choice_product, self.substitutes_id)


class Substitutes:
    """This class is used to display the substitute of the product and return
     a SaveSubstituteCommand command call"""
    def __init__(self, product, substitute):
        self.productdisplay = ModelMapping()
        self.product_id = product
        self.substitute_id = substitute

    def display(self):
        print("-" * 80)
        print(
            "This product belongs to the same category chosen with"
            " a nutriscore better than that of the chosen product"
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
            "1: Save this substitute among your favorites  - 2: Quit "
            )
        if self.save_choice == "1":
            return SaveSubstituteCommand(self.product_id, self.substitute_id)
        else:
            return QuitCommand()


class SaveSubstitute:
    """In this class, the user is asked to choose between
     see your favorites, find a substitute for another product
     or quit the application"""
    def __init__(self):
        self.interfacing = ModelMapping()

    def display(self):
        print("Product saved in your favorites")
        user_choice = input(
            "1- See your favorites\n"
            "2- Find a substitute for another product\n"
            "3- Exit the application\n==========>>"
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
    """This class is used to display saved favorites
     in the favorite table"""
    def __init__(self):
        self.interfacing = ModelMapping()
        self.display_favor = DisplayFavorisCommand()

    def display(self):
        # self.interfacing.display_all_substitutes()
        print("Saved products are :  \n")
        for product in self.display_favor.product_lst:
            id = product[0]
            self.interfacing.display_details(id)
        print("Saved substitutes are :  \n")
        for substitute in self.display_favor.substitute_lst:
            ident = substitute[0]
            self.interfacing.display_details(ident)
        return QuitCommand()
