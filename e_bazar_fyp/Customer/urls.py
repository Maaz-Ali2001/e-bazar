from django.urls import path
from .views import Customer
customer=Customer()
urlpatterns = [
    path('', customer.renHomePage, name="logIn")
]