import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.x0xge.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print(db.list_collection_names)
