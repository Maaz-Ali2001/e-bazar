from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View

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
            password = request.POST['password']
            rePassword = request.POST['rePassword']
            creditCard = request.POST['creditCard']
            cardHolder = request.POST['cardHolder']
            billingAddress = request.POST['billingAddress']

            db= utils.connect_database("vendor1")
            cnicCheckCount= db.find({"cnic":cnic}).count()


            if cnicCheckCount==0:
                vendor= {
                    "firstName":firstName,
                    "middleName":middleName,
                    "lastName":lastName,
                    "businessType":businessType,
                    "dto":dto,
                    "city":city,
                    "province":province,
                    "address1":address1,
                    "address2": address2,
                    "postalCode":postalCode,
                    "cnic":cnic,
                    "email": email,
                    "password":password,
                    "phone":phone,
                    "creditCard":creditCard,
                    "cardHolder":cardHolder,
                    "billingAddress":billingAddress,
                }

                db.insert_one(vendor)
            else:
                return render(request, 'Vendor_registration/Registration.html', {
                    'error_message': "Maybe you are already registered or entered incorrect information !",
                })

        return render(request, 'Vendor_registration/Registration.html')



