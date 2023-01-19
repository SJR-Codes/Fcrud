"""
* Taitotalo Python 18.01.2023
* db.py
* MongoDB connection
* Created by Samu Reinikainen
"""

from pymongo import MongoClient
from secret import MongoUser as MU
from bson.objectid import ObjectId

def connectToMongo():
    try:
        c = f"mongodb+srv://{MU.username}:{MU.passwd}@{MU.murl}/?retryWrites=true&w=majority"
        conn = MongoClient(c)
        db = conn['TestiDB']
        return db['Testi']
    except ConnetionError:
        print("Can't connect to MongoDB")

def get_all_blogs(db):
    #blogs_collection = db['Testi']
    #tarkistus onko tyhjä collection
    blogs = len(list(db.find()))
    if blogs == 0:
        #HUOM: palautetaan listana
        return [{"title": "Nada Blogs found!"}]
    else:
        return db.find() #hakee kaikki

def get_blog(db, id):
    #blogs_collection = db['Testi']
    myquery = { "_id": ObjectId(id) }
    
    return db.find_one(myquery) #hakee yhden

def delete_blog(db, id):
    #blogs_collection = db['Testi']
    myquery = { "_id": ObjectId(id) }
    
    return db.delete_one(myquery) #poistaa yhden

def create_blog(db, form):
    #blogs_collection = db['Testi']
    title = form['title']
    snippet = form['snippet']
    body = form['body']

    new_blog = { "title": title, "snippet": snippet, "body": body }

    x = db.insert_one(new_blog)

    return(x.inserted_id)

def update_blog(db, id, form):
    #blogs_collection = db['Testi']
    title = form['title']
    snippet = form['snippet']
    body = form['body']

    myquery = { "_id": ObjectId(id) }
    newvalues = { "$set": { "title": title, "snippet": snippet, "body": body } }

    x = db.update_one(myquery, newvalues)

    return(x)

#print(db.list_database_names())