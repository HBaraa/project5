# -*- coding: utf-8 -*-
from modules.application import AppSql
from modules.interfacing import Interface_diplay


def main_script():
    app = AppSql()
    interface = Interface_diplay()
    app.insert_datas()
    user_choice = input("Entrez 1 ou 2 selon vore choix \
                        1 - Souhaitez-vous trouver un élément à remplacer ?\
                        2 - Retrouver mes aliments substitués.     ")
    if int(user_choice) == 1:
        print("good choice")
        interface.display_all_categories()
        category_choice = input("Entrez l'id de la catégorie choisie:  ")
        category_id = int(category_choice)
        if int(category_id) in range(378):
            print("NIce")
            interface.display_category(category_id)
            interface.display_all_products(category_id)
            product_choice = input("Choose a product and type its id  :  ")
            product_id = int(product_choice)
            if product_id in range(50):
                print("you have choosen a product")
                interface.display_product(product_id)
            else:
                print("this number doesn't represent a product")
                pass
            favoris_choice = input("To save the substitut type 1\n else 2\n ")
            if int(favoris_choice) == 1:
                substitute_id = interface.get_sustitute_id(
                    product_id, category_id
                    )
                interface.save_substitute(product_id, substitute_id)
            else:
                print("product not saved")
                pass
        else:
            print("not like this")
    elif int(user_choice) == 2:
        print("good choice")
        interface.display_saved_favorites()
        substituted_choice = input("Type id to check its substitute")
        substituted_id = int(substituted_choice)
        if int(substituted_id):
            print("the substitute of the choosen product is :  ")
            substitute_id = interface.get_substitute(substituted_id)
            interface.display_substitute(substitute_id)
        else:
            print("this number does not correspond to a saved product")
            pass
    else:
        print("Try again!! You have to type 1 or 2 ")
        pass


if __name__ == "__main__":
    main_script()
