from app import app 
from flask import render_template
from databasehelper import verifyConnection
#configure paths
@app.route('/')
def welcome():
    return render_template('index.html',textToDisplay='Welcome to the app on azure')

@app.route('/getResults')
def getResults():
    results = verifyConnection()
    return render_template('DisplayResults.html',results=results)
