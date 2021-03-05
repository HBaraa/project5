# -*- coding: utf-8 -*-
import requests
import sqlite3

from data_search import find_datas
from connect_opff import connect_db
import openFOODfacts as opff
from scoreTOid import convert_score

def insert_into_database():
    
