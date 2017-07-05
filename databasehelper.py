# Module consisting of the all the database utilities
import os
import json
import pymysql as sql
from app  import app
def connectToDatabase():
    clearDBService = json.loads(os.environ['VCAP_SERVICES'])['cleardb'][0]
    clearDBServiceCredentials = clearDBService['credentials']
    host = clearDBServiceCredentials['hostname']
    port = int(clearDBServiceCredentials['port'])
    userName = clearDBServiceCredentials['username']
    password = clearDBServiceCredentials['password']
    database = clearDBServiceCredentials['name']
    connection = sql.connect(host=host,
                             port=port,
                             user=userName,
                             password=password,
                             db=database,
                             charset='utf8mb4',
                             cursorclass=sql.cursors.DictCursor)
    return connection
def connectToLocalDatabase():
     connection = sql.connect(host="cloud6331-az.mysql.database.azure.com",
                             port=3306,
                             user="mba@cloud6331-az",
                             password="",
                             db="testdb",
                             charset='utf8mb4',
                             cursorclass=sql.cursors.DictCursor)
     return connection
def uploadFileToDatabase():
    print("uploading file to the database")

def verifyConnection():
    connection = connectToLocalDatabase()
    results = []
    try:
        with connection.cursor() as cursor:
            sql_statement='select * from classes'
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for row in results:
                results.append(row)
        return results
    finally:
        connection.close()
