import mysql.connector
import pandas
from json import loads, dumps

def verkrijgverbinding():
    mijndb = mysql.connector.connect(
    host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
    user="yc2403admin",
    password="abcd1234ABCD!@#$",
    database="woz_waarde_azure_db1"
    )
    return mijndb  

def pagina5(zoekterm):

    mijndb = verkrijgverbinding()
    mijncursor = mijndb.cursor()

    mijncursor.execute("SELECT * FROM eigenaar")

    mijnresultaat = mijncursor.fetchall()
    keys = [i[0] for i in mijncursor.description]

    data = [
        dict(zip(keys, row)) for row in mijnresultaat
    ]
    return data