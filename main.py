import datetime
import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.test_database
print(db)

collection = db.test_collection
print(collection)

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
print(posts)

post_id = posts.insert_one(post).inserted_id
print(post_id)
