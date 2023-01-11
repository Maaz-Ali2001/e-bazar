from django.urls import path
from .views import vendorRegister

vendor= vendorRegister()
urlpatterns = [
    path('', vendor.logIn, name="logIn"),
    path('register',vendor.register,name="register")
]