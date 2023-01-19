from pymongo import MongoClient
from django.conf import settings

def connect_database(databaseName):

    connection_string= "mongodb+srv://fypecommerce:maazali786@cluster0.ycmix0k.mongodb.net/test"
    client = MongoClient(connection_string)
    database = client[databaseName]
    return database