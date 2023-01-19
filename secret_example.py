"""
* Taitotalo Python 18.01.2023
* secret_example.py
* MongoDB connection secrets example
* Created by Samu Reinikainen
"""

#add secret.py to .gitignore
#rename this file as secret.py
#insert your MongoDB username & password & url to your database
#insert string flashSecret

class MongoUser():
    username = "" #MongoDB username
    passwd = "" #MongoDB password
    murl = "" #MongoDB url

class FlashSecret():
    flashSecret = b"" #add secret string for flash