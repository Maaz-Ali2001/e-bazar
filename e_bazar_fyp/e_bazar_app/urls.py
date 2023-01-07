from django.urls import path
from . import views

user= views.User_vw()
urlpatterns = [
    path('', views.index, name="index"),
    path('register',user.register,name="register")
]