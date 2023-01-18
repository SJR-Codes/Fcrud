"""
* Taitotalo Python 18.01.2023
* main.py
* Flask CRUD + MongoDB
* Created by Samu Reinikainen
"""

from flask import Flask, render_template
from db import *

app = Flask(__name__)

db = connectToMongo()
get_all_blogs(db)

@app.route("/")
def index():
    pageTitle = "Index page"
    indexContent = "Welcome to index page"
    testCont = ['1. First','2. Second','3. Third']
    return render_template("index.html", title=pageTitle, content=indexContent, listcontent=testCont)

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    app.run()