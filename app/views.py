from app import app
from flask import render_template
from databasehelper import verifyConnection
#configure paths
@app.route('/')
def welcome():
    render_template('index.html',textToDisplay='Welcome to the app on azure')

@app.route('getResults',methods=["GET","POST"])
def getResults():
    results = verifyConnection()
    render_template('DisplayResults.html',results=results)
