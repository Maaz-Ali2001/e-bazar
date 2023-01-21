from pymongo import MongoClient
from django.conf import settings

def createClient():
    connection_string = "mongodb+srv://fypecommerce:maazali786@cluster0.ycmix0k.mongodb.net/test"
    client = MongoClient(connection_string)
    return client

def connect_database(databaseName,collectionname):
    client=createClient()
    database = client[databaseName]
    a= database[collectionname]
    return a
def getAllVendors():
    client=createClient()
    databases=client.list_database_names()
    database_list=[]
    for i in databases:
        if "vendor" in i:
            database_list.append(i)
    return database_list