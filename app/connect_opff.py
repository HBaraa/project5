# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
import mysql.connector
from mysql.connector import Error


def connect_db(USER, PASSWORD, HOST, DATABASE_NAME):
    connection = None
    try:
        connexion = mysql.connector.connect(user=USER,
                                    password=PASSWORD,
                                    host=HOST,
                                    database=DATABASE_NAME)
        cursor = connexion.cursor
        print (" ****** connected to database ****** ")
    except Error as e:
        print(f"The error '{e}' occurred")
        pass

    return connexion

if __name__ == "__main__":
    connect_db(USER, PASSWORD, HOST, DATABASE_NAME)
