from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

class admin:
    def home(self,request):
        return redirect("verify")

    def verify(self,request):
        if request.method=="POST":
            pass
