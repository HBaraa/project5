# -*- coding: utf-8 -*-
from basic_modules.fill_table import *


def main():
    insert_datas()
    possible_choices = []
    user_choice = input("Entrez 1 ou 2 selon vore choix \
                        1 - Quel aliment souhaitez-vous remplacer ?\
                        2 - Retrouver mes aliments substitués.")
    if int(user_choice) == 1:
        print("good choice")
        display_all_categories()
        category_choice = input("Entrez le chiffre de la catégorie choisie: ")
        category_id = int(category_choice)
        if category_id in range(392):
            print("NIce")
            display_category(category_id)
            display_all_products(category_id)
            product_choice = input("Choose a number and type its id  :  ")
            product_id = int(product_choice)
            if product_id in range(127):
                print("you have choosen a product")
                display_product(product_id)
            else:
                print("this number doesn't represent a product")
            favoris_choice = input("To save the substitut type 1\n else 2\n  ")
            if int(favoris_choice) == 1:
                substitute_id = get_sustitute_id(product_id, category_id)
                save_substitute(product_id, substitute_id)
            else:
                print("product not saved")
        else:
            print("not like this")
    elif int(user_choice) == 2:
        print("good choice")
        display_saved_favorites()
        substituted_choice = input("type the id to check its substitute")
        substituted_id = int(substituted_choice)
        if substituted_id:
            print("the substitute of the choosen product is :  ")
            substitute_id = get_substitute(substituted_id)
            display_substitute(substitute_id)
        else:
            print("this number does not correspond to a saved product")
    else:
        print("Try again!! You have to type 1 or 2 ")


if __name__ == "__main__":
    main()
