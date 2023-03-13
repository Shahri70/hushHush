from pymongo import MongoClient
import pandas as pd
import json
def mongoimportupdate(data,filtering, db_name, coll_name, db_url='localhost', db_port=27017):
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    #data = pd.read_csv(csv_path)
    #payload = json.loads(data.to_json(orient='records'))
    #coll.delete_many({})
    #coll.insert_one(data)
    coll.update_one(filtering, {"$set": data })
    return coll.count()
