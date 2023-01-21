from pymongo import MongoClient
from django.conf import settings

connection_string = "mongodb+srv://fypecommerce:maazali786@cluster0.ycmix0k.mongodb.net/test"
client = MongoClient(connection_string)
def connect_database(databaseName):

    database = client[databaseName]
    return database

def get_database_names():
    return client.list_database_names()