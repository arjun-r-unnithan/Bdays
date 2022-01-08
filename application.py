import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")

        db.execute("INSERT INTO birthdays (name,date) VALUES(?,?,?)",name,date )
        return redirect("/")

    else:

        bdays=db.execute("SELECT * FROM birthdays")
        return render_template("index.html", bday=bday)


