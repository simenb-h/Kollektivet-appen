from flask import render_template, url_for, redirect, flash, request
from kollektivet_appen import app, db, weeknr

@app.route("/", methods = ['GET','POST'])
@app.route("/home", methods = ['GET','POST'])
def home():
    cleaninglist = weeknr.thisweek()
    week = weeknr.getWeek()
    label = 'Current Week: '
    return render_template('cleaning.html',label=label, cleaninglist=cleaninglist, week=week)

@app.route("/home/lastweek", methods = ['GET','POST'])
def lastweek():
    cleaninglist = weeknr.lastweek()
    week = weeknr.getWeek()-1
    moving = 'back'
    label = 'Last Week:'
    return render_template('cleaning.html', cleaninglist=cleaninglist, label=label, week=week, moving=moving)

@app.route("/home/nextweek", methods = ['GET','POST'])
def nextweek():
    cleaninglist = weeknr.nextweek()
    week = weeknr.getWeek()+1
    moving = 'forward'
    label = 'Next Week:'
    return render_template('cleaning.html', cleaninglist=cleaninglist, label=label, week=week, moving=moving)

    
