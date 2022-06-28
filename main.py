from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.test_database
print(db.collection_names())