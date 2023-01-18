"""
* Taitotalo Python 18.01.2023
* main.py
* Flask CRUD + MongoDB
* Created by Samu Reinikainen
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    app.run()