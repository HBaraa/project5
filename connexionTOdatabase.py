# -*- coding: utf8 -*-
import pymysql
import mysql.connector

from data_connexion import DATABASE_NAME, HOST, USER, PASSWORD

def connect_ddb():
    try:
        """  Connection to the database """
        connexion = mysql.connector.connect(user=USER,
                                    password=PASSWORD,
                                    host= HOST,
                                    database=DATABASE_NAME,)
        cursor = connexion.cursor
    except pymysql.InternalError:
        print("No database founded, we have to create a one ")
        connexion = mysql.connector.connect(user=USER,
                                    password=PASSWORD,
                                    host= HOST, )
                    
        cursor = connexion.cursor()
        cursor.execute(" DROP database IF EXISTS openfoodfact")
        sql = "CREATE database openfoodfact"
        cursor.execute (sql) 
        db_file(cursor,"openfoodfact.sql")

if __name__ == "__main__":
    connect_ddb()