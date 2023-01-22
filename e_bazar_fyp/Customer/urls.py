from django.urls import path
from .views import Customer
customer=Customer()
urlpatterns = [
    path('', customer.renHomePage, name="logIn"),
    path('productdetail/',customer.productdetail,name='productdetail'),
    path('cart/',customer.add_to_cart,name='cart')
]