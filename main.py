"""
* Taitotalo Python 18.01.2023
* main.py
* Flask CRUD + MongoDB
* Created by Samu Reinikainen
"""

from flask import Flask, render_template, redirect, request, flash, url_for
from secret import FlashSecret as FS
from db import *
import json
from bson import json_util

app = Flask(__name__)

#flash vaatii secretkey muuttujan
app.secret_key = FS.flashSecret

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
        url = "/blog/" + str(id)
        flash("Blog Created!")
        return redirect(url)
    else:
        pageTitle = "Create Blog page"
        return render_template("create.html", title=pageTitle)

@app.route("/delete_blog/<blog_id>", methods = ['POST', 'GET'])
def del_blog(blog_id):
    do = delete_blog(db, blog_id)
    if do:
        flash("Blog Deleted!")
    else:
        flash("Nothing Happens!")
    return redirect("/")

@app.route("/update_blog/<blog_id>", methods = ['POST', 'GET'])
def upd_blog(blog_id):
    if request.method == 'POST':
        do = update_blog(db, blog_id, request.form)
        if do:
            flash("Blog Updated!")
        else:
            flash("Nothing Happens!")
        url = "/blog/" + str(blog_id)
        return redirect(url)
        
    else:
        blog = get_blog(db, blog_id)
        pageTitle = "Update Blog page"
        return render_template("update.html", title=pageTitle, content=blog)

@app.route("/blog/<page_id>")
def blog(page_id):
    id = page_id
    blog = get_blog(db, id)
    pageTitle = "Blog page"
    return render_template("blog.html", title=pageTitle, content=blog)

@app.route("/api/")
def get_api_all_blogs():
    blogs = get_all_blogs(db)
    #objectId fix
    return json.loads(json_util.dumps(blogs))

@app.route("/api/<page_id>")
def get_api_blog(page_id):
    blog = get_blog(db, page_id)
    #objectId fix
    return json.loads(json_util.dumps(blog))

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    app.run()