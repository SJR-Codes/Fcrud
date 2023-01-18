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
        return conn['TestiDB']
    except ConnetionError:
        print("Can't connect to MongoDB")

def get_all_blogs(db):
    blogs_collection = db['Testi']
    #tarkistus onko tyhjä collection
    blogs = len(list(blogs_collection.find()))
    if blogs == 0:
        #HUOM: palautetaan listana
        return [{"title": "Nada Blogs found!"}]
    else:
        return blogs_collection.find() #hakee kaikki

def get_blog(db, id):
    blogs_collection = db['Testi']    
    objInstance = ObjectId(id)
    myquery = { "_id": objInstance }
    #print(myquery)
    return blogs_collection.find_one(myquery) #hakee yhden

def create_blog(db, form):
    blogs_collection = db['Testi']
    title = form['title']
    snippet = form['snippet']
    body = form['body']

    mydict = { "title": title, "snippet": snippet, "body": body }

    x = blogs_collection.insert_one(mydict)

    return(x.inserted_id)

#print(db.list_database_names())