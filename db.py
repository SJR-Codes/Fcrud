"""
* Taitotalo Python 18.01.2023
* db.py
* description
* Created by Samu Reinikainen
"""

from pymongo import MongoClient
from secret import MongoUser as MU

def connectToMongo():
    try:
        conn = MongoClient(f"mongodb+srv://{MU.usern}:{MU.passwd}@cluster0.ehcdbaf.mongodb.net/?retryWrites=true&w=majority")
        #db = conn.test
        #print("Mongooo!!")
        return conn['TestiDB']
    except ConnetionError:
        print("Can't connect to MongoDB")

def get_all_blogs(db):
    blogs_collection = db['Testi']
    #TODO: lisää tarkistus onko tyhjä
    blogs = blogs_collection.find() #hakee kaikki

    for blog in blogs:
        print(blog)

#print(db.list_database_names())