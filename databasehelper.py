# Module consisting of the all the database utilities
import os
import json
#import pymysql as sql
import mysql.connector as con
from app  import app
#TODO:Move the config to a file
def connectToLocalDatabase():
    connection = con.connect(user="mba@cloud6331-az",
                                         password="Passis1234$#Passis1234$#",
                                         host="cloud6331-az.mysql.database.azure.com",
                                         port=3306,
                                         database="testdb",ssl_verify_cert=False,ssl_ca="")
    '''
     connection = sql.connect(host="cloud6331-az.mysql.database.azure.com",
                             port=3306,
                             user="mba@cloud6331-az",
                             password="",
                             db="testdb",
                             charset='utf8mb4')
                             #cursorclass=sql.cursors.DictCursor,max_allowed_packet =45*1024*1024)
                             # ssl={'key': 'C:/Users/tabrez/Desktop/MyServerCACert.pem','ca': 'C:/Users/tabrez/Downloads/BaltimoreCyberTrustRoot.crt'})
    '''
    return connection
def uploadFileToDatabase():
    print("uploading file to the database")

def verifyConnection():
    connection = connectToLocalDatabase()
    results = []
    try:
        cur=connection.cursor(dictionary=True)
        sql_statement='''select * from classes'''
        cur.execute(sql_statement)
        resultset = cur.fetchall()
        for row in resultset:
            results.append(row)
    finally:
        connection.close()
    return results
