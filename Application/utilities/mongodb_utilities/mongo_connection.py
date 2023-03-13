from pymongo import MongoClient
def mongo_local():
    client = MongoClient("mongodb://localhost:27017")
    return client

