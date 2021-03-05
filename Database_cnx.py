import requests
import pymysql
import mysql.connector

from data_search import find_datas
from data_connexion import DATABASE_NAME, HOST, USER, PASSWORD
import openFOODfacts as opff

#def fill_Procudcts():

 

def fill_Procudcts():
    products = []
    codes = []
    descriptions = []
    links = []
    stores = []
    nutriscores = []
    categories = []
    products, codes, descriptions, links, stores, nutriscores, categories = find_datas()
    print(products, codes)
    for prof in products:
        try:
            

if __name__ == "__main__":
    fill_Procudcts()

