# -*- coding: utf-8 -*-
import requests

from basic_modules.scoreconv import convert_score

URL = (
    "https://world.openfoodfacts.org/cgi/search.pl?action=",
    "process&tagtype_0=",
    " categories&tagtype_1=countries&tag_contains_1=",
    "france&page_size=10&json=1.json")


def get_products() -> list:
    products = []
    datas = requests.get(URL, )
    if datas.status_code == 200:
        print('Success!')
    elif datas.status_code == 404:
        print('DATA Not Found.')
    prods = datas.json()
    # pprint(prods)
    if prods:
        print("*********____DONE____*******")
        pass
    products = prods['products']
    prod_list = []
    for product in products:
        if product.get("nutriscore_grade") in ["a", "b", "c", "d", "e"]:
            prod_list.append(product)
        else:
            pass
    # print(type(products))
    # pprint(products)
    return prod_list


def get_categories(product: dict) -> list:
    categories = []
    category_list = product.get("categories")
    clean_categories = category_list.split(',')
    for category in clean_categories:
        if type(category) == str:
            # print("category is valid")
            categories.append(category)
    # print(categories)
    return categories


def clean_product(product: dict) -> dict:
    cleaned_product = {}
    try:
        cleaned_product = {
            "prod_name": product["product_name"],
            "prod_code": product["code"],
            "details": product["ingredients_text_fr"],
            "link": product["url"],
            "prod_store": product["stores"],
            "nutri_score": convert_score(product["nutriscore_grade"])
        }
    except KeyError:
        return None
    return cleaned_product
