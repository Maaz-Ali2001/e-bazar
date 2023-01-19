from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
from pprint import pprint



connection_string= "mongodb+srv://fypecommerce:maazali786@cluster0.ycmix0k.mongodb.net/test"
client = MongoClient(connection_string)
# print(client.list_database_names())
database = client["E-Bazar"]
# dbConnection= database["vendor1"]
# vendors= dbConnection.find({})
# for i in vendors:
#     print(i["email"],i["password"])
#
# print(client.list_database_names())
# lst= database['status']
# lst= lst.find({})
#
# lst1=[]
# for i in lst:
#     #print(i['name'])
#     lst1.append(i['name'])
# print(lst1)
# dictionary= { 'firstName': 'aaa', 'middleName': 'aaa', 'lastName': 'aaa', 'businessType': 'individual', 'dto': '8/8/8',
# 'city': 'aaa', 'province': 'aaa', 'address1': 'aaa', 'address2': 'aaa', 'postalCode': '234234', 'cnic': 534534534, 'email': 'aaa', 'password': 'aaaaaa', 'phone': 'aaa', 'creditCard': '24353535', 'cardHolder': 'aaaaa', 'billingAddress': 'aaaaa', 'status': '63c6a6c20d36d86c08f5297b'}
# dictionary= {0:{'name':'maaz','age':18},1:{'name':'maaz','age':18}}
# for k,v in dictionary.items():
#     for key,value in v.items():
#         print(value)
status_collec = database['status']
status_id = status_collec.find({'name': 'not verified'})
for id in status_id:
    status_id=id['_id']
print(status_id)

