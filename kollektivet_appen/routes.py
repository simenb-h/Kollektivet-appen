from flask import render_template, url_for, redirect, flash, request
from kollektivet_appen import app, db

@app.route("/", methods = ['GET','POST'])
@app.route("/home", methods = ['GET','POST'])
def home():
    return render_template('home.html')