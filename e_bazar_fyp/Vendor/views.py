from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import hashlib
from bson.objectid import ObjectId

from . import utils

# class User_vw:
#
#
#     @csrf_exempt
#     def register(self,request):
#
#         user_mdl=User(user_Name=request.POST.get('user_name'),user_Password = request.POST.get('password'),user_email_phone = request.POST.get('Mob_or_Eml'))
#
#         user_mdl.save()
#         print(request.POST.get('username'))
#         return HttpResponse(request.POST.get('user_name'))
#     # def post(self,request):
#     #     user_creation=self.register(request)
#     #     return user_creation

class vendorRegister:
    def __init__(self):
        pass

    def logIn(self,request):

        return redirect("register")

    def register(self,request):
        if request.method == 'POST':
            firstName = request.POST['firstName']
            middleName = request.POST['middleName']
            lastName = request.POST['lastName']
            businessType = request.POST['businessType']
            dto = request.POST['dto']
            city = request.POST['city']
            province = request.POST['province']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            postalCode = request.POST['postalCode']
            cnic = int(request.POST['cnic'])
            phone = request.POST['phone']
            email = request.POST['email']
            email=email.strip()
            password = request.POST['password']
            password= password.strip()
            rePassword = request.POST['rePassword']
            creditCard = request.POST['creditCard']
            cardHolder = request.POST['cardHolder']
            billingAddress = request.POST['billingAddress']

            emailpass= email+password
            #vendor_databse_name = hashlib.sha256(emailpass.encode('utf-8')).hexdigest()
            vendor_databse_name= 'vendor'+str(cnic)

            database_genvendor= utils.connect_database("E-Bazar")
            db_status= database_genvendor["status"]
            not_verified= db_status.find({"name":"not verified"})
            for i in not_verified:
                not_verified= ObjectId(i["_id"])
            db_genvendor= database_genvendor["vendor2"]
            database_specvendor= utils.connect_database(vendor_databse_name)
            db_info = database_specvendor["Information"]
            db_products= database_specvendor["Products"]
            cnicCheckCount= db_genvendor.find({"cnic":cnic}).count()

            if cnicCheckCount==0:
                vendor_login= {
                    "email": email,
                    "password":password,
                    "phone":phone,
                    'status':not_verified,
                    'database_name':vendor_databse_name }
                vendor_info={
                    "firstName": firstName,
                    "middleName": middleName,
                    "lastName": lastName,
                    "businessType": businessType,
                    "dto": dto,
                    "city": city,
                    "province": province,
                    "address1": address1,
                    "address2": address2,
                    "postalCode": postalCode,
                    "cnic": cnic,
                    "creditCard": creditCard,
                    "cardHolder": cardHolder,
                    "billingAddress": billingAddress,
                }
                print(vendor_info)
                print(vendor_login)
                #db_genvendor.insert_one()
                db_genvendor.insert_one(vendor_login)
                db_info.insert_one(vendor_info)

                return redirect("register")
            else:
                return render(request, 'Vendor_registration/Registration.html', {
                    'error_message': "Maybe you are already registered or entered incorrect information !",
                })

        return render(request, 'Vendor_registration/Registration.html')
class Category:
    connection_string = "mongodb+srv://fypecommerce:maazali786@cluster0.ycmix0k.mongodb.net/test"
    client = MongoClient(connection_string)
    database = client["E-Bazar"]
    dbConnection = database["Categories"]
    def __init__(self):
        pass

    def fetchAll(self,request):
        categories=self.dbConnection.find({"parent":"/"})
        categoriesList=[]
        for i in categories:
            categoriesList.append(i)
        return categoriesList
    def fetchChild(self,request,parent):
        subcategories = self.dbConnection.find({"parent": parent})
        subcategoriesList = []
        for i in subcategories:
            subcategoriesList.append(i)
        return subcategoriesList


    # def fetchSubCat(self,request):

class Product:
    category=Category()
    def __init__(self):
        self.context={}

    # def storeContext(self,name,value):
    #     self.context[name]=value

    def renselectCat(self,request):
        return render(request, "Products/Search_Category.html")
    def selectCat(self,request):
        main_categories=self.category.fetchAll(request)
        # sub_categories=[]
        # leaf_categories=[]
        #
        # for i in main_categories:
        #     j=self.category.fetchChild(request,"/" + i["name"])
        #     sub_categories.append([i["name"],j])
        #     for k in j:
        #         leaf=self.category.fetchChild(request,"/" + i["name"] + "/" + k["name"])
        #         leaf_categories.append([k["name"],leaf])



        self.context['maincats']=main_categories


        return render(request,"Products/Search_Category_1.html",self.context)
    def selectSubCat(self,request):
        category= request.POST['category']
        print(2)
        sub_categories=self.category.fetchChild(request,category)
        self.context['subcats']=sub_categories
        return render(request,"Products/Search_Category_2.html",self.context)

    def selectLeafCat(self,request):
        category = request.POST['category']
        leaf_categories=self.category.fetchChild(request,category)
        print(3)
        self.context['leafcats']=leaf_categories
        return render(request,"Products/Search_Category_3.html",self.context)















