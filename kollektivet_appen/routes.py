from flask import render_template, url_for, redirect, flash, request
from kollektivet_appen import app, db, weeknr

@app.route("/", methods = ['GET','POST'])
@app.route("/home", methods = ['GET','POST'])
def home():
    cleaninglist = weeknr.getCleaninglist()
    week = weeknr.getWeek()
    return render_template('cleaning.html', cleaninglist=cleaninglist, week=week)