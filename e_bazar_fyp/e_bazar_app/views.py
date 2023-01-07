from django.shortcuts import render
from django.http import HttpResponse,request,Http404,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from .models import *
def index(request):
    return render(request,'User_registration.html')

class User_vw:


    @csrf_exempt
    def register(self,request):

        user_mdl=User(user_Name=request.POST.get('user_name'),user_Password = request.POST.get('password'),user_email_phone = request.POST.get('Mob_or_Eml'))

        user_mdl.save()
        print(request.POST.get('username'))
        return HttpResponse(request.POST.get('user_name'))
    # def post(self,request):
    #     user_creation=self.register(request)
    #     return user_creation


