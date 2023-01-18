"""
* Taitotalo Python 18.01.2023
* main.py
* Flask CRUD + MongoDB
* Created by Samu Reinikainen
"""

from flask import Flask, render_template, redirect, request, flash
from db import *

app = Flask(__name__)

#flash vaatii secretkey muuttujan
app.secret_key = b"ncd lc,cvnfjoirjfenfdinff098302"

db = connectToMongo()

@app.route("/")
def index():
    blogs = get_all_blogs(db)    
    pageTitle = "Blog page"
    return render_template("index.html", title=pageTitle, content=blogs)

@app.route("/blogs/create", methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        id = create_blog(db, request.form)
        url = "/blogs/" + str(id)
        flash("Blog Created!")
        return redirect(url)
    else:
        pageTitle = "Create Blog page"
        return render_template("create.html", title=pageTitle)

@app.route("/blogs/<page_id>")
def blog(page_id):
    id = page_id
    blog = get_blog(db, id)
    pageTitle = "Blog page"
    return render_template("blog.html", title=pageTitle, content=blog)

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    app.run()