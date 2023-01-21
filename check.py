from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
from pprint import pprint



connection_string= "mongodb+srv://fypecommerce:maazali786@cluster0.ycmix0k.mongodb.net/test"
client = MongoClient(connection_string)
# print(client.list_database_names())
database = client["E-Bazar"]
dbConnection= database["Categories"]
#cate=dbConnection.find({'parent':'/Electronics'})
# for cat in cate:
#     print(cat)
categories={}
def nested(path,categories,index,actual_path):
    if index==len(path)-1:
        child= dbConnection.find({'parent':actual_path})
        if child.count()==0:
            leaf = dbConnection.find({'category': actual_path})
            for l in leaf:
                categories[path[index]] = {'leaf':l['_id']}
        else:
            categories[path[index]]={}
        return
    else:
        if path[index] in categories.keys():
            nested(path,categories[path[index]],index+1,actual_path)
        else:
            categories[path[index]]={}
            nested(path,categories,index,actual_path)


cat= dbConnection.find({})
for element in cat:
    actual_path= element['category']
    path= actual_path.split('/')
    path= path[1:]
    #print(path)
    #categories={}
    index=0
    #path=['Electronics', 'embedded','audio']
    #categories={'Electronics': {'embedded': {}}}
    #nested(path,categories,index,actual_path)
#print(categories)
flag= True
def recursive(category):
        print(category.keys())
c= {'maaz':{'age':18}}
recursive(c)

# cat= dbConnection.find({})
# categories={}
# for sub in cat:
#     path= sub['category']
#     path=path.split('/')
#     path= path[1:]
#     flag= False
#     index=0
#     if path[0] not in categories.keys():
#         categories[path[0]]={}
#         temp= categories[path[0]]
#     else:
#         temp=categories[path[0]]
#     index+=1
#     while index<len(path) :
#         element= path[index] # element of list /Electronics/embedded
#         if element in temp.keys():
#             index+=1
#             temp= temp[element]
#             child= dbConnection.find({'parent':sub['category']})
#             if child.count()==0:
#                 temp['leaf']= sub['_id']
#         else:
#             temp[element]={}
#     categories=temp

#reg=dbConnection.find({'parent' : {'$regex' : 'Circuit Boards & Components$'}})


# def get_category(parent,cat_dict):
#     child= dbConnection.find({"parent":parent})
#     # for ch in child:
#     #     print(ch['name'])
#     if child.count()==0:
#         print(child.count())
#         leaf = dbConnection.find({"category": parent})
#         for l in leaf:
#            leaf_ret= {l['name']:{"leaf":l['_id']}}
#         return leaf_ret
#     else:
#         child = dbConnection.find({"parent": parent})
#         for sub in child:
#             parent_name= parent.split('/')
#             cat_dict[parent_name[-1]]= get_category(sub["category"],cat_dict)
#             print(cat_dict)
#
#         return cat_dict
#
# categories= get_category("/Electronics",{})
# print(categories.items())
# pprint(categories.items())

# cat_dict={}
# base= dbConnection.find({"parent": "/"})
# base_list=[]
# for main in base:
#     cat_dict[main]=
#
# print(base_list)
# count=1
# category_dic={}
# while count!=0:
#     for name in base_list:
#         subcategory= dbConnection.find({"parent": name})
#         category_dic[name]=subcategory


# # {base:{categories:[kj,jkb,..],leaf:[id,name]]

## {electronic{}}