from app import app
from flask import render_template, url_for, flash, redirect, request


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    

    return render_template("home.html", title="Home")

