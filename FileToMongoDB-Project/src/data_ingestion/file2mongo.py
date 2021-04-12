#!/usr/bin/env python3

import colorama
import pymongo
from pymongo import MongoClient
import pandas as pd 
import xlrd
import json
import sys
from config import *
import config


def read_excel_file():
    data = pd.read_excel (config.EXCEL_FILE_PATH, dtype=str,sheet_name='data') 
    data_json = json.loads(data.to_json(orient='records'))
    return data_json


def main() -> None:
    """read excel file"""
    """Write your mongoDB Connection and code"""
    mng_client = pymongo.MongoClient(config.MONGODB_SERVER, config.MONGODB_PORT)
    mng_db = mng_client[config.MONGODB_DATABASE] # Replace mongo db name
    collection_name = config.MONGODB_COLLECTION # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    db_cm.insert_many(read_excel_file())
    print("########## Sample Print ######### : {}"+format(db_cm))


# Allow the script to be run standalone (useful during development).
if __name__ == "__main__":
    main()
